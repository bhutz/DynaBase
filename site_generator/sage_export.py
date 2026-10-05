"""
"Export to Sage" files: a .sage file that, loaded in Sage with load(...),
defines the maps of one site table (or section) as a list of dynamical systems.

    sage: load("rational-preperiodic-QQ.sage")
    sage: f, label = dynabase_systems[0]

Pure Python - no Sage needed to write the files. Each map is written over the
field of its table row, in the model the table displays (render.choose_coeffs).
A field is rebuilt from its label: QQ, a quadratic field from its LMFDB label
(the polredabs defining polynomial is determined by the discriminant, and the
stored coefficients are in its generator a, as normalize_field_NF makes them),
or the defining polynomial itself for a field not in the LMFDB. Other LMFDB
labels (degree 3+) can't be rebuilt without the LMFDB, so those maps are left
out with a comment and a printed warning.
"""

import os
import re

from labels import is_lmfdb_label
from render import choose_coeffs, format_label

SITE_URL = 'https://dynabase.org'


def field_polynomial(label):
    """
    The defining polynomial (in t) of the field with this label, None for QQ.
    Raises NotImplementedError for an LMFDB label of degree 3 or more.
    """
    if not is_lmfdb_label(label):
        return label.replace('x', 't')  # a defining-polynomial label, in x
    n, r, D, _ = (int(v) for v in label.split('.'))
    if n == 1:
        return None
    if n == 2:
        D = D if r == 2 else -D  # real (signature 2) or imaginary (0) quadratic
        if D % 4 == 1:
            c = (1 - D) // 4
            return f't^2 - t {"+" if c >= 0 else "-"} {abs(c)}'
        return f't^2 {"-" if D > 0 else "+"} {abs(D) // 4}'
    raise NotImplementedError(f'field {label}: only QQ and quadratic LMFDB labels can be rebuilt')


def sage_homog_poly(coeffs):
    """coeffs[i] = coefficient of x^(d-i) y^i (get_coefficients' convention) -> Sage expression"""
    d = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        c = (c or '0').strip()
        if c == '0':
            continue
        mono = '*'.join(m for m in (
            '' if d - i == 0 else ('x' if d - i == 1 else f'x^{d - i}'),
            '' if i == 0 else ('y' if i == 1 else f'y^{i}')) if m)
        neg = re.fullmatch(r'-\d+(/\d+)?', c) is not None  # a negative rational: write it with ' - '
        mag = c[1:] if neg else c
        coeff = mag if re.fullmatch(r'\d+(/\d+)?', mag) else f'({mag})'
        terms.append((neg, coeff if not mono else (mono if mag == '1' else f'{coeff}*{mono}')))
    if not terms:
        return '0'
    out = ('-' if terms[0][0] else '') + terms[0][1]
    for neg, term in terms[1:]:
        out += (' - ' if neg else ' + ') + term
    return out


def sage_point(point):
    """a stored point string, e.g. '(0 : 1)' or '(1/2*a : 1)', as a point of P"""
    if not point:
        return 'None'
    coords = [c.strip() for c in point.strip().strip('()').split(':')]
    return f'P({", ".join(coords)})'


def write_sage_file(path, title, rows, citations_by_id, dimension=1, model_of=None, field_of=None,
                    with_points=False):
    """
    Write the .sage file for these DB rows (in table order) to path.
    model_of(row): the model to export (default: the displayed one);
    field_of(row): the field label to define the map over (default: the row's).
    with_points: also give each map its smallest_height_point (small height tables),
    making the entries [map, label, point]; the point is in the exported model's
    coordinates, which is why model_of must be smallest_height_model there.
    Returns the number of maps written.
    """
    body, fields_used = [], False
    n, current_field, skipped = 0, object(), []
    for row in rows:
        field = field_of(row) if field_of else row['base_field_label']
        coeffs = choose_coeffs(row, model_of(row) if model_of else None)
        label = format_label(dimension, row)
        if not coeffs:
            skipped.append((label, 'no model stored'))
            continue
        if field != current_field:
            try:
                poly = field_polynomial(field)
            except NotImplementedError as e:
                skipped.append((label, str(e)))
                continue
            current_field = field
            body.append('')
            if poly is None:
                body.append('K = QQ')
            else:
                fields_used = True
                body.append(f'K.<a> = NumberField({poly})  # {field}')
            body.append('P.<x,y> = ProjectiveSpace(K, 1)')
        cites = ', '.join(citations_by_id[c]['label'] for c in (row.get('citations') or [])
                          if c in citations_by_id)
        comment = [cites] if cites else []
        if with_points and row.get('smallest_height_ratio') is not None:
            comment.append(f'height ratio {float(row["smallest_height_ratio"]):.5g}')
        if comment:
            body.append('# ' + '; '.join(comment))
        polys = ', '.join(sage_homog_poly(c) for c in coeffs)
        entry = f'DynamicalSystem([{polys}], domain=P), {label!r}'
        if with_points:
            entry += ', ' + sage_point(row.get('smallest_height_point'))
        body.append(f'dynabase_systems.append([{entry}])')
        n += 1
    for label, why in skipped:
        body.append(f'# left out: {label} ({why})')
        print(f'  sage export {path}: left out {label} ({why})')
    names = 'K, a, P, x, y, R, t' if fields_used else 'K, P, x, y'
    lines = [
        f'# Dynabase ({SITE_URL}): {title}',
        '#',
        '# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of',
        ('# [map, label, point] triples in table order: the map as a DynamicalSystem over the'
         if with_points else
         '# [map, label] pairs in table order: the map as a DynamicalSystem over the field of'),
        ('# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the'
         if with_points else
         '# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).'),
    ] + ([
        '# point of smallest known height ratio, a point of the map\'s domain.',
    ] if with_points else []) + [
        f'# Loading also (re)defines {names}.',
        '',
    ]
    if fields_used:
        lines.append('R.<t> = QQ[]')
    lines.append('dynabase_systems = []')
    lines += body
    lines += [
        '',
        f'print("Dynabase: {n} dynamical system{"" if n == 1 else "s"} in dynabase_systems")',
        '',
    ]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return n
