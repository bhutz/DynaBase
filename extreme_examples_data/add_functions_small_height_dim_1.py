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
log_file = open(path_to_log, 'a', 1)

#small canonical height ratio examples, polynomials and rational maps of every degree

###########################################
#Hutz Examples (genetic algorithm)
#arXiv:2601.11482 / Hutz2026, Appendix (Extended Data Set), Small Height Ratio
#tables: the 3 smallest ratios for each degree and type (polynomials of degree
#2-12, rational maps of degree 2-5; the degree 2 rational table has only 2 maps
#and the degree 13 table is empty). The ratio is hhat(0)/h_M(f), with h_M the
#largest height of the first sigma invariants. Each map is determined by the
#orbit of 0 the paper lists for it: f sends each orbit point to the next (d+2
#points for a degree d polynomial, 2d+2 for a degree d rational map), recovered
#here by interpolation. The tables for degree 7 and up print orbits without
#their leading 0; it is restored. Each entry gives the paper's ratio, and every
#map was checked to reproduce it (relative error < 3e-4).
#The point 0 is passed to add_function_all_NF, which stores its ratio as the
#smallest height (smallest_height_model 'original') instead of searching.
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

def orbit_rational_system(orbit):
    """the rational map N/D of degree d = (len(orbit) - 2)/2 on P^1 sending each
    point a of orbit to the next point b: N(a) - b*D(a) = 0 is linear in the
    coefficients of N and D, and its solution is unique up to scaling"""
    d = (len(orbit) - 2) // 2
    M = matrix(QQ, [[QQ(a)**j for j in range(d + 1)] + [-QQ(b)*QQ(a)**j for j in range(d + 1)]
                    for a, b in zip(orbit[:-1], orbit[1:])])
    v = M.right_kernel().basis()[0]
    return DynamicalSystem([sum(v[j]*x**j*y**(d - j) for j in range(d + 1)),
                            sum(v[d + 1 + j]*x**j*y**(d - j) for j in range(d + 1))])

#(type, orbit of 0, the paper's height ratio)
small_height = []

# degree 2 polynomial
small_height.append(('poly', [0, -2, 1, -3], 0.006604))
# the paper prints the orbit [0, 1, -1, 2] (0 is preperiodic there); this is the
# orbit of the map it prints, -1/6z^2 - 17/6z + 1, which has the stated ratio
small_height.append(('poly', [0, 1, -2, 6], 0.01102))
small_height.append(('poly', [0, 18, 21, 14], 0.01346))

# degree 2 rational
small_height.append(('rational', [0, -1, -16, 4, 8, 2], 0.0004657))
small_height.append(('rational', [0, 1, 6, -6, -5, -3], 0.001183))

# degree 3 polynomial
small_height.append(('poly', [0, 1, -3, -4, -8], 9.2099e-05))
small_height.append(('poly', [0, 1, 3, -1, -3], 0.00016547))
small_height.append(('poly', [0, 1, 2, 4, 3], 0.00016738))

# degree 3 rational
small_height.append(('rational', [0, -1, -7, 3, -11, 5, -3, -5], 3.079e-06))
small_height.append(('rational', [0, -1, 1, -25, 3, 7, 11, 15], 3.2584e-06))
small_height.append(('rational', [0, 1, -6, -1, -4, -3, 6, 3], 3.2983e-06))

# degree 4 polynomial
small_height.append(('poly', [0, 1, 4, 5, -1, 3], 2.9015e-06))
small_height.append(('poly', [0, 1, 7, 5, 8, 3], 2.9568e-06))
small_height.append(('poly', [0, 1, -3, -2, 2, -4], 3.0905e-06))

# degree 4 rational
small_height.append(('rational', [0, -1, -4, -3, -9, 2, -6, -2, -5, 1], 2.1843e-08))
small_height.append(('rational', [0, 1, 8, 5, -4, -1, -3, -2, 2, 4], 2.6346e-08))
small_height.append(('rational', [0, -1, -4, -5, 3, -9, -6, -3, -2, 1], 2.9735e-08))

# degree 5 polynomial
small_height.append(('poly', [0, -1, -2, -6, -4, -5, -3], 9.1519e-09))
small_height.append(('poly', [0, -1, -4, -3, -6, -5, -2], 1.6874e-08))
small_height.append(('poly', [0, -1, -4, -11, -8, -15, -12], 2.8227e-08))

# degree 5 rational
small_height.append(('rational', [0, 1, -1, 7, -17, 13, -27, -8, -2, 14, -29, 4], 3.6941e-10))
small_height.append(('rational', [0, 1, -14, 22, 14, -20, 7, -11, -2, 16, 25, -1], 3.7088e-10))
small_height.append(('rational', [0, -1, -91, -15, 1, 17, 6, -19, 23, -5, 2, -6], 3.7574e-10))

# degree 6 polynomial
small_height.append(('poly', [0, -1, -8, -9, -7, -10, -2, -4], 2.056e-09))
small_height.append(('poly', [0, 1, -1, -4, -9, -2, -7, -3], 2.1833e-09))
small_height.append(('poly', [0, 1, -4, -2, -5, -3, -1, -7], 2.3064e-09))

# degree 7 polynomial
small_height.append(('poly', [0, -1, 1, 11, 2, 10, 8, 9, 3], 1.0564e-10))
small_height.append(('poly', [0, 1, 5, -1, 14, 2, 10, 12, 13], 1.4693e-10))
small_height.append(('poly', [0, 1, 10, 13, -1, 12, 2, 15, 14], 1.5717e-10))

# degree 8 polynomial
small_height.append(('poly', [0, 1, 3, -10, -12, 2, -1, -9, -11, -8], 8.771e-13))
small_height.append(('poly', [0, 1, -2, -3, -9, -11, -10, -8, -1, 2], 1.1829e-12))
small_height.append(('poly', [0, -1, 3, -2, 2, -11, 1, -8, -10, -9], 1.3585e-12))

# degree 9 polynomial
small_height.append(('poly', [0, -1, -12, -9, 1, -4, -3, -8, -11, -10, 2], 1.7173e-14))
small_height.append(('poly', [0, -1, -3, -12, 2, -13, -11, 1, -4, -9, -10], 5.5356e-14))
small_height.append(('poly', [0, -1, -9, -14, -13, 2, -2, -12, -3, 1, -11], 7.5618e-14))

# degree 10 polynomial
small_height.append(('poly', [0, -1, 3, 15, 9, 12, 1, 10, 11, 4, 14, 2], 9.9368e-16))
small_height.append(('poly', [0, 1, 7, 13, 6, 8, 12, 9, 5, 2, 3, -1], 1.3982e-15))
small_height.append(('poly', [0, 1, 2, 12, -1, 11, 3, 10, 9, 13, 8, 14], 1.5071e-15))

# degree 11 polynomial
small_height.append(('poly', [0, -1, 1, -10, -9, -12, -11, -8, -14, -3, -2, 2, -13], 7.3446e-17))
# the paper prints the ratio as 7.8701 10^{17}
small_height.append(('poly', [0, 1, -2, -11, -4, -6, -10, -14, -12, -1, -8, -13, -15], 7.8701e-17))
small_height.append(('poly', [0, -1, -9, -2, -8, -3, -6, -10, 1, -5, -12, 3, -11], 9.7411e-17))

# degree 12 polynomial
small_height.append(('poly', [0, 1, -2, -11, -8, -1, 12, 7, 3, -18, 8, 5, 2, -15], 5.9715e-19))
small_height.append(('poly', [0, -1, -10, 3, -3, -8, -2, 2, -5, 9, 1, -6, 8, 16], 1.5221e-18))
small_height.append(('poly', [0, -1, -10, 3, 7, 4, -3, -12, -15, -2, 1, 9, -4, 20], 1.7538e-18))

for map_type, orbit, ratio in small_height:
    if map_type == 'poly':
        F = orbit_poly_system(orbit)
    else:
        F = orbit_rational_system(orbit)
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        #the paper's point is 0
        F_id = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file, smallest_height_point=[0,1])
    my_session.commit()


my_session.commit()

log_file.close()

#my_session.close()
