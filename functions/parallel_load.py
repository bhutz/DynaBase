"""
Add a data file's maps, with their computations done in parallel.

A data file compiles its maps into a MapList (each with its citations and options), then
calls add_maps_NF once. Loading has to stay in order: a map's function_id, its graph rows
and which map a table keeps for a graph all follow the load order, and a map is compared
with those loaded before it. So the database is still written by one process, in order,
and only the computations are parallel:

1. Find the maps that need add_function_all_NF: those not in the database (the guard,
   model_in_database_NF), and, with compute_missing, the stored ones too (to rerun their
   missing steps). The rest only get their citations.
2. Fork a worker per such map, build_cpus() at a time. Each runs the real
   add_function_all_NF on its own connection, records every computation's result
   (run_in_child's key), and rolls back. Workers see only what's committed and never
   touch the LMFDB (field_helpers_NF.no_lmfdb): lookups come from what step 1 found.
3. Add the maps in order. A computation with a recorded result uses it; anything else is
   computed then, so a worker failing or seeing different inputs only costs time.

A timeout recorded by a worker is reused too, which is the one way the result can differ
from a serial load: a computation near its limit can time out under load.

The build settings (environment variables, read when add_maps_NF runs, so a data file
loaded on its own uses them too): DYNABASE_CPUS (build_cpus), DYNABASE_TIMEOUT
(build_timeout) and DYNABASE_COMPUTE_MISSING (build_compute_missing).
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

import os
import sys
import time

import psycopg2
import psycopg2.extras
from sage.parallel.decorate import parallel

import config
import fields.field_helpers_NF as field_helpers
import functions.function_dim_1_helpers_generic as generic
import functions.function_dim_1_helpers_NF as helpers

# the rows workers insert roll back, but the numbers they took don't
SEQUENCES = [('functions_dim_1_NF', 'function_id'), ('graphs_dim_1_NF', 'graph_id'),
             ('rational_preperiodic_dim_1_NF', 'id')]

def precompute_jobs(jobs, num_cpus):
    """
    Fill in run_in_child's recorded results for these maps, num_cpus workers at a time.
    jobs: a list of (F, timeout, smallest_height_point, compute_missing).
    """
    if not jobs:
        return

    @parallel(ncpus=num_cpus)
    def work(i):
        #this process's stdout goes back to the parent; the load after this logs it all
        sys.stdout = open(os.devnull, 'w')
        log_file = open(os.devnull, 'w')
        field_helpers.no_lmfdb = True
        generic.start_recording_computations()
        conn = psycopg2.connect(**config.load_config())
        error = None
        try:
            F, timeout, point, compute_missing = jobs[i]
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            helpers.add_function_all_NF(F, cursor, log_file=log_file, timeout=timeout,
                                        smallest_height_point=point, compute_missing=compute_missing)
        except BaseException as e:
            error = repr(e)
        finally:
            conn.rollback()
            conn.close()
        return generic.recorded_computations(), error

    start = time.time()
    print(f'computing {len(jobs)} maps with {num_cpus} processes')
    sys.stdout.flush()
    done, failed = 0, 0
    for _, result in work(list(range(len(jobs)))):
        done += 1
        if isinstance(result, tuple):
            computations, error = result
            generic.add_recorded_computations(computations)
            failed += error is not None
        else:
            failed += 1  # the worker crashed: the load computes this map itself
        print(f'  {done}/{len(jobs)} maps, {time.time() - start:.0f} s')
        sys.stdout.flush()
    if failed:
        print(f'  {failed} workers did not finish: the load computes what is left')

    conn = psycopg2.connect(**config.load_config())
    cursor = conn.cursor()
    for table, column in SEQUENCES:
        cursor.execute(f"""SELECT setval(pg_get_serial_sequence('{table}', '{column}'),
            COALESCE(MAX({column}), 1), MAX({column}) IS NOT NULL) FROM {table}""")
    conn.commit()
    conn.close()


class MapList:
    """
    The maps a data file adds, in order, each with its citations (string labels) and the
    options add_function_all_NF takes. compute_missing=None means build_compute_missing().
    """
    def __init__(self):
        self.entries = []

    def add(self, F, citations=[], timeout=30, smallest_height_point=None, compute_missing=None):
        self.entries.append({'F': F, 'citations': list(citations), 'timeout': timeout,
                             'point': smallest_height_point, 'compute_missing': compute_missing})

    def extend(self, Fs, citations=[], **options):
        for F in Fs:
            self.add(F, citations, **options)

    def __len__(self):
        return len(self.entries)


def add_maps_NF(maps, my_session, my_cursor, log_file=sys.stdout):
    """
    Add every map of the MapList maps, in order, committing after each: a map not in the
    database (model_in_database_NF) with add_function_all_NF, a stored one with only its
    citations, or with add_function_all_NF when compute_missing (to rerun its missing steps).
    The computations of the maps that need add_function_all_NF are done in parallel first,
    with build_cpus() processes (see the module docstring).
    """
    num_cpus = generic.build_cpus()
    default_missing = generic.build_compute_missing()
    entries = maps.entries
    for e in entries:
        if e['compute_missing'] is None:
            e['compute_missing'] = default_missing

    # quick check to see if the map is there
    def guard(e):
        if 'sigma_1' not in e:
            e['sigma_1'] = generic.sigma_hash(e['F'].sigma_invariants(1))
        return helpers.model_in_database_NF(e['F'], my_cursor, sigma_1=e['sigma_1'], log_file=log_file)

    # 1. the maps that need add_function_all_NF, judged on what is committed now
    jobs = {}
    for e in entries:
        found, _ = guard(e)
        if not found or e['compute_missing']:
            F = e['F']
            key = (str(list(F)), str(F.base_ring()), e['timeout'], str(e['point']), e['compute_missing'])
            jobs.setdefault(key, (F, e['timeout'], e['point'], e['compute_missing']))
    my_session.commit() # the workers see only what is committed
    log_file.write(f'{len(entries)} maps, {len(jobs)} to compute\n')

    # 2. their computations, in parallel
    if num_cpus > 1 and len(jobs) > 1:
        precompute_jobs(list(jobs.values()), num_cpus)

    # 3. add them, in order
    for e in entries:
        found, F_id = guard(e)
        if found and not e['compute_missing']:
            helpers.add_citations_NF(F_id, e['citations'], my_cursor, log_file=log_file)
        else:
            helpers.add_function_all_NF(e['F'], my_cursor, citations=e['citations'], log_file=log_file,
                timeout=e['timeout'], smallest_height_point=e['point'], compute_missing=e['compute_missing'])
        my_session.commit()
    generic.clear_recorded_computations()
