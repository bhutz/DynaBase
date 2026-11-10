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

from functions.parallel_load import MapList, add_maps_NF

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_automorphisms_log.txt"
log_file = open(path_to_log, 'w', 1)

# the file's maps, in order; added (and computed) together at the end
maps = MapList()

# maps with a given exact automorphism group, polynomials and rational maps of any degree

###########################################
#de Faria-Hutz, arXiv:1509.06670 / dFH2018, Figure 1 (Exact Automorphism Groups):
#for each finite subgroup of PGL_2, a map defined over QQ whose automorphism group
#is exactly that group. The cyclic and dihedral groups are infinite families with
#the degree depending on n, so they can't be stored as families; their first few
#members are stored instead:
#
#  C_n:    (x^(n+1) + x*y^n : y^(n+1)), degree n+1, n = 2..8
#  D_2n:   (y^(n-1) : x^(n-1)), degree n-1, n = 3..8 (n = 2 is degree 1, so D_4
#          is not covered by this formula)
#  S_4, A_5: as printed.
#
#The paper's A_4 map is over QQ(sqrt(-3)), and its Theorem 4.8 says no map over QQ
#has automorphism group A_4. Gontmacher-Hutz-Jorgenson-Srimani-Xu (GHJSX2021,
#Section 2/3.1) found (z^3 - 3)/(-3z^2), over QQ, with automorphism group A_4; that
#map is used instead.
#
#The automorphism group is computed over QQbar; its type is stored as GAP's
#StructureDescription (C2, ..., S3 for D_6, D4 for D_8, A4, S4, A5). 
######################

P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()
timeout = int(120) #DYNABASE_TIMEOUT overrides it

#(map, citations)
func_list = []

# cyclic C_n
for n in range(2, 9):
    func_list.append((DynamicalSystem([x**(n + 1) + x*y**n, y**(n + 1)]), ['dFH2018']))

# dihedral D_2n
for n in range(3, 9):
    func_list.append((DynamicalSystem([y**(n - 1), x**(n - 1)]), ['dFH2018']))

# tetrahedral A_4: (z^3 - 3)/(-3z^2)
func_list.append((DynamicalSystem([x**3 - 3*y**3, -3*x**2*y]), ['GHJSX2021']))

# octahedral S_4
func_list.append((DynamicalSystem([-x**5 + 5*x*y**4, 5*x**4*y - y**5]), ['dFH2018']))
# the same map as written in Miasnikov-Stout-Williams, arXiv:1408.5655 / Miasnikov2017,
# Example 1: (z^5 - 5z)/(1 - 5z^4), the single point of the A_4 = S_4 locus in degree 5
# (function 438, checked 2026-10-12); this only adds the citation
func_list.append((DynamicalSystem([x**5 - 5*x*y**4, y**5 - 5*x**4*y]), ['Miasnikov2017']))

# icosahedral A_5
func_list.append((DynamicalSystem([-(x**11 + 66*x**6*y**5 - 11*x*y**10),
                                   11*x**10*y + 66*x**5*y**6 - y**11]), ['dFH2018']))

###########################################
#Gontmacher-Hutz-Jorgenson-Srimani-Xu, arXiv:2007.15483 / GHJSX2021, Sections 2 and 4
# (summarized in the introduction): the automorphism locus in degrees 3 and 4.
# For a family, the member of smallest height, integers preferred on ties, whose
# automorphism group over QQbar is exactly the family's group - smaller parameters
# can give a larger group, e.g. a = 0 in the D_2 families is 1/z^3, with group D_4.
# Each was checked in Sage. The single classes 1/z^3 (D_4), the A_4 map above and
# 1/z^4 (D_5) are already in the dFH2018 lists; listing them again adds the citation
# GHJSX2021.

# degree 2: the rational maps' groups are C_2 and
# S_3; S_3 is the D_6 map (y^2 : x^2) above, and for C_2 the smallest height example,
# z + 1/z. Cited to Milnor1993, whose symmetry locus of quadratic rational maps gives the degree 2
# groups (C_2 generically, S_3 at one point).
func_list.append((DynamicalSystem([x**2 + y**2, x*y]), ['Milnor1993']))                # (z^2 + 1)/z: C_2

# degree 3
func_list.append((DynamicalSystem([y**3, x**3]), ['GHJSX2021']))                       # 1/z^3: D_4 (= C_4 locus)
func_list.append((DynamicalSystem([x**3 - 3*y**3, -3*x**2*y]), ['GHJSX2021']))         # A_4
func_list.append((DynamicalSystem([x**3 + y**3, x**2*y]), ['GHJSX2021']))              # C_3: (z^3 + a)/(a z^2), a = 1
func_list.append((DynamicalSystem([2*x**2*y + y**3, x**3 + 2*x*y**2]), ['GHJSX2021'])) # C_2 x C_2: (a z^2 + 1)/(z^3 + a z), a = 2
func_list.append((DynamicalSystem([2*x**2*y - y**3, x**3 - 2*x*y**2]), ['GHJSX2021'])) # C_2 x C_2: (a z^2 - 1)/(z^3 - a z), a = 2
func_list.append((DynamicalSystem([x**3, x**2*y + y**3]), ['GHJSX2021']))              # C_2: (z^3 + a z)/(b z^2 + 1), (a, b) = (0, 1)
func_list.append((DynamicalSystem([y**3, x**3 + x*y**2]), ['GHJSX2021']))              # C_2: (a z^2 + 1)/(z^3 + b z), (a, b) = (0, 1)

# degree 4
func_list.append((DynamicalSystem([y**4, x**4]), ['GHJSX2021']))                       # 1/z^4: D_5 (= C_5 locus)
func_list.append((DynamicalSystem([x**4 + y**4, x**3*y]), ['GHJSX2021']))              # C_4: (z^4 + 1)/(k z^3), k = 1
func_list.append((DynamicalSystem([x**4, y**4]), ['GHJSX2021']))                       # S_3 (D_3): (z^4 + k z)/(k z^3 + 1), k = 0, i.e. z^4
func_list.append((DynamicalSystem([x**4, x**3*y + y**4]), ['GHJSX2021']))              # C_3: (z^4 + k1 z)/(k2 z^3 + 1), (k1, k2) = (0, 1)
func_list.append((DynamicalSystem([x**4 + y**4, x*y**3]), ['GHJSX2021']))              # C_2: (z^4 + k1 z^2 + 1)/(k2 z^3 + k3 z), (k1, k2, k3) = (0, 0, 1)

###########################################
# Polynomials (Fujimura-Nishizawa, FN1997, symmetry loci of polynomial maps): a
# polynomial of degree d conjugate to z^d has the dihedral group of order 2(d-1) as
# automorphism group; any other one has a cyclic group C_m with m dividing d-1, and
# has C_m exactly when its monic centered form is z*g(z^m). So these are all the Aut
# groups a polynomial can have. One example of each, for every degree d <= 10, with
# all coefficients 1:
#  z^d                       dihedral of order 2(d-1) (GAP: C2, C2 x C2, S3, D4, ...)
#  z^d + z                   C_(d-1)
#  z^d + z^(m+1)             C_m, for each divisor 1 < m < d-1 of d-1
# Several are already in the database (z^2 from
# Poonen1998, z^(n+1) + z from dFH2018, z^4 from GHJSX2021); for those this only
# adds the FN1997 citation.
for d in range(2, 11):
    func_list.append((DynamicalSystem([x**d, y**d]), ['FN1997']))
    for m in ZZ(d - 1).divisors():
        if m == 1:
            continue
        e = 1 if m == d - 1 else m + 1  # z^d + z^e has automorphism group C_m
        func_list.append((DynamicalSystem([x**d + x**e*y**(d - e), y**d]), ['FN1997']))

# Creates the maps list and needed call data
for F, cites in func_list:
    maps.add(F, cites, timeout=timeout)




# add them all: computed in parallel, written in order (functions/parallel_load.py)
add_maps_NF(maps, my_session, my_cursor, log_file=log_file)

my_session.commit()
log_file.close()

#my_session.close()
