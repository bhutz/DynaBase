"""
Functions to help working with functions in dimension 1
over any field.

AUTHORS:

- Ben Hutz (2023-10): initial version

"""

# ****************************************************************************
#       Copyright (C) 2023 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from copy import copy
from sage.graphs.digraph import DiGraph
from sage.misc.verbose import set_verbose
from sage.rings.fraction_field import is_FractionField
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_general

#sagerel -pip install pysha3
import sha3  #adds shake to hashlib
import hashlib  #for shake
import ctypes
import os
import signal
import sys
from sage.parallel.decorate import fork


###########################################
# General Functions
###########################################

def get_coefficients(F, d=None):
    """
        Get all coefficients of F (including 0) in lexicographic order
    """
    if d is None:
        d = F.degree()
    C = []
    x, y = F.parent().gens()
    for i in range(0,d+1):
        C.append(str(F.coefficient({x:d-i,y:i})))
    return C

def get_post_critical(Fbar):
    """
    Determine the critical and post-critical set of the given map
    """
    set_verbose(None)
    post_crit = set()
    crit = Fbar.critical_points()
    images_needed = copy(crit)
    while len(images_needed) != 0:
        Q = images_needed.pop()
        Q2 = Fbar(Q)
        if Q2 not in post_crit:
           post_crit.add(Q2)
           images_needed.append(Q2)
    return crit, list(post_crit)

def choose_display_model(function_id, my_cursor, log_file=sys.stdout):
    """
    From the list of computed models set one as display.
    If the model required a field extension over original, then it is not chosen.
    The order of preference is

    chebyshev
    monic centered
    reduced
    original
    """
    #determine which to display
    query={}
    query['function_id']=function_id
    my_cursor.execute("""SELECT (original_model).base_field_label FROM functions_dim_1_NF where function_id = %(function_id)s""", query)
    original_field_label = my_cursor.fetchone()['base_field_label']
#    my_cursor.execute("""SELECT is_chebyshev FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
#    is_cheby = my_cursor.fetchone()['is_chebyshev']
#    if is_cheby:
#        query['display_model'] = 'chebyshev'
#        my_cursor.execute("""UPDATE functions_dim_1_NF
#            SET display_model = %(display_model)s
#            WHERE
#                function_id = %(function_id)s
#            """, query)
#        return True
    my_cursor.execute("""SELECT is_polynomial FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
    is_poly = my_cursor.fetchone()['is_polynomial']
    if is_poly:
        my_cursor.execute("""SELECT (monic_centered).base_field_label FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
        mc_field_label = my_cursor.fetchone()['base_field_label']
        if original_field_label == mc_field_label:
            query['display_model'] = 'monic centered'
            my_cursor.execute("""UPDATE functions_dim_1_NF
                SET display_model = %(display_model)s
                WHERE
                    function_id = %(function_id)s
                """, query)
            return True
    my_cursor.execute("""SELECT (reduced_model).coeffs FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
    my_coeffs = my_cursor.fetchone()['coeffs']
    if not my_coeffs is None:
        my_cursor.execute("""SELECT (reduced_model).base_field_label FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
        red_field_label = my_cursor.fetchone()['base_field_label']
        if original_field_label == red_field_label:
            query['display_model'] = 'reduced'
            my_cursor.execute("""UPDATE functions_dim_1_NF
                SET display_model = %(display_model)s
                WHERE
                    function_id = %(function_id)s
                """, query)
            return True
#    my_cursor.execute("""SELECT (newton_model).coeffs FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
#    my_coeffs = my_cursor.fetchone()['coeffs']
#    if not my_coeffs is None:
#        my_cursor.execute("""SELECT (newton_model).base_field_label FROM functions_dim_1_NF where function_id = %(function_id)s""",query)
#        new_field_label = my_cursor.fetchone()['base_field_label']
#        if original_field_label == new_field_label:
#            query['display_model'] = 'newton'
#            my_cursor.execute("""UPDATE functions_dim_1_NF
#                SET display_model = %(display_model)s
#                WHERE
#                    function_id = %(function_id)s
#                """, query)
#            return True
    query['display_model'] = 'original'
    my_cursor.execute("""UPDATE functions_dim_1_NF
        SET display_model = %(display_model)s
        WHERE
            function_id = %(function_id)s
        """, query)
    return True

def graph_to_array(G):
    #graph to array
    n = G.num_verts()
    G.relabel(tuple([t for t in range(n)]))
    E = [-1 for i in range(n)]
    for v in G.edges():
        E[v[0]] = v[1]
    return E

def array_to_graph(E):
    #array to graph
    Ed = []
    for i in range(len(E)):
        Ed.append((i,E[i]))
    return DiGraph(Ed, loops=True)

class ChildTimeout(BaseException):
    """
    Raised by run_in_child when the child process is killed for taking too long.

    A BaseException, like cysignals' AlarmInterrupt which it replaces, so an
    'except Exception' does not swallow it.
    """
    pass


def run_in_child(compute, timeout=30, log_file=sys.stdout):
    """
    Return compute() evaluated in a forked child process (Sage's fork decorator),
    which is killed after timeout seconds (0 means no limit).

    Raises ChildTimeout on a timeout, and RuntimeError if compute raised (with its
    message) or the child crashed.

    Why a child process instead of a cysignals alarm: an alarm raises
    AlarmInterrupt by longjmp-ing out of whatever C/C++ library code is running
    (PARI, NTL, FLINT, Singular), which skips that library's cleanup (C++
    destructors, frees, internal bookkeeping). On 2026-09-25 a long data run that
    had timed out many times in heavy QQbar / number field computations
    segfaulted inside PARI while merely converting a polynomial for a resultant
    (add_reduced_model_NF on function 201, degree 13), a computation that is
    instant and fine in a fresh process. Killing a child leaves this process
    untouched, whatever state the computation was in, and the kill also works in
    C code that never checks for signals.

    (A 'Fatal Python error: Aborted' seen with faulthandler during those
    computations is not the cause: it is Sage's normal fallback when NTL runs out
    of FFT primes inverting a number field element of huge degree; NTL aborts,
    cysignals turns that into an NTLError, and Sage retries with PARI.)

    compute must not use the database cursor or the LMFDB connection (e.g.,
    get_sage_func_NF, get_sage_field_NF, lmfdb_field_label_NF): the child shares
    their sockets with this process. Do those before or after. Its result must be
    picklable. It may write to log_file.
    """
    #the child makes its own process group and reports its pid, so that afterwards the
    #whole group is killed: sage's fork only kills the child, and processes the child
    #forked (e.g. sage's parallel workers in automorphism_group) would keep running
    pid_read, pid_write = os.pipe()
    def child():
        os.close(pid_read)
        os.setpgid(0, 0)
        os.write(pid_write, str(os.getpid()).encode())
        os.close(pid_write) #before compute forks, so its workers don't hold the pipe open
        os.environ["CYSIGNALS_CRASH_NDEBUG"] = "yes" #skip the slow enhanced backtrace on a crash
        try:
            #no core dump on a crash: capturing one (WSL pipes it to a crash handler) takes
            #seconds for a process this size, so the crash would be reported as a timeout
            ctypes.CDLL(None).prctl(4, 0, 0, 0, 0) #PR_SET_DUMPABLE = 4
        except Exception:
            pass
        try:
            result = ('ok', compute())
        except Exception as e:
            result = ('error', str(e))
        log_file.flush()
        return result

    sys.stdout.flush()
    log_file.flush()
    try:
        result = fork(child, timeout=timeout)()
    finally:
        os.close(pid_write)
        child_pid = os.read(pid_read, 32) #the child has exited, so this doesn't block
        os.close(pid_read)
        if child_pid:
            try:
                os.killpg(int(child_pid), signal.SIGKILL)
            except ProcessLookupError:
                pass #nothing left in the group
    if isinstance(result, tuple):
        if result[0] == 'ok':
            return result[1]
        raise RuntimeError(result[1])
    #otherwise a string from sage's fork: 'NO DATA (timed out)', 'NO DATA' or 'INVALID DATA ...'
    if 'timed out' in result:
        raise ChildTimeout()
    raise RuntimeError('child process crashed: ' + result)
