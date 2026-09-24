"""
Pure formatting helpers: turn raw DB rows into display strings.
No DB access here - keeps this testable without a live connection.
"""

import html
import re

from labels import is_lmfdb_label


def choose_coeffs(row):
    """
    Pick which model's coefficients to display, following functions_dim_1_NF's
    own 'display_model' column.

    Only 'original_model', 'reduced_model' and 'monic_centered' actually store
    coefficients (model_type composites). 'chebyshev' and 'newton' are valid
    display_model values but have no dedicated coefficient storage of their
    own (newton_polynomial_coeffs holds a *different* thing - the auxiliary
    polynomial being Newton-iterated, not this map's own homogeneous
    coordinates) - confirmed against live data, where a real 'chebyshev'-
    display row (x^2-2, i.e. the degree-2 Chebyshev map) has identical
    original/monic/reduced coeffs anyway. So for those two cases, and as a
    last-resort fallback if the named model happens to be null, fall back to
    original_model, which is always populated.
    """
    model = row.get('display_model')
    by_name = {
        'original': row.get('original_coeffs'),
        'reduced': row.get('reduced_coeffs'),
        'monic centered': row.get('monic_coeffs'),
    }
    coeffs = by_name.get(model)
    if coeffs is None:
        coeffs = row.get('original_coeffs')
    return coeffs


def format_homog_poly(coeffs):
    """
    coeffs: list of degree+1 strings, coeffs[i] = coefficient of x^(deg-i) y^i
    (this is exactly get_coefficients()'s convention in
    functions/function_dim_1_helpers_generic.py). Returns an HTML string.
    """
    if not coeffs:
        return '&mdash;'
    deg = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        c = (c or '0').strip()
        if c == '0':
            continue
        xexp, yexp = deg - i, i
        mono = ''
        if xexp == 1:
            mono += 'x'
        elif xexp > 1:
            mono += f'x<sup>{xexp}</sup>'
        if yexp == 1:
            mono += 'y'
        elif yexp > 1:
            mono += f'y<sup>{yexp}</sup>'

        neg = c.startswith('-')
        mag = c[1:] if neg else c
        if mono == '':
            body = mag
        elif mag == '1':
            body = mono
        elif '/' in mag:
            # e.g. '1/4x' reads ambiguously as '1/(4x)' - add a visible separator
            body = f'{mag}&middot;{mono}'
        else:
            body = f'{mag}{mono}'
        terms.append((neg, body))

    if not terms:
        return '0'
    out = ('-' if terms[0][0] else '') + terms[0][1]
    for neg, body in terms[1:]:
        out += (' &minus; ' if neg else ' + ') + body
    return out


def format_function(row):
    """Render '(F0(x,y) : F1(x,y))' for one function row - projective
    coordinate notation, per Ben's request in place of '[F0, F1]'."""
    coeffs = choose_coeffs(row)
    if not coeffs or len(coeffs) != 2:
        return '&mdash;'
    f0 = format_homog_poly(coeffs[0])
    f1 = format_homog_poly(coeffs[1])
    return f'({f0}&nbsp;:&nbsp;{f1})'


def format_int_list(values):
    if values is None:
        return '&mdash;'
    return ', '.join(str(v) for v in values)


def format_field_link(base_field_label):
    """Field of Definition cells link out to the field's LMFDB page - the
    base_field_label is normally an LMFDB number-field label (see
    lmfdb_field_label_NF in fields/field_helpers_NF.py), so this is a direct
    lookup, not a search. A field not in the LMFDB is labeled by its defining
    polynomial instead (e.g. 'x^2 - x - 1'); that has no LMFDB page, so it is
    shown as the polynomial, unlinked."""
    if not base_field_label:
        return '&mdash;'
    if not is_lmfdb_label(base_field_label):
        poly = html.escape(base_field_label)
        poly = re.sub(r'\^(\d+)', r'<sup>\1</sup>', poly).replace(' - ', ' &minus; ')
        return f'&#x211A;[x]/({poly})'
    return f'<a href="https://www.lmfdb.org/NumberField/{base_field_label}">{base_field_label}</a>'


def field_degree_label(base_field_degree):
    if base_field_degree == 1:
        return 'Functions over &#x211A;'  # blackboard-bold Q
    if base_field_degree == 2:
        return 'Functions over quadratic fields'
    return f'Functions over fields of degree {base_field_degree}'


def find_longest_cycle_row(rows):
    """
    The row (and that row's longest single periodic-cycle length) with the
    largest such length among rows that have periodic_cycles data. Ties keep
    whichever row was encountered first - rows should be passed in a stable,
    deterministic order (e.g. by function_id, see db.get_extreme_source_rows).
    """
    best, best_len = None, -1
    for row in rows:
        cycles = row.get('periodic_cycles')
        if not cycles:
            continue
        m = max(cycles)
        if m > best_len:
            best, best_len = row, m
    return best, (best_len if best is not None else None)


def find_longest_tail_row(rows):
    """Same idea as find_longest_cycle_row, but for graphs_dim_1_NF.max_tail
    (already a single integer per function, not a list to take the max of)."""
    best, best_tail = None, -1
    for row in rows:
        tail = row.get('max_tail')
        if tail is None:
            continue
        if tail > best_tail:
            best, best_tail = row, tail
    return best, (best_tail if best is not None else None)


def build_extreme_row(degree, row, value, citations_by_id, root):
    """
    The section a row sits under (see build_extreme_groups in
    generate_site.py) conveys the field *degree* only - QQ vs. quadratic
    field - matching how the main data pages group. But a 'quadratic fields'
    section can span several distinct actual fields (a different one per
    degree, say), so the specific field still needs its own column, same as
    the main data pages' 'Field of Definition'.
    """
    return {
        'degree': degree,
        'function': format_function(row),
        'field': format_field_link(row['base_field_label']),
        'value': value,
        'citations': format_citations(row.get('citations'), citations_by_id, root),
    }


def format_label(dimension, row):
    """
    dim.sigma1.sigma2.ordinal - the function's real label. Not function_id;
    that was a stand-in before this was specified. dimension is which table
    the row came from (functions_dim_1_NF -> 1), not a database column.
    """
    return f"{dimension}.{row['sigma_one']}.{row['sigma_two']}.{row['ordinal']}"


def format_citations(citation_ids, citations_by_id, root):
    """
    functions_dim_1_NF.citations is int[] of citations.id. Render each as its
    short label, linked to its entry in the Summary of Included Data page's
    bibliography (see format_bibliography / the #cite-<label> anchors it
    writes there).
    """
    if not citation_ids:
        return '&mdash;'
    parts = []
    for cid in citation_ids:
        c = citations_by_id.get(cid)
        if c is None:
            continue  # stale id, shouldn't happen, but don't break the page over it
        parts.append(f'<a href="{root}data-summary.html#cite-{c["label"]}">{c["label"]}</a>')
    return ', '.join(parts) if parts else '&mdash;'


def build_table_rows(dimension, rows, citations_by_id, root):
    """Turn raw DB rows into the exact cell strings the table template needs."""
    out = []
    for row in rows:
        out.append({
            'label': format_label(dimension, row),
            'function': format_function(row),
            'field': format_field_link(row['base_field_label']),
            'cardinality': row['cardinality'] if row['cardinality'] is not None else '&mdash;',
            'periodic_cycles': format_int_list(row['periodic_cycles']),
            'preperiodic_components': format_int_list(row['preperiodic_components']),
            'max_tail': row['max_tail'] if row['max_tail'] is not None else '&mdash;',
            'citations': format_citations(row.get('citations'), citations_by_id, root),
        })
    return out


def filter_distinct_graphs(rows):
    """
    Each table (one field degree on one degree/type page) should show one
    (function, field) pair per rational preperiodic graph structure. graph_id
    already identifies an isomorphism class (identify_graph in
    functions/function_dim_1_helpers_NF.py reuses a graphs_dim_1_NF row
    whenever is_isomorphic matches), so two pairs in the same table with the
    same graph_id are duplicates. Rows must arrive in load order (see
    db.get_functions_dim_1); the first-loaded pair for each graph is kept,
    matching which entry the sample_data/ files leave uncommented.

    Rows with no preperiodic data (graph_id null - e.g. the computation timed
    out) can't be shown to be distinct, so they're left out too.

    Returns (kept, duplicates, no_graph); kept is re-sorted for display -
    grouped by base_field_degree, largest cardinality (number of rational
    preperiodic points) first, then by function_id and field - and
    duplicates is a list of (row, kept_row) pairs so the caller can report
    what was dropped.
    """
    kept, duplicates, no_graph = [], [], []
    first_with_graph = {}
    for row in rows:
        if row.get('graph_id') is None:
            no_graph.append(row)
            continue
        key = (row['base_field_degree'], row['graph_id'])
        if key in first_with_graph:
            duplicates.append((row, first_with_graph[key]))
        else:
            first_with_graph[key] = row
            kept.append(row)
    kept.sort(key=lambda r: (r['base_field_degree'], -r['cardinality'],
                             r['function_id'], r['base_field_label']))
    return kept, duplicates, no_graph


def group_by_field_degree(dimension, rows, citations_by_id, root):
    """
    Group already-sorted (by base_field_degree first) rows into a list
    of (heading, [row, ...]) tuples, one per distinct base_field_degree
    present - so a table only appears for field-degrees that actually have data.
    Expects rows already passed through filter_distinct_graphs, so the row
    count of each table is its number of distinct graph structures.
    """
    groups = []
    current_degree = object()  # sentinel, never equals a real degree
    current_rows = None
    for row in rows:
        d = row['base_field_degree']
        if d != current_degree:
            current_degree = d
            current_rows = []
            groups.append((field_degree_label(d), current_rows))
        current_rows.append(row)
    return [(f'{heading}: {len(rs)} distinct graph structure{"" if len(rs) == 1 else "s"}',
             build_table_rows(dimension, rs, citations_by_id, root))
            for heading, rs in groups]


def count_conjugacy_classes(rows):
    """
    Number of conjugacy classes over the algebraic closure of QQ among rows.
    Distinct functions in the database are distinct up to conjugacy over their
    field, but twists (functions_dim_1_NF.rational_twists) are conjugate over an
    extension - the same class over QQbar, which is how PCF classifications
    count. Union-find over the twist links between rows present.
    """
    parent = {row['function_id']: row['function_id'] for row in rows}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for row in rows:
        for t in row.get('rational_twists') or []:
            if t in parent:
                parent[find(t)] = find(row['function_id'])
    return len({find(i) for i in parent})


QBAR = '<span class="qbar">&#x211A;</span>'  # styled with an overline


def build_pcf_rows(dimension, rows, citations_by_id, root):
    out = []
    for row in rows:
        def dash(v):
            return v if v is not None else '&mdash;'
        out.append({
            'label': format_label(dimension, row),
            'function': format_function(row),
            'field': format_field_link(row['base_field_label']),
            'cp_cardinality': dash(row['cp_cardinality']),
            'cp_field': format_field_link(row['cp_field_of_defn']),
            'portrait_cardinality': dash(row['portrait_cardinality']),
            'portrait_cycles': format_int_list(row['portrait_cycles']),
            'portrait_components': format_int_list(row['portrait_components']),
            'citations': format_citations(row.get('citations'), citations_by_id, root),
        })
    return out


def group_pcf_by_field_degree(dimension, rows, citations_by_id, root):
    """
    PCF functions grouped by their field's degree, one table per degree
    present, each sorted by critical portrait size (largest first) then
    function_id. Headings count conjugacy classes over QQbar, and the maps
    too when twists make those differ.
    """
    by_degree = {}
    for row in rows:
        by_degree.setdefault(row['base_field_degree'], []).append(row)
    groups = []
    for d in sorted(by_degree):
        rs = sorted(by_degree[d], key=lambda r: (-(r['portrait_cardinality'] or 0), r['function_id']))
        classes = count_conjugacy_classes(rs)
        heading = (f'{field_degree_label(d)}: {classes} conjugacy class{"" if classes == 1 else "es"}'
                   f' over {QBAR}')
        if len(rs) != classes:
            heading += f' ({len(rs)} maps, counting rational twists separately)'
        groups.append((heading, build_pcf_rows(dimension, rs, citations_by_id, root)))
    return groups


def format_bibliography(citation_rows):
    """
    citation_rows: list of citations-table dicts (label, authors, journal,
    year, citation, mathscinet), already sorted by caller. Renders the actual
    reference text, each with an #cite-<label> anchor matching the links
    format_citations() builds from the data tables, plus a MathSciNet link
    when available.
    """
    if not citation_rows:
        return '<p class="empty">No citations are attached to any function currently on this site.</p>'
    items = []
    for c in citation_rows:
        mr = c.get('mathscinet')
        mr_link = ''
        if mr:
            mr_num = mr[2:] if mr.upper().startswith('MR') else mr
            mr_link = f' <a href="https://mathscinet.ams.org/mathscinet-getitem?mr={mr_num}">{mr}</a>'
        items.append(
            f'<li id="cite-{c["label"]}"><b>[{c["label"]}]</b> {c["citation"]}{mr_link}</li>'
        )
    return '<ul class="bibliography">\n' + '\n'.join(items) + '\n</ul>'
