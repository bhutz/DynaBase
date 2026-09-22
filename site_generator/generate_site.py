#!/usr/bin/env python3
"""
Generate the public static site (into ../docs/) from the DynaBase database.

../docs/ is deliberate, not just a name choice: GitHub Pages' "Deploy from a
branch" source only offers repo root or /docs as the served folder, so this
lets Pages serve the site directly with no build/Actions step.

Usage:
    python3 generate_site.py               # uses postgresql_local
    python3 generate_site.py --section postgresql   # Neon - currently stale, avoid

This only ever reads from the database. It requires no Sage, only psycopg2 +
Jinja2 (both plain Python).
"""

import argparse
import os
import shutil
import sys

from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db
import render
import mdlite

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SITE_DIR = os.path.join(REPO_ROOT, 'docs')
DATA_SOURCES_MD = os.path.join(REPO_ROOT, 'sample_data', 'data_sources.md')

CUSTOM_DOMAIN = 'dynabase.org'

DIMENSIONS = [1]
DEGREES = [2, 3]
TYPES = [('polynomial', True), ('rational', False)]
PROBLEM = 'rational-preperiodic'
TYPE_LABELS = {'polynomial': 'Polynomial', 'rational': 'Rational'}

DEFAULT_DEGREE = 2
DEFAULT_TYPE = 'polynomial'


def make_env():
    return Environment(
        loader=FileSystemLoader(os.path.join(HERE, 'templates')),
        autoescape=False,  # we control escaping ourselves; most fields are pre-built HTML
    )


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def root_prefix(rel_path):
    """
    '../' once per directory level rel_path is nested under SITE_DIR, so every
    page - regardless of depth - links to assets/other pages relative to
    itself. Needed for GitHub Pages (domain root) *and* for opening files
    directly via file:// while testing locally: a root-absolute '/assets/...'
    resolves against the filesystem root under file://, not the site root,
    which is exactly why the selector/View button appeared to do nothing in
    local testing before this fix.
    """
    depth = rel_path.count('/')
    return '../' * depth


def render_data_page(env, conn, dimension, degree, type_name, is_polynomial, root,
                      citations_by_id, used_citation_ids):
    rows = db.get_functions_dim_1(conn, degree=degree, is_polynomial=is_polynomial)
    for row in rows:
        used_citation_ids.update(row.get('citations') or [])
    groups = render.group_by_field_degree(dimension, rows, citations_by_id, root)
    template = env.get_template('data_page.html')
    return template.render(
        title=f'Degree {degree} {TYPE_LABELS[type_name]} Rational Preperiodic',
        dimension=dimension,
        degree=degree,
        type_=type_name,
        type_label=TYPE_LABELS[type_name],
        groups=groups,
        root=root,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--section', default='postgresql_local',
                         help="database.ini section to read from "
                              "(default: postgresql_local; 'postgresql' [Neon] is stale as of 2026-09-22)")
    args = parser.parse_args()

    conn = db.connect(section=args.section)
    env = make_env()
    type_by_name = dict(TYPES)  # 'polynomial' -> True, 'rational' -> False

    citations_by_id = db.get_citations_by_id(conn)
    used_citation_ids = set()

    # --- data pages: dimension=1 x degree in {2,3} x type in {polynomial,rational} ---
    for dimension in DIMENSIONS:
        for degree in DEGREES:
            for type_name, is_polynomial in TYPES:
                rel = f'data/{dimension}/{degree}/{type_name}/{PROBLEM}.html'
                html = render_data_page(env, conn, dimension, degree, type_name,
                                         is_polynomial, root=root_prefix(rel),
                                         citations_by_id=citations_by_id,
                                         used_citation_ids=used_citation_ids)
                write(os.path.join(SITE_DIR, rel), html)
                print('wrote', rel)

    # index.html = the default combination re-rendered at depth 0 (root='') -
    # can't just reuse the data/ page's HTML, its links/JS are relative to a
    # different depth.
    index_html = render_data_page(env, conn, DIMENSIONS[0], DEFAULT_DEGREE, DEFAULT_TYPE,
                                   type_by_name[DEFAULT_TYPE], root='',
                                   citations_by_id=citations_by_id,
                                   used_citation_ids=used_citation_ids)
    write(os.path.join(SITE_DIR, 'index.html'), index_html)
    print('wrote index.html (= dimension 1, degree', DEFAULT_DEGREE, ',', DEFAULT_TYPE, ')')

    # Extreme Examples: for each field category (QQ, quadratic fields - same
    # grouping as the main data pages) and each degree, the polynomial with
    # the longest periodic cycle / longest preperiodic tail among those
    # currently loaded. One row per degree *within* each field-grouped
    # section - field category is conveyed by the section, not a column.
    # Computed before the bibliography below, so a citation used only by one
    # of these winning rows still makes it into the citation list.
    extreme_rows_by_degree = {degree: db.get_extreme_source_rows(conn, degree) for degree in DEGREES}

    def build_extreme_groups(finder):
        groups = []
        for base_field_degree in (1, 2):
            rows_out = []
            for degree in DEGREES:
                candidates = [r for r in extreme_rows_by_degree[degree]
                              if r['base_field_degree'] == base_field_degree]
                winner, value = finder(candidates)
                if winner is None:
                    continue
                used_citation_ids.update(winner.get('citations') or [])
                rows_out.append(render.build_extreme_row(degree, winner, value, citations_by_id, root=''))
            if rows_out:
                groups.append((render.field_degree_label(base_field_degree), rows_out))
        return groups

    longest_cycle_groups = build_extreme_groups(render.find_longest_cycle_row)
    longest_tail_groups = build_extreme_groups(render.find_longest_tail_row)

    write(os.path.join(SITE_DIR, 'extreme-examples.html'),
          env.get_template('extreme_examples.html').render(
              title='Summary of Extreme Examples', root='',
              longest_cycle_groups=longest_cycle_groups, longest_tail_groups=longest_tail_groups))

    # --- static-link pages (all top-level, so root='') ---
    write(os.path.join(SITE_DIR, 'about.html'),
          env.get_template('about.html').render(title='About', root=''))

    data_sources_text = open(DATA_SOURCES_MD, encoding='utf-8').read()
    content_html = mdlite.render(data_sources_text)
    # Bibliography = citations actually attached to a function on some page
    # just generated above, not the whole citations table - keeps this in
    # sync with what's really on the site rather than what's merely planned.
    bib_rows = sorted(
        (citations_by_id[cid] for cid in used_citation_ids if cid in citations_by_id),
        key=lambda c: c['label']
    )
    bibliography_html = render.format_bibliography(bib_rows)
    write(os.path.join(SITE_DIR, 'data-summary.html'),
          env.get_template('data_summary.html').render(
              title='Summary of Included Data', root='',
              content_html=content_html, bibliography_html=bibliography_html))

    # --- assets ---
    os.makedirs(os.path.join(SITE_DIR, 'assets'), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, 'static', 'style.css'),
                     os.path.join(SITE_DIR, 'assets', 'style.css'))

    # GitHub Pages: don't run this through Jekyll
    open(os.path.join(SITE_DIR, '.nojekyll'), 'a').close()

    # Custom domain - GitHub Pages reads this file to serve dynabase.org.
    # Written here (not just once by hand) so it survives every regeneration.
    write(os.path.join(SITE_DIR, 'CNAME'), CUSTOM_DOMAIN + '\n')

    conn.close()
    print('done ->', SITE_DIR)


if __name__ == '__main__':
    main()
