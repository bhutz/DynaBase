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
import sage_export
import graph_images
import mdlite

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SITE_DIR = os.path.join(REPO_ROOT, 'docs')
DATA_SOURCES_MD = os.path.join(REPO_ROOT, 'extreme_examples_data', 'data_sources.md')

CUSTOM_DOMAIN = 'dynabase.org'

# GoatCounter page-view counting (no cookies, no personal data): the site's code at
# goatcounter.com, i.e. <code>.goatcounter.com. None leaves the script off every page.
GOATCOUNTER_CODE = 'dynabase'

# The comments page embeds this Google Form (fields: who is submitting, contact
# information, comment). Paste the form's "Send" link - the docs.google.com/forms/
# .../viewform URL. None shows a "coming soon" note instead.
COMMENTS_FORM_URL ='https://docs.google.com/forms/d/e/1FAIpQLSdbonxno00EEOX-NNrLCMRt6i9o8DedRrbM39mQxInD77qEdg/viewform'

DIMENSIONS = [1]
DEGREES = list(range(2, 16))  # 2..15
TYPES = [('polynomial', True), ('rational', False)]
PROBLEMS = [('rational-preperiodic', 'Rational Preperiodic'),
            ('postcritically-finite', 'Postcritically Finite'),
            ('small-height', 'Small Height Ratio'),
            ('automorphism-groups', 'Automorphism Groups')]
# The status chart is by degree, which doesn't fit the automorphism group problem
# (one question per group, not per degree), so it has no chart.
STATUS_CHART_PROBLEMS = ['rational-preperiodic', 'postcritically-finite', 'small-height']
TYPE_LABELS = {'polynomial': 'Polynomial', 'rational': 'Rational'}

DEFAULT_DEGREE = 2
DEFAULT_TYPE = 'polynomial'

# Status of each problem, for the chart on the data summary page. Set by hand,
# not computed from the data. Keyed by problem, then (field, type), then
# degree; anything not listed is 'open'.
STATUS_FIELDS = [('QQ', '&#x211A;'), ('quadratic', '[K:&#x211A;] = 2')]
PROBLEM_STATUS = {
    'rational-preperiodic': {
        ('QQ', 'polynomial'): {2: 'conjectural', **{d: 'experimental' for d in range(3, 14)}},
        ('QQ', 'rational'): {2: 'experimental'},
        ('quadratic', 'polynomial'): {2: 'experimental'},
    },
    'postcritically-finite': {
        ('QQ', 'polynomial'): {2: 'proven', 3: 'proven', 4: 'proven'},
        ('QQ', 'rational'): {2: 'proven'},
    },
    'small-height': {  # Hutz2026's genetic algorithm data
        ('QQ', 'polynomial'): {d: 'experimental' for d in range(2, 13)},
        ('QQ', 'rational'): {d: 'experimental' for d in range(2, 6)},
    },
}


def build_automorphism_summary(rows):
    """
    The automorphism group table on the data summary page: one row per group type
    with a map in the database (by order, then name), columns as in the status
    charts (field category x type), each cell the smallest degree of a map with
    exactly that group - linked to that degree's automorphism page - or 'open'.
    Returns [(group html, order, [(degree, link) or None per column])].
    """
    field_degrees = {'QQ': 1, 'quadratic': 2}
    smallest = {}  # (iso type, field degree, type name) -> smallest degree
    orders = {}
    for row in rows:
        type_name = 'polynomial' if row['is_polynomial'] else 'rational'
        key = (row['automorphism_group_iso_type'], row['base_field_degree'], type_name)
        smallest[key] = min(smallest.get(key, row['degree']), row['degree'])
        orders[row['automorphism_group_iso_type']] = row['automorphism_group_cardinality']
    table = []
    for iso_type in sorted(orders, key=lambda t: (orders[t], t)):
        cells = []
        for field, _ in STATUS_FIELDS:
            for type_name, _ in TYPES:
                d = smallest.get((iso_type, field_degrees[field], type_name))
                cells.append((d, f'data/1/{d}/{type_name}/automorphism-groups.html') if d else None)
        table.append((render.format_group(iso_type), orders[iso_type], cells))
    return table


def build_status_tables():
    """[(problem name, [(degree, [status per field x type])])] for the chart."""
    tables = []
    for problem, problem_name in PROBLEMS:
        if problem not in STATUS_CHART_PROBLEMS:
            continue
        status = PROBLEM_STATUS.get(problem, {})
        rows = [(degree, [status.get((field, type_name), {}).get(degree, 'open')
                          for field, _ in STATUS_FIELDS for type_name, _ in TYPES])
                for degree in DEGREES]
        tables.append((problem_name, rows))
    return tables


def make_env():
    env = Environment(
        loader=FileSystemLoader(os.path.join(HERE, 'templates')),
        autoescape=False,  # we control escaping ourselves; most fields are pre-built HTML
    )
    env.globals['degrees'] = DEGREES  # header selector options, on every page
    env.globals['problems'] = PROBLEMS
    env.globals['goatcounter_code'] = GOATCOUNTER_CODE
    return env


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


def comments_embed_url(form_url):
    """The embeddable version of a Google Form link (its viewform URL with
    embedded=true), or None if the link can't be embedded - e.g. a forms.gle
    short link, which the comments page then just links to."""
    if not form_url or 'docs.google.com/forms/' not in form_url or '/viewform' not in form_url:
        return None
    if 'embedded=true' in form_url:
        return form_url
    return form_url + ('&' if '?' in form_url else '?') + 'embedded=true'


def report_excluded(dimension, degree, type_name, duplicates, no_graph):
    """Print which (function, field) pairs filter_distinct_graphs left off a
    page, so regenerating the site doubles as a check that the data files
    hold only one pair per graph structure per table."""
    where = f'dimension {dimension}, degree {degree}, {type_name}'
    for row, kept in duplicates:
        print(f'  excluded (duplicate graph, {where}, field degree {row["base_field_degree"]}): '
              f'{render.format_label(dimension, row)} over {row["base_field_label"]} '
              f'[function_id {row["function_id"]}] has graph {row["graph_id"]}, already shown for '
              f'{render.format_label(dimension, kept)} over {kept["base_field_label"]} '
              f'[function_id {kept["function_id"]}]')
    for row in no_graph:
        print(f'  excluded (no preperiodic data, {where}, field degree {row["base_field_degree"]}): '
              f'{render.format_label(dimension, row)} over {row["base_field_label"]} '
              f'[function_id {row["function_id"]}]')


FIELD_SLUGS = {1: 'QQ', 2: 'quadratic'}
FIELD_TITLES = {1: 'over QQ', 2: 'over quadratic fields'}


def export_page_tables(groups, dimension, degree, type_name, problem, root, citations_by_id, model_of=None,
                       with_points=False):
    """
    Write the Export to Sage files of one data page: one per table (field degree)
    and one for the whole page. Returns (page link or None, [(heading, formatted
    rows, table link)]) for the template. Links are relative to the page (root).
    """
    base = f'data/{dimension}/{degree}/{type_name}/{problem}'
    problem_name = dict(PROBLEMS)[problem]
    title = f'dimension {dimension}, degree {degree}, {TYPE_LABELS[type_name].lower()} maps, {problem_name}'
    out, all_rows = [], []
    for heading, formatted, raw, d in groups:
        rel = f'{base}-{FIELD_SLUGS.get(d, f"degree-{d}")}.sage'
        sage_export.write_sage_file(os.path.join(SITE_DIR, rel),
                                    f'{title}, {FIELD_TITLES.get(d, f"over fields of degree {d}")}',
                                    raw, citations_by_id, dimension=dimension, model_of=model_of,
                                    with_points=with_points)
        out.append((heading, formatted, root + rel))
        all_rows += raw
    if not all_rows:
        return None, out
    rel = base + '.sage'
    sage_export.write_sage_file(os.path.join(SITE_DIR, rel), title, all_rows, citations_by_id,
                                dimension=dimension, model_of=model_of, with_points=with_points)
    return root + rel, out


def render_data_page(env, conn, dimension, degree, type_name, is_polynomial, root,
                      citations_by_id, used_citation_ids, report=True):
    rows = db.get_functions_dim_1(conn, degree=degree, is_polynomial=is_polynomial)
    rows, duplicates, no_graph = render.filter_distinct_graphs(rows)
    if report:
        report_excluded(dimension, degree, type_name, duplicates, no_graph)
    for row in rows:
        used_citation_ids.update(row.get('citations') or [])
    groups = render.group_by_field_degree(dimension, rows, citations_by_id, root)
    page_export, groups = export_page_tables(
        groups, dimension, degree, type_name, 'rational-preperiodic', root, citations_by_id)
    template = env.get_template('data_page.html')
    return template.render(
        title=f'Degree {degree} {TYPE_LABELS[type_name]} Rational Preperiodic',
        problem='rational-preperiodic',
        dimension=dimension,
        degree=degree,
        type_=type_name,
        type_label=TYPE_LABELS[type_name],
        groups=groups,
        page_export=page_export,
        root=root,
    )


def render_pcf_page(env, conn, dimension, degree, type_name, is_polynomial, root,
                    citations_by_id, used_citation_ids, report=True):
    rows, not_computed = db.get_pcf_functions_dim_1(conn, degree=degree, is_polynomial=is_polynomial)
    if report and not_computed:
        print(f'  note (dimension {dimension}, degree {degree}, {type_name}): '
              f'{not_computed} function(s) have is_pcf not computed, so cannot appear on the PCF page')
    for row in rows:
        used_citation_ids.update(row.get('citations') or [])
    groups = render.group_pcf_by_field_degree(dimension, rows, citations_by_id, root)
    page_export, groups = export_page_tables(
        groups, dimension, degree, type_name, 'postcritically-finite', root, citations_by_id)
    return env.get_template('pcf_page.html').render(
        title=f'Degree {degree} {TYPE_LABELS[type_name]} Postcritically Finite',
        problem='postcritically-finite',
        dimension=dimension,
        degree=degree,
        type_=type_name,
        type_label=TYPE_LABELS[type_name],
        groups=groups,
        page_export=page_export,
        root=root,
    )


def render_small_height_page(env, conn, dimension, degree, type_name, is_polynomial, root,
                             citations_by_id, used_citation_ids, report=True):
    rows, not_computed = db.get_small_height_functions_dim_1(conn, degree=degree, is_polynomial=is_polynomial)
    if report and not_computed:
        print(f'  note (dimension {dimension}, degree {degree}, {type_name}): '
              f'{not_computed} function(s) have no smallest height ratio, so cannot appear on the small height page')
    for row in rows:
        used_citation_ids.update(row.get('citations') or [])
    groups = render.group_small_height_by_field_degree(dimension, rows, citations_by_id, root)
    page_export, groups = export_page_tables(
        groups, dimension, degree, type_name, 'small-height', root, citations_by_id,
        model_of=lambda r: r.get('smallest_height_model') or 'original', with_points=True)
    return env.get_template('small_height_page.html').render(
        title=f'Degree {degree} {TYPE_LABELS[type_name]} Small Height Ratio',
        problem='small-height',
        dimension=dimension,
        degree=degree,
        type_=type_name,
        type_label=TYPE_LABELS[type_name],
        groups=groups,
        page_export=page_export,
        root=root,
    )


def render_automorphism_page(env, conn, dimension, degree, type_name, is_polynomial, root,
                             citations_by_id, used_citation_ids, report=True):
    rows, not_computed = db.get_automorphism_functions_dim_1(conn, degree=degree, is_polynomial=is_polynomial)
    if report and not_computed:
        print(f'  note (dimension {dimension}, degree {degree}, {type_name}): '
              f'{not_computed} function(s) have no automorphism group type, so cannot appear on the automorphism page')
    for row in rows:
        used_citation_ids.update(row.get('citations') or [])
    groups = render.group_automorphism_by_field_degree(dimension, rows, citations_by_id, root)
    page_export, groups = export_page_tables(
        groups, dimension, degree, type_name, 'automorphism-groups', root, citations_by_id)
    return env.get_template('automorphism_page.html').render(
        title=f'Degree {degree} {TYPE_LABELS[type_name]} Automorphism Groups',
        problem='automorphism-groups',
        dimension=dimension,
        degree=degree,
        type_=type_name,
        type_label=TYPE_LABELS[type_name],
        groups=groups,
        page_export=page_export,
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

    # images of the graph structures (rational preperiodic graphs and critical portraits),
    # linked from the tables
    render.GRAPH_IMAGES = graph_images.write_graph_images(SITE_DIR, db.get_site_graphs(conn))
    print('wrote', len(render.GRAPH_IMAGES), 'graph images')

    citations_by_id = db.get_citations_by_id(conn)
    used_citation_ids = set()

    # --- data pages: dimension=1 x degree in {2,3} x type in {polynomial,rational} ---
    for dimension in DIMENSIONS:
        for degree in DEGREES:
            for type_name, is_polynomial in TYPES:
                for problem, renderer in [('rational-preperiodic', render_data_page),
                                          ('postcritically-finite', render_pcf_page),
                                          ('small-height', render_small_height_page),
                                          ('automorphism-groups', render_automorphism_page)]:
                    rel = f'data/{dimension}/{degree}/{type_name}/{problem}.html'
                    html = renderer(env, conn, dimension, degree, type_name,
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
                                   used_citation_ids=used_citation_ids,
                                   report=False)  # same rows as its data/ page, already reported
    write(os.path.join(SITE_DIR, 'index.html'), index_html)
    print('wrote index.html (= dimension 1, degree', DEFAULT_DEGREE, ',', DEFAULT_TYPE, ')')

    # Extreme Examples: one section per problem. Each has a table per (field
    # category - QQ or quadratic fields, as on the data pages - and type) with
    # data, and one row per degree: the most extreme map currently loaded, ties
    # going to the lowest function_id. The field category is conveyed by the
    # table, not a column. Computed before the bibliography below, so a
    # citation used only by one of these winning rows still makes it into the
    # citation list.
    combos = [(degree, type_name, is_polynomial) for degree in DEGREES for type_name, is_polynomial in TYPES]
    preperiodic_rows = {(d, t): db.get_extreme_source_rows(conn, d, p) for d, t, p in combos}
    pcf_rows = {(d, t): db.get_pcf_functions_dim_1(conn, degree=d, is_polynomial=p)[0] for d, t, p in combos}
    small_height_rows = {(d, t): db.get_small_height_functions_dim_1(conn, degree=d, is_polynomial=p)[0]
                         for d, t, p in combos}
    status_fields = {1: 'QQ', 2: 'quadratic'}  # base_field_degree -> PROBLEM_STATUS field

    def write_extreme_export(name, title, rows, model_of=None, with_points=False):
        """an Export to Sage file of the Extreme Examples page; returns its link"""
        rel = f'sage/extreme-examples/{name}.sage'
        sage_export.write_sage_file(os.path.join(SITE_DIR, rel), f'Summary of Extreme Examples, {title}',
                                    rows, citations_by_id, model_of=model_of, with_points=with_points)
        return rel

    def build_extreme_groups(source_rows, finder, problem, name, title, model_of=None, extra=None,
                             export_all=False, with_points=False):
        """source_rows: (degree, type_name) -> rows; finder(rows) -> (winner, value).
        model_of(winner): the model to display; extra(row, rows, status, is_polynomial): more cells.
        Writes the Export to Sage files (name: the file name stem, title: for the file header) -
        one per table and one for the section - with each row's winner, or with all its
        candidates if export_all (PCF, whose rows show counts, not one map).
        Returns {'groups': [(heading, rows, table link)], 'export': section link, 'rows': raw rows}."""
        groups, section_rows = [], []
        for base_field_degree in (1, 2):
            for type_name, is_polynomial in TYPES:
                rows_out, export_rows = [], []
                for degree in DEGREES:
                    candidates = [r for r in source_rows[(degree, type_name)]
                                  if r['base_field_degree'] == base_field_degree]
                    winner, value = finder(candidates)
                    if winner is None or value == 0:  # e.g. no rational preperiodic points: not an example
                        continue
                    used_citation_ids.update(winner.get('citations') or [])
                    row = render.build_extreme_row(
                        degree, winner, value, citations_by_id, root='',
                        link=f'data/1/{degree}/{type_name}/{problem}.html',
                        model=model_of(winner) if model_of else None)
                    if extra:
                        status = PROBLEM_STATUS.get(problem, {}).get(
                            (status_fields[base_field_degree], type_name), {}).get(degree, 'open')
                        row.update(extra(winner, candidates, status, is_polynomial))
                    rows_out.append(row)
                    export_rows += candidates if export_all else [winner]
                if rows_out:
                    field = FIELD_SLUGS.get(base_field_degree, f'degree-{base_field_degree}')
                    field_title = FIELD_TITLES.get(base_field_degree, f'over fields of degree {base_field_degree}')
                    link = write_extreme_export(f'{name}-{type_name}-{field}',
                                                f'{title}, {TYPE_LABELS[type_name].lower()} maps {field_title}',
                                                export_rows, model_of, with_points)
                    groups.append((render.extreme_heading(is_polynomial, base_field_degree), rows_out, link))
                    section_rows += export_rows
        export = write_extreme_export(name, title, section_rows, model_of, with_points) if section_rows else None
        return {'groups': groups, 'export': export, 'rows': section_rows}

    def any_pcf(rows):
        # the PCF rows show counts, not one map: any row will do as the "winner"
        return (rows[0], len(rows)) if rows else (None, None)

    def pcf_extra(winner, rows, status, is_polynomial):
        # the sources of all of this degree's PCF maps, in order of first appearance
        cites = []
        for row in rows:
            for cid in row.get('citations') or []:
                if cid not in cites:
                    cites.append(cid)
        used_citation_ids.update(cites)
        return {'classes': render.count_conjugacy_classes(rows), 'status': status,
                'citations': render.format_citations(cites, citations_by_id, ''),
                'excludes_polynomials': not is_polynomial}  # footnoted on the page

    def smallest_ratio(rows):
        best = min(rows, key=lambda r: (r['smallest_height_ratio'], r['function_id']), default=None)
        return best, (render.format_ratio(best['smallest_height_ratio']) if best is not None else None)

    extreme_sections = {
        'many_points': build_extreme_groups(preperiodic_rows, render.find_most_points_row, 'rational-preperiodic',
                                            'many-points', 'many rational preperiodic points'),
        'long_cycles': build_extreme_groups(preperiodic_rows, render.find_longest_cycle_row, 'rational-preperiodic',
                                            'long-cycles', 'long rational cycles'),
        'long_tails': build_extreme_groups(preperiodic_rows, render.find_longest_tail_row, 'rational-preperiodic',
                                           'long-tails', 'long rational tails'),
        'pcf': build_extreme_groups(pcf_rows, any_pcf, 'postcritically-finite', 'postcritically-finite',
                                    'postcritically finite maps (all of them, for each row)',
                                    extra=pcf_extra, export_all=True),
        'small_height': build_extreme_groups(
            small_height_rows, smallest_ratio, 'small-height', 'small-height', 'small canonical heights',
            # heights stored before the smallest_height_model column all used the original model
            model_of=lambda winner: winner.get('smallest_height_model') or 'original', with_points=True),
    }
    # the rational preperiodic section: its three subsections' maps, each (map, field) once
    seen, preperiodic_export = set(), []
    for sub in ('many_points', 'long_cycles', 'long_tails'):
        for row in extreme_sections[sub]['rows']:
            key = (row['function_id'], row['base_field_label'])
            if key not in seen:
                seen.add(key)
                preperiodic_export.append(row)
    extreme_sections['rational_preperiodic_export'] = (
        write_extreme_export('rational-preperiodic', 'rational preperiodic points', preperiodic_export)
        if preperiodic_export else None)

    # automorphism groups: one row per group type, the map of smallest degree (then
    # smallest field) with exactly that automorphism group
    automorphism_rows = []
    automorphism_winners = render.smallest_map_per_group(db.get_automorphism_source_rows(conn))
    for row in automorphism_winners:
        used_citation_ids.update(row.get('citations') or [])
        type_name = 'polynomial' if row['is_polynomial'] else 'rational'
        automorphism_rows.append({
            'group': render.format_group(row['automorphism_group_iso_type']),
            'order': row['automorphism_group_cardinality'],
            'degree': f'<a href="data/1/{row["degree"]}/{type_name}/automorphism-groups.html">{row["degree"]}</a>',
            'type': TYPE_LABELS[type_name],
            'function': render.format_function(row),
            'field': render.format_field_link(row['base_field_label']),
            'citations': render.format_citations(row.get('citations'), citations_by_id, ''),
        })
    extreme_sections['automorphisms'] = {
        'rows': automorphism_rows,
        'export': (write_extreme_export('automorphism-groups', 'automorphism groups (smallest degree for each group)',
                                        automorphism_winners) if automorphism_winners else None)}

    write(os.path.join(SITE_DIR, 'extreme-examples.html'),
          env.get_template('extreme_examples.html').render(
              title='Summary of Extreme Examples', root='', sections=extreme_sections))

    # --- static-link pages (all top-level, so root='') ---
    write(os.path.join(SITE_DIR, 'about.html'),
          env.get_template('about.html').render(title='About', root=''))
    write(os.path.join(SITE_DIR, 'comments.html'),
          env.get_template('comments.html').render(
              title='Comments', root='', form_url=COMMENTS_FORM_URL,
              embed_url=comments_embed_url(COMMENTS_FORM_URL)))
    write(os.path.join(SITE_DIR, 'background.html'),
          env.get_template('background.html').render(title='Mathematical Background', root=''))

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
              status_tables=build_status_tables(), status_fields=STATUS_FIELDS,
              automorphism_summary=build_automorphism_summary(db.get_automorphism_source_rows(conn)),
              type_labels=[TYPE_LABELS[t] for t, _ in TYPES],
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
