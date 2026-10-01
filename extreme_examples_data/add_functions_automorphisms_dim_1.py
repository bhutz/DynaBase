from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF
from functions.function_dim_1_helpers_NF import add_citations_NF
from functions.function_dim_1_helpers_NF import add_automorphism_group_NF

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_log.txt"
log_file = open(path_to_log, 'a', 1)

#maps with a given exact automorphism group, polynomials and rational maps of any degree

###########################################
#de Faria-Hutz, arXiv:1509.06670 / dFH2018, Figure 1 (Exact Automorphism Groups):
#for each finite subgroup of PGL_2, a map defined over QQ whose automorphism group
#is exactly that group. The cyclic and dihedral groups are infinite families with
#the degree depending on n, so they can't be stored as families; their first few
#members are stored instead:
#  C_n:    (x^(n+1) + x*y^n : y^(n+1)), degree n+1, n = 2..8
#  D_2n:   (y^(n-1) : x^(n-1)), degree n-1, n = 3..8 (n = 2 is degree 1, so D_4
#          is not covered by this formula)
#  S_4, A_5: as printed.
#The paper's A_4 map is over QQ(sqrt(-3)), and its Theorem 4.8 says no map over QQ
#has automorphism group A_4. Gontmacher-Hutz-Jorgenson-Srimani-Xu (GHJSX2021,
#Section 2/3.1) found (z^3 - 3)/(-3z^2), over QQ, with automorphism group A_4; that
#map is used instead.
#The automorphism group is computed over QQbar; its type is stored as GAP's
#StructureDescription (C2, ..., S3 for D_6, D4 for D_8, A4, S4, A5). Checked for
#all of these maps before adding them. A_5's group takes ~30 s, so the timeout is
#raised to 120 s.
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()
timeout = int(120)

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

# icosahedral A_5
func_list.append((DynamicalSystem([-(x**11 + 66*x**6*y**5 - 11*x*y**10),
                                   11*x**10*y + 66*x**5*y**6 - y**11]), ['dFH2018']))

for F, cites in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
        #e.g. D_6 = (y^2 : x^2) is already a Lukas2014 map (182), stored before the iso type column
        my_cursor.execute("""SELECT automorphism_group_iso_type FROM functions_dim_1_NF
            WHERE function_id = %s""", [F_id])
        if my_cursor.fetchone()['automorphism_group_iso_type'] is None:
            add_automorphism_group_NF(F_id, my_cursor, log_file=log_file, timeout=timeout)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file, timeout=timeout)
    my_session.commit()


my_session.commit()

log_file.close()

#my_session.close()
