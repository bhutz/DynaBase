from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF

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
#a*z^3 + b*z + c
#Benedetto-Dickman-Joseph-Krause-Rubin-Zhou Examples
#https://mgolech.github.io/cubics/index.html , f(z) column
#Table I: form a*z^3 + b*z + 1 (79 preperiodic portraits, rows I1-I79;
#some portraits have two representative maps, both included)
#Table II: form a*z^3 + b*z (37 preperiodic portraits, rows II1-II37)
cites = ['Benedetto2009']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

# I1: f(z) = z^3 + 1
F = DynamicalSystem([x**3 + 0*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I2: f(z) = -z^3 + 1
F = DynamicalSystem([-x**3 + 0*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I3: f(z) = z^3 + z + 1
F = DynamicalSystem([x**3 + x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I4: f(z) = z^3 - z + 1
F = DynamicalSystem([x**3 - x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I5: f(z) = z^3/2 - z/2 + 1
F = DynamicalSystem([QQ(1)/2*x**3 - QQ(1)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I6: f(z) = -2z^3 + z/2 + 1
F = DynamicalSystem([-2*x**3 + QQ(1)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I7: f(z) = -z^3 + 3z + 1
F = DynamicalSystem([-x**3 + 3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I8: f(z) = z^3/2 - 3z/2 + 1
F = DynamicalSystem([QQ(1)/2*x**3 - QQ(3)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I9: f(z) = -z^3/2 + 3z/2 + 1
F = DynamicalSystem([-QQ(1)/2*x**3 + QQ(3)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I10: f(z) = z^3/3 - z/3 + 1
F = DynamicalSystem([QQ(1)/3*x**3 - QQ(1)/3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I11: f(z) = 4z^3 - 2z + 1
F = DynamicalSystem([4*x**3 - 2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I12: f(z) = -4z^3 + 3z + 1
F = DynamicalSystem([-4*x**3 + 3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I13: f(z) = z^3/3 - 4z/3 + 1
F = DynamicalSystem([QQ(1)/3*x**3 - QQ(4)/3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I14: f(z) = 4z^3/3 - 4z/3 + 1
F = DynamicalSystem([QQ(4)/3*x**3 - QQ(4)/3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I15: f(z) = -z^3 + 5z/4 + 1
F = DynamicalSystem([-x**3 + QQ(5)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I16: f(z) = -2z^3/3 + 5z/3 + 1
F = DynamicalSystem([-QQ(2)/3*x**3 + QQ(5)/3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I17: f(z) = z^3/6 - z/6 + 1
F = DynamicalSystem([QQ(1)/6*x**3 - QQ(1)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I18: f(z) = -z^3/6 + z/6 + 1
F = DynamicalSystem([-QQ(1)/6*x**3 + QQ(1)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I19: f(z) = -2z^3/3 + z/6 + 1
F = DynamicalSystem([-QQ(2)/3*x**3 + QQ(1)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I20: f(z) = -3z^3/2 + z/6 + 1
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(1)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I21: f(z) = z^3/3 - 7z/3 + 1
F = DynamicalSystem([QQ(1)/3*x**3 - QQ(7)/3*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I22: f(z) = 2z^3/3 - 7z/6 + 1
F = DynamicalSystem([QQ(2)/3*x**3 - QQ(7)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I23: f(z) = -2z^3/3 + 7z/6 + 1
F = DynamicalSystem([-QQ(2)/3*x**3 + QQ(7)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I24: f(z) = -3z^3/2 + 7z/6 + 1
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(7)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I25: f(z) = z^3/6 - 7z/6 + 1
F = DynamicalSystem([QQ(1)/6*x**3 - QQ(7)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I26: f(z) = -z^3/6 + 7z/6 + 1
F = DynamicalSystem([-QQ(1)/6*x**3 + QQ(7)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I27: f(z) = 3z^3/2 - 9z/2 + 1
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(9)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I28: f(z) = z^3/4 - 9z/4 + 1
F = DynamicalSystem([QQ(1)/4*x**3 - QQ(9)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I29: f(z) = 9z^3/2 - 5z/2 + 1
F = DynamicalSystem([QQ(9)/2*x**3 - QQ(5)/2*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I30: f(z) = -9z^3/10 - z/10 + 1
F = DynamicalSystem([-QQ(9)/10*x**3 - QQ(1)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I31: f(z) = -9z^3/10 + 11z/10 + 1
F = DynamicalSystem([-QQ(9)/10*x**3 + QQ(11)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I32: f(z) = z^3/6 - 13z/6 + 1
F = DynamicalSystem([QQ(1)/6*x**3 - QQ(13)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I33: f(z) = -z^3/6 + 13z/6 + 1
F = DynamicalSystem([-QQ(1)/6*x**3 + QQ(13)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I34: f(z) = 2z^3/3 - 13z/6 + 1
F = DynamicalSystem([QQ(2)/3*x**3 - QQ(13)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I35: f(z) = -4z^3/3 + 13z/12 + 1
F = DynamicalSystem([-QQ(4)/3*x**3 + QQ(13)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I36: f(z) = z^3/16 - 7z/4 + 1
F = DynamicalSystem([QQ(1)/16*x**3 - QQ(7)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I36: f(z) = -9z^3/10 + 21z/10 + 1
F = DynamicalSystem([-QQ(9)/10*x**3 + QQ(21)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I37: f(z) = -z^3/16 + 7z/4 + 1
F = DynamicalSystem([-QQ(1)/16*x**3 + QQ(7)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I38: f(z) = 3z^3/16 - 7z/12 + 1
F = DynamicalSystem([QQ(3)/16*x**3 - QQ(7)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I38: f(z) = 2z^3/15 - 38z/15 + 1
F = DynamicalSystem([QQ(2)/15*x**3 - QQ(38)/15*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I39: f(z) = 3z^3/16 - 9z/4 + 1
F = DynamicalSystem([QQ(3)/16*x**3 - QQ(9)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I40: f(z) = 9z^3/16 - 3z/4 + 1
F = DynamicalSystem([QQ(9)/16*x**3 - QQ(3)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I41: f(z) = -9z^3/16 + 3z/4 + 1
F = DynamicalSystem([-QQ(9)/16*x**3 + QQ(3)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I42: f(z) = -16z^3/15 + 16z/15 + 1
F = DynamicalSystem([-QQ(16)/15*x**3 + QQ(16)/15*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I43: f(z) = 9z^3/10 - 21z/10 + 1
F = DynamicalSystem([QQ(9)/10*x**3 - QQ(21)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I44: f(z) = 25z^3/12 - 25z/12 + 1
F = DynamicalSystem([QQ(25)/12*x**3 - QQ(25)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I45: f(z) = z^3/12 - 25z/12 + 1
F = DynamicalSystem([QQ(1)/12*x**3 - QQ(25)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I46: f(z) = -z^3/12 + 25z/12 + 1
F = DynamicalSystem([-QQ(1)/12*x**3 + QQ(25)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I47: f(z) = 3z^3/4 - 25z/12 + 1
F = DynamicalSystem([QQ(3)/4*x**3 - QQ(25)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I48: f(z) = 7z^3/6 - 25z/6 + 1
F = DynamicalSystem([QQ(7)/6*x**3 - QQ(25)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I49: f(z) = -2z^3/15 + 19z/30 + 1
F = DynamicalSystem([-QQ(2)/15*x**3 + QQ(19)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I50: f(z) = -z^3/3 + 37z/12 + 1
F = DynamicalSystem([-QQ(1)/3*x**3 + QQ(37)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I51: f(z) = -4z^3/3 + 37z/12 + 1
F = DynamicalSystem([-QQ(4)/3*x**3 + QQ(37)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I52: f(z) = -32z^3/3 + 37z/6 + 1
F = DynamicalSystem([-QQ(32)/3*x**3 + QQ(37)/6*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I53: f(z) = 32z^3/15 - 47z/15 + 1
F = DynamicalSystem([QQ(32)/15*x**3 - QQ(47)/15*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I54: f(z) = z^3/48 - 19z/12 + 1
F = DynamicalSystem([QQ(1)/48*x**3 - QQ(19)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I55: f(z) = z^3/48 - 31z/12 + 1
F = DynamicalSystem([QQ(1)/48*x**3 - QQ(31)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I55: f(z) = -49z^3/48 + 19z/12 + 1
F = DynamicalSystem([-QQ(49)/48*x**3 + QQ(19)/12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I56: f(z) = 25z^3/24 - 49z/24 + 1
F = DynamicalSystem([QQ(25)/24*x**3 - QQ(49)/24*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I57: f(z) = 5z^3/12 - 49z/60 + 1
F = DynamicalSystem([QQ(5)/12*x**3 - QQ(49)/60*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I58: f(z) = -5z^3/12 + 49z/60 + 1
F = DynamicalSystem([-QQ(5)/12*x**3 + QQ(49)/60*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I59: f(z) = 6z^3/5 - 61z/30 + 1
F = DynamicalSystem([QQ(6)/5*x**3 - QQ(61)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I60: f(z) = z^3/6 - 73z/24 + 1
F = DynamicalSystem([QQ(1)/6*x**3 - QQ(73)/24*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I61: f(z) = -z^3/6 + 73z/24 + 1
F = DynamicalSystem([-QQ(1)/6*x**3 + QQ(73)/24*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I62: f(z) = z^3/30 - 79z/30 + 1
F = DynamicalSystem([QQ(1)/30*x**3 - QQ(79)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I63: f(z) = 49z^3/30 - 79z/30 + 1
F = DynamicalSystem([QQ(49)/30*x**3 - QQ(79)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I64: f(z) = -z^3/30 + 91z/30 + 1
F = DynamicalSystem([-QQ(1)/30*x**3 + QQ(91)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I65: f(z) = 8z^3/15 - 121z/30 + 1
F = DynamicalSystem([QQ(8)/15*x**3 - QQ(121)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I66: f(z) = 121z^3/80 - 91z/20 + 1
F = DynamicalSystem([QQ(121)/80*x**3 - QQ(91)/20*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I67: f(z) = -121z^3/80 + 71z/20 + 1
F = DynamicalSystem([-QQ(121)/80*x**3 + QQ(71)/20*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I68: f(z) = 18z^3/125 - 3z/10 + 1
F = DynamicalSystem([QQ(18)/125*x**3 - QQ(3)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I68: f(z) = 144z^3 - 12z + 1
F = DynamicalSystem([144*x**3 - 12*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I69: f(z) = 16z^3/125 - 12z/5 + 1
F = DynamicalSystem([QQ(16)/125*x**3 - QQ(12)/5*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I69: f(z) = -121z^3/250 + 3z/10 + 1
F = DynamicalSystem([-QQ(121)/250*x**3 + QQ(3)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I70: f(z) = 3z^3/128 - 55z/24 + 1
F = DynamicalSystem([QQ(3)/128*x**3 - QQ(55)/24*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I71: f(z) = -147z^3/80 + 31z/60 + 1
F = DynamicalSystem([-QQ(147)/80*x**3 + QQ(31)/60*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I72: f(z) = -z^3/120 + 169z/120 + 1
F = DynamicalSystem([-QQ(1)/120*x**3 + QQ(169)/120*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I73: f(z) = 49z^3/120 - 169z/120 + 1
F = DynamicalSystem([QQ(49)/120*x**3 - QQ(169)/120*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I74: f(z) = -169z^3/96 + 109z/24 + 1
F = DynamicalSystem([-QQ(169)/96*x**3 + QQ(109)/24*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I75: f(z) = -147z^3/10 + 181z/30 + 1
F = DynamicalSystem([-QQ(147)/10*x**3 + QQ(181)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I76: f(z) = z^3/240 - 151z/60 + 1
F = DynamicalSystem([QQ(1)/240*x**3 - QQ(151)/60*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I77: f(z) = 243z^3/10 - 151z/30 + 1
F = DynamicalSystem([QQ(243)/10*x**3 - QQ(151)/30*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I78: f(z) = -49z^3/250 + 27z/10 + 1
F = DynamicalSystem([-QQ(49)/250*x**3 + QQ(27)/10*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I78: f(z) = -289z^3/16 + 27z/4 + 1
F = DynamicalSystem([-QQ(289)/16*x**3 + QQ(27)/4*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# I79: f(z) = 27z^3/256 - 133z/48 + 1
F = DynamicalSystem([QQ(27)/256*x**3 - QQ(133)/48*x*y**2 + y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II1: f(z) = z^3
F = DynamicalSystem([x**3 + 0*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II2: f(z) = -z^3
F = DynamicalSystem([-x**3 + 0*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II3: f(z) = z^3 + z
F = DynamicalSystem([x**3 + x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II4: f(z) = z^3 - z
F = DynamicalSystem([x**3 - x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II5: f(z) = z^3 - 3z
F = DynamicalSystem([x**3 - 3*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II6: f(z) = -z^3 + 3z
F = DynamicalSystem([-x**3 + 3*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II7: f(z) = 3z^3 - z/3
F = DynamicalSystem([3*x**3 - QQ(1)/3*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II8: f(z) = -3z^3 + z/3
F = DynamicalSystem([-3*x**3 + QQ(1)/3*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II9: f(z) = z^3 - 5z/4
F = DynamicalSystem([x**3 - QQ(5)/4*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II10: f(z) = 2z^3 - 5z/2
F = DynamicalSystem([2*x**3 - QQ(5)/2*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II11: f(z) = 3z^3/2 - z/6
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(1)/6*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II12: f(z) = 2z^3 - 7z/2
F = DynamicalSystem([2*x**3 - QQ(7)/2*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II13: f(z) = -2z^3 + 7z/2
F = DynamicalSystem([-2*x**3 + QQ(7)/2*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II14: f(z) = 3z^3/2 - 13z/6
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(13)/6*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II15: f(z) = 3z^3 - 13z/12
F = DynamicalSystem([3*x**3 - QQ(13)/12*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II16: f(z) = -3z^3 + 13z/12
F = DynamicalSystem([-3*x**3 + QQ(13)/12*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II17: f(z) = 6z^3/5 - 17z/6
F = DynamicalSystem([QQ(6)/5*x**3 - QQ(17)/6*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II18: f(z) = 3z^3/2 - 19z/6
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(19)/6*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II19: f(z) = -3z^3/2 + 19z/6
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(19)/6*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II20: f(z) = 3z^3/2 - z/24
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(1)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II21: f(z) = -3z^3/2 + z/24
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(1)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II22: f(z) = 3z^3 - 25z/12
F = DynamicalSystem([3*x**3 - QQ(25)/12*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II23: f(z) = 3z^3/2 - 25z/24
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(25)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II24: f(z) = 5z^3/3 - 34z/15
F = DynamicalSystem([QQ(5)/3*x**3 - QQ(34)/15*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II25: f(z) = -5z^3/3 + 34z/15
F = DynamicalSystem([-QQ(5)/3*x**3 + QQ(34)/15*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II26: f(z) = 3z^3 - 37z/12
F = DynamicalSystem([3*x**3 - QQ(37)/12*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II27: f(z) = -3z^3 + 37z/12
F = DynamicalSystem([-3*x**3 + QQ(37)/12*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II28: f(z) = 3z^3/2 - 49z/24
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(49)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II29: f(z) = -3z^3/2 + 49z/24
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(49)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II30: f(z) = 3z^3/2 - 73z/24
F = DynamicalSystem([QQ(3)/2*x**3 - QQ(73)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II31: f(z) = -3z^3/2 + 73z/24
F = DynamicalSystem([-QQ(3)/2*x**3 + QQ(73)/24*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II32: f(z) = 7z^3/6 - 163z/42
F = DynamicalSystem([QQ(7)/6*x**3 - QQ(163)/42*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II33: f(z) = -7z^3/6 + 163z/42
F = DynamicalSystem([-QQ(7)/6*x**3 + QQ(163)/42*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II34: f(z) = 6z^3/5 - 169z/120
F = DynamicalSystem([QQ(6)/5*x**3 - QQ(169)/120*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II35: f(z) = -6z^3/5 + 169z/120
F = DynamicalSystem([-QQ(6)/5*x**3 + QQ(169)/120*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II36: f(z) = 6z^3/5 - 289z/120
F = DynamicalSystem([QQ(6)/5*x**3 - QQ(289)/120*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

# II37: f(z) = -6z^3/5 + 289z/120
F = DynamicalSystem([-QQ(6)/5*x**3 + QQ(289)/120*x*y**2 + 0*y**3, y**3])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor,
        citations=cites, log_file=log_file)

my_session.commit()

log_file.close()

#my_session.close()
