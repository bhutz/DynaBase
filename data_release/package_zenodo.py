#!/usr/bin/env python3
"""
Package one data version of Dynabase for Zenodo.

    python3 data_release/package_zenodo.py 1.0.0

Run it after make_release.py, once the version is committed and tagged (data-vX.Y.Z): the
package is built from what the tag holds, so it is the same version whenever it is built.
It writes, under releases/ (not tracked):

    dynabase-vX.Y.Z/              the package
        dynabase-vX.Y.Z.sql.gz    a pg_dump of the database (left out with --no-database)
        schema.sql, exports/      the version's schema and tables, from data_release/latest/
        labels.jsonl              the permanent labels
        releases.jsonl            every version up to this one
        source.tar.gz             the code and data files at the tag, without docs/
        README.md, MANIFEST.json  what the files are; environment, row counts, SHA-256s
        LICENSE.txt               the data CC BY 4.0, the code (source.tar.gz) GPL 3+
    dynabase-vX.Y.Z.zip           the package, zipped, to upload
    dynabase-vX.Y.Z.zenodo.json   the record's metadata, for the upload form (not uploaded)

The database dump is only made if the database still holds exactly this version: its
newest data_releases row is this version and its tables and schema match the tag's
exports. Otherwise it stops; --no-database packages the exports alone.

Nothing is uploaded. Plain Python, like make_release.py.
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
import gzip
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile

DATA_RELEASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(DATA_RELEASE_DIR)
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, DATA_RELEASE_DIR)

import psycopg2

from config import load_config
from functions.release_files import version_key
from make_release import (compare_tables, dump_schema, export_tables, normalized_schema,
                          pg_env_and_args, read_exports)

OUTPUT_DIR = os.path.join(REPO_ROOT, 'releases')
# what the package takes from the tag, at these paths in the repo
TAG_PATHS = {'data_release/latest': '', 'extreme_examples_data/labels.jsonl': 'labels.jsonl',
             'extreme_examples_data/releases.jsonl': 'releases.jsonl'}

TITLE = 'Dynabase: a database of extreme examples in arithmetic dynamics'
CREATORS = [{'name': 'Hutz, Benjamin', 'affiliation': 'Saint Louis University'}]
DESCRIPTION = ('Dynamical systems on the projective line over number fields with extreme '
               'arithmetic behavior: many rational preperiodic points, long cycles and tails, '
               'postcritically finite maps, small canonical height ratios and automorphism groups, '
               'with their sources. The data behind https://dynabase.org.')
KEYWORDS = ['arithmetic dynamics', 'preperiodic points', 'postcritically finite',
            'canonical height', 'automorphism groups', 'SageMath']
# the data is CC BY 4.0; the code (source.tar.gz) keeps the repo's GPL
DATA_LICENSE = 'CC-BY-4.0'
DATA_LICENSE_NAME = 'Creative Commons Attribution 4.0 International'
DATA_LICENSE_URL = 'https://creativecommons.org/licenses/by/4.0/'
CODE_LICENSE = 'GPL-3.0-or-later'


def fail(message):
    sys.exit('package_zenodo: ' + message)


def tag_name(version):
    return f'data-v{version}'


def git_bytes(*args):
    return subprocess.run(['git'] + list(args), cwd=REPO_ROOT, check=True, stdout=subprocess.PIPE).stdout


def extract_from_tag(tag, directory):
    """Write the tag's TAG_PATHS into directory, at their package paths."""
    archive = git_bytes('archive', '--format=tar', tag, '--', *TAG_PATHS)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar.getmembers():
            if not member.isfile():
                continue
            for repo_path, package_path in TAG_PATHS.items():
                if member.name == repo_path or member.name.startswith(repo_path + '/'):
                    rest = member.name[len(repo_path):].lstrip('/')
                    target = os.path.join(directory, package_path or rest)
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    with open(target, 'wb') as f:
                        f.write(tar.extractfile(member).read())


def read_jsonl(path):
    with open(path, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def check_database(conn, config, version, directory):
    """Why the database isn't exactly this version, or None if it is."""
    cur = conn.cursor()
    cur.execute('SELECT version FROM data_releases')
    versions = sorted((v for (v,) in cur.fetchall()), key=version_key)
    if not versions or versions[-1] != version:
        return f"its newest version is {versions[-1] if versions else 'none'}, not {version}"
    counts, _ = compare_tables(read_exports(os.path.join(directory, 'exports')), export_tables(conn))
    changed = {t: c for t, c in counts.items() if any(c.values())}
    if changed:
        return 'its tables changed since the release: ' + '; '.join(f'{t} {c}' for t, c in changed.items())
    with open(os.path.join(directory, 'schema.sql'), encoding='utf-8') as f:
        if normalized_schema(f.read()) != dump_schema(config):
            return 'its schema changed since the release'
    return None


def dump_database(config, path):
    env, args = pg_env_and_args(config)
    data = subprocess.run(['pg_dump', '--no-owner', '--no-privileges'] + args, env=env, check=True,
                          stdout=subprocess.PIPE).stdout
    with gzip.GzipFile(path, 'wb', mtime=0) as f:
        f.write(data)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def write_readme(directory, name, release, with_database):
    database = (f"""- `{name}.sql.gz`: the PostgreSQL database. To restore it:
  `createdb dynabase && gunzip -c {name}.sql.gz | psql dynabase`
""" if with_database else '')
    with open(os.path.join(directory, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(f"""# Dynabase data, version {release['version']}

Released {release['release_date']}. Browse the current version at https://dynabase.org.

{release['notes']}

{database}- `schema.sql`: the database schema.
- `exports/`: every table as JSON lines, one file per table, sorted, with internal ids
  resolved to labels (e.g. a map's `citation_labels` next to its `citations` ids).
- `labels.jsonl`: the permanent label of every map, the model it was first recorded with, and
  the versions that added and last changed it.
- `releases.jsonl`: every version up to this one.
- `source.tar.gz`: the code and data files that produced this version (git tag
  `{tag_name(release['version'])}`; the data was computed at commit {release['git_commit']}).
  The computations are SageMath; see its README.
- `MANIFEST.json`: the version's environment, row counts and each file's SHA-256.
- `LICENSE.txt`: the licenses, below.

Computed with {release['sage_version']}. Number fields are named by their LMFDB labels
(https://www.lmfdb.org), or by a defining polynomial for a field not in the LMFDB.

Versions are major.minor.patch: major for a schema change, minor for data added or newly
computed, patch for a correction to existing values. A map's label,
dimension.sigma_one.sigma_two.ordinal, is permanent.

## License

The data (every file here but `source.tar.gz`) is licensed under the {DATA_LICENSE_NAME}
license ({DATA_LICENSE}), {DATA_LICENSE_URL}: you may share and adapt it, with credit to
Dynabase and this version. The code in `source.tar.gz` is licensed under the GNU General Public
License, version 3 or later ({CODE_LICENSE}); see the LICENSE file inside it.
""")


def write_license(directory, release):
    with open(os.path.join(directory, 'LICENSE.txt'), 'w', encoding='utf-8') as f:
        f.write(f"""Dynabase data, version {release['version']}
Copyright (C) {release['release_date'][:4]} Ben Hutz

The data in this package, every file except source.tar.gz, is licensed under the
{DATA_LICENSE_NAME} license ({DATA_LICENSE}). To view a copy of the license, visit
{DATA_LICENSE_URL} (legal code: {DATA_LICENSE_URL}legalcode).

The code in source.tar.gz is licensed under the GNU General Public License, version 3 or
later ({CODE_LICENSE}): https://www.gnu.org/licenses/
""")


def write_manifest(directory, release, tables):
    checksums = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            if filename != 'MANIFEST.json':
                checksums[os.path.relpath(path, directory)] = sha256(path)
    with open(os.path.join(directory, 'MANIFEST.json'), 'w', encoding='utf-8') as f:
        json.dump({'version': release['version'], 'release_date': release['release_date'],
                   'git_tag': tag_name(release['version']), 'git_commit': release['git_commit'],
                   'sage_version': release['sage_version'],
                   'row_counts': {t: len(rows) for t, rows in tables.items()},
                   'changes': (release.get('summary') or {}).get('changes'),
                   'sha256': dict(sorted(checksums.items()))}, f, indent=2, sort_keys=True)
        f.write('\n')


def zenodo_metadata(release, maps):
    """The record's metadata, in the Zenodo deposit API's form."""
    return {'metadata': {
        'upload_type': 'dataset',
        'title': TITLE,
        'version': release['version'],
        'publication_date': release['release_date'],
        'creators': CREATORS,
        'description': f"{DESCRIPTION} Version {release['version']}: {maps} maps. {release['notes']}",
        'keywords': KEYWORDS,
        'license': DATA_LICENSE.lower(),
        'related_identifiers': [
            {'identifier': 'https://dynabase.org', 'relation': 'isDocumentedBy', 'scheme': 'url'},
            {'identifier': f"https://github.com/bhutz/DynaBase/tree/{tag_name(release['version'])}",
             'relation': 'isSupplementTo', 'scheme': 'url'}],
    }}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('version', help='major.minor.patch, already released and tagged')
    parser.add_argument('--section', default='postgresql_local', help='database.ini section')
    parser.add_argument('--output', default=OUTPUT_DIR, help='where to write the package')
    parser.add_argument('--no-database', action='store_true',
                        help="leave out the database dump, e.g. when the database has moved past this version")
    args = parser.parse_args()

    version, tag = args.version, tag_name(args.version)
    if subprocess.run(['git', 'rev-parse', '--verify', '--quiet', tag + '^{commit}'], cwd=REPO_ROOT,
                      stdout=subprocess.DEVNULL).returncode:
        fail(f'there is no git tag {tag}: make the release, commit it and tag it first')

    name = f'dynabase-v{version}'
    directory = os.path.join(args.output, name)
    shutil.rmtree(directory, ignore_errors=True)
    os.makedirs(directory)
    extract_from_tag(tag, directory)
    if not os.path.isdir(os.path.join(directory, 'exports')):
        fail(f'{tag} has no data_release/latest/exports')
    releases = [r for r in read_jsonl(os.path.join(directory, 'releases.jsonl'))
                if version_key(r['version']) <= version_key(version)]
    release = next((r for r in releases if r['version'] == version), None)
    if release is None:
        fail(f"{tag}'s releases.jsonl has no version {version}")
    # a later version's rows don't belong in this one's package
    with open(os.path.join(directory, 'releases.jsonl'), 'w', encoding='utf-8') as f:
        for r in releases:
            f.write(json.dumps(r, sort_keys=True, separators=(',', ':')) + '\n')
    tables = read_exports(os.path.join(directory, 'exports'))

    with_database = not args.no_database
    if with_database:
        config = load_config(section=args.section)
        conn = psycopg2.connect(**config)
        problem = check_database(conn, config, version, directory)
        conn.close()
        if problem:
            shutil.rmtree(directory)
            fail(f'the database ({args.section}) is not version {version}: {problem}. '
                 'Use --no-database to package the exports without a dump.')
        dump_database(config, os.path.join(directory, name + '.sql.gz'))

    with open(os.path.join(directory, 'source.tar.gz'), 'wb') as f:
        # docs/ is the site, generated from the data; it stays in the git tag
        f.write(git_bytes('archive', '--format=tar.gz', f'--prefix=dynabase-{tag}/', tag, '--', '.',
                          ':(exclude)docs'))
    write_readme(directory, name, release, with_database)
    write_license(directory, release)
    write_manifest(directory, release, tables)
    package = shutil.make_archive(directory, 'zip', args.output, name)

    metadata_path = directory + '.zenodo.json'
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(zenodo_metadata(release, len(tables.get('functions_dim_1_nf', []))), f, indent=2)
        f.write('\n')

    size = os.path.getsize(package) / 2 ** 20
    print(f"""Packaged version {version}{'' if with_database else ' (no database dump)'}: {package} ({size:.1f} MB)

Next, on zenodo.org:
  1. For the first version, "New upload"; after that, "New version" on the existing record,
     so the versions share one concept DOI.
  2. Upload {os.path.basename(package)}, and fill in the form from {metadata_path}.
  3. Publish.""")


if __name__ == '__main__':
    main()
