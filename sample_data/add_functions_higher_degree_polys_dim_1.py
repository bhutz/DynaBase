from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF
from functions.function_dim_1_helpers_NF import add_citations_NF

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_log.txt"
log_file = open(path_to_log, 'w', 1)

###########################################
#polynomials of degree 4 through 15, one table per degree
#Doyle-Hyde Examples
#arXiv:2201.11707 / DH2025
#Table 2: f(z) = N(z)/D with f([m]) in [n] for [k] = {1,...,k}, degrees 4-9
#(the d=2 and d=3 rows are in the quadratic/cubic files).
#Table 4: degrees 10-15, given only by the interpolating values
#(f(1), ..., f(d+1)); f is recovered by Lagrange interpolation.
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['DH2025']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# Table 2 - each N(z)/D entered as [N(x,y), D*y^d]

# d=4, m=10, n=8: f(z) = (z^4 - 22z^3 + 167z^2 - 506z + 552)/24
func_list.append(DynamicalSystem([x**4 - 22*x**3*y + 167*x**2*y**2 - 506*x*y**3 + 552*y**4, 24*y**4]))

# d=5, m=13, n=9: f(z) = (z^5 - 35z^4 + 445z^3 - 2485z^2 + 5794z - 3600)/120
func_list.append(DynamicalSystem([x**5 - 35*x**4*y + 445*x**3*y**2 - 2485*x**2*y**3 + 5794*x*y**4 - 3600*y**5, 120*y**5]))

# d=6, m=14, n=10: f(z) = (z^6 - 45z^5 + 775z^4 - 6375z^3 + 25504z^2 - 45060z + 30960)/720
func_list.append(DynamicalSystem([x**6 - 45*x**5*y + 775*x**4*y**2 - 6375*x**3*y**3 + 25504*x**2*y**4 - 45060*x*y**5 + 30960*y**6, 720*y**6]))

# d=7, m=15, n=15: f(z) = (z^7 - 56z^6 + 1246z^5 - 14000z^4 + 83629z^3 - 258104z^2 + 373764z - 151200)/5040
func_list.append(DynamicalSystem([x**7 - 56*x**6*y + 1246*x**5*y**2 - 14000*x**4*y**3 + 83629*x**3*y**4 - 258104*x**2*y**5 + 373764*x*y**6 - 151200*y**7, 5040*y**7]))

# d=8, m=16, n=16: f(z) = (z^8 - 68z^7 + 1918z^6 - 29036z^5 + 254989z^4 - 1309952z^3 + 3765012z^2 - 5343984z + 2862720)/20160
func_list.append(DynamicalSystem([x**8 - 68*x**7*y + 1918*x**6*y**2 - 29036*x**5*y**3 + 254989*x**4*y**4 - 1309952*x**3*y**5 + 3765012*x**2*y**6 - 5343984*x*y**7 + 2862720*y**8, 20160*y**8]))

# d=8, m=16, n=15: f(z) = (z^8 - 68z^7 + 1946z^6 - 30464z^5 + 282569z^4 - 1559852z^3 + 4836124z^2 - 7320336z + 4273920)/40320
func_list.append(DynamicalSystem([x**8 - 68*x**7*y + 1946*x**6*y**2 - 30464*x**5*y**3 + 282569*x**4*y**4 - 1559852*x**3*y**5 + 4836124*x**2*y**6 - 7320336*x*y**7 + 4273920*y**8, 40320*y**8]))

# d=9, m=19, n=17: f(z) = (z^9 - 90z^8 + 3426z^7 - 71820z^6 + 904449z^5 - 7002450z^4 + 32752124z^3 - 87183720z^2 + 116300160z - 55520640)/181440
func_list.append(DynamicalSystem([x**9 - 90*x**8*y + 3426*x**7*y**2 - 71820*x**6*y**3 + 904449*x**5*y**4 - 7002450*x**4*y**5 + 32752124*x**3*y**6 - 87183720*x**2*y**7 + 116300160*x*y**8 - 55520640*y**9, 181440*y**9]))

# Table 4 - (f(1), ..., f(d+1)) as printed; f by Lagrange interpolation
R = PolynomialRing(QQ, 'z')

def interpolated_system(values):
    """the dynamical system [f(x,y), y^d] on P^1 for the polynomial f of
    degree d = len(values) - 1 with f(k) = values[k-1] for k = 1, ..., d+1"""
    f = R.lagrange_polynomial([(k + 1, v) for k, v in enumerate(values)])
    d = f.degree()
    return DynamicalSystem([sum(c*x**i*y**(d - i) for i, c in enumerate(f.list())), y**d])

# d=10
func_list.append(interpolated_system([14, 6, 14, 6, 1, 6, 14, 17, 14, 10, 10]))

# d=11
func_list.append(interpolated_system([17, 1, 15, 3, 4, 14, 17, 12, 8, 9, 10, 6]))

# d=12
func_list.append(interpolated_system([17, 1, 17, 3, 4, 14, 17, 12, 6, 3, 3, 6, 12]))

# d=13
func_list.append(interpolated_system([17, 1, 17, 1, 3, 13, 16, 13, 10, 9, 9, 9, 8, 5]))

# d=14
func_list.append(interpolated_system([20, 4, 20, 4, 20, 14, 1, 8, 21, 18, 6, 6, 18, 21, 8]))

# d=15
func_list.append(interpolated_system([21, 1, 2, 20, 4, 1, 9, 10, 5, 3, 6, 11, 16, 19, 17, 12]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()


my_session.commit()

###########################################
#Hutz Examples (genetic algorithm)
#arXiv:2601.11482 / Hutz2026, Appendix (Extended Data Set): the maps from the
#Many Preperiodic Points ("many"), Long Periodic Cycles ("cycle") and Long
#Preperiodic Tail ("tail") tables; the Small Height ratio tables are not used.
#Each map is determined by the orbit the paper lists for it: f sends each orbit
#point to the next (d+2 points for a degree d polynomial, 2d+2 for a degree d
#rational map), recovered here by interpolation. Some tables print an orbit
#without its leading 0 (the map sends 0 to the first printed point); the 0 is
#restored below. Comments give the paper's result: (tail, cycle) of the orbit,
#after the number of rational preperiodic points in the "many" table. A map
#listed in several tables appears once. Not yet checked for repeated graph
#structures - the site generator drops repeats within a table.
cites = ['Hutz2026']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

R = PolynomialRing(QQ, 'z')

def orbit_poly_system(orbit):
    """the polynomial map of degree d = len(orbit) - 2 on P^1 sending each point
    of orbit to the next, by Lagrange interpolation"""
    f = R.lagrange_polynomial(list(zip(orbit[:-1], orbit[1:])))
    d = f.degree()
    return DynamicalSystem([sum(c*x**i*y**(d - i) for i, c in enumerate(f.list())), y**d])

func_list = []

# degree 4
# many 11 (1, 6), cycle (1, 6): orbit [0, 1, 10, 4, 8, 3]
func_list.append(orbit_poly_system([0, 1, 10, 4, 8, 3]))
# many 10 (3, 3): orbit [0, 1, 6, -3, -6, -1]
func_list.append(orbit_poly_system([0, 1, 6, -3, -6, -1]))
# cycle (1, 6): orbit [0, 1, 5, 4, 6, 2]
func_list.append(orbit_poly_system([0, 1, 5, 4, 6, 2]))
# cycle (1, 6): orbit [0, 1, 3, -1, -2, -5]
func_list.append(orbit_poly_system([0, 1, 3, -1, -2, -5]))
# cycle (0, 6): orbit [0, 1, 4, -1, -2, 3]
func_list.append(orbit_poly_system([0, 1, 4, -1, -2, 3]))
# tail (5, 1) 7: orbit [0, 1, -1, 2, -3, 4]
func_list.append(orbit_poly_system([0, 1, -1, 2, -3, 4]))
# tail (5, 1) 7: orbit [0, 1, -1, 2, -2, 3]
func_list.append(orbit_poly_system([0, 1, -1, 2, -2, 3]))
# tail (5, 1) 8: orbit [0, 1, -3, -2, 2, -5]
func_list.append(orbit_poly_system([0, 1, -3, -2, 2, -5]))
# tail (5, 1) 7: orbit [0, 1, 5, -1, 2, 9]
func_list.append(orbit_poly_system([0, 1, 5, -1, 2, 9]))

# degree 5
# many 12(1, 6): orbit [0, 1, 3, 5, -7, -9, -11]
func_list.append(orbit_poly_system([0, 1, 3, 5, -7, -9, -11]))
# many 11(1, 6): orbit [0, -1, 2, -5, 1, -4, 3]
func_list.append(orbit_poly_system([0, -1, 2, -5, 1, -4, 3]))
# many 11(5, 2): orbit [0, -1, 3, -7, -6, -4, 5]
func_list.append(orbit_poly_system([0, -1, 3, -7, -6, -4, 5]))
# many 11(3, 7): orbit [0, 1, -2, 2, -3, -1, 3]
func_list.append(orbit_poly_system([0, 1, -2, 2, -3, -1, 3]))
# many 11(4, 3): orbit [0, -1, -2, -4, -3, -5, 3]
func_list.append(orbit_poly_system([0, -1, -2, -4, -3, -5, 3]))
# cycle (0, 8): orbit [0, 1, 7, 5, -1, 3, 8]
func_list.append(orbit_poly_system([0, 1, 7, 5, -1, 3, 8]))
# cycle (0, 8): orbit [0, 1, 8, 3, 7, 6, -1]
func_list.append(orbit_poly_system([0, 1, 8, 3, 7, 6, -1]))
# cycle (0, 8): orbit [0, 1, -1, 9, 7, 3, 6]
func_list.append(orbit_poly_system([0, 1, -1, 9, 7, 3, 6]))
# tail (6, 2): orbit [0, -1, -2, 3, 5, 6, 7]
func_list.append(orbit_poly_system([0, -1, -2, 3, 5, 6, 7]))
# tail (6, 1): orbit [0, -1, 6, 4, 8, 1, 7]
func_list.append(orbit_poly_system([0, -1, 6, 4, 8, 1, 7]))
# tail (6, 1): orbit [0, 1, 3, 2, 4, -1, 6]
func_list.append(orbit_poly_system([0, 1, 3, 2, 4, -1, 6]))

# degree 6
# many 12 (5, 4): orbit [0, 1, -9, -2, -8, -3, -7, -1]
func_list.append(orbit_poly_system([0, 1, -9, -2, -8, -3, -7, -1]))
# many 12 (5, 3): orbit [0, 1, -3, -4, -5, -1, 2, -7]
func_list.append(orbit_poly_system([0, 1, -3, -4, -5, -1, 2, -7]))
# many 12 (6, 2): orbit [0, 1, 3, 8, 9, 7, 10, 6]
func_list.append(orbit_poly_system([0, 1, 3, 8, 9, 7, 10, 6]))
# many 12 (4, 4): orbit [0, -1, -6, -2, -9, -10, -3, -8]
func_list.append(orbit_poly_system([0, -1, -6, -2, -9, -10, -3, -8]))
# many 12(4, 4): orbit [0, 1, 2, 3, 5, 8, 9, 10]
func_list.append(orbit_poly_system([0, 1, 2, 3, 5, 8, 9, 10]))
# many 12 (6, 2): orbit [0, -1, -2, -5, -7, 2, -4, -9]
func_list.append(orbit_poly_system([0, -1, -2, -5, -7, 2, -4, -9]))
# many 12 (5, 3): orbit [0, -1, -4, 4, -6, 3, -3, 1]
func_list.append(orbit_poly_system([0, -1, -4, 4, -6, 3, -3, 1]))
# cycle (1, 8): orbit [0, 1, -8, -5, -1, 2, -7, -4]
func_list.append(orbit_poly_system([0, 1, -8, -5, -1, 2, -7, -4]))
# cycle (1, 8): orbit [0, -1, 4, 1, -6, -3, -5, -2]
func_list.append(orbit_poly_system([0, -1, 4, 1, -6, -3, -5, -2]))
# cycle (0, 8): orbit [0, -1, -12, -10, -3, -13, 1, -14]
func_list.append(orbit_poly_system([0, -1, -12, -10, -3, -13, 1, -14]))
# cycle (0, 8): orbit [0, -1, 1, -10, -13, -3, -14, -12]
func_list.append(orbit_poly_system([0, -1, 1, -10, -13, -3, -14, -12]))
# cycle (0, 8): orbit [0, -1, -11, -14, -13, -10, 1, -3]
func_list.append(orbit_poly_system([0, -1, -11, -14, -13, -10, 1, -3]))
# cycle (0, 8): orbit [0, -1, -11, -14, -10, 1, -13, -3]
func_list.append(orbit_poly_system([0, -1, -11, -14, -10, 1, -13, -3]))
# tail (7, 2): orbit [0, 1, 2, 7, 6, 5, 8, 9]
func_list.append(orbit_poly_system([0, 1, 2, 7, 6, 5, 8, 9]))
# tail (7, 2): orbit [0, 1, 3, 7, 4, 2, 8, 9]
func_list.append(orbit_poly_system([0, 1, 3, 7, 4, 2, 8, 9]))
# tail (7, 1): orbit [0, 1, -2, -1, 3, 4, 6, -3]
func_list.append(orbit_poly_system([0, 1, -2, -1, 3, 4, 6, -3]))
# tail (7, 1): orbit [0, 1, 3, -2, 2, -1, -3, 4]
func_list.append(orbit_poly_system([0, 1, 3, -2, 2, -1, -3, 4]))
# tail (7, 1): orbit [0, -1, 2, 6, 7, 1, 5, 8]
func_list.append(orbit_poly_system([0, -1, 2, 6, 7, 1, 5, 8]))
# tail (7, 1): orbit [0, 1, 2, 4, 6, 7, 8, -1]
func_list.append(orbit_poly_system([0, 1, 2, 4, 6, 7, 8, -1]))
# tail (7, 1): orbit [0, 1, 3, 2, 5, 4, -1, 6]
func_list.append(orbit_poly_system([0, 1, 3, 2, 5, 4, -1, 6]))

# degree 7
# many 13(9, 1), tail (9, 1): orbit [1, 2, -8, -1, -4, -6, -2, -7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 2, -8, -1, -4, -6, -2, -7]))
# many 12(6, 4): orbit [-1, -6, -2, -8, -9, -4, -5, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -6, -2, -8, -9, -4, -5, -3]))
# many 12(7, 2): orbit [-1, -2, -3, -4, -6, -9, -7, -8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -2, -3, -4, -6, -9, -7, -8]))
# many 12(5, 4): orbit [-1, -9, -7, -2, -6, -5, -8, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -9, -7, -2, -6, -5, -8, -3]))
# many 12(6, 3): orbit [-1, -5, -4, -6, -3, -8, 1, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -5, -4, -6, -3, -8, 1, -2]))
# many 12(0, 9): orbit [-1, -6, -7, -5, -2, -8, -3, -4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -6, -7, -5, -2, -8, -3, -4]))
# many 12(1, 8): orbit [-1, -6, -8, -7, -9, -4, -2, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -6, -8, -7, -9, -4, -2, -3]))
# many 12(0, 9): orbit [-1, 1, -6, -2, -3, -7, -4, -5] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 1, -6, -2, -3, -7, -4, -5]))
# cycle (0, 10): orbit [-1, 1, -2, -6, -8, -5, -4, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 1, -2, -6, -8, -5, -4, -3]))
# cycle (1, 9): orbit [1, -7, -5, -4, -8, -1, -2, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -7, -5, -4, -8, -1, -2, -3]))
# cycle (0, 9): orbit [1, -1, -2, -6, -3, -4, 2, -5] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -1, -2, -6, -3, -4, 2, -5]))
# tail (9, 1): orbit [1, 3, 5, 4, 6, -1, -3, -4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 3, 5, 4, 6, -1, -3, -4]))
# tail (8, 2): orbit [-1, -7, -2, -5, -9, -4, -6, -8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -7, -2, -5, -9, -4, -6, -8]))
# tail (8, 2): orbit [1, -6, 2, -2, -8, -3, -5, -1] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -6, 2, -2, -8, -3, -5, -1]))

# degree 8
# many 12: orbit [-1, 3, 2, -2, 1, -3, -6, -4, -7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 3, 2, -2, 1, -3, -6, -4, -7]))
# many 12: orbit [1, -2, -3, -1, 3, 5, 4, 7, 6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -2, -3, -1, 3, 5, 4, 7, 6]))
# many 12: orbit [-1, -2, 3, 7, 6, 1, 4, 5, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -2, 3, 7, 6, 1, 4, 5, 2]))
# many 12: orbit [1, 4, 6, 7, -1, -2, 2, 5, 8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 4, 6, 7, -1, -2, 2, 5, 8]))
# many 12: orbit [-1, 4, 6, 9, 8, 2, 3, 1, 7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 4, 6, 9, 8, 2, 3, 1, 7]))
# cycle (0, 11): orbit [1, 7, 5, 8, 6, 9, 4, 2, 3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 7, 5, 8, 6, 9, 4, 2, 3]))
# cycle (0, 11): orbit [1, 9, 4, 8, 6, 2, 7, 5, 3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 9, 4, 8, 6, 2, 7, 5, 3]))
# cycle (0, 11): orbit [1, 3, 7, 2, 5, 8, 6, 4, 9] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 3, 7, 2, 5, 8, 6, 4, 9]))
# cycle (0, 11): orbit [1, -1, -5, -7, -6, -9, -8, -4, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -1, -5, -7, -6, -9, -8, -4, -2]))
# cycle (0, 11): orbit [1, -1, -2, -3, -4, -7, -6, -5, -8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -1, -2, -3, -4, -7, -6, -5, -8]))
# tail (9, 2): orbit [-1, -5, -7, -3, -8, -2, -6, -4, -9] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -5, -7, -3, -8, -2, -6, -4, -9]))
# tail (9, 2): orbit [1, 5, -1, 8, 2, 7, 6, 4, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 5, -1, 8, 2, 7, 6, 4, -2]))
# tail (9, 1): orbit [1, 4, 7, -1, 10, 8, 2, 11, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 4, 7, -1, 10, 8, 2, 11, -2]))
# tail (9, 1): orbit [1, 3, 9, 2, 7, 11, 10, -1, 8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 3, 9, 2, 7, 11, 10, -1, 8]))
# tail (9, 1): orbit [1, 7, 6, -1, -2, 4, 5, 2, 8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 7, 6, -1, -2, 4, 5, 2, 8]))
# tail (9, 1): orbit [1, 10, -1, 6, 7, 11, 5, 4, 8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 10, -1, 6, 7, 11, 5, 4, 8]))

# degree 9
# tail (10, 1): orbit [1, -1, 6, 11, 8, 9, 10, 4, 3, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -1, 6, 11, 8, 9, 10, 4, 3, 2]))
# tail (10, 1): orbit [1, 5, 12, 4, 9, 7, 8, 11, 3, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 5, 12, 4, 9, 7, 8, 11, 3, 2]))
# tail (10, 1): orbit [1, 5, 7, 9, 11, -1, 8, 4, 3, 10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 5, 7, 9, 11, -1, 8, 4, 3, 10]))
# tail (10, 1): orbit [1, 8, 11, 4, 10, 7, 3, 6, -1, 9] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 8, 11, 4, 10, 7, 3, 6, -1, 9]))
# tail (10, 1): orbit [1, 5, 4, 6, -2, 7, 10, -1, 9, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 5, 4, 6, -2, 7, 10, -1, 9, 2]))
# cycle (1, 11): orbit [1, 3, 2, 4, 8, 9, 10, 6, 7, 5] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 3, 2, 4, 8, 9, 10, 6, 7, 5]))
# cycle (0, 11): orbit [-1, 2, -5, -2, 4, 1, -4, 3, -3, 5] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 2, -5, -2, 4, 1, -4, 3, -3, 5]))
# cycle (0, 11): orbit [1, 2, -1, 3, -5, -4, -2, 4, -6, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 2, -1, 3, -5, -4, -2, 4, -6, -3]))
# cycle (0, 11): orbit [1, 5, -5, -3, 2, -1, -4, -2, 3, 4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 5, -5, -3, 2, -1, -4, -2, 3, 4]))
# cycle (0, 11): orbit [-1, -5, -6, 4, 1, -2, -4, -3, 3, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -5, -6, 4, 1, -2, -4, -3, 3, 2]))

# degree 10
# cycle (0, 12): orbit [1, 2, 3, -6, -11, -2, -7, 4, -9, -10, -1] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 2, 3, -6, -11, -2, -7, 4, -9, -10, -1]))
# cycle (0, 12): orbit [-1, 1, 2, 3, -12, -3, -10, -11, -6, -9, -8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 1, 2, 3, -12, -3, -10, -11, -6, -9, -8]))
# cycle (0, 12): orbit [-1, -8, -14, -4, -6, -3, -2, -9, -11, -13, -10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -8, -14, -4, -6, -3, -2, -9, -11, -13, -10]))
# cycle (0, 12): orbit [-1, -9, -2, -7, -4, 1, -6, -3, 2, 3, -8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -9, -2, -7, -4, 1, -6, -3, 2, 3, -8]))
# cycle (0, 12): orbit [-1, -2, 1, -10, -13, 2, -9, -4, -11, -12, -3] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -2, 1, -10, -13, 2, -9, -4, -11, -12, -3]))
# tail (11, 1): orbit [-1, 2, 4, -7, -5, 1, -4, -3, -8, 3, -6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 2, 4, -7, -5, 1, -4, -3, -8, 3, -6]))
# tail (11, 1): orbit [-1, 3, -9, 4, -5, 5, 2, -8, -4, 1, -6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 3, -9, 4, -5, 5, 2, -8, -4, 1, -6]))
# tail (11, 1): orbit [-1, -2, 2, 1, 3, -8, -9, -6, -7, -11, -10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -2, 2, 1, 3, -8, -9, -6, -7, -11, -10]))
# tail (11, 1): orbit [1, -2, 2, -6, -7, 3, 5, -5, -4, 4, -1] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -2, 2, -6, -7, 3, 5, -5, -4, 4, -1]))
# tail (11, 1): orbit [1, -6, -1, -2, -4, 2, -3, 3, -5, -7, 4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -6, -1, -2, -4, 2, -3, 3, -5, -7, 4]))

# degree 11
# cycle (0, 13): orbit [1, 7, 4, -2, 11, 6, -4, -1, 12, 9, 8, 10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 7, 4, -2, 11, 6, -4, -1, 12, 9, 8, 10]))
# cycle (0, 13): orbit [1, 8, -3, 6, -1, 4, 3, 2, 7, -4, 5, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 8, -3, 6, -1, 4, 3, 2, 7, -4, 5, -2]))
# cycle (0, 13): orbit [1, 8, 6, 3, 4, 9, 7, -1, 2, 5, 10, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 8, 6, 3, 4, 9, 7, -1, 2, 5, 10, -2]))
# cycle (0, 13): orbit [1, 6, 2, 8, 10, 9, 5, 4, -2, 3, -1, 7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 6, 2, 8, 10, 9, 5, 4, -2, 3, -1, 7]))
# tail (12, 1): orbit [-1, -5, -7, -2, -8, -11, 3, -6, 1, -10, -9, 2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -5, -7, -2, -8, -11, 3, -6, 1, -10, -9, 2]))
# tail (12, 1): orbit [1, -10, 2, -6, -12, -4, -1, -3, 3, -5, -11, -9] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -10, 2, -6, -12, -4, -1, -3, 3, -5, -11, -9]))
# tail (12, 1): orbit [-1, -7, -2, 1, -9, -12, -6, 3, -11, -8, -10, 4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -7, -2, 1, -9, -12, -6, 3, -11, -8, -10, 4]))
# tail (12, 1): orbit [-1, -8, 1, -2, -4, -9, -7, 2, -10, -11, -12, -6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -8, 1, -2, -4, -9, -7, 2, -10, -11, -12, -6]))

# degree 12
# cycle (0, 14): orbit [-1, -6, 7, -7, -8, 4, 6, -3, 5, -4, 1, 3, -5] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -6, 7, -7, -8, 4, 6, -3, 5, -4, 1, 3, -5]))
# cycle (0, 14): orbit [1, 4, -4, 5, 7, -3, 8, 2, -6, 9, -7, -5, 6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 4, -4, 5, 7, -3, 8, 2, -6, 9, -7, -5, 6]))
# cycle (0, 14): orbit [1, 10, -3, 8, 6, 4, -6, 7, -4, -5, -2, 9, -1] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 10, -3, 8, 6, 4, -6, 7, -4, -5, -2, 9, -1]))
# cycle (0, 14): orbit [-1, 6, -5, -7, -2, 5, -6, 4, -8, -3, 3, 7, -4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 6, -5, -7, -2, 5, -6, 4, -8, -3, 3, 7, -4]))
# tail (13, 1): orbit [1, 10, 13, 3, 6, 9, 2, 5, 12, -1, 4, 11, -2] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 10, 13, 3, 6, 9, 2, 5, 12, -1, 4, 11, -2]))
# tail (13, 1): orbit [1, 9, -1, -6, -2, 5, 4, 8, 3, 6, -4, -7, 7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 9, -1, -6, -2, 5, 4, 8, 3, 6, -4, -7, 7]))
# tail (13, 1): orbit [1, 3, -3, -5, -2, 6, 4, -4, 8, 10, 2, 5, 9] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 3, -3, -5, -2, 6, 4, -4, 8, 10, 2, 5, 9]))
# tail (13, 1): orbit [1, -12, -6, -15, -4, -3, -1, -8, -13, -11, -2, -5, -10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -12, -6, -15, -4, -3, -1, -8, -13, -11, -2, -5, -10]))

# degree 13
# cycle (0, 15): orbit [-1, -3, -2, -13, 1, -12, -10, -11, -5, -7, -8, -6, -9, -4] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -3, -2, -13, 1, -12, -10, -11, -5, -7, -8, -6, -9, -4]))
# cycle (0, 15): orbit [-1, 1, 3, 10, 13, 6, 5, 11, 9, 14, 2, 4, 12, 7] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, 1, 3, 10, 13, 6, 5, 11, 9, 14, 2, 4, 12, 7]))
# cycle (0, 15): orbit [1, -3, 2, 8, 7, -5, -4, -1, 5, 4, -2, 6, 3, 10] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, -3, 2, 8, 7, -5, -4, -1, 5, 4, -2, 6, 3, 10]))
# cycle (0, 15): orbit [1, 9, 8, 10, 12, 6, 11, 2, 5, 4, -2, -3, 13, -1] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 9, 8, 10, 12, 6, 11, 2, 5, 4, -2, -3, 13, -1]))
# tail (14, 1): orbit [-1, -2, -4, -12, -14, -8, -10, -3, -5, -7, -13, -11, 1, -6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, -1, -2, -4, -12, -14, -8, -10, -3, -5, -7, -13, -11, 1, -6]))
# tail (14, 1): orbit [1, 7, -3, -1, 8, 2, 3, 5, -5, 4, 10, -4, 6, -6] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 7, -3, -1, 8, 2, 3, 5, -5, 4, 10, -4, 6, -6]))
# tail (14, 1): orbit [1, 6, 9, 15, 2, -1, 4, 12, 10, 13, 11, 3, 14, 8] (printed without its leading 0)
func_list.append(orbit_poly_system([0, 1, 6, 9, 15, 2, -1, 4, 12, 10, 13, 11, 3, 14, 8]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()


my_session.commit()

###########################################
#postcritically finite (PCF) quartic polynomials over QQ
#Fraser, On PCF polynomials (PhD dissertation, Fraser2024), Theorem 4.9: exactly
#16 conjugacy classes, Table 4.1. The six bicritical classes are entered in the
#Table 4.2 form (critical points moved to 0 and 1), which the dissertation gives
#as conjugate to the Table 4.1 representatives.
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['Fraser2024']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# unicritical: z^4
func_list.append(DynamicalSystem([x**4, y**4]))
# unicritical: -z^4 + 1
func_list.append(DynamicalSystem([-x**4 + y**4, y**4]))
# unicritical: -2z^4 + 1
func_list.append(DynamicalSystem([-2*x**4 + y**4, y**4]))
# bicritical (Table 4.2): -3z^4 + 4z^3
func_list.append(DynamicalSystem([-3*x**4 + 4*x**3*y, y**4]))
# bicritical (Table 4.2): 3z^4 - 4z^3 + 1
func_list.append(DynamicalSystem([3*x**4 - 4*x**3*y + y**4, y**4]))
# bicritical (Table 4.2): z^4 - 4/3z^3 + 4/3
func_list.append(DynamicalSystem([x**4 - QQ(4)/3*x**3*y + QQ(4)/3*y**4, y**4]))
# bicritical (Table 4.2): -z^4 + 4/3z^3 + 1
func_list.append(DynamicalSystem([-x**4 + QQ(4)/3*x**3*y + y**4, y**4]))
# bicritical (Table 4.2): 4z^4 - 16/3z^3 + 4/3
func_list.append(DynamicalSystem([4*x**4 - QQ(16)/3*x**3*y + QQ(4)/3*y**4, y**4]))
# bicritical (Table 4.2): -4z^4 + 16/3z^3
func_list.append(DynamicalSystem([-4*x**4 + QQ(16)/3*x**3*y, y**4]))
# tricritical: z^4 - 2z^2 + 1
func_list.append(DynamicalSystem([x**4 - 2*x**2*y**2 + y**4, y**4]))
# tricritical: 2z^4 - 4z^2 + 1
func_list.append(DynamicalSystem([2*x**4 - 4*x**2*y**2 + y**4, y**4]))
# tricritical: z^4 - 2z^2
func_list.append(DynamicalSystem([x**4 - 2*x**2*y**2, y**4]))
# tricritical: 1/3z^4 + 4/3z
func_list.append(DynamicalSystem([QQ(1)/3*x**4 + QQ(4)/3*x*y**3, y**4]))
# tricritical: 4z^4 - 4z^2
func_list.append(DynamicalSystem([4*x**4 - 4*x**2*y**2, y**4]))
# tricritical: 4z^4 - 4z^2 + 1
func_list.append(DynamicalSystem([4*x**4 - 4*x**2*y**2 + y**4, y**4]))
# tricritical, Chebyshev T_4: 8z^4 - 8z^2 + 1
func_list.append(DynamicalSystem([8*x**4 - 8*x**2*y**2 + y**4, y**4]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()


my_session.commit()

log_file.close()

#my_session.close()
