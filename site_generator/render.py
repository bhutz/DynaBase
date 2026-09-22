"""
Pure formatting helpers: turn raw DB rows into display strings.
No DB access here - keeps this testable without a live connection.
"""


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


def field_degree_label(base_field_degree):
    if base_field_degree == 1:
        return 'Functions over &#x211A;'  # blackboard-bold Q
    if base_field_degree == 2:
        return 'Functions over quadratic fields'
    return f'Functions over fields of degree {base_field_degree}'


def format_label(dimension, row):
    """
    dim.sigma1.sigma2.ordinal - the function's real label. Not function_id;
    that was a stand-in before this was specified. dimension is which table
    the row came from (functions_dim_1_NF -> 1), not a database column.
    """
    return f"{dimension}.{row['sigma_one']}.{row['sigma_two']}.{row['ordinal']}"


def build_table_rows(dimension, rows):
    """Turn raw DB rows into the exact cell strings the table template needs."""
    out = []
    for row in rows:
        out.append({
            'label': format_label(dimension, row),
            'function': format_function(row),
            'field': row['base_field_label'] or '&mdash;',
            'cardinality': row['cardinality'] if row['cardinality'] is not None else '&mdash;',
            'periodic_cycles': format_int_list(row['periodic_cycles']),
            'preperiodic_components': format_int_list(row['preperiodic_components']),
        })
    return out


def group_by_field_degree(dimension, rows):
    """
    Group already-sorted (by base_field_degree, function_id) rows into a list
    of (heading, [row, ...]) tuples, one per distinct base_field_degree
    present - so a table only appears for field-degrees that actually have data.
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
    return [(heading, build_table_rows(dimension, rs)) for heading, rs in groups]
