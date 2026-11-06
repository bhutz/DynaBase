#!/usr/bin/env python3
"""
Make one data version of Dynabase.

    python3 data_release/make_release.py 1.0.0 --notes "First version."

Versions are major.minor.patch: major for a schema change, minor for data added or newly
computed, patch for a correction to existing values. Comparing with the previous version's
exports (data_release/latest/, tracked in git) decides which one this is, and a version
number that doesn't match is refused.

It checks the labels against extreme_examples_data/labels.jsonl, records the version in
data_releases and functions_dim_1_NF's first_release / last_changed_release, updates the
label file, releases.jsonl and data_release/latest/, and regenerates docs/. Committing and
tagging are not done; it prints the steps. --dry-run stops after the checks and changes
nothing.

Plain Python, like the site generator: it only reads what is already computed.
"""

# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

import psycopg2
import psycopg2.extras
from psycopg2.extras import Json

from config import load_config
from functions.release_files import (LABEL_ROWS_QUERY, compare_labels, format_label, read_label_file,
                                      read_release_file, version_key, write_label_file, write_release_file)

# this version's tables and schema, which the next version is compared with. Tracked in git,
# so each version's tag holds its own.
BASELINE_DIR = os.path.join(REPO_ROOT, 'data_release', 'latest')
SAGE = '/home/ben/sage-rel/sage'

# files make_release.py itself rewrites, or generates: they don't make the code version unclear
GENERATED_PATHS = ('docs/', 'data_release/latest/', 'extreme_examples_data/labels.jsonl',
                   'extreme_examples_data/releases.jsonl')

# x^2 + y^2's invariants and label hashes (function_dim_1_helpers_generic.sigma_hash): the
# hashes are comma separated.
SENTINEL_COEFFS = [['1', '0', '1'], ['0', '0', '1']]
SENTINEL_SIGMA_ONE = hashlib.shake_256(b'2,4,0').hexdigest(4)

# internal ids depend on load order: the exports resolve them, and the comparison skips them
ID_COLUMNS = {'id', 'graph_id', 'family_id', 'function_id', 'citations', 'family', 'rational_twists',
              'critical_portrait_graph_id', 'first_release', 'last_changed_release'}
# table -> its rows' key in the comparison, for the tables with a natural one
TABLE_KEYS = {
    'functions_dim_1_nf': lambda r: r['label'],
    'rational_preperiodic_dim_1_nf': lambda r: r['function_label'] + ' ' + r['base_field_label'],
    'citations': lambda r: r['label'],
    'families_dim_1_nf': lambda r: r['name'],
    'graphs_dim_1_nf': lambda r: json.dumps(r['edges']),
}
ADDITIVE_COLUMNS = {'citation_labels', 'family_names', 'rational_twist_labels'}


def fail(message):
    sys.exit('make_release: ' + message)


def run(command, env=None, stdout=None):
    return subprocess.run(command, check=True, env=env, stdout=stdout, cwd=REPO_ROOT)


def export_tables(conn):
    """table -> its rows as dicts, with internal ids resolved to labels, sorted by key."""
    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE' ORDER BY table_name""")
    tables = {}
    for (table,) in cur.fetchall():
        cur.execute(f'SELECT to_jsonb(t) FROM {table} t')
        tables[table] = [row[0] for row in cur.fetchall()]

    citations = {r['id']: r['label'] for r in tables['citations']}
    families = {r['family_id']: r['name'] for r in tables['families_dim_1_nf']}
    edges = {r['graph_id']: r['edges'] for r in tables['graphs_dim_1_nf']}
    labels = {r['function_id']: format_label(r) for r in tables['functions_dim_1_nf']}
    for r in tables['functions_dim_1_nf']:
        r['label'] = labels[r['function_id']]
        r['citation_labels'] = sorted(citations[i] for i in r['citations'] or [])
        r['family_names'] = sorted(families[i] for i in r['family'] or [])
        r['rational_twist_labels'] = sorted(labels[i] for i in r['rational_twists'] or [] if i in labels)
        portrait = r['critical_portrait_graph_id']
        r['critical_portrait_edges'] = edges.get(int(portrait)) if portrait else None
    for r in tables['rational_preperiodic_dim_1_nf']:
        r['function_label'] = labels[r['function_id']]
        r['graph_edges'] = edges.get(r['graph_id'])
    for r in tables['families_dim_1_nf']:
        r['citation_labels'] = sorted(citations[i] for i in r['citations'] or [])
    for table, rows in tables.items():
        rows.sort(key=lambda r: row_key(table, r))
    return tables


def row_key(table, row):
    if table in TABLE_KEYS:
        return TABLE_KEYS[table](row)
    return json.dumps({k: v for k, v in row.items() if k not in ID_COLUMNS}, sort_keys=True)


def write_exports(tables, directory):
    os.makedirs(directory, exist_ok=True)
    for table, rows in tables.items():
        with open(os.path.join(directory, table + '.jsonl'), 'w', encoding='utf-8') as f:
            for row in rows:
                f.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + '\n')


def read_exports(directory):
    tables = {}
    for name in os.listdir(directory):
        if name.endswith('.jsonl'):
            with open(os.path.join(directory, name), encoding='utf-8') as f:
                tables[name[:-len('.jsonl')]] = [json.loads(line) for line in f if line.strip()]
    return tables


def compare_tables(old, new):
    """
    What changed between two versions' exports: counts per table of rows added and
    removed, values newly computed (null to a value; a list only growing, like a map's
    citations) and values corrected (a value to anything else), and the labels of the
    functions touched by any of these.
    """
    counts, touched = {}, set()
    for table in sorted(set(old) | set(new)):
        if table == 'data_releases':
            continue
        before = {row_key(table, r): r for r in old.get(table, [])}
        after = {row_key(table, r): r for r in new.get(table, [])}
        c = {'added': len(after.keys() - before.keys()), 'removed': len(before.keys() - after.keys()),
             'newly_computed': 0, 'corrected': 0}
        changed_keys = set()
        for key in before.keys() & after.keys():
            for column in (before[key].keys() | after[key].keys()) - ID_COLUMNS:
                a, b = before[key].get(column), after[key].get(column)
                if a == b:
                    continue
                changed_keys.add(key)
                grew = column in ADDITIVE_COLUMNS and set(a or []) <= set(b or [])
                c['newly_computed' if a is None or grew else 'corrected'] += 1
        counts[table] = c
        if table == 'functions_dim_1_nf':
            touched |= changed_keys | (after.keys() - before.keys())
        elif table == 'rational_preperiodic_dim_1_nf':
            for key in changed_keys | (after.keys() - before.keys()):
                touched.add(after[key]['function_label'])
    return counts, touched


def required_version(previous, counts, schema_changed):
    """The next version number these changes call for; None if nothing changed."""
    major, minor, patch = version_key(previous)
    total = lambda *kinds: sum(c[k] for c in counts.values() for k in kinds)
    if schema_changed:
        return f'{major + 1}.0.0'
    if total('added', 'newly_computed'):
        return f'{major}.{minor + 1}.0'
    if total('removed', 'corrected'):
        return f'{major}.{minor}.{patch + 1}'
    return None


def normalized_schema(text):
    """pg_dump --schema-only without its comments and settings, which vary between runs."""
    lines = [line for line in text.splitlines()
             if line.strip() and not line.startswith('--') and not line.startswith('SET ')
             and not line.startswith('SELECT pg_catalog.set_config') and not line.startswith('\\')]
    return '\n'.join(lines) + '\n'


def pg_env_and_args(config):
    env = dict(os.environ, PGPASSWORD=config.get('password', ''))
    args = ['-h', config['host'], '-p', str(config.get('port', 5432)), '-U', config['user'], config['database']]
    return env, args


def dump_schema(config):
    env, args = pg_env_and_args(config)
    out = subprocess.run(['pg_dump', '--schema-only', '--no-owner', '--no-privileges'] + args, env=env,
                         check=True, stdout=subprocess.PIPE, text=True).stdout
    return normalized_schema(out)


def git_output(*args):
    return subprocess.run(['git'] + list(args), cwd=REPO_ROOT, check=True, stdout=subprocess.PIPE,
                          text=True).stdout.strip()


def dirty_paths():
    """Tracked or new files with changes, other than the ones this helper generates."""
    paths = [line[3:] for line in git_output('status', '--porcelain').splitlines()]
    return [p for p in paths if not p.startswith(GENERATED_PATHS)]


def sage_version(sage):
    out = subprocess.run([sage, '--version'], check=True, stdout=subprocess.PIPE, text=True).stdout
    return out.strip().splitlines()[-1]


def check_labels(cur, entries, force):
    cur.execute("""SELECT sigma_one FROM functions_dim_1_NF
        WHERE degree = 2 AND (original_model).coeffs = %s::varchar[]""", [SENTINEL_COEFFS])
    row = cur.fetchone()
    if row is None:
        fail('x^2 + y^2 is not in the database, so the label hashes cannot be checked')
    if row['sigma_one'] != SENTINEL_SIGMA_ONE:
        fail(f"x^2 + y^2 has sigma_one {row['sigma_one']}, not {SENTINEL_SIGMA_ONE}: this database "
             'has hashes from before they were comma separated. Recompute it first.')
    cur.execute(LABEL_ROWS_QUERY)
    rows = [dict(r) for r in cur.fetchall()]
    result = compare_labels(entries, rows)
    for old, new in result['changed']:
        print(f'  label changed: {old} is now {new}')
    for old in result['missing']:
        print(f'  label missing: {old}')
    if (result['changed'] or result['missing']) and not force:
        fail('labels are permanent, and these did not survive. Fix the data, or use --force '
             'if each of these is intended.')
    return rows


def write_baseline(tables, schema):
    """Replace data_release/latest/ with this version's exports and schema."""
    shutil.rmtree(BASELINE_DIR, ignore_errors=True)
    write_exports(tables, os.path.join(BASELINE_DIR, 'exports'))
    with open(os.path.join(BASELINE_DIR, 'schema.sql'), 'w', encoding='utf-8') as f:
        f.write(schema)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('version', help='major.minor.patch')
    parser.add_argument('--notes', help="what's in this version, for the changelog")
    parser.add_argument('--section', default='postgresql_local', help='database.ini section')
    parser.add_argument('--sage', default=SAGE, help='the Sage that computed the data')
    parser.add_argument('--dry-run', action='store_true', help='stop after the checks, change nothing')
    parser.add_argument('--no-site', action='store_true', help="don't regenerate docs/")
    parser.add_argument('--allow-dirty', action='store_true', help='allow uncommitted code or data changes')
    parser.add_argument('--force', action='store_true', help='release despite label or version number problems')
    args = parser.parse_args()

    if not re.fullmatch(r'\d+\.\d+\.\d+', args.version):
        fail('the version must be major.minor.patch')
    config = load_config(section=args.section)
    conn = psycopg2.connect(**config)
    if not args.notes:
        fail('--notes is required')

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # --- the checks: nothing is written until they pass
    dirty = dirty_paths()
    if dirty and not args.allow_dirty:
        fail('uncommitted changes, so the commit would not identify this data:\n  ' + '\n  '.join(dirty))
    entries = read_label_file()
    rows = check_labels(cur, entries, args.force)
    tables = export_tables(conn)
    schema = dump_schema(config)

    history = read_release_file()
    earlier = sorted((r for r in history if version_key(r['version']) < version_key(args.version)),
                     key=lambda r: version_key(r['version']))
    counts, touched = {}, set()
    if earlier:
        previous = earlier[-1]['version']
        if not os.path.isdir(os.path.join(BASELINE_DIR, 'exports')):
            fail(f'{BASELINE_DIR} has no exports: restore it from the data-v{previous} git tag')
        counts, touched = compare_tables(read_exports(os.path.join(BASELINE_DIR, 'exports')), tables)
        with open(os.path.join(BASELINE_DIR, 'schema.sql'), encoding='utf-8') as f:
            schema_changed = normalized_schema(f.read()) != schema
        needed = required_version(previous, counts, schema_changed)
        print(f'compared with {previous}: schema {"changed" if schema_changed else "unchanged"}')
        for table, c in counts.items():
            if any(c.values()):
                print(f'  {table}: {c}')
        if needed is None and not args.force:
            fail(f'nothing changed since {previous}')
        if needed != args.version and not args.force:
            fail(f'these changes make the next version {needed}, not {args.version}')
    elif args.version != '1.0.0' and not args.force:
        fail('the first version is 1.0.0')

    sage = sage_version(args.sage)
    print(f'version {args.version}: {len(rows)} maps, commit {git_output("rev-parse", "--short", "HEAD")}, {sage}')
    if args.dry_run:
        print('dry run: nothing changed')
        return

    # --- record it
    version = args.version
    today = datetime.date.today().isoformat()
    release = {'version': version, 'release_date': today, 'git_commit': git_output('rev-parse', 'HEAD'),
               'sage_version': sage, 'notes': args.notes,
               'summary': {'maps': len(rows), 'changes': counts}}
    recorded = {e['label']: e for e in entries}
    new_entries = []
    for r in rows:
        label = format_label(r)
        e = recorded.get(label, {})
        first = e.get('first_release') or version
        last = version if label in touched or not e else e.get('last_changed_release') or version
        # a label keeps the model it was first recorded with
        new_entries.append({'label': label, 'degree': r['degree'], 'sigma_one': r['sigma_one'],
                            'sigma_two': r['sigma_two'], 'ordinal': r['ordinal'],
                            'field': e.get('field', r['base_field_label']), 'coeffs': e.get('coeffs', r['coeffs']),
                            'first_release': first, 'last_changed_release': last})
        cur.execute("""UPDATE functions_dim_1_NF SET first_release = %s, last_changed_release = %s
            WHERE function_id = %s""", [first, last, r['function_id']])
    cur.execute("""INSERT INTO data_releases
        (version, release_date, git_commit, sage_version, notes, summary)
        VALUES (%(version)s, %(release_date)s, %(git_commit)s, %(sage_version)s,
                %(notes)s, %(summary_json)s)
        ON CONFLICT (version) DO UPDATE SET release_date = EXCLUDED.release_date,
            git_commit = EXCLUDED.git_commit, sage_version = EXCLUDED.sage_version,
            notes = EXCLUDED.notes,
            summary = EXCLUDED.summary""", dict(release, summary_json=Json(release['summary'])))
    conn.commit()
    write_label_file(new_entries)
    write_release_file([r for r in history if r['version'] != version] + [release])

    # --- the comparison point for the next version
    write_baseline(export_tables(conn), dump_schema(config))

    if not args.no_site:
        run([sys.executable, 'site_generator/generate_site.py', '--section', args.section])

    print(f"""
Version {version} is recorded. Next:
  git add data_release/latest extreme_examples_data/labels.jsonl extreme_examples_data/releases.jsonl docs
  git commit -m "data version {version}" && git tag data-v{version}""")


if __name__ == '__main__':
    main()
