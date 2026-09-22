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


def connect(section='postgresql_local'):
    config = load_config(section=section)
    conn = psycopg2.connect(**config)
    return conn


def get_functions_dim_1(conn, degree, is_polynomial):
    """
    All dimension-1 functions of the given degree and polynomial/rational
    type, joined with their rational-preperiodic-point graph data (for their
    own base field). One row per function (LEFT JOIN, so functions without
    computed preperiodic-point data yet still appear, with nulls).
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT
            f.function_id,
            f.base_field_label,
            f.base_field_degree,
            f.sigma_one,
            f.sigma_two,
            f.ordinal,
            f.citations,
            f.display_model,
            (f.original_model).coeffs   AS original_coeffs,
            (f.reduced_model).coeffs    AS reduced_coeffs,
            (f.monic_centered).coeffs   AS monic_coeffs,
            g.cardinality,
            g.periodic_cycles,
            g.preperiodic_components
        FROM functions_dim_1_nf f
        LEFT JOIN rational_preperiodic_dim_1_nf r
               ON r.function_id = f.function_id
              AND r.base_field_label = f.base_field_label
        LEFT JOIN graphs_dim_1_nf g ON g.graph_id = r.graph_id
        WHERE f.degree = %(degree)s AND f.is_polynomial = %(is_polynomial)s
        ORDER BY f.base_field_degree, f.function_id
    """, {'degree': degree, 'is_polynomial': is_polynomial})
    return [dict(row) for row in cur.fetchall()]


def get_extreme_source_rows(conn, degree):
    """
    Polynomial functions of the given degree, defined over QQ or a quadratic
    field, with their graph data - the source rows for the Extreme Examples
    page's per-degree "longest cycle" / "longest tail" tables. Ordered by
    function_id so tie-breaking (in render.find_longest_*_row) is deterministic.
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT
            f.function_id,
            f.base_field_label,
            f.base_field_degree,
            f.citations,
            f.display_model,
            (f.original_model).coeffs AS original_coeffs,
            (f.reduced_model).coeffs  AS reduced_coeffs,
            (f.monic_centered).coeffs AS monic_coeffs,
            g.periodic_cycles,
            g.max_tail
        FROM functions_dim_1_nf f
        LEFT JOIN rational_preperiodic_dim_1_nf r
               ON r.function_id = f.function_id
              AND r.base_field_label = f.base_field_label
        LEFT JOIN graphs_dim_1_nf g ON g.graph_id = r.graph_id
        WHERE f.degree = %(degree)s
          AND f.is_polynomial = true
          AND f.base_field_degree IN (1, 2)
        ORDER BY f.function_id
    """, {'degree': degree})
    return [dict(row) for row in cur.fetchall()]


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
