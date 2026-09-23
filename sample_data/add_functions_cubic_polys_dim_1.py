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
#a*z^3 + b*z + c
#Benedetto-Dickman-Joseph-Krause-Rubin-Zhou Examples
#https://mgolech.github.io/cubics/index.html , f(z) column
#Table I: form a*z^3 + b*z + 1 (79 preperiodic portraits, rows I1-I79;
#some portraits have two representative maps, both included)
#Table II: form a*z^3 + b*z (37 preperiodic portraits, rows II1-II37)
cites = ['Benedetto2009']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# I1: f(z) = z^3 + 1
func_list.append(DynamicalSystem([x**3 + 0*x*y**2 + y**3, y**3]))

# I2: f(z) = -z^3 + 1
func_list.append(DynamicalSystem([-x**3 + 0*x*y**2 + y**3, y**3]))

# I3: f(z) = z^3 + z + 1
func_list.append(DynamicalSystem([x**3 + x*y**2 + y**3, y**3]))

# I4: f(z) = z^3 - z + 1
func_list.append(DynamicalSystem([x**3 - x*y**2 + y**3, y**3]))

# I5: f(z) = z^3/2 - z/2 + 1
func_list.append(DynamicalSystem([QQ(1)/2*x**3 - QQ(1)/2*x*y**2 + y**3, y**3]))

# I6: f(z) = -2z^3 + z/2 + 1
func_list.append(DynamicalSystem([-2*x**3 + QQ(1)/2*x*y**2 + y**3, y**3]))

# I7: f(z) = -z^3 + 3z + 1
func_list.append(DynamicalSystem([-x**3 + 3*x*y**2 + y**3, y**3]))

# I8: f(z) = z^3/2 - 3z/2 + 1
func_list.append(DynamicalSystem([QQ(1)/2*x**3 - QQ(3)/2*x*y**2 + y**3, y**3]))

# I9: f(z) = -z^3/2 + 3z/2 + 1
func_list.append(DynamicalSystem([-QQ(1)/2*x**3 + QQ(3)/2*x*y**2 + y**3, y**3]))

# I10: f(z) = z^3/3 - z/3 + 1
func_list.append(DynamicalSystem([QQ(1)/3*x**3 - QQ(1)/3*x*y**2 + y**3, y**3]))

# I11: f(z) = 4z^3 - 2z + 1
func_list.append(DynamicalSystem([4*x**3 - 2*x*y**2 + y**3, y**3]))

# I12: f(z) = -4z^3 + 3z + 1
func_list.append(DynamicalSystem([-4*x**3 + 3*x*y**2 + y**3, y**3]))

# I13: f(z) = z^3/3 - 4z/3 + 1
func_list.append(DynamicalSystem([QQ(1)/3*x**3 - QQ(4)/3*x*y**2 + y**3, y**3]))

# I14: f(z) = 4z^3/3 - 4z/3 + 1
func_list.append(DynamicalSystem([QQ(4)/3*x**3 - QQ(4)/3*x*y**2 + y**3, y**3]))

# I15: f(z) = -z^3 + 5z/4 + 1
func_list.append(DynamicalSystem([-x**3 + QQ(5)/4*x*y**2 + y**3, y**3]))

# I16: f(z) = -2z^3/3 + 5z/3 + 1
func_list.append(DynamicalSystem([-QQ(2)/3*x**3 + QQ(5)/3*x*y**2 + y**3, y**3]))

# I17: f(z) = z^3/6 - z/6 + 1
func_list.append(DynamicalSystem([QQ(1)/6*x**3 - QQ(1)/6*x*y**2 + y**3, y**3]))

# I18: f(z) = -z^3/6 + z/6 + 1
func_list.append(DynamicalSystem([-QQ(1)/6*x**3 + QQ(1)/6*x*y**2 + y**3, y**3]))

# I19: f(z) = -2z^3/3 + z/6 + 1
func_list.append(DynamicalSystem([-QQ(2)/3*x**3 + QQ(1)/6*x*y**2 + y**3, y**3]))

# I20: f(z) = -3z^3/2 + z/6 + 1
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(1)/6*x*y**2 + y**3, y**3]))

# I21: f(z) = z^3/3 - 7z/3 + 1
func_list.append(DynamicalSystem([QQ(1)/3*x**3 - QQ(7)/3*x*y**2 + y**3, y**3]))

# I22: f(z) = 2z^3/3 - 7z/6 + 1
func_list.append(DynamicalSystem([QQ(2)/3*x**3 - QQ(7)/6*x*y**2 + y**3, y**3]))

# I23: f(z) = -2z^3/3 + 7z/6 + 1
func_list.append(DynamicalSystem([-QQ(2)/3*x**3 + QQ(7)/6*x*y**2 + y**3, y**3]))

# I24: f(z) = -3z^3/2 + 7z/6 + 1
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(7)/6*x*y**2 + y**3, y**3]))

# I25: f(z) = z^3/6 - 7z/6 + 1
func_list.append(DynamicalSystem([QQ(1)/6*x**3 - QQ(7)/6*x*y**2 + y**3, y**3]))

# I26: f(z) = -z^3/6 + 7z/6 + 1
func_list.append(DynamicalSystem([-QQ(1)/6*x**3 + QQ(7)/6*x*y**2 + y**3, y**3]))

# I27: f(z) = 3z^3/2 - 9z/2 + 1
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(9)/2*x*y**2 + y**3, y**3]))

# I28: f(z) = z^3/4 - 9z/4 + 1
func_list.append(DynamicalSystem([QQ(1)/4*x**3 - QQ(9)/4*x*y**2 + y**3, y**3]))

# I29: f(z) = 9z^3/2 - 5z/2 + 1
func_list.append(DynamicalSystem([QQ(9)/2*x**3 - QQ(5)/2*x*y**2 + y**3, y**3]))

# I30: f(z) = -9z^3/10 - z/10 + 1
func_list.append(DynamicalSystem([-QQ(9)/10*x**3 - QQ(1)/10*x*y**2 + y**3, y**3]))

# I31: f(z) = -9z^3/10 + 11z/10 + 1
func_list.append(DynamicalSystem([-QQ(9)/10*x**3 + QQ(11)/10*x*y**2 + y**3, y**3]))

# I32: f(z) = z^3/6 - 13z/6 + 1
func_list.append(DynamicalSystem([QQ(1)/6*x**3 - QQ(13)/6*x*y**2 + y**3, y**3]))

# I33: f(z) = -z^3/6 + 13z/6 + 1
func_list.append(DynamicalSystem([-QQ(1)/6*x**3 + QQ(13)/6*x*y**2 + y**3, y**3]))

# I34: f(z) = 2z^3/3 - 13z/6 + 1
func_list.append(DynamicalSystem([QQ(2)/3*x**3 - QQ(13)/6*x*y**2 + y**3, y**3]))

# I35: f(z) = -4z^3/3 + 13z/12 + 1
func_list.append(DynamicalSystem([-QQ(4)/3*x**3 + QQ(13)/12*x*y**2 + y**3, y**3]))

# I36: f(z) = z^3/16 - 7z/4 + 1
func_list.append(DynamicalSystem([QQ(1)/16*x**3 - QQ(7)/4*x*y**2 + y**3, y**3]))

# I36: f(z) = -9z^3/10 + 21z/10 + 1
func_list.append(DynamicalSystem([-QQ(9)/10*x**3 + QQ(21)/10*x*y**2 + y**3, y**3]))

# I37: f(z) = -z^3/16 + 7z/4 + 1
func_list.append(DynamicalSystem([-QQ(1)/16*x**3 + QQ(7)/4*x*y**2 + y**3, y**3]))

# I38: f(z) = 3z^3/16 - 7z/12 + 1
func_list.append(DynamicalSystem([QQ(3)/16*x**3 - QQ(7)/12*x*y**2 + y**3, y**3]))

# I38: f(z) = 2z^3/15 - 38z/15 + 1
func_list.append(DynamicalSystem([QQ(2)/15*x**3 - QQ(38)/15*x*y**2 + y**3, y**3]))

# I39: f(z) = 3z^3/16 - 9z/4 + 1
func_list.append(DynamicalSystem([QQ(3)/16*x**3 - QQ(9)/4*x*y**2 + y**3, y**3]))

# I40: f(z) = 9z^3/16 - 3z/4 + 1
func_list.append(DynamicalSystem([QQ(9)/16*x**3 - QQ(3)/4*x*y**2 + y**3, y**3]))

# I41: f(z) = -9z^3/16 + 3z/4 + 1
func_list.append(DynamicalSystem([-QQ(9)/16*x**3 + QQ(3)/4*x*y**2 + y**3, y**3]))

# I42: f(z) = -16z^3/15 + 16z/15 + 1
func_list.append(DynamicalSystem([-QQ(16)/15*x**3 + QQ(16)/15*x*y**2 + y**3, y**3]))

# I43: f(z) = 9z^3/10 - 21z/10 + 1
func_list.append(DynamicalSystem([QQ(9)/10*x**3 - QQ(21)/10*x*y**2 + y**3, y**3]))

# I44: f(z) = 25z^3/12 - 25z/12 + 1
func_list.append(DynamicalSystem([QQ(25)/12*x**3 - QQ(25)/12*x*y**2 + y**3, y**3]))

# I45: f(z) = z^3/12 - 25z/12 + 1
func_list.append(DynamicalSystem([QQ(1)/12*x**3 - QQ(25)/12*x*y**2 + y**3, y**3]))

# I46: f(z) = -z^3/12 + 25z/12 + 1
func_list.append(DynamicalSystem([-QQ(1)/12*x**3 + QQ(25)/12*x*y**2 + y**3, y**3]))

# I47: f(z) = 3z^3/4 - 25z/12 + 1
func_list.append(DynamicalSystem([QQ(3)/4*x**3 - QQ(25)/12*x*y**2 + y**3, y**3]))

# I48: f(z) = 7z^3/6 - 25z/6 + 1
func_list.append(DynamicalSystem([QQ(7)/6*x**3 - QQ(25)/6*x*y**2 + y**3, y**3]))

# I49: f(z) = -2z^3/15 + 19z/30 + 1
func_list.append(DynamicalSystem([-QQ(2)/15*x**3 + QQ(19)/30*x*y**2 + y**3, y**3]))

# I50: f(z) = -z^3/3 + 37z/12 + 1
func_list.append(DynamicalSystem([-QQ(1)/3*x**3 + QQ(37)/12*x*y**2 + y**3, y**3]))

# I51: f(z) = -4z^3/3 + 37z/12 + 1
func_list.append(DynamicalSystem([-QQ(4)/3*x**3 + QQ(37)/12*x*y**2 + y**3, y**3]))

# I52: f(z) = -32z^3/3 + 37z/6 + 1
func_list.append(DynamicalSystem([-QQ(32)/3*x**3 + QQ(37)/6*x*y**2 + y**3, y**3]))

# I53: f(z) = 32z^3/15 - 47z/15 + 1
func_list.append(DynamicalSystem([QQ(32)/15*x**3 - QQ(47)/15*x*y**2 + y**3, y**3]))

# I54: f(z) = z^3/48 - 19z/12 + 1
func_list.append(DynamicalSystem([QQ(1)/48*x**3 - QQ(19)/12*x*y**2 + y**3, y**3]))

# I55: f(z) = z^3/48 - 31z/12 + 1
func_list.append(DynamicalSystem([QQ(1)/48*x**3 - QQ(31)/12*x*y**2 + y**3, y**3]))

# I55: f(z) = -49z^3/48 + 19z/12 + 1
func_list.append(DynamicalSystem([-QQ(49)/48*x**3 + QQ(19)/12*x*y**2 + y**3, y**3]))

# I56: f(z) = 25z^3/24 - 49z/24 + 1
func_list.append(DynamicalSystem([QQ(25)/24*x**3 - QQ(49)/24*x*y**2 + y**3, y**3]))

# I57: f(z) = 5z^3/12 - 49z/60 + 1
func_list.append(DynamicalSystem([QQ(5)/12*x**3 - QQ(49)/60*x*y**2 + y**3, y**3]))

# I58: f(z) = -5z^3/12 + 49z/60 + 1
func_list.append(DynamicalSystem([-QQ(5)/12*x**3 + QQ(49)/60*x*y**2 + y**3, y**3]))

# I59: f(z) = 6z^3/5 - 61z/30 + 1
func_list.append(DynamicalSystem([QQ(6)/5*x**3 - QQ(61)/30*x*y**2 + y**3, y**3]))

# I60: f(z) = z^3/6 - 73z/24 + 1
func_list.append(DynamicalSystem([QQ(1)/6*x**3 - QQ(73)/24*x*y**2 + y**3, y**3]))

# I61: f(z) = -z^3/6 + 73z/24 + 1
func_list.append(DynamicalSystem([-QQ(1)/6*x**3 + QQ(73)/24*x*y**2 + y**3, y**3]))

# I62: f(z) = z^3/30 - 79z/30 + 1
func_list.append(DynamicalSystem([QQ(1)/30*x**3 - QQ(79)/30*x*y**2 + y**3, y**3]))

# I63: f(z) = 49z^3/30 - 79z/30 + 1
func_list.append(DynamicalSystem([QQ(49)/30*x**3 - QQ(79)/30*x*y**2 + y**3, y**3]))

# I64: f(z) = -z^3/30 + 91z/30 + 1
func_list.append(DynamicalSystem([-QQ(1)/30*x**3 + QQ(91)/30*x*y**2 + y**3, y**3]))

# I65: f(z) = 8z^3/15 - 121z/30 + 1
func_list.append(DynamicalSystem([QQ(8)/15*x**3 - QQ(121)/30*x*y**2 + y**3, y**3]))

# I66: f(z) = 121z^3/80 - 91z/20 + 1
func_list.append(DynamicalSystem([QQ(121)/80*x**3 - QQ(91)/20*x*y**2 + y**3, y**3]))

# I67: f(z) = -121z^3/80 + 71z/20 + 1
func_list.append(DynamicalSystem([-QQ(121)/80*x**3 + QQ(71)/20*x*y**2 + y**3, y**3]))

# I68: f(z) = 18z^3/125 - 3z/10 + 1
func_list.append(DynamicalSystem([QQ(18)/125*x**3 - QQ(3)/10*x*y**2 + y**3, y**3]))

# I68: f(z) = 144z^3 - 12z + 1
func_list.append(DynamicalSystem([144*x**3 - 12*x*y**2 + y**3, y**3]))

# I69: f(z) = 16z^3/125 - 12z/5 + 1
func_list.append(DynamicalSystem([QQ(16)/125*x**3 - QQ(12)/5*x*y**2 + y**3, y**3]))

# I69: f(z) = -121z^3/250 + 3z/10 + 1
func_list.append(DynamicalSystem([-QQ(121)/250*x**3 + QQ(3)/10*x*y**2 + y**3, y**3]))

# I70: f(z) = 3z^3/128 - 55z/24 + 1
func_list.append(DynamicalSystem([QQ(3)/128*x**3 - QQ(55)/24*x*y**2 + y**3, y**3]))

# I71: f(z) = -147z^3/80 + 31z/60 + 1
func_list.append(DynamicalSystem([-QQ(147)/80*x**3 + QQ(31)/60*x*y**2 + y**3, y**3]))

# I72: f(z) = -z^3/120 + 169z/120 + 1
func_list.append(DynamicalSystem([-QQ(1)/120*x**3 + QQ(169)/120*x*y**2 + y**3, y**3]))

# I73: f(z) = 49z^3/120 - 169z/120 + 1
func_list.append(DynamicalSystem([QQ(49)/120*x**3 - QQ(169)/120*x*y**2 + y**3, y**3]))

# I74: f(z) = -169z^3/96 + 109z/24 + 1
func_list.append(DynamicalSystem([-QQ(169)/96*x**3 + QQ(109)/24*x*y**2 + y**3, y**3]))

# I75: f(z) = -147z^3/10 + 181z/30 + 1
func_list.append(DynamicalSystem([-QQ(147)/10*x**3 + QQ(181)/30*x*y**2 + y**3, y**3]))

# I76: f(z) = z^3/240 - 151z/60 + 1
func_list.append(DynamicalSystem([QQ(1)/240*x**3 - QQ(151)/60*x*y**2 + y**3, y**3]))

# I77: f(z) = 243z^3/10 - 151z/30 + 1
func_list.append(DynamicalSystem([QQ(243)/10*x**3 - QQ(151)/30*x*y**2 + y**3, y**3]))

# I78: f(z) = -49z^3/250 + 27z/10 + 1
func_list.append(DynamicalSystem([-QQ(49)/250*x**3 + QQ(27)/10*x*y**2 + y**3, y**3]))

# I78: f(z) = -289z^3/16 + 27z/4 + 1
func_list.append(DynamicalSystem([-QQ(289)/16*x**3 + QQ(27)/4*x*y**2 + y**3, y**3]))

# I79: f(z) = 27z^3/256 - 133z/48 + 1
func_list.append(DynamicalSystem([QQ(27)/256*x**3 - QQ(133)/48*x*y**2 + y**3, y**3]))

# II1: f(z) = z^3
func_list.append(DynamicalSystem([x**3 + 0*x*y**2 + 0*y**3, y**3]))

# II2: f(z) = -z^3
func_list.append(DynamicalSystem([-x**3 + 0*x*y**2 + 0*y**3, y**3]))

# II3: f(z) = z^3 + z
func_list.append(DynamicalSystem([x**3 + x*y**2 + 0*y**3, y**3]))

# II4: f(z) = z^3 - z
func_list.append(DynamicalSystem([x**3 - x*y**2 + 0*y**3, y**3]))

# II5: f(z) = z^3 - 3z
func_list.append(DynamicalSystem([x**3 - 3*x*y**2 + 0*y**3, y**3]))

# II6: f(z) = -z^3 + 3z
func_list.append(DynamicalSystem([-x**3 + 3*x*y**2 + 0*y**3, y**3]))

# II7: f(z) = 3z^3 - z/3
func_list.append(DynamicalSystem([3*x**3 - QQ(1)/3*x*y**2 + 0*y**3, y**3]))

# II8: f(z) = -3z^3 + z/3
func_list.append(DynamicalSystem([-3*x**3 + QQ(1)/3*x*y**2 + 0*y**3, y**3]))

# II9: f(z) = z^3 - 5z/4
func_list.append(DynamicalSystem([x**3 - QQ(5)/4*x*y**2 + 0*y**3, y**3]))

# II10: f(z) = 2z^3 - 5z/2
func_list.append(DynamicalSystem([2*x**3 - QQ(5)/2*x*y**2 + 0*y**3, y**3]))

# II11: f(z) = 3z^3/2 - z/6
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(1)/6*x*y**2 + 0*y**3, y**3]))

# II12: f(z) = 2z^3 - 7z/2
func_list.append(DynamicalSystem([2*x**3 - QQ(7)/2*x*y**2 + 0*y**3, y**3]))

# II13: f(z) = -2z^3 + 7z/2
func_list.append(DynamicalSystem([-2*x**3 + QQ(7)/2*x*y**2 + 0*y**3, y**3]))

# II14: f(z) = 3z^3/2 - 13z/6
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(13)/6*x*y**2 + 0*y**3, y**3]))

# II15: f(z) = 3z^3 - 13z/12
func_list.append(DynamicalSystem([3*x**3 - QQ(13)/12*x*y**2 + 0*y**3, y**3]))

# II16: f(z) = -3z^3 + 13z/12
func_list.append(DynamicalSystem([-3*x**3 + QQ(13)/12*x*y**2 + 0*y**3, y**3]))

# II17: f(z) = 6z^3/5 - 17z/6
func_list.append(DynamicalSystem([QQ(6)/5*x**3 - QQ(17)/6*x*y**2 + 0*y**3, y**3]))

# II18: f(z) = 3z^3/2 - 19z/6
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(19)/6*x*y**2 + 0*y**3, y**3]))

# II19: f(z) = -3z^3/2 + 19z/6
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(19)/6*x*y**2 + 0*y**3, y**3]))

# II20: f(z) = 3z^3/2 - z/24
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(1)/24*x*y**2 + 0*y**3, y**3]))

# II21: f(z) = -3z^3/2 + z/24
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(1)/24*x*y**2 + 0*y**3, y**3]))

# II22: f(z) = 3z^3 - 25z/12
func_list.append(DynamicalSystem([3*x**3 - QQ(25)/12*x*y**2 + 0*y**3, y**3]))

# II23: f(z) = 3z^3/2 - 25z/24
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(25)/24*x*y**2 + 0*y**3, y**3]))

# II24: f(z) = 5z^3/3 - 34z/15
func_list.append(DynamicalSystem([QQ(5)/3*x**3 - QQ(34)/15*x*y**2 + 0*y**3, y**3]))

# II25: f(z) = -5z^3/3 + 34z/15
func_list.append(DynamicalSystem([-QQ(5)/3*x**3 + QQ(34)/15*x*y**2 + 0*y**3, y**3]))

# II26: f(z) = 3z^3 - 37z/12
func_list.append(DynamicalSystem([3*x**3 - QQ(37)/12*x*y**2 + 0*y**3, y**3]))

# II27: f(z) = -3z^3 + 37z/12
func_list.append(DynamicalSystem([-3*x**3 + QQ(37)/12*x*y**2 + 0*y**3, y**3]))

# II28: f(z) = 3z^3/2 - 49z/24
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(49)/24*x*y**2 + 0*y**3, y**3]))

# II29: f(z) = -3z^3/2 + 49z/24
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(49)/24*x*y**2 + 0*y**3, y**3]))

# II30: f(z) = 3z^3/2 - 73z/24
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(73)/24*x*y**2 + 0*y**3, y**3]))

# II31: f(z) = -3z^3/2 + 73z/24
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(73)/24*x*y**2 + 0*y**3, y**3]))

# II32: f(z) = 7z^3/6 - 163z/42
func_list.append(DynamicalSystem([QQ(7)/6*x**3 - QQ(163)/42*x*y**2 + 0*y**3, y**3]))

# II33: f(z) = -7z^3/6 + 163z/42
func_list.append(DynamicalSystem([-QQ(7)/6*x**3 + QQ(163)/42*x*y**2 + 0*y**3, y**3]))

# II34: f(z) = 6z^3/5 - 169z/120
func_list.append(DynamicalSystem([QQ(6)/5*x**3 - QQ(169)/120*x*y**2 + 0*y**3, y**3]))

# II35: f(z) = -6z^3/5 + 169z/120
func_list.append(DynamicalSystem([-QQ(6)/5*x**3 + QQ(169)/120*x*y**2 + 0*y**3, y**3]))

# II36: f(z) = 6z^3/5 - 289z/120
func_list.append(DynamicalSystem([QQ(6)/5*x**3 - QQ(289)/120*x*y**2 + 0*y**3, y**3]))

# II37: f(z) = -6z^3/5 + 289z/120
func_list.append(DynamicalSystem([-QQ(6)/5*x**3 + QQ(289)/120*x*y**2 + 0*y**3, y**3]))

for F in func_list:
    found, F_id = model_in_database_NF(F, my_cursor)
    if found:
        add_citations_NF(F_id, cites, my_cursor, log_file=log_file)
    else: #not in database
        label = add_function_all_NF(F, my_cursor,\
                citations=cites, log_file=log_file)


my_session.commit()

log_file.close()

#my_session.close()
