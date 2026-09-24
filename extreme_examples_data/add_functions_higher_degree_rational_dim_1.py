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


my_session.commit()

log_file.close()

#my_session.close()
