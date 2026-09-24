"""
Read-only data access for the static site generator.

Connects with plain psycopg2 (no Sage needed - the site only reads columns
that have already been computed and stored by the sample_data/ scripts).

IMPORTANT: as of 2026-09-22 the 'postgresql' (Neon, remote) section in
database.ini is stale/outdated. Generate against 'postgresql_local' until
told otherwise.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg2
import psycopg2.extras
from config import load_config

from labels import field_degree_from_label


def connect(section='postgresql_local'):
    config = load_config(section=section)
    conn = psycopg2.connect(**config)
    return conn


def get_functions_dim_1(conn, degree, is_polynomial):
    """
    All dimension-1 (function, field) pairs of the given degree and
    polynomial/rational type: one row per rational_preperiodic_dim_1_NF row,
    i.e. per field the function's rational preperiodic points were computed
    over - not just the function's own base field. A function first loaded
    over QQ can also carry data over quadratic fields (e.g. a Doyle-Faber-Krumm
    x^2+c with rational c); each such pair belongs in the table for *its*
    field's degree. base_field_label / base_field_degree here are the pair's
    field, the degree read off the label by field_degree_from_label (in
    Python, since a field not in the LMFDB is labeled by its polynomial).

    Functions with no preperiodic data at all still get one row (over their
    own field, graph columns null) so the caller can report them.

    Ordered by preperiodic row id = insertion order = the order the
    sample_data/ files were loaded, so "first" means first loaded.
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT
            f.function_id,
            COALESCE(r.base_field_label, f.base_field_label) AS base_field_label,
            r.id AS preperiodic_id,
            f.sigma_one,
            f.sigma_two,
            f.ordinal,
            f.citations,
            f.display_model,
            (f.original_model).coeffs   AS original_coeffs,
            (f.reduced_model).coeffs    AS reduced_coeffs,
            (f.monic_centered).coeffs   AS monic_coeffs,
            r.graph_id,
            g.cardinality,
            g.periodic_cycles,
            g.preperiodic_components,
            g.max_tail
        FROM functions_dim_1_nf f
        LEFT JOIN rational_preperiodic_dim_1_nf r ON r.function_id = f.function_id
        LEFT JOIN graphs_dim_1_nf g ON g.graph_id = r.graph_id
        WHERE f.degree = %(degree)s AND f.is_polynomial = %(is_polynomial)s
        ORDER BY r.id NULLS LAST, f.function_id
    """, {'degree': degree, 'is_polynomial': is_polynomial})
    rows = [dict(row) for row in cur.fetchall()]
    for row in rows:
        row['base_field_degree'] = field_degree_from_label(row['base_field_label'])
    return rows


def get_pcf_functions_dim_1(conn, degree, is_polynomial):
    """
    Dimension-1 functions of the given degree and type with is_pcf true, with
    their critical portrait (the critical points and their forward orbits, a
    graphs_dim_1_NF row - critical_portrait_graph_id is stored as varchar).
    Being PCF is a property of the function itself, so this is one row per
    function over its own field, not per (function, field) pair.
    Also returns how many functions of this degree/type have is_pcf null
    (not computed), so the caller can report them.
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT
            f.function_id,
            f.base_field_label,
            f.sigma_one,
            f.sigma_two,
            f.ordinal,
            f.citations,
            f.display_model,
            (f.original_model).coeffs   AS original_coeffs,
            (f.reduced_model).coeffs    AS reduced_coeffs,
            (f.monic_centered).coeffs   AS monic_coeffs,
            f.cp_cardinality,
            f.cp_field_of_defn,
            f.rational_twists,
            g.cardinality               AS portrait_cardinality,
            g.periodic_cycles           AS portrait_cycles,
            g.preperiodic_components    AS portrait_components
        FROM functions_dim_1_nf f
        LEFT JOIN graphs_dim_1_nf g ON g.graph_id::varchar = f.critical_portrait_graph_id
        WHERE f.degree = %(degree)s AND f.is_polynomial = %(is_polynomial)s AND f.is_pcf
        ORDER BY f.function_id
    """, {'degree': degree, 'is_polynomial': is_polynomial})
    rows = [dict(row) for row in cur.fetchall()]
    for row in rows:
        row['base_field_degree'] = field_degree_from_label(row['base_field_label'])
    cur.execute("""
        SELECT count(*) FROM functions_dim_1_nf
        WHERE degree = %(degree)s AND is_polynomial = %(is_polynomial)s AND is_pcf IS NULL
    """, {'degree': degree, 'is_polynomial': is_polynomial})
    return rows, cur.fetchone()[0]


def get_extreme_source_rows(conn, degree):
    """
    Polynomial (function, field) pairs of the given degree whose field is QQ
    or quadratic, with their graph data - the source rows for the Extreme
    Examples page's per-degree "longest cycle" / "longest tail" tables. Pairs,
    not functions, for the same reason as get_functions_dim_1. Ordered by
    function_id (then field) so tie-breaking (in render.find_longest_*_row)
    is deterministic.
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT
            f.function_id,
            r.base_field_label,
            f.citations,
            f.display_model,
            (f.original_model).coeffs AS original_coeffs,
            (f.reduced_model).coeffs  AS reduced_coeffs,
            (f.monic_centered).coeffs AS monic_coeffs,
            g.periodic_cycles,
            g.max_tail
        FROM functions_dim_1_nf f
        JOIN rational_preperiodic_dim_1_nf r ON r.function_id = f.function_id
        LEFT JOIN graphs_dim_1_nf g ON g.graph_id = r.graph_id
        WHERE f.degree = %(degree)s
          AND f.is_polynomial = true
        ORDER BY f.function_id, r.base_field_label
    """, {'degree': degree})
    rows = [dict(row) for row in cur.fetchall()]
    for row in rows:
        row['base_field_degree'] = field_degree_from_label(row['base_field_label'])
    return [row for row in rows if row['base_field_degree'] in (1, 2)]


def get_citations_by_id(conn):
    """{citations.id: {label, authors, journal, year, citation, mathscinet}} for every
    row in the citations table - small (~20 rows), loaded once per generation run
    and used to resolve functions_dim_1_NF.citations (an int[] of these ids)."""
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, label, authors, journal, year, citation, mathscinet FROM citations")
    return {row['id']: dict(row) for row in cur.fetchall()}


def get_summary_counts(conn):
    """(degree, is_polynomial, base_field_degree) -> count, for the included-data summary page."""
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT degree, is_polynomial, base_field_degree, count(*) AS n
        FROM functions_dim_1_nf
        GROUP BY 1, 2, 3
        ORDER BY 1, 2, 3
    """)
    return [dict(row) for row in cur.fetchall()]
