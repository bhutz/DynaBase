"""
Field-label helpers shared by db.py and render.py. Pure Python - no Sage,
no database.

A field label is normally an LMFDB number field label (n.r.D.i, e.g.
'2.2.5.1'). A field not in the LMFDB is labeled by its defining polynomial in
x instead (e.g. 'x^2 - x - 1') - see lmfdb_field_label_NF in
fields/field_helpers_NF.py.
"""

import re


def is_lmfdb_label(label):
    """True for an LMFDB number field label (n.r.D.i, e.g. '2.2.5.1'); False
    for the defining-polynomial label (e.g. 'x^2 - x - 1') that
    lmfdb_field_label_NF in fields/field_helpers_NF.py uses for a field not in
    the LMFDB. Mirrors that file's is_lmfdb_label_NF, without needing Sage."""
    return re.fullmatch(r'\d+\.\d+\.\d+\.\d+', label or '') is not None


def field_degree_from_label(label):
    """Degree of the field a label names: the first component of an LMFDB
    label, or the degree of a defining-polynomial label (in x)."""
    if is_lmfdb_label(label):
        return int(label.split('.')[0])
    exponents = [int(e) for e in re.findall(r'x\^(\d+)', label)]
    return max(exponents) if exponents else 1
