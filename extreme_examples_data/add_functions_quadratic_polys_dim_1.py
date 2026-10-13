
from fields.field_helpers_NF import normalize_field_NF
from fields.field_helpers_NF import lmfdb_field_label_NF

from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF
from functions.function_dim_1_helpers_NF import normalize_function_NF
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

###########################################
#x^2 + c
#Poonen's Examples
cites = ['Poonen1998']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

func_list.append(DynamicalSystem([x**2+y**2,y**2]))
func_list.append(DynamicalSystem([x**2-y**2,y**2]))
func_list.append(DynamicalSystem([x**2+QQ(1)/4*y**2,y**2]))
func_list.append(DynamicalSystem([x**2+0*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-2*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(3)/4*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(7)/4*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(10)/9*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(13)/9*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(21)/16*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(301)/144*y**2,y**2]))
func_list.append(DynamicalSystem([x**2-QQ(29)/16*y**2,y**2]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


my_session.commit()

###########################################
#x^2 + c
#Walde-Russo Examples
#WR1994 (Amer. Math. Monthly 101 (1994), 318-331): Table 1 gives 12 values of c with
#rational fixed points and a rational 2-cycle (c = -3/4 - (X/Y)^2 for Pythagorean triples,
#Corollary 1), Table 2 gives 8 values of c with a rational 3-cycle (formula (7) of
#Theorem 3 at tau = 1, 2, 1/2, 3, 1/3, 3/2, 2/3, 4/3), and Example 2 is x^2 - 2. Checked
#2026-10-12 (the c values recomputed from the paper's formulas): no new graphs - Table 1
#all have the graph of x^2 - 21/16, Table 2 after tau = 1 that of x^2 - 301/144. The maps
#already in the database get the citation; the others are not added:
#Table 1: -91/36, -133/144, -651/100, -481/576, -2451/196, -273/64, -931/900, -1281/1600,
#-6643/324, -741/400, -2923/1764; Table 2: -421/144, -1849/576, -2689/576, -6469/3600,
#-8149/3600, -49561/28224
cites = ['WR1994']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

func_list.append(DynamicalSystem([x**2-QQ(21)/16*y**2,y**2]))  # Table 1, (m, n) = (2, 1)
func_list.append(DynamicalSystem([x**2-QQ(29)/16*y**2,y**2]))  # Table 2, tau = 1
func_list.append(DynamicalSystem([x**2-QQ(301)/144*y**2,y**2]))  # Table 2, tau = 2
func_list.append(DynamicalSystem([x**2-2*y**2,y**2]))  # Example 2

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


my_session.commit()

###########################################
#x^2 + c
#Morton Examples
#Morton1992 (Acta Arith. 62 (1992), 343-372): examples of the factorization and Galois
#group of the period 3 dynatomic polynomial of x^2 + a - over QQ a = 0, -7/2 (cyclic),
#-1/8 (S3), 1 (full wreath product); a = -1 - 11 sqrt(3)/24 over Q(sqrt(3)) and
#a = -(67 +- sqrt(17))/32 over Q(sqrt(17)) (Phi_3 a product of three quadratics).
#Checked 2026-10-12: no new graphs - all but x^2 have no finite rational preperiodic
#points (the graph of x^2 + 1, also over Q(sqrt(5))). x^2 and x^2 + 1 are in the
#database and get the citation; x^2 - 7/2, x^2 - 1/8 and the three maps over quadratic
#fields are not added.
cites = ['Morton1992']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

func_list.append(DynamicalSystem([x**2+0*y**2,y**2]))
func_list.append(DynamicalSystem([x**2+y**2,y**2]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


my_session.commit()

###########################################
#x^2 + c
#Hutz-Ingram and Stoll Examples
#Hutz2013 (arXiv:0909.5050): x^2 - 29/16 (a rational 3-cycle) and x^2 - 71/48, whose
#6-cycle is defined over Q(sqrt(33)); Stoll2008 (arXiv:0803.2836, Section 5) finds the same
#6-cycle. Both maps are in the database (functions 12 and 31, checked 2026-10-12), so this
#only adds the citations. Hutz-Ingram's other example, c = (omega + 1)/4 over Q(sqrt(-3))
#(a fixed point with multiplier omega), is not added: its graph, two fixed points each
#with one preimage (4(1,1)), is already known.
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()
F = DynamicalSystem([x**2-QQ(29)/16*y**2,y**2])
found, F_id = model_in_database_NF(F, my_cursor)
if found:
    add_citations_NF(F_id, ['Hutz2013'], my_cursor, log_file=log_file)
else: #not in database
    label = add_function_all_NF(F, my_cursor, citations=['Hutz2013'], log_file=log_file)

R = PolynomialRing(QQ, 't')
t = R.gen()
K, phi = normalize_field_NF(NumberField(t**2 - t - 8, 'v'))
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
F = DynamicalSystem([x**2 - QQ(71)/48*y**2, y**2])
found, F_id = model_in_database_NF(F, my_cursor)
if found:
    add_citations_NF(F_id, ['Hutz2013', 'Stoll2008'], my_cursor, log_file=log_file)
else: #not in database
    label = add_function_all_NF(F, my_cursor, citations=['Hutz2013', 'Stoll2008'], log_file=log_file)


my_session.commit()

###########################################
#x^2 + c
#Doyle-Faber-Krumm Examples
#arXiv:1309.6401 / Doyle2014, Appendix C representative data:
#(K, p(t), c) triples for quadratic polynomials x^2+c realizing each
#preperiodic graph structure; K's defining polynomial p(t) has root v,
#matching the paper's root g. c is normalized into the field's
#canonical (LMFDB) model via normalize_field_NF before use.
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['Doyle2014']

R = PolynomialRing(QQ, 't')
t = R.gen()

func_list = []

# 0: K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 0 (earlier map), already in this table - commented out
# 0: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 2
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(2)
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 2(1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1/4
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 2(1) (earlier map), already in this table - commented out
# 2(1): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 1/4
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(1)/4
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 3(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 0
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 3(1,1) (earlier map), already in this table - commented out
# 3(1,1): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 0
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(0)
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 3(2): K = Q(sqrt(3)), p(t) = t^2-3, c = -1
poly = t**2 - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 3(2) (earlier map), already in this table - commented out
# 3(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -1
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-1)
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 4(1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 1/4
poly = t**2 - t + 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 4(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1/5
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)/5
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 4(1,1) (earlier map), already in this table - commented out
# 4(1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 1
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(1)
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 4(2): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -4/5
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-4)/5
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 4(2) (earlier map), already in this table - commented out
# 4(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -2/3
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-2)/3
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 5(1,1)a: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -2
poly = t**2 - t - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 5(1,1)a (earlier map), already in this table - commented out
# 5(1,1)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -2
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-2)
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 5(1,1)b: K = Q(sqrt(-1)), p(t) = t^2+1, c = 0
poly = t**2 + 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 5(2)a: K = Q(sqrt(-1)), p(t) = t^2+1, c = v
poly = t**2 + 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = a
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 5(2)b: K = Q(sqrt(2)), p(t) = t^2-2, c = -1
poly = t**2 - 2
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 6(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -3/4
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-3)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 6(1,1) (earlier map), already in this table - commented out
# 6(1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -3/4
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-3)/4
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 6(2): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -3
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-3)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 6(2) (earlier map), already in this table - commented out
# 6(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -13/9
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-13)/9
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 6(2,1): K = Q(sqrt(-1)), p(t) = t^2+1, c = 1/4
poly = t**2 + 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 6(3): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -301/144
poly = t**2 - t - 8
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 6(3) (earlier map), already in this table - commented out
# 6(3): K = Q(sqrt(-67)), p(t) = t^2-t+17, c = -301/144
#poly = t**2 - t + 17
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-301)/144
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 7(1,1)a: K = Q(sqrt(2)), p(t) = t^2-2, c = -2
poly = t**2 - 2
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 7(1,1)b: K = Q(sqrt(3)), p(t) = t^2-3, c = -2
poly = t**2 - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 7(2,1,1)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 0
poly = t**2 - t + 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 7(2,1,1)b: K = Q(sqrt(5)), p(t) = t^2-t-1, c = -1
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(1,1)a: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -289/144
poly = t**2 - t - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-289)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(1,1)a (earlier map), already in this table - commented out
# 8(1,1)a: K = Q(sqrt(-15)), p(t) = t^2-t+4, c = -5/16
#poly = t**2 - t + 4
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-5)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(1,1)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -40/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-40)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(1,1)b (earlier map), already in this table - commented out
# 8(1,1)b: K = Q(sqrt(-2)), p(t) = t^2+2, c = -10/9
#poly = t**2 + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-10)/9
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(2)a: K = Q(sqrt(10)), p(t) = t^2-10, c = -13/9
poly = t**2 - 10
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-13)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(2)a (earlier map), already in this table - commented out
# 8(2)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -5/12
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-5)/12
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(2)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -37/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-37)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(2)b (earlier map), already in this table - commented out
# 8(2)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -13/16
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-13)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(2,1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -12
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-12)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(2,1,1) (earlier map), already in this table - commented out
# 8(2,1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 7/12
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(7)/12
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(3): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -29/16
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(3) (earlier map), already in this table - commented out
# 8(3): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -29/16
#poly = t**2 - t + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-29)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 8(4): K = Q(sqrt(10)), p(t) = t^2-10, c = -155/72
poly = t**2 - 10
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-155)/72
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 8(4) (earlier map), already in this table - commented out
# 8(4): K = Q(sqrt(-455)), p(t) = t^2-t+114, c = 199/720
#poly = t**2 - t + 114
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(199)/720
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 9(2,1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -2
poly = t**2 - t - 1
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(1,1)a: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 3/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(3)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(1,1)b: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -1/2*v-13/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = -QQ(1)/2*a - QQ(13)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(2): K = Q(sqrt(73)), p(t) = t^2-t-18, c = 1/9*v-205/144
poly = t**2 - t - 18
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(1)/9*a - QQ(205)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 10(2) (earlier map), already in this table - commented out
# 10(2): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -1/2*v-5/16
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = -QQ(1)/2*a - QQ(5)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(2,1,1)a: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -273/64
poly = t**2 - t - 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-273)/64
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 10(2,1,1)a (earlier map), already in this table - commented out
# 10(2,1,1)a: K = Q(sqrt(-1)), p(t) = t^2+1, c = 3/8*v-1/4
#poly = t**2 + 1
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(3)/8*a - QQ(1)/4
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(2,1,1)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -10/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-10)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 10(2,1,1)b (earlier map), already in this table - commented out
# 10(2,1,1)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -21/16
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-21)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(3)a: K = Q(sqrt(41)), p(t) = t^2-t-10, c = -29/16
poly = t**2 - t - 10
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(3)b: K = Q(sqrt(57)), p(t) = t^2-t-14, c = -29/16
poly = t**2 - t - 14
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(3,1,1): K = Q(sqrt(337)), p(t) = t^2-t-84, c = -301/144
poly = t**2 - t - 84
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 10(3,2): K = Q(sqrt(193)), p(t) = t^2-t-48, c = -301/144
poly = t**2 - t - 48
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(2): K = Q(sqrt(2)), p(t) = t^2-2, c = -15/8
poly = t**2 - 2
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-15)/8
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(2,1,1)a: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -13/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-13)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(2,1,1)b: K = Q(sqrt(33)), p(t) = t^2-t-8, c = -45/16
poly = t**2 - t - 8
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-45)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# DUPLICATE - same rational preperiodic graph as 12(2,1,1)b (earlier map), already in this table - commented out
# 12(2,1,1)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -5/16
#poly = t**2 - t + 2
#K0 = NumberField(poly, 'a')
#a = K0.gen()
#c0 = QQ(-5)/16
#K, phi = normalize_field_NF(K0)
#P = ProjectiveSpace(K, 1, 'x,y')
#x, y = P.gens()
#c = phi(c0)
#func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(3): K = Q(sqrt(73)), p(t) = t^2-t-18, c = -301/144
poly = t**2 - t - 18
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(4): K = Q(sqrt(105)), p(t) = t^2-t-26, c = -95/48
poly = t**2 - t - 26
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-95)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(4,2): K = Q(sqrt(-15)), p(t) = t^2-t+4, c = -31/48
poly = t**2 - t + 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-31)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 12(6): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -71/48
poly = t**2 - t - 8
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-71)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 14(2,1,1): K = Q(sqrt(17)), p(t) = t^2-t-4, c = -21/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-21)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 14(3,1,1): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -29/16
poly = t**2 - t - 8
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# 14(3,2): K = Q(sqrt(17)), p(t) = t^2-t-4, c = -29/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'a')
a = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


my_session.commit()

###########################################
#x^2 + c
#Doyle (2018) Examples
#arXiv:1509.07098 / Doyle2018, Appendix A.2 representative data: (graph, p(t), c) for
#each known graph G(f_c, K) over a quadratic field K, x^2 + c, K = Q(g) with p(g) = 0.
#The 67 rows are the same (K, c) pairs as Doyle-Faber-Krumm's Appendix C above (checked
#2026-10-12; the paper prints the label of the Q(sqrt(337)) row without its colon, and
#it is 10(3,1,1)), so they get both citations. All are loaded here, including the 21 that
#the DFK section above leaves commented out as duplicates of a graph over another
#quadratic field: each (function, field) pair counts. With c in QQ the function may be
#the QQ map x^2 + c, and loading it over K adds that map's preperiodic row over K.
cites = ['Doyle2014', 'Doyle2018']

doyle2018_rows = [
    ('0', t**2 - t - 1, lambda v: QQ(1)),  # Q(sqrt(5))
    ('0', t**2 - t + 1, lambda v: QQ(2)),  # Q(sqrt(-3))
    ('2(1)', t**2 - t - 1, lambda v: QQ(1)/4),  # Q(sqrt(5))
    ('2(1)', t**2 - t + 2, lambda v: QQ(1)/4),  # Q(sqrt(-7))
    ('3(1,1)', t**2 - t - 1, lambda v: QQ(0)),  # Q(sqrt(5))
    ('3(1,1)', t**2 - t + 2, lambda v: QQ(0)),  # Q(sqrt(-7))
    ('3(2)', t**2 - 3, lambda v: QQ(-1)),  # Q(sqrt(3))
    ('3(2)', t**2 - t + 1, lambda v: QQ(-1)),  # Q(sqrt(-3))
    ('4(1)', t**2 - t + 1, lambda v: QQ(1)/4),  # Q(sqrt(-3))
    ('4(1,1)', t**2 - t - 1, lambda v: QQ(1)/5),  # Q(sqrt(5))
    ('4(1,1)', t**2 - t + 1, lambda v: QQ(1)),  # Q(sqrt(-3))
    ('4(2)', t**2 - t - 1, lambda v: -QQ(4)/5),  # Q(sqrt(5))
    ('4(2)', t**2 - t + 1, lambda v: -QQ(2)/3),  # Q(sqrt(-3))
    ('5(1,1)a', t**2 - t - 3, lambda v: QQ(-2)),  # Q(sqrt(13))
    ('5(1,1)a', t**2 - t + 1, lambda v: QQ(-2)),  # Q(sqrt(-3))
    ('5(1,1)b', t**2 + 1, lambda v: QQ(0)),  # Q(sqrt(-1))
    ('5(2)a', t**2 + 1, lambda v: v),  # Q(sqrt(-1))
    ('5(2)b', t**2 - 2, lambda v: QQ(-1)),  # Q(sqrt(2))
    ('6(1,1)', t**2 - t - 1, lambda v: -QQ(3)/4),  # Q(sqrt(5))
    ('6(1,1)', t**2 - t + 1, lambda v: -QQ(3)/4),  # Q(sqrt(-3))
    ('6(2)', t**2 - t - 1, lambda v: QQ(-3)),  # Q(sqrt(5))
    ('6(2)', t**2 - t + 1, lambda v: -QQ(13)/9),  # Q(sqrt(-3))
    ('6(2,1)', t**2 + 1, lambda v: QQ(1)/4),  # Q(sqrt(-1))
    ('6(3)', t**2 - t - 8, lambda v: -QQ(301)/144),  # Q(sqrt(33))
    ('6(3)', t**2 - t + 17, lambda v: -QQ(301)/144),  # Q(sqrt(-67))
    ('7(1,1)a', t**2 - 2, lambda v: QQ(-2)),  # Q(sqrt(2))
    ('7(1,1)b', t**2 - 3, lambda v: QQ(-2)),  # Q(sqrt(3))
    ('7(2,1,1)a', t**2 - t + 1, lambda v: QQ(0)),  # Q(sqrt(-3))
    ('7(2,1,1)b', t**2 - t - 1, lambda v: QQ(-1)),  # Q(sqrt(5))
    ('8(1,1)a', t**2 - t - 3, lambda v: -QQ(289)/144),  # Q(sqrt(13))
    ('8(1,1)a', t**2 - t + 4, lambda v: -QQ(5)/16),  # Q(sqrt(-15))
    ('8(1,1)b', t**2 - t - 3, lambda v: -QQ(40)/9),  # Q(sqrt(13))
    ('8(1,1)b', t**2 + 2, lambda v: -QQ(10)/9),  # Q(sqrt(-2))
    ('8(2)a', t**2 - 10, lambda v: -QQ(13)/9),  # Q(sqrt(10))
    ('8(2)a', t**2 - t + 1, lambda v: -QQ(5)/12),  # Q(sqrt(-3))
    ('8(2)b', t**2 - t - 3, lambda v: -QQ(37)/9),  # Q(sqrt(13))
    ('8(2)b', t**2 - t + 2, lambda v: -QQ(13)/16),  # Q(sqrt(-7))
    ('8(2,1,1)', t**2 - t - 1, lambda v: QQ(-12)),  # Q(sqrt(5))
    ('8(2,1,1)', t**2 - t + 1, lambda v: QQ(7)/12),  # Q(sqrt(-3))
    ('8(3)', t**2 - t - 1, lambda v: -QQ(29)/16),  # Q(sqrt(5))
    ('8(3)', t**2 - t + 1, lambda v: -QQ(29)/16),  # Q(sqrt(-3))
    ('8(4)', t**2 - 10, lambda v: -QQ(155)/72),  # Q(sqrt(10))
    ('8(4)', t**2 - t + 114, lambda v: QQ(199)/720),  # Q(sqrt(-455))
    ('9(2,1,1)', t**2 - t - 1, lambda v: QQ(-2)),  # Q(sqrt(5))
    ('10(1,1)a', t**2 - t + 2, lambda v: QQ(3)/16),  # Q(sqrt(-7))
    ('10(1,1)b', t**2 - t - 4, lambda v: -QQ(1)/2*v - QQ(13)/16),  # Q(sqrt(17))
    ('10(2)', t**2 - t - 18, lambda v: QQ(1)/9*v - QQ(205)/144),  # Q(sqrt(73))
    ('10(2)', t**2 - t + 2, lambda v: -QQ(1)/2*v - QQ(5)/16),  # Q(sqrt(-7))
    ('10(2,1,1)a', t**2 - t - 4, lambda v: -QQ(273)/64),  # Q(sqrt(17))
    ('10(2,1,1)a', t**2 + 1, lambda v: QQ(3)/8*v - QQ(1)/4),  # Q(sqrt(-1))
    ('10(2,1,1)b', t**2 - t - 3, lambda v: -QQ(10)/9),  # Q(sqrt(13))
    ('10(2,1,1)b', t**2 - t + 2, lambda v: -QQ(21)/16),  # Q(sqrt(-7))
    ('10(3)a', t**2 - t - 10, lambda v: -QQ(29)/16),  # Q(sqrt(41))
    ('10(3)b', t**2 - t - 14, lambda v: -QQ(29)/16),  # Q(sqrt(57))
    ('10(3,1,1)', t**2 - t - 84, lambda v: -QQ(301)/144),  # Q(sqrt(337))
    ('10(3,2)', t**2 - t - 48, lambda v: -QQ(301)/144),  # Q(sqrt(193))
    ('12(2)', t**2 - 2, lambda v: -QQ(15)/8),  # Q(sqrt(2))
    ('12(2,1,1)a', t**2 - t - 4, lambda v: -QQ(13)/16),  # Q(sqrt(17))
    ('12(2,1,1)b', t**2 - t - 8, lambda v: -QQ(45)/16),  # Q(sqrt(33))
    ('12(2,1,1)b', t**2 - t + 2, lambda v: -QQ(5)/16),  # Q(sqrt(-7))
    ('12(3)', t**2 - t - 18, lambda v: -QQ(301)/144),  # Q(sqrt(73))
    ('12(4)', t**2 - t - 26, lambda v: -QQ(95)/48),  # Q(sqrt(105))
    ('12(4,2)', t**2 - t + 4, lambda v: -QQ(31)/48),  # Q(sqrt(-15))
    ('12(6)', t**2 - t - 8, lambda v: -QQ(71)/48),  # Q(sqrt(33))
    ('14(2,1,1)', t**2 - t - 4, lambda v: -QQ(21)/16),  # Q(sqrt(17))
    ('14(3,1,1)', t**2 - t - 8, lambda v: -QQ(29)/16),  # Q(sqrt(33))
    ('14(3,2)', t**2 - t - 4, lambda v: -QQ(29)/16),  # Q(sqrt(17))
]

for graph, poly, c_of in doyle2018_rows:
    K0 = NumberField(poly, 'v')
    c0 = c_of(K0.gen())
    K, phi = normalize_field_NF(K0)
    P = ProjectiveSpace(K, 1, 'x,y')
    x, y = P.gens()
    c = phi(c0)
    F = DynamicalSystem([x**2 + c*y**2, y**2])
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database, or not over K
        #x^2 + 1/4's preperiodic points over a quadratic field take ~2 minutes (checked
        #2026-10-12), so with the default 30 s its rows over K were never stored
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file, timeout=300 if c0 == QQ(1)/4 else 30)
    my_session.commit()


my_session.commit()

###########################################
#x^2 + c
#Doyle (2020) Examples
#arXiv:1801.09003 / Doyle2020, Appendix B Table 1: a representative c for each graph
#G(f_c, K) realized over K = Q(i) or Q(omega) (17 graphs; 28 (c, K) pairs, a graph with
#no dagger being realized by the same c over both). Checked against the database and the
#Doyle (2018) section above 2026-10-12: every listed point set matches. The only graphs
#not already in the database are 4(1) over Q(omega) and 6(2,1) over Q(i), both
#x^2 + 1/4 (function 3), whose rows over those fields had timed out (~2 minutes each);
#they are added with a 5 minute timeout. Every other map already stored gets the
#citation, entered in the model it is stored in (over QQ for rational c), so only the
#citation is attached. c = -6 (4(1,1)) and c = -3 (4(2)) are not stored and their graphs
#are, so they are not added.
cites = ['Doyle2020']

R = PolynomialRing(QQ, 't')
t = R.gen()
func_list = []

# over QQ: 3(2) c = -1, 5(1,1)a c = -2, 5(1,1)b and 7(2,1,1)a c = 0, 6(1,1) c = -10/9,
# 6(2) c = -13/9, 6(3) c = -301/144, 8(2,1,1) c = -21/16, 8(3) c = -29/16
P = ProjectiveSpace(QQ, 1, 'x,y')
x, y = P.gens()
for c in [QQ(-1), QQ(-2), QQ(0), QQ(-10)/9, QQ(-13)/9, QQ(-301)/144, QQ(-21)/16, QQ(-29)/16]:
    func_list.append(DynamicalSystem([x**2 + c*y**2, y**2]))

# over Q(i): 5(2)a c = i, 10(2,1,1)a c = -1/4 + 3i/8 (from the Doyle (2018) section)
K, phi = normalize_field_NF(NumberField(t**2 + 1, 'v'))
v = phi.domain().gen()
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
for c0 in [v, QQ(-1)/4 + QQ(3)/8*v]:
    func_list.append(DynamicalSystem([x**2 + phi(c0)*y**2, y**2]))

# over Q(omega): 0 c = 2, 8(2)a c = -5/12 (both from the Doyle (2018) section)
K, phi = normalize_field_NF(NumberField(t**2 + t + 1, 'v'))
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
for c0 in [QQ(2), QQ(-5)/12]:
    func_list.append(DynamicalSystem([x**2 + phi(c0)*y**2, y**2]))

# NOT ADDED - 4(1,1) c = -6 and 4(2) c = -3, over Q(i) and Q(omega): graphs already known
#for c0 in [QQ(-6), QQ(-3)]:

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()

# new graphs: 4(1) over Q(omega) and 6(2,1) over Q(i), x^2 + 1/4 (function 3, over QQ):
# entered over K so its preperiodic row over K is computed
for poly in [t**2 + t + 1, t**2 + 1]:
    K, phi = normalize_field_NF(NumberField(poly, 'v'))
    P = ProjectiveSpace(K, 1, 'x,y')
    x, y = P.gens()
    F = DynamicalSystem([x**2 + QQ(1)/4*y**2, y**2])
    label = add_function_all_NF(F, my_cursor, citations=cites, log_file=log_file, timeout=300)
    my_session.commit()


my_session.commit()

###########################################
#x^2 + c
#Doyle-Hyde Examples
#arXiv:2201.11707 / DoHy2025, Table 2 row d=2: f([m]) in [n] for [k] = {1,...,k}
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['DoHy2025']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# conjugate to Poonen's x^2 - 29/16 (as the paper notes): adds no new function,
# only attaches the DoHy2025 citation to the existing one
# d=2, m=8, n=7: f(z) = (z^2 - 9z + 22)/2
func_list.append(DynamicalSystem([x**2 - 9*x*y + 22*y**2, 2*y**2]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


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

# degree 2
# many 9 (2,3), cycle (2,3), tail (2,3): orbit [0, 1, -1, 2]
func_list.append(orbit_poly_system([0, 1, -1, 2]))
# many 9 (1,3), cycle (1,3): orbit [0, 1, 4, 7]
func_list.append(orbit_poly_system([0, 1, 4, 7]))
# many 9 (1,3): orbit [0, -4, 2, -1]
func_list.append(orbit_poly_system([0, -4, 2, -1]))
# tail (2,2): orbit [0, 4, 2, 1]
func_list.append(orbit_poly_system([0, 4, 2, 1]))
# tail (2,2): orbit [0, 1, -1, 4]
func_list.append(orbit_poly_system([0, 1, -1, 4]))
# tail (2,2): orbit [0, 1, -3, 16]
func_list.append(orbit_poly_system([0, 1, -3, 16]))

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
#postcritically finite (PCF) quadratic polynomials over QQ
#Ingram, A finiteness result for post-critically finite polynomials (Ingram2012),
#Section 4: z^2 + c with c in QQ is PCF only for c in {0, -1, -2}
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['Ingram2012']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# c = 0
func_list.append(DynamicalSystem([x**2, y**2]))
# c = -1
func_list.append(DynamicalSystem([x**2 - y**2, y**2]))
# c = -2
func_list.append(DynamicalSystem([x**2 - 2*y**2, y**2]))

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
#postcritically finite (PCF) quadratic maps over QQ that are polynomials
#Lukas-Manes-Yap, A census of quadratic post-critically finite rational functions
#defined over Q (Lukas2014), Theorem 1 maps (1), (3), (4); the rest of the twelve
#are in add_functions_quadratic_rational_dim_1.py
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['Lukas2014']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# (1) z^2
func_list.append(DynamicalSystem([x**2, y**2]))
# (3) z^2 - 2
func_list.append(DynamicalSystem([x**2 - 2*y**2, y**2]))
# (4) z^2 - 1
func_list.append(DynamicalSystem([x**2 - y**2, y**2]))

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
#Doyle-Hindes Examples
#arXiv:2510.14067 / DoHi2025, Table 1 (Theorem 1.1 and its corollary): the 12 nonempty
#skeletons of PrePer(x^d + c, K) for algebraic integers c and large d. One map x^d + c
#for each, found 2026-10-12 from the conditions in the proofs (arXiv:2408.14657,
#Section 4: c built from roots of unity; (1)a from c = y - y^d): smallest field, then
#smallest d. The 12 are split by degree over the quadratic, cubic and higher degree
#polynomial files; the full list is in the higher degree file.
#Here (verified with the full preperiodic computation): (2)b x^2 - 1 over QQ (function 2,
#so only the citation) and (1,1) x^2 + 1 over Q(sqrt(-3)) = Q(zeta_3) (function 1; loading it
#over Q(zeta_3) adds that field's preperiodic row).
cites = ['DoHi2025']
func_list = []
P = ProjectiveSpace(QQ, 1, 'x,y')
x, y = P.gens()
func_list.append(DynamicalSystem([x**2 - y**2, y**2]))  # (2)b
R = PolynomialRing(QQ, 't')
t = R.gen()
K, phi = normalize_field_NF(NumberField(t**2 + t + 1, 'v'))  # Q(zeta_3)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
func_list.append(DynamicalSystem([x**2 + y**2, y**2]))  # (1,1)

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database (or not over this field)
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)
    my_session.commit()


my_session.commit()

log_file.close()

#my_session.close()
