# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

# Can be run independently, but must set the environment variables to change the defaults
# of DYNABASE_CPUS, DYNABASE_TIMEOUT, DYNABASE_COMPUTE_MISSING

load_attach_path('/home/ben/dynabase')
import sys
sys.path.append('/home/ben/dynabase')

from fields.field_helpers_NF import normalize_field_NF, lmfdb_field_label_NF
from functions.parallel_load import MapList, add_maps_NF
from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_NF
from functions.function_dim_1_helpers_NF import identify_graph, simple_cycles
from functions.function_dim_1_helpers_generic import build_timeout

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_special_cases_log.txt"
log_file = open(path_to_log, 'w', 1)

# the file's maps, in order; added (and computed) together at the end
maps = MapList()

###########################################
# This file is to treat special cases where the default computations fail. For each map it
# adds the function (if it isn't stored yet, without the other computations) and computes
# its rational preperiodic points here, serially and with no time limit (they are pre-tested
# to be fast). Then add_maps_NF adds all of them, in parallel, with the usual timeouts
# (DYNABASE_TIMEOUT if set): add_function_all_NF skips the preperiodic points, as that row
# is now stored. A map this file inserted gets every other step (compute_missing=True);
# one already stored reruns its missing steps only with DYNABASE_COMPUTE_MISSING.
# The models are built exactly as in the higher degree file.

def function_id_for(F):
    """(is_new, the id of F), adding F (without the other computations) if it isn't stored"""
    found, F_id = model_in_database_NF(F, my_cursor, log_file=log_file)
    if found:
        return False, F_id
    return add_function_NF(F, my_cursor, log_file=log_file, timeout=build_timeout(30))

def preperiodic_row_exists(F_id, field_label):
    my_cursor.execute("""SELECT id FROM rational_preperiodic_dim_1_NF
        WHERE function_id=%s AND base_field_label=%s""", [F_id, field_label])
    return my_cursor.rowcount != 0

def store_preperiodic_graph(F_id, F, field_label, preper):
    """insert the rational preperiodic graph preper of F over its base field, as
    add_rational_preperiodic_points_NF does"""
    preperiodic_data = {'function_id': F_id, 'base_field_label': field_label}
    # one point per cycle; before identify_graph, which relabels the graph in place
    periodic = []
    for c in simple_cycles(preper): #not preper.all_simple_cycles(), see simple_cycles
        periodic.append([str(t) for t in c[0]])
    preperiodic_data['rational_periodic_points'] = periodic

    #identify graph and add if necessary
    preperiodic_data['graph_id'] = identify_graph(preper, F, my_cursor, 1, log_file=log_file)

    my_cursor.execute("""INSERT INTO rational_preperiodic_dim_1_NF
        (function_id, base_field_label, rational_periodic_points, graph_id)
        VALUES
        (%(function_id)s, %(base_field_label)s, %(rational_periodic_points)s, %(graph_id)s)
        RETURNING id """, preperiodic_data)
    if my_cursor.rowcount == 0: #error check rowcount after insert
        log_file.write('add_rational_preperiodic_points_NF failure: ' + str(F_id) + ' not inserted \n')
    else:
        log_file.write('add_rational_preperiodic_points_NF: ' + str(F_id) + ' successfully inserted \n')
    log_file.write('rational preperiodic points computed for:' + str(F_id) + '\n')

def add_preperiodic_special_NF(f, cites, compute_graph):
    """add f if needed, then its rational preperiodic graph compute_graph(f) over its own
    field, unless a row for that field is already stored (so a rerun adds no duplicate);
    then queue f for add_maps_NF, which adds the rest of its data"""
    is_new, F_id = function_id_for(f)
    bool_lmfdb, field_label = lmfdb_field_label_NF(f.base_ring(), log_file=log_file)
    if preperiodic_row_exists(F_id, field_label):
        log_file.write('rational preperiodic points already known for:' + str(F_id) + ' over ' + str(field_label) + '\n')
    else:
        log_file.write('starting rational preperiodic points for:' + str(F_id) + '\n')
        try:
            store_preperiodic_graph(F_id, f, field_label, compute_graph(f))
        except Exception as e:
            log_file.write('failure: preperiodic points for:' + str(F_id) + 'with error:' + str(e) + '\n')
            #raise
    my_session.commit()
    #inserted just now: compute everything else, whatever DYNABASE_COMPUTE_MISSING says
    maps.add(f, cites, compute_missing=True if is_new else None)


###########################################
# Hutz Examples (genetic algorithm)
# arXiv:2601.11482 / Hutz2026, Appendix (Extended Data Set): the degree 9 map
# -(z^9 - 2z^8 - 46z^7 + 140z^6 + 833z^5 - 2338z^4 - 13364z^3 + 2200z^2 + 133536z + 40320)/40320,
# built from its orbit as in the higher degree polynomial file.
#
# Just need to change the lifting prime in the rational periodic points algorithm

cites = ['Hutz2026']
P = ProjectiveSpace(QQ, 1, 'x,y')
x, y = P.gens()

R = PolynomialRing(QQ, 'z')

def orbit_poly_system(orbit):
    """the polynomial map of degree d = len(orbit) - 2 on P^1 sending each point
    of orbit to the next, by Lagrange interpolation (as in the higher degree file)"""
    f = R.lagrange_polynomial(list(zip(orbit[:-1], orbit[1:])))
    d = f.degree()
    return DynamicalSystem([sum(c*x**i*y**(d - i) for i, c in enumerate(f.list())), y**d])

def hutz_preperiodic_graph(f):
    return f.rational_preperiodic_graph(lifting_prime=13)

f = orbit_poly_system([0, -1, 2, -5, -2, 4, 1, -4, 3, -3, 5])
add_preperiodic_special_NF(f, cites, hutz_preperiodic_graph)


###########################################
# Doyle-Hindes Examples
# arXiv:2510.14067 / DoHi2025, Table 1 (Theorem 1.1 and its corollary): the 7 maps over
# cyclotomic fields of degree 4 to 12, built as in the higher degree polynomial file.
# The complete computation, with no assumption from the paper (Theorem 1.1 needs d at least
# an unknown D(q,t)): the possible periods by reduction modulo primes of K, then every
# K-rational root of the dynatomic polynomials of those periods (any height), then all
# their K-rational preimages.
#
# The current possible_periods() in Sage does not work over numberfields, so
# this version was needed

cites = ['DoHi2025']

R = PolynomialRing(QQ, 't')
t = R.gen()
func_list = []
for poly, d, c_of in [(t**4 - t**2 + 1, 7, lambda v: v**3 - v),  # (2,2), Q(zeta_12)
                      (t**4 - t**2 + 1, 11, lambda v: -v**3),  # (2,1,1)
                      (t**6 + t**3 + 1, 6, lambda v: v**3),  # (1)d, Q(zeta_9)
                      (t**6 + t**3 + 1, 7, lambda v: v**5 + v**2),  # (3)
                      (t**8 + 1, 4, lambda v: -v**4 - 1),  # (1)b, Q(zeta_16)
                      (t**12 - t**6 + 1, 6, lambda v: v**6 - 1),  # (1)e, Q(zeta_36)
                      (t**12 - t**6 + 1, 6, lambda v: QQ(-1))]:  # (2)c
    K0 = NumberField(poly, 'v')
    c0 = c_of(K0.gen())
    K, phi = normalize_field_NF(K0)
    P = ProjectiveSpace(K, 1, 'x,y')
    x, y = P.gens()
    func_list.append(DynamicalSystem([x**d + phi(c0)*y**d, y**d]))

def possible_periods_K(f, num_rational_primes=10, pbound=5000):
    """
    Possible periods of the K-rational periodic points of f (a map on P^1 over a number
    field K with integral coefficients): the intersection of possible_periods() of f
    modulo the degree 1 primes of K above the first num_rational_primes unramified rational
    primes that have one. Sage's finite field possible_periods needs a prime field, and its
    bound on the periods (m, m*r, m*r*p, and m*r*4, m*r*8 for p = 2) assumes p unramified.
    Primes of bad reduction are skipped (x^d + c with c integral has none).
    """
    K = f.base_ring()
    disc = K.discriminant()
    periods = None
    used = []
    for p in primes(2, pbound):
        if len(used) >= num_rational_primes:
            break
        if disc % p == 0:
            continue
        degree_one = [Pr for Pr in K.primes_above(p) if Pr.residue_class_degree() == 1]
        good = False
        for Pr in degree_one:
            k = Pr.residue_field()
            Pk = ProjectiveSpace(k, 1, 'x,y')
            X, Y = Pk.gens()
            g = DynamicalSystem([sum(k(coeff)*X**e[0]*Y**e[1] for e, coeff in poly.dict().items())
                                 for poly in f], domain=Pk)
            if g.degree() != f.degree() or not g.is_morphism():
                continue
            s = set(g.possible_periods())
            periods = s if periods is None else periods & s
            good = True
        if good:
            used.append(p)
    if periods is None:
        raise ValueError('no degree 1 primes of good reduction found')
    log_file.write('possible periods ' + str(sorted(periods)) + ' from the primes of K above ' + str(used) + '\n')
    return sorted(periods)

def dohi_preperiodic_graph(f):
    K = f.base_ring()
    P = f.domain()
    z = PolynomialRing(K, 'z').gen()
    periodic = [P(1, 0)] #infinity, the only point with y = 0
    for n in possible_periods_K(f):
        Dyn = f.dynatomic_polynomial(n) #homogeneous in x, y
        periodic += [P(r, 1) for r in Dyn(z, 1).roots(multiplicities=False)]

    preper = set([])
    for Q in periodic:
        preper = preper.union(set(f.connected_rational_component(Q)))
    return f._preperiodic_points_to_cyclegraph(preper)

for f in func_list:
    add_preperiodic_special_NF(f, cites, dohi_preperiodic_graph)


my_session.commit()

# everything else for all of them: computed in parallel, written in order (functions/parallel_load.py)
add_maps_NF(maps, my_session, my_cursor, log_file=log_file)

log_file.close()

#my_session.close()
