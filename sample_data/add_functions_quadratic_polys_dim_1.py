
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
log_file = open(path_to_log, 'w', 1)

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
#Doyle-Hyde Examples
#arXiv:2201.11707 / DH2025, Table 2 row d=2: f([m]) in [n] for [k] = {1,...,k}
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['DH2025']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# conjugate to Poonen's x^2 - 29/16 (as the paper notes): adds no new function,
# only attaches the DH2025 citation to the existing one
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
log_file.close()

#my_session.close()
