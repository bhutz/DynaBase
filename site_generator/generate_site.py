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
STATUS_CHART_PROBLEMS = ['rational-preperiodic', 'postcritically-finite', 'small-height', 'automorphism-groups']
# charts whose cells also give a count from the database (degree, type, field): for
# automorphism groups, the number of distinct nontrivial groups among the maps
COUNTED_STATUS_PROBLEMS = ['automorphism-groups']
TYPE_LABELS = {'polynomial': 'Polynomial', 'rational': 'Rational'}

DEFAULT_DEGREE = 2
DEFAULT_TYPE = 'polynomial'

# Status of each problem, for the chart on the data summary page. Set by hand,
# not computed from the data. Keyed by problem, then (field, type), then
# degree; anything not listed is 'open'.
STATUS_FIELDS = [('QQ', '&#x211A;'), ('quadratic', '[K:&#x211A;] = 2')]
PROBLEM_STATUS = {
    'postcritically-finite': {
        ('QQ', 'polynomial'): {2: 'proven', 3: 'proven', 4: 'proven'},
        ('QQ', 'rational'): {2: 'proven'},
    },
    # polynomials' automorphism groups are classified (FN1997), and the database has an
    # example of every possible group in each degree up to 10 (the automorphisms data file)
    'automorphism-groups': {
        ('QQ', 'polynomial'): {d: 'proven' if d <= 10 else 'uncomputed' for d in range(2, 16)},
        # the possible groups are known in degree 2 (C_2, S_3) and, from GHJSX2021's complete
        # loci, in degrees 3 and 4; the database has an example of each
        ('QQ', 'rational'): {2: 'proven', 3: 'proven', 4: 'proven'},
    },
    'small-height': {  # Hutz2026's genetic algorithm data
        ('QQ', 'polynomial'): {d: 'experimental' for d in range(2, 13)},
        ('QQ', 'rational'): {d: 'experimental' for d in range(2, 6)},
    },
}


def polynomial_min_degree(iso_type):
    """
    The smallest degree of a polynomial with exactly this automorphism group, or None
    if no polynomial has it. A polynomial conjugate to z^d has the dihedral group of
    order 2(d-1); any other has a cyclic group C_m with m dividing d-1, e.g. z^(m+1) + z
    (Fujimura-Nishizawa; see the Background page). GAP names: dihedral of order 2n is
    C2 (n = 1), C2 x C2 (n = 2), S3 (n = 3), Dn.
    """
    if iso_type == 'C2':
        return 2                     # z^2
    if iso_type == 'C2 x C2':
        return 3                     # z^3
    if iso_type == 'S3':
        return 4                     # z^4
    kind, n = iso_type[:1], iso_type[1:]
    if n.isdigit() and kind in 'CD':
        return int(n) + 1            # C_m: z^(m+1) + z; D_n: z^(n+1)
    return None                      # e.g. A4, S4, A5


def build_automorphism_summary(rows):
    """
    The automorphism group table on the data summary page: one row per group type
    with a map in the database (by order, then name), columns as in the status
    charts (field category x type). A cell is the smallest degree of a map with
    exactly that group - linked to that degree's automorphism page - or 'open'.
    The polynomial column over QQ is known completely (polynomial_min_degree): the
    classification's degree, or 'none' if no polynomial has the group (plain, like the
    other columns - Ben, 2026-10-08).
    Returns [(group html, order, [{'text', 'link', 'cls'} per column])].
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
                link = f'data/1/{d}/{type_name}/automorphism-groups.html' if d else None
                if field == 'QQ' and type_name == 'polynomial':
                    known = polynomial_min_degree(iso_type)
                    if known is None:
                        cells.append({'text': 'none', 'link': None, 'cls': ''})
                    else:
                        cells.append({'text': str(known), 'link': link if d == known else None, 'cls': ''})
                elif d:
                    cells.append({'text': str(d), 'link': link, 'cls': ''})
                else:
                    cells.append({'text': 'open', 'link': None, 'cls': 'status status-open'})
        table.append((render.format_group(iso_type), orders[iso_type], cells))
    return table


# The sources of the 'proven' and 'conjectural' cells of the status charts: problem ->
# (field, type) -> degree -> citation labels (for a chart with subproblems, all its rows).
# Shown under the rating, linked to the bibliography.
CITED_STATUSES = ('proven', 'conjectural')
STATUS_CITATIONS = {
    'rational-preperiodic': {
        ('QQ', 'polynomial'): {2: ['Poonen1998']},
    },
    'postcritically-finite': {
        ('QQ', 'polynomial'): {2: ['Ingram2012'], 3: ['AMT2020', 'Ingram2012'], 4: ['Fraser2024']},
        ('QQ', 'rational'): {2: ['Lukas2014']},
    },
    'automorphism-groups': {
        ('QQ', 'polynomial'): {d: ['FN1997'] for d in range(2, 16)},
        ('QQ', 'rational'): {2: ['Milnor1993'], 3: ['GHJSX2021'], 4: ['GHJSX2021']},
    },
}
# the source of the polynomial column of the automorphism table by group
POLYNOMIAL_AUTOMORPHISM_CITATION = 'FN1997'


def status_citation_labels():
    """every label cited by the status page, so the bibliography includes them"""
    labels = {POLYNOMIAL_AUTOMORPHISM_CITATION}
    for by_cell in STATUS_CITATIONS.values():
        for by_degree in by_cell.values():
            for cites in by_degree.values():
                labels.update(cites)
    return labels


# Problems whose chart has a row for each subproblem in each degree (Ben, 2026-10-08):
# problem -> [(subproblem label, its status as in PROBLEM_STATUS)]. Rational preperiodic
# points (Ben, 2026-10-08): quadratic polynomials over QQ are conjectural (Poonen), the
# other rated cells (quadratic rational maps over QQ, quadratic polynomials over quadratic
# fields, polynomials of degree 3-13 over QQ) experimental, the same for all three
# subproblems.
_RATIONAL_PREPERIODIC = {
    ('QQ', 'polynomial'): {2: 'conjectural', **{d: 'experimental' for d in range(3, 14)}},
    ('QQ', 'rational'): {2: 'experimental'},
    ('quadratic', 'polynomial'): {2: 'experimental'},
}
SUBPROBLEM_STATUS = {
    'rational-preperiodic': [
        ('Many points', _RATIONAL_PREPERIODIC),
        ('Long cycles', _RATIONAL_PREPERIODIC),
        ('Long tails', _RATIONAL_PREPERIODIC),
    ],
}


def build_map_count_table(counts):
    """
    The table of distinct maps in the database on the Summary of Included Data page:
    [(degree, [count per field x type], row total)], plus the column totals and the
    grand total. counts: db.get_map_counts. Only degrees with a map are listed.
    """
    field_degrees = {'QQ': 1, 'quadratic': 2}
    keys = [(field_degrees[field], is_poly) for field, _ in STATUS_FIELDS for _, is_poly in TYPES]
    degrees = sorted({d for d, _, _ in counts})
    rows = []
    for d in degrees:
        cells = [counts.get((d, is_poly, fd), 0) for fd, is_poly in keys]
        rows.append((d, cells, sum(v for (dd, _, _), v in counts.items() if dd == d)))
    column_totals = [sum(counts.get((d, is_poly, fd), 0) for d in degrees) for fd, is_poly in keys]
    return rows, column_totals, sum(counts.values())


def build_status_tables(counts, citations_by_label, root=''):
    """
    [(problem name, has subproblems, [(degree, [(subproblem label or None,
    [(status, count or None, citations html) per field x type])])])] for the charts: one
    row per degree, or one per subproblem in each degree (SUBPROBLEM_STATUS). counts:
    db.get_group_counts (distinct nontrivial automorphism groups); only
    COUNTED_STATUS_PROBLEMS show it. The citations (STATUS_CITATIONS) are given for
    proven and conjectural cells (CITED_STATUSES).
    """
    field_degrees = {'QQ': 1, 'quadratic': 2}
    tables = []
    for problem, problem_name in PROBLEMS:
        if problem not in STATUS_CHART_PROBLEMS:
            continue
        subproblems = SUBPROBLEM_STATUS.get(problem, [(None, PROBLEM_STATUS.get(problem, {}))])
        counted = problem in COUNTED_STATUS_PROBLEMS
        cited = STATUS_CITATIONS.get(problem, {})

        def cell(status, field, type_name, is_poly, degree):
            rating = status.get((field, type_name), {}).get(degree, 'open')
            count = counts.get((degree, is_poly, field_degrees[field]), 0) if counted else None
            labels = cited.get((field, type_name), {}).get(degree, []) if rating in CITED_STATUSES else []
            cites = render.format_citations([citations_by_label[l]['id'] for l in labels if l in citations_by_label],
                                            {citations_by_label[l]['id']: citations_by_label[l] for l in labels
                                             if l in citations_by_label}, root) if labels else ''
            return rating, count, cites

        rows = [(degree, [(label, [cell(status, field, type_name, is_poly, degree)
                                   for field, _ in STATUS_FIELDS for type_name, is_poly in TYPES])
                          for label, status in subproblems])
                for degree in DEGREES]
        tables.append((problem_name, problem in SUBPROBLEM_STATUS, rows))
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
    automorphism_source = db.get_automorphism_source_rows(conn)
    automorphism_rows = []
    automorphism_winners = render.smallest_map_per_group(automorphism_source)
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
    # the groups realized in each degree: rows by degree, a cell per field category and
    # type, each group linked to that degree's automorphism page of that type
    by_degree = render.groups_by_degree(automorphism_source)
    groups_table = []
    for degree in sorted(by_degree):
        cells = []
        for fd in (1, 2):
            for type_name, _ in TYPES:
                entries = by_degree[degree].get((fd, type_name), [])
                link = f'data/1/{degree}/{type_name}/automorphism-groups.html'
                cells.append(', '.join(f'<a href="{link}">{render.format_group(iso)}</a>' for iso in entries)
                             or '&mdash;')
        groups_table.append((degree, cells))
    extreme_sections['automorphism_groups_by_degree'] = groups_table
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
    # the status page cites the sources of its proven cells: include them too
    used_citation_ids.update(c['id'] for c in citations_by_id.values() if c['label'] in status_citation_labels())
    bib_rows = sorted(
        (citations_by_id[cid] for cid in used_citation_ids if cid in citations_by_id),
        key=lambda c: c['label']
    )
    bibliography_html = render.format_bibliography(bib_rows)
    map_rows, map_column_totals, map_total = build_map_count_table(db.get_map_counts(conn))
    write(os.path.join(SITE_DIR, 'data-summary.html'),
          env.get_template('data_summary.html').render(
              title='Summary of Included Data', root='',
              status_fields=STATUS_FIELDS, type_labels=[TYPE_LABELS[t] for t, _ in TYPES],
              map_rows=map_rows, map_column_totals=map_column_totals, map_total=map_total,
              content_html=content_html, bibliography_html=bibliography_html))
    write(os.path.join(SITE_DIR, 'status.html'),
          env.get_template('status.html').render(
              title='Status of Problems', root='',
              status_tables=build_status_tables(db.get_group_counts(conn),
                                                {c['label']: c for c in citations_by_id.values()}),
              polynomial_automorphism_citation=render.format_citations(
                  [c['id'] for c in citations_by_id.values() if c['label'] == POLYNOMIAL_AUTOMORPHISM_CITATION],
                  citations_by_id, ''),
              status_fields=STATUS_FIELDS,
              automorphism_summary=build_automorphism_summary(db.get_automorphism_source_rows(conn)),
              type_labels=[TYPE_LABELS[t] for t, _ in TYPES]))

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
