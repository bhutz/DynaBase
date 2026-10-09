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

#rational functions of degree 3 and higher, one table per degree

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

func_list = []

# degree 3
# many 13 (6,2): orbit [0, 1, 2, 3, 5, 4, -7, 6]
func_list.append(orbit_rational_system([0, 1, 2, 3, 5, 4, -7, 6]))
# many 13 (6,2): orbit [0, -1, 1, -9, -15, 3, 9, 6]
func_list.append(orbit_rational_system([0, -1, 1, -9, -15, 3, 9, 6]))
# many 13 (2,6): orbit [0, -1, -2, -4, -3, -10, -8, -5]
func_list.append(orbit_rational_system([0, -1, -2, -4, -3, -10, -8, -5]))
# many 12 (4,5): orbit [0, -1, -2, 5, 1, 4, -5, 3]
func_list.append(orbit_rational_system([0, -1, -2, 5, 1, 4, -5, 3]))
# many 12 (7,1): orbit [0, 1, 11, 5, -1, 2, -7, 3]
func_list.append(orbit_rational_system([0, 1, 11, 5, -1, 2, -7, 3]))
# many 12 (6,3): orbit [0, -1, -2, -3, -6, 2, 4, 1]
func_list.append(orbit_rational_system([0, -1, -2, -3, -6, 2, 4, 1]))
# cycle (0, 8): orbit [0, 1, 5, -9, -5, -3, -1, 3]
func_list.append(orbit_rational_system([0, 1, 5, -9, -5, -3, -1, 3]))
# cycle (0, 8): orbit [0, 1, -1, 7, -5, -9, 3, -3]
func_list.append(orbit_rational_system([0, 1, -1, 7, -5, -9, 3, -3]))
# cycle (1, 8): orbit [0, -1, -3, -9, 3, 5, 15, 9]
func_list.append(orbit_rational_system([0, -1, -3, -9, 3, 5, 15, 9]))
# cycle (0, 8): orbit [0, 1, 2, -1, -4, 5, -2, -5]
func_list.append(orbit_rational_system([0, 1, 2, -1, -4, 5, -2, -5]))
# cycle (1, 8): orbit [0, -1, -7, 5, -5, 1, -3, -4]
func_list.append(orbit_rational_system([0, -1, -7, 5, -5, 1, -3, -4]))
# cycle (1, 8): orbit [0, 1, -3, -7, -5, -9, 7, 3]
func_list.append(orbit_rational_system([0, 1, -3, -7, -5, -9, 7, 3]))
# tail (8, 2): orbit [0, -1, 2, 3, -3, 11, 1, 5]
func_list.append(orbit_rational_system([0, -1, 2, 3, -3, 11, 1, 5]))
# tail (8, 2): orbit [0, 1, 3, 5, 7, 21, 6, 9]
func_list.append(orbit_rational_system([0, 1, 3, 5, 7, 21, 6, 9]))
# tail (7, 1): orbit [0, 1, -1, -2, -7, -5, -3, 3]
func_list.append(orbit_rational_system([0, 1, -1, -2, -7, -5, -3, 3]))
# tail (7, 1): orbit [0, -1, -2, -3, 7, 2, 3, -8]
func_list.append(orbit_rational_system([0, -1, -2, -3, 7, 2, 3, -8]))
# tail (7, 1): orbit [0, 1, 7, -1, -3, 5, -5, 3]
func_list.append(orbit_rational_system([0, 1, 7, -1, -3, 5, -5, 3]))

# degree 4
# many 11 (7, 3): orbit [0, 1, 3, 2, 5, -2, -3, -4, -5, -9]
func_list.append(orbit_rational_system([0, 1, 3, 2, 5, -2, -3, -4, -5, -9]))
# many 11 (1, 10): orbit [1, -1, 5, 7, 3, -5, -4, -3, -2] (printed without its leading 0)
func_list.append(orbit_rational_system([0, 1, -1, 5, 7, 3, -5, -4, -3, -2]))
# many 11, (1, 9): orbit [0, 1, -2, 7, -1, 3, -3, -7, 2, -5]
func_list.append(orbit_rational_system([0, 1, -2, 7, -1, 3, -3, -7, 2, -5]))
# cycle (0, 10): orbit [0, -1, -2, -4, 3, 6, 5, 4, -5, 1]
func_list.append(orbit_rational_system([0, -1, -2, -4, 3, 6, 5, 4, -5, 1]))
# cycle (0, 10): orbit [0, -1, -7, -9, 7, -5, -3, 5, 3, 1]
func_list.append(orbit_rational_system([0, -1, -7, -9, 7, -5, -3, 5, 3, 1]))
# cycle (1, 9): orbit [0, 1, 3, 5, 7, -1, -3, -2, -7, -5]
func_list.append(orbit_rational_system([0, 1, 3, 5, 7, -1, -3, -2, -7, -5]))
# cycle (1, 9): orbit [0, 1, -3, -5, -1, 3, 2, 5, 4, 9]
func_list.append(orbit_rational_system([0, 1, -3, -5, -1, 3, 2, 5, 4, 9]))
# tail (9, 1): orbit [0, -1, 1, 9, 5, -11, -9, -7, -5, -3]
func_list.append(orbit_rational_system([0, -1, 1, 9, 5, -11, -9, -7, -5, -3]))
# tail (8, 2): orbit [0, -1, -4, 4, 2, -2, 1, -3, 3, 6]
func_list.append(orbit_rational_system([0, -1, -4, 4, 2, -2, 1, -3, 3, 6]))
# tail (8, 2): orbit [0, -1, 3, -3, 4, -5, 1, -2, 2, -6]
func_list.append(orbit_rational_system([0, -1, 3, -3, 4, -5, 1, -2, 2, -6]))
# tail (9, 1): orbit [0, 1, -5, -7, -1, 3, 9, 7, -3, 5]
func_list.append(orbit_rational_system([0, 1, -5, -7, -1, 3, 9, 7, -3, 5]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()


###########################################
#Gontmacher-Hutz-Jorgenson-Srimani-Xu, arXiv:2007.15483 / GHJSX2021, Sections 6 and 7:
#rational preperiodic graph structures over QQ of the maps with a nontrivial
#automorphism group in degrees 3 and 4. For the families with one parameter the
#paper classifies the structures by a parametrization of the parameter; for the
#others it gives a census table labeled by parameter values. Only the structures
#not already in the database (over QQ, same degree, polynomial or not) are added,
#each once: checked in Sage on 2026-10-08 against the database graphs, isomorphism
#classes as unlabeled directed graphs. For a parametrized structure the parameter
#of smallest height found is used (t ranging over p/q with |p|, |q| <= 4, plus a
#grid with |p|, |q| <= 6); for a table structure, the paper's parameters. G_1 of the
#C_3 family (a point on the elliptic curve y^2 - y = x^3 - 1) is a = 343/342 (t = 1/7).
#Each comment gives the family, the parameter(s) and the number of rational
#preperiodic points.
cites = ['GHJSX2021']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

def ghjsx_3_C3(a): return DynamicalSystem([x**3 + a*y**3, a*x**2*y])
def ghjsx_3_D2f(a): return DynamicalSystem([a*x**2*y + y**3, x**3 + a*x*y**2])
def ghjsx_3_D2g(a): return DynamicalSystem([a*x**2*y - y**3, x**3 - a*x*y**2])
def ghjsx_3_C2f(a, b): return DynamicalSystem([x**3 + a*x*y**2, b*x**2*y + y**3])
def ghjsx_3_C2g(a, b): return DynamicalSystem([a*x**2*y + y**3, x**3 + b*x*y**2])
def ghjsx_4_C4(k): return DynamicalSystem([x**4 + y**4, k*x**3*y])
def ghjsx_4_D3(k): return DynamicalSystem([x**4 + k*x*y**3, k*x**3*y + y**4])
def ghjsx_4_C3(k1, k2): return DynamicalSystem([x**4 + k1*x*y**3, k2*x**3*y + y**4])
def ghjsx_4_C2(k1, k2, k3): return DynamicalSystem([x**4 + k1*x**2*y**2 + y**4, k2*x**3*y + k3*x*y**3])

func_list = []

# degree 3, (z^3 + a)/(a z^2)
func_list.append(ghjsx_3_C3(QQ(-1)))  # (-1): 3 points
func_list.append(ghjsx_3_C3(QQ(1)/2))  # (1/2): 3 points
func_list.append(ghjsx_3_C3(QQ(343)/342))  # (343/342): 5 points

# degree 3, (a z^2 + 1)/(z^3 + a z)
func_list.append(ghjsx_3_D2f(QQ(-4)))  # (-4): 8 points
func_list.append(ghjsx_3_D2f(QQ(-17)/8))  # (-17/8): 8 points
func_list.append(ghjsx_3_D2f(QQ(-3)/2))  # (-3/2): 8 points

# degree 3, (a z^2 - 1)/(z^3 - a z)
func_list.append(ghjsx_3_D2g(QQ(0)))  # (0): 4 points
func_list.append(ghjsx_3_D2g(QQ(3)/2))  # (3/2): 8 points
func_list.append(ghjsx_3_D2g(QQ(17)/8))  # (17/8): 8 points

# degree 4, (z^4 + 1)/(k z^3)
func_list.append(ghjsx_4_C4(QQ(-17)/4))  # (-17/4): 6 points
func_list.append(ghjsx_4_C4(QQ(-1)))  # (-1): 2 points
func_list.append(ghjsx_4_C4(QQ(2)))  # (2): 4 points

# degree 4, (z^4 + k z)/(k z^3 + 1)
func_list.append(ghjsx_4_D3(QQ(-8)))  # (-8): 6 points
func_list.append(ghjsx_4_D3(QQ(-5)/2))  # (-5/2): 6 points
func_list.append(ghjsx_4_D3(QQ(-17)/10))  # (-17/10): 6 points
func_list.append(ghjsx_4_D3(QQ(11)/4))  # (11/4): 6 points

# degree 3, (z^3 + a z)/(b z^2 + 1)
func_list.append(ghjsx_3_C2f(QQ(1), QQ(-9)))  # (1, -9): 6 points
func_list.append(ghjsx_3_C2f(QQ(-1), QQ(-1)/4))  # (-1, -1/4): 6 points
func_list.append(ghjsx_3_C2f(QQ(-1), QQ(-5)/2))  # (-1, -5/2): 6 points
func_list.append(ghjsx_3_C2f(QQ(-1)/2, QQ(-15)/4))  # (-1/2, -15/4): 6 points
func_list.append(ghjsx_3_C2f(QQ(2), QQ(-7)/4))  # (2, -7/4): 6 points
func_list.append(ghjsx_3_C2f(QQ(-7)/4, QQ(-11)/8))  # (-7/4, -11/8): 6 points
func_list.append(ghjsx_3_C2f(QQ(-1), QQ(-13)/4))  # (-1, -13/4): 8 points
func_list.append(ghjsx_3_C2f(QQ(1)/2, QQ(-7)))  # (1/2, -7): 8 points
func_list.append(ghjsx_3_C2f(QQ(-2)/3, QQ(-11)/4))  # (-2/3, -11/4): 8 points
func_list.append(ghjsx_3_C2f(QQ(-3)/2, QQ(-1)/9))  # (-3/2, -1/9): 8 points
func_list.append(ghjsx_3_C2f(QQ(-1)/4, QQ(-11)/5))  # (-1/4, -11/5): 8 points
func_list.append(ghjsx_3_C2f(QQ(11)/4, QQ(-16)))  # (11/4, -16): 8 points
func_list.append(ghjsx_3_C2f(QQ(-1), QQ(-25)/9))  # (-1, -25/9): 8 points
func_list.append(ghjsx_3_C2f(QQ(-16)/9, QQ(-21)/4))  # (-16/9, -21/4): 8 points
func_list.append(ghjsx_3_C2f(QQ(-2), QQ(-13)/12))  # (-2, -13/12): 10 points
func_list.append(ghjsx_3_C2f(QQ(-3), QQ(-9)/16))  # (-3, -9/16): 10 points
func_list.append(ghjsx_3_C2f(QQ(-5)/2, QQ(-7)/4))  # (-5/2, -7/4): 10 points
func_list.append(ghjsx_3_C2f(QQ(4)/5, QQ(-9)/4))  # (4/5, -9/4): 10 points
func_list.append(ghjsx_3_C2f(QQ(-5)/4, QQ(-16)/9))  # (-5/4, -16/9): 12 points
func_list.append(ghjsx_3_C2f(QQ(7)/8, QQ(-17)/2))  # (7/8, -17/2): 10 points
func_list.append(ghjsx_3_C2f(QQ(-19)/3, QQ(-25)/9))  # (-19/3, -25/9): 12 points

# degree 3, (a z^2 + 1)/(z^3 + b z)
func_list.append(ghjsx_3_C2g(QQ(0), QQ(-1)))  # (0, -1): 4 points
func_list.append(ghjsx_3_C2g(QQ(-1), QQ(-1)/4))  # (-1, -1/4): 6 points
func_list.append(ghjsx_3_C2g(QQ(-1), QQ(-5)/2))  # (-1, -5/2): 6 points
func_list.append(ghjsx_3_C2g(QQ(-1), QQ(11)/4))  # (-1, 11/4): 6 points
func_list.append(ghjsx_3_C2g(QQ(-1)/2, QQ(-15)/4))  # (-1/2, -15/4): 6 points
func_list.append(ghjsx_3_C2g(QQ(2), QQ(-7)/4))  # (2, -7/4): 6 points
func_list.append(ghjsx_3_C2g(QQ(2), QQ(-4)))  # (2, -4): 6 points
func_list.append(ghjsx_3_C2g(QQ(8)/5, QQ(-13)/10))  # (8/5, -13/10): 6 points
func_list.append(ghjsx_3_C2g(QQ(-1), QQ(-13)/4))  # (-1, -13/4): 8 points
func_list.append(ghjsx_3_C2g(QQ(-9)/4, QQ(-16)))  # (-9/4, -16): 8 points
func_list.append(ghjsx_3_C2g(QQ(-1), QQ(-77)/45))  # (-1, -77/45): 8 points
func_list.append(ghjsx_3_C2g(QQ(3)/2, QQ(-9)/4))  # (3/2, -9/4): 10 points
func_list.append(ghjsx_3_C2g(QQ(-5)/2, QQ(-7)/4))  # (-5/2, -7/4): 10 points
func_list.append(ghjsx_3_C2g(QQ(-13)/5, QQ(-13)/15))  # (-13/5, -13/15): 2 points
func_list.append(ghjsx_3_C2g(QQ(-9)/4, QQ(-23)/8))  # (-9/4, -23/8): 10 points
func_list.append(ghjsx_3_C2g(QQ(-19)/3, QQ(-25)/9))  # (-19/3, -25/9): 12 points

# degree 4, (z^4 + k1 z)/(k2 z^3 + 1)
func_list.append(ghjsx_4_C3(QQ(1), QQ(-1)))  # (1, -1): 4 points
func_list.append(ghjsx_4_C3(QQ(1), QQ(-3)))  # (1, -3): 4 points
func_list.append(ghjsx_4_C3(QQ(1)/2, QQ(-7)/4))  # (1/2, -7/4): 4 points
func_list.append(ghjsx_4_C3(QQ(4)/3, QQ(-8)))  # (4/3, -8): 5 points
func_list.append(ghjsx_4_C3(QQ(-5)/12, QQ(-25)/18))  # (-5/12, -25/18): 5 points

# degree 4, (z^4 + k1 z^2 + 1)/(k2 z^3 + k3 z)
func_list.append(ghjsx_4_C2(QQ(0), QQ(1), QQ(-1)))  # (0, 1, -1): 4 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(0), QQ(1)))  # (-2, 0, 1): 4 points
func_list.append(ghjsx_4_C2(QQ(0), QQ(1)/3, QQ(-4)/3))  # (0, 1/3, -4/3): 6 points
func_list.append(ghjsx_4_C2(QQ(0), QQ(-3), QQ(5)))  # (0, -3, 5): 6 points
func_list.append(ghjsx_4_C2(QQ(0), QQ(2)/3, QQ(-8)/3))  # (0, 2/3, -8/3): 6 points
func_list.append(ghjsx_4_C2(QQ(1), QQ(-1), QQ(-5)))  # (1, -1, -5): 6 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(0), QQ(9)/2))  # (-2, 0, 9/2): 6 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(1), QQ(-1)/4))  # (-2, 1, -1/4): 6 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(1), QQ(-5)/2))  # (-2, 1, -5/2): 6 points
func_list.append(ghjsx_4_C2(QQ(1)/4, QQ(9), QQ(-9)/2))  # (1/4, 9, -9/2): 6 points
func_list.append(ghjsx_4_C2(QQ(1), QQ(7), QQ(-7)))  # (1, 7, -7): 8 points
func_list.append(ghjsx_4_C2(QQ(1), QQ(-7), QQ(7)))  # (1, -7, 7): 8 points
func_list.append(ghjsx_4_C2(QQ(1), QQ(7)/2, QQ(-7)/2))  # (1, 7/2, -7/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-1)/2, QQ(3), QQ(-9)/2))  # (-1/2, 3, -9/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-1)/2, QQ(-3), QQ(9)/2))  # (-1/2, -3, 9/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-1)/2, QQ(3)/2, QQ(3)/2))  # (-1/2, 3/2, 3/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-1)/2, QQ(3)/2, QQ(-9)/4))  # (-1/2, 3/2, -9/4): 8 points
func_list.append(ghjsx_4_C2(QQ(-1)/2, QQ(-3)/2, QQ(9)/4))  # (-1/2, -3/2, 9/4): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(0), QQ(9)/4))  # (-2, 0, 9/4): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(0), QQ(-9)/4))  # (-2, 0, -9/4): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(1)/4, QQ(7)/2))  # (-2, 1/4, 7/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(4)/5, QQ(-5)))  # (-2, 4/5, -5): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(6), QQ(-3)/8))  # (-2, 6, -3/8): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(7), QQ(1)/2))  # (-2, 7, 1/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-2), QQ(-7), QQ(-1)/2))  # (-2, -7, -1/2): 8 points
func_list.append(ghjsx_4_C2(QQ(1)/3, QQ(8)/3, QQ(-3)/2))  # (1/3, 8/3, -3/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(1), QQ(1)))  # (-3, 1, 1): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(1), QQ(-3)/2))  # (-3, 1, -3/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(-1), QQ(-1)))  # (-3, -1, -1): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(-1), QQ(3)/2))  # (-3, -1, 3/2): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(1)/3, QQ(-4)/3))  # (-3, 1/3, -4/3): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(2)/3, QQ(-1)/6))  # (-3, 2/3, -1/6): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(3)/2, QQ(-1)))  # (-3, 3/2, -1): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(-3)/2, QQ(1)))  # (-3, -3/2, 1): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(4)/3, QQ(-1)/3))  # (-3, 4/3, -1/3): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(-4)/3, QQ(1)/3))  # (-3, -4/3, 1/3): 8 points
func_list.append(ghjsx_4_C2(QQ(-3), QQ(1)/6, QQ(-2)/3))  # (-3, 1/6, -2/3): 8 points
func_list.append(ghjsx_4_C2(QQ(-4)/3, QQ(8)/9, QQ(-2)/9))  # (-4/3, 8/9, -2/9): 8 points
func_list.append(ghjsx_4_C2(QQ(-5)/4, QQ(-5)/4, QQ(2)))  # (-5/4, -5/4, 2): 8 points
func_list.append(ghjsx_4_C2(QQ(-3)/4, QQ(1)/6, QQ(-8)/3))  # (-3/4, 1/6, -8/3): 10 points
func_list.append(ghjsx_4_C2(QQ(-5)/4, QQ(5)/3, QQ(-8)/3))  # (-5/4, 5/3, -8/3): 10 points
func_list.append(ghjsx_4_C2(QQ(-5)/4, QQ(8)/3, QQ(-5)/3))  # (-5/4, 8/3, -5/3): 10 points
func_list.append(ghjsx_4_C2(QQ(-3)/4, QQ(7)/3, QQ(-7)/3))  # (-3/4, 7/3, -7/3): 12 points
func_list.append(ghjsx_4_C2(QQ(-3)/4, QQ(7)/2, QQ(-7)/2))  # (-3/4, 7/2, -7/2): 12 points
func_list.append(ghjsx_4_C2(QQ(-3)/4, QQ(-7)/2, QQ(7)/2))  # (-3/4, -7/2, 7/2): 12 points
func_list.append(ghjsx_4_C2(QQ(7)/4, QQ(8), QQ(-8)))  # (7/4, 8, -8): 12 points
func_list.append(ghjsx_4_C2(QQ(7)/4, QQ(-8), QQ(8)))  # (7/4, -8, 8): 12 points

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
