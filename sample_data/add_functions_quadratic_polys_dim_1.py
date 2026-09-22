
from fields.field_helpers_NF import normalize_field_NF
from fields.field_helpers_NF import lmfdb_field_label_NF

from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF
from functions.function_dim_1_helpers_NF import normalize_function_NF

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

F = DynamicalSystem([x**2+y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2+QQ(1)/4*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2+0*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-2*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(3)/4*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(7)/4*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(10)/9*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(13)/9*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(21)/16*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(301)/144*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(29)/16*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
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
cites = ['Doyle2014']

R = PolynomialRing(QQ, 't')
t = R.gen()

# 0: K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 0: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 2
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 2(1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1/4
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 2(1): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 1/4
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 3(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 0
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 3(1,1): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 0
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 3(2): K = Q(sqrt(3)), p(t) = t^2-3, c = -1
poly = t**2 - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 3(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -1
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 4(1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 1/4
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 4(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = 1/5
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/5
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 4(1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 1
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 4(2): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -4/5
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-4)/5
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 4(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -2/3
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)/3
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 5(1,1)a: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -2
poly = t**2 - t - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 5(1,1)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -2
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 5(1,1)b: K = Q(sqrt(-1)), p(t) = t^2+1, c = 0
poly = t**2 + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 5(2)a: K = Q(sqrt(-1)), p(t) = t^2+1, c = v
poly = t**2 + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = v
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 5(2)b: K = Q(sqrt(2)), p(t) = t^2-2, c = -1
poly = t**2 - 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -3/4
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-3)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -3/4
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-3)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(2): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -3
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-3)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(2): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -13/9
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-13)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(2,1): K = Q(sqrt(-1)), p(t) = t^2+1, c = 1/4
poly = t**2 + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(3): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -301/144
poly = t**2 - t - 8
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 6(3): K = Q(sqrt(-67)), p(t) = t^2-t+17, c = -301/144
poly = t**2 - t + 17
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 7(1,1)a: K = Q(sqrt(2)), p(t) = t^2-2, c = -2
poly = t**2 - 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 7(1,1)b: K = Q(sqrt(3)), p(t) = t^2-3, c = -2
poly = t**2 - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 7(2,1,1)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 0
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(0)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 7(2,1,1)b: K = Q(sqrt(5)), p(t) = t^2-t-1, c = -1
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-1)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(1,1)a: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -289/144
poly = t**2 - t - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-289)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(1,1)a: K = Q(sqrt(-15)), p(t) = t^2-t+4, c = -5/16
poly = t**2 - t + 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-5)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(1,1)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -40/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-40)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(1,1)b: K = Q(sqrt(-2)), p(t) = t^2+2, c = -10/9
poly = t**2 + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-10)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2)a: K = Q(sqrt(10)), p(t) = t^2-10, c = -13/9
poly = t**2 - 10
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-13)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2)a: K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -5/12
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-5)/12
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -37/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-37)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -13/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-13)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2,1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -12
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-12)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(2,1,1): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = 7/12
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(7)/12
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(3): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -29/16
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(3): K = Q(sqrt(-3)), p(t) = t^2-t+1, c = -29/16
poly = t**2 - t + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(4): K = Q(sqrt(10)), p(t) = t^2-10, c = -155/72
poly = t**2 - 10
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-155)/72
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 8(4): K = Q(sqrt(-455)), p(t) = t^2-t+114, c = 199/720
poly = t**2 - t + 114
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(199)/720
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 9(2,1,1): K = Q(sqrt(5)), p(t) = t^2-t-1, c = -2
poly = t**2 - t - 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-2)
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(1,1)a: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = 3/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(3)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(1,1)b: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -1/2*v-13/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = -QQ(1)/2*v - QQ(13)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2): K = Q(sqrt(73)), p(t) = t^2-t-18, c = 1/9*v-205/144
poly = t**2 - t - 18
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(1)/9*v - QQ(205)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2): K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -1/2*v-5/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = -QQ(1)/2*v - QQ(5)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2,1,1)a: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -273/64
poly = t**2 - t - 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-273)/64
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2,1,1)a: K = Q(sqrt(-1)), p(t) = t^2+1, c = 3/8*v-1/4
poly = t**2 + 1
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(3)/8*v - QQ(1)/4
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2,1,1)b: K = Q(sqrt(13)), p(t) = t^2-t-3, c = -10/9
poly = t**2 - t - 3
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-10)/9
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(2,1,1)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -21/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-21)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(3)a: K = Q(sqrt(41)), p(t) = t^2-t-10, c = -29/16
poly = t**2 - t - 10
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(3)b: K = Q(sqrt(57)), p(t) = t^2-t-14, c = -29/16
poly = t**2 - t - 14
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(3,1,1): K = Q(sqrt(337)), p(t) = t^2-t-84, c = -301/144
poly = t**2 - t - 84
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 10(3,2): K = Q(sqrt(193)), p(t) = t^2-t-48, c = -301/144
poly = t**2 - t - 48
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(2): K = Q(sqrt(2)), p(t) = t^2-2, c = -15/8
poly = t**2 - 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-15)/8
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(2,1,1)a: K = Q(sqrt(17)), p(t) = t^2-t-4, c = -13/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-13)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(2,1,1)b: K = Q(sqrt(33)), p(t) = t^2-t-8, c = -45/16
poly = t**2 - t - 8
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-45)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(2,1,1)b: K = Q(sqrt(-7)), p(t) = t^2-t+2, c = -5/16
poly = t**2 - t + 2
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-5)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(3): K = Q(sqrt(73)), p(t) = t^2-t-18, c = -301/144
poly = t**2 - t - 18
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-301)/144
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(4): K = Q(sqrt(105)), p(t) = t^2-t-26, c = -95/48
poly = t**2 - t - 26
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-95)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(4,2): K = Q(sqrt(-15)), p(t) = t^2-t+4, c = -31/48
poly = t**2 - t + 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-31)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 12(6): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -71/48
poly = t**2 - t - 8
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-71)/48
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 14(2,1,1): K = Q(sqrt(17)), p(t) = t^2-t-4, c = -21/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-21)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 14(3,1,1): K = Q(sqrt(33)), p(t) = t^2-t-8, c = -29/16
poly = t**2 - t - 8
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# 14(3,2): K = Q(sqrt(17)), p(t) = t^2-t-4, c = -29/16
poly = t**2 - t - 4
K0 = NumberField(poly, 'v')
v = K0.gen()
c0 = QQ(-29)/16
K, phi = normalize_field_NF(K0)
P = ProjectiveSpace(K, 1, 'x,y')
x, y = P.gens()
c = phi(c0)
F = DynamicalSystem([x**2 + c*y**2, y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

my_session.commit()
log_file.close()

#my_session.close()
