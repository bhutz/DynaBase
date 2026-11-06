"""
Run the data files with their computations done in parallel.

Loading has to stay in order: a map's function_id, its graph rows and which map a table
keeps for a graph all follow the load order, and a map is compared with those loaded
before it. So the database is still written by one process, in order, and only the
computations are parallel, in three steps for each data file (extreme_examples.sage):

1. start_collecting: load the data file with add_function_all_NF only noting each map
   that isn't stored yet. Nothing is computed or written.
2. precompute_jobs: fork a worker per map, num_cpus at a time. Each runs the real
   add_function_all_NF on its own connection, records every computation's result
   (run_in_child's key), and rolls back. Workers see only what's committed and never
   touch the LMFDB (field_helpers_NF.no_lmfdb): lookups come from what step 1 found.
3. Load the data file normally. A computation with a recorded result uses it; anything
   else is computed then, so a worker failing or seeing different inputs only costs time.

A timeout recorded by a worker is reused too, which is the one way the result can differ
from a serial load: a computation near its limit can time out under load.
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

_originals = {}


def default_num_cpus():
    """Half of the CPUs available to this process, or the DYNABASE_CPUS environment variable."""
    requested = os.environ.get('DYNABASE_CPUS')
    if requested:
        return max(1, int(requested))
    return max(1, len(os.sched_getaffinity(0)) // 2)


def start_collecting():
    """Until stop_collecting, a data file loaded here only adds its new maps to the returned list."""
    jobs = {}

    def collect(F, my_cursor, citations=[], log_file=sys.stdout, timeout=30, smallest_height_point=None):
        key = (str(list(F)), str(F.base_ring()), timeout, str(smallest_height_point))
        jobs.setdefault(key, (F, timeout, smallest_height_point))

    def nothing(*args, **kwds):
        return None

    for name, stand_in in [('add_function_all_NF', collect), ('add_citations_NF', nothing),
                           ('add_automorphism_group_NF', nothing)]:
        _originals[name] = getattr(helpers, name)
        setattr(helpers, name, stand_in)
    return jobs


def stop_collecting():
    for name, original in _originals.items():
        setattr(helpers, name, original)
    _originals.clear()


def precompute_jobs(jobs, num_cpus):
    """Fill in run_in_child's recorded results for these maps, num_cpus workers at a time."""
    jobs = list(jobs.values())
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
            F, timeout, point = jobs[i]
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            helpers.add_function_all_NF(F, cursor, log_file=log_file, timeout=timeout,
                                        smallest_height_point=point)
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
