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

###########################################
#a*z^3 + b*z + c
#Benedetto-Dickman-Joseph-Krause-Rubin-Zhou Examples
#https://mgolech.github.io/cubics/index.html , f(z) column
#Table I: form a*z^3 + b*z + 1 (79 preperiodic portraits, rows I1-I79;
#some portraits have two representative maps, both included)
#Table II: form a*z^3 + b*z (37 preperiodic portraits, rows II1-II37)
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
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

# DUPLICATE - same rational preperiodic graph as I36 (earlier map), already in this table - commented out
# I36: f(z) = -9z^3/10 + 21z/10 + 1
#func_list.append(DynamicalSystem([-QQ(9)/10*x**3 + QQ(21)/10*x*y**2 + y**3, y**3]))

# I37: f(z) = -z^3/16 + 7z/4 + 1
func_list.append(DynamicalSystem([-QQ(1)/16*x**3 + QQ(7)/4*x*y**2 + y**3, y**3]))

# I38: f(z) = 3z^3/16 - 7z/12 + 1
func_list.append(DynamicalSystem([QQ(3)/16*x**3 - QQ(7)/12*x*y**2 + y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I38 (earlier map), already in this table - commented out
# I38: f(z) = 2z^3/15 - 38z/15 + 1
#func_list.append(DynamicalSystem([QQ(2)/15*x**3 - QQ(38)/15*x*y**2 + y**3, y**3]))

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

# DUPLICATE - same rational preperiodic graph as I55 (earlier map), already in this table - commented out
# I55: f(z) = -49z^3/48 + 19z/12 + 1
#func_list.append(DynamicalSystem([-QQ(49)/48*x**3 + QQ(19)/12*x*y**2 + y**3, y**3]))

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

# DUPLICATE - same rational preperiodic graph as I68 (earlier map), already in this table - commented out
# I68: f(z) = 144z^3 - 12z + 1
#func_list.append(DynamicalSystem([144*x**3 - 12*x*y**2 + y**3, y**3]))

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

# DUPLICATE - same rational preperiodic graph as I78 (earlier map), already in this table - commented out
# I78: f(z) = -289z^3/16 + 27z/4 + 1
#func_list.append(DynamicalSystem([-QQ(289)/16*x**3 + QQ(27)/4*x*y**2 + y**3, y**3]))

# I79: f(z) = 27z^3/256 - 133z/48 + 1
func_list.append(DynamicalSystem([QQ(27)/256*x**3 - QQ(133)/48*x*y**2 + y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I29, already in this table - commented out
# II1: f(z) = z^3
#func_list.append(DynamicalSystem([x**3 + 0*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I30, already in this table - commented out
# II2: f(z) = -z^3
#func_list.append(DynamicalSystem([-x**3 + 0*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I3, already in this table - commented out
# II3: f(z) = z^3 + z
#func_list.append(DynamicalSystem([x**3 + x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I4, already in this table - commented out
# II4: f(z) = z^3 - z
#func_list.append(DynamicalSystem([x**3 - x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I40, already in this table - commented out
# II5: f(z) = z^3 - 3z
#func_list.append(DynamicalSystem([x**3 - 3*x*y**2 + 0*y**3, y**3]))

# II6: f(z) = -z^3 + 3z
func_list.append(DynamicalSystem([-x**3 + 3*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I14, already in this table - commented out
# II7: f(z) = 3z^3 - z/3
#func_list.append(DynamicalSystem([3*x**3 - QQ(1)/3*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I44, already in this table - commented out
# II8: f(z) = -3z^3 + z/3
#func_list.append(DynamicalSystem([-3*x**3 + QQ(1)/3*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I53, already in this table - commented out
# II9: f(z) = z^3 - 5z/4
#func_list.append(DynamicalSystem([x**3 - QQ(5)/4*x*y**2 + 0*y**3, y**3]))

# II10: f(z) = 2z^3 - 5z/2
func_list.append(DynamicalSystem([2*x**3 - QQ(5)/2*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I49, already in this table - commented out
# II11: f(z) = 3z^3/2 - z/6
#func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(1)/6*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I43, already in this table - commented out
# II12: f(z) = 2z^3 - 7z/2
#func_list.append(DynamicalSystem([2*x**3 - QQ(7)/2*x*y**2 + 0*y**3, y**3]))

# II13: f(z) = -2z^3 + 7z/2
func_list.append(DynamicalSystem([-2*x**3 + QQ(7)/2*x*y**2 + 0*y**3, y**3]))

# II14: f(z) = 3z^3/2 - 13z/6
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(13)/6*x*y**2 + 0*y**3, y**3]))

# II15: f(z) = 3z^3 - 13z/12
func_list.append(DynamicalSystem([3*x**3 - QQ(13)/12*x*y**2 + 0*y**3, y**3]))

# II16: f(z) = -3z^3 + 13z/12
func_list.append(DynamicalSystem([-3*x**3 + QQ(13)/12*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I70, already in this table - commented out
# II17: f(z) = 6z^3/5 - 17z/6
#func_list.append(DynamicalSystem([QQ(6)/5*x**3 - QQ(17)/6*x*y**2 + 0*y**3, y**3]))

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

# DUPLICATE - same rational preperiodic graph as I66, already in this table - commented out
# II29: f(z) = -3z^3/2 + 49z/24
#func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(49)/24*x*y**2 + 0*y**3, y**3]))

# II30: f(z) = 3z^3/2 - 73z/24
func_list.append(DynamicalSystem([QQ(3)/2*x**3 - QQ(73)/24*x*y**2 + 0*y**3, y**3]))

# II31: f(z) = -3z^3/2 + 73z/24
func_list.append(DynamicalSystem([-QQ(3)/2*x**3 + QQ(73)/24*x*y**2 + 0*y**3, y**3]))

# II32: f(z) = 7z^3/6 - 163z/42
func_list.append(DynamicalSystem([QQ(7)/6*x**3 - QQ(163)/42*x*y**2 + 0*y**3, y**3]))

# DUPLICATE - same rational preperiodic graph as I33, already in this table - commented out
# II33: f(z) = -7z^3/6 + 163z/42
#func_list.append(DynamicalSystem([-QQ(7)/6*x**3 + QQ(163)/42*x*y**2 + 0*y**3, y**3]))

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

###########################################
#Doyle-Hyde Examples
#arXiv:2201.11707 / DH2025, Table 2 row d=3: f([m]) in [n] for [k] = {1,...,k}
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['DH2025']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# conjugate to II18 (one of Benedetto et al.'s record cubics, as the paper notes):
# adds no new function, only attaches the DH2025 citation to the existing one
# d=3, m=11, n=11: f(z) = (z^3 - 18z^2 + 89z - 66)/6
func_list.append(DynamicalSystem([x**3 - 18*x**2*y + 89*x*y**2 - 66*y**3, 6*y**3]))

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

# degree 3
# many 10 (3,2): orbit [0, 1, -3, -1, 4]
func_list.append(orbit_poly_system([0, 1, -3, -1, 4]))
# cycle (1, 5): orbit [0, 1, -1, 3, -3]
func_list.append(orbit_poly_system([0, 1, -1, 3, -3]))
# cycle (0, 5): orbit [0, 1, -1, 2, -2]
func_list.append(orbit_poly_system([0, 1, -1, 2, -2]))
# tail (4, 1): orbit [0, 1, -1, 2, -3]
func_list.append(orbit_poly_system([0, 1, -1, 2, -3]))
# tail (4, 1): orbit [0, 1, 4, 9, 10]
func_list.append(orbit_poly_system([0, 1, 4, 9, 10]))
# tail (4, 1): orbit [0, 1, 7, 3, 8]
func_list.append(orbit_poly_system([0, 1, 7, 3, 8]))

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
#postcritically finite (PCF) cubic polynomials over QQ
#Anderson-Manes-Tobin, Cubic post-critically finite polynomials defined over Q
#(AMT2020), Theorem: exactly fifteen conjugacy classes over QQbar.
#The theorem statement prints (5) and (13) identically as -z^3 + 3/2z^2 - 1;
#Table 1 has both -z^3 + 3/2z^2 - 1 and -z^3 + 3/2z^2 + 1, and both are PCF,
#so (13) is taken to be the + 1 map.
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['AMT2020']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# (1) z^3
func_list.append(DynamicalSystem([x**3, y**3]))
# (2) -z^3 + 1
func_list.append(DynamicalSystem([-x**3 + y**3, y**3]))
# (3) -2z^3 + 3z^2 + 1/2
func_list.append(DynamicalSystem([-2*x**3 + 3*x**2*y + QQ(1)/2*y**3, y**3]))
# (4) -2z^3 + 3z^2
func_list.append(DynamicalSystem([-2*x**3 + 3*x**2*y, y**3]))
# (5) -z^3 + 3/2z^2 - 1
func_list.append(DynamicalSystem([-x**3 + QQ(3)/2*x**2*y - y**3, y**3]))
# (6) 2z^3 - 3z^2 + 1
func_list.append(DynamicalSystem([2*x**3 - 3*x**2*y + y**3, y**3]))
# (7) 2z^3 - 3z^2 + 1/2
func_list.append(DynamicalSystem([2*x**3 - 3*x**2*y + QQ(1)/2*y**3, y**3]))
# (8) z^3 - 3/2z^2
func_list.append(DynamicalSystem([x**3 - QQ(3)/2*x**2*y, y**3]))
# (9) -3z^3 + 9/2z^2
func_list.append(DynamicalSystem([-3*x**3 + QQ(9)/2*x**2*y, y**3]))
# (10) -4z^3 + 6z^2 - 1/2
func_list.append(DynamicalSystem([-4*x**3 + 6*x**2*y - QQ(1)/2*y**3, y**3]))
# (11) 4z^3 - 6z^2 + 3/2
func_list.append(DynamicalSystem([4*x**3 - 6*x**2*y + QQ(3)/2*y**3, y**3]))
# (12) 3z^3 - 9/2z^2 + 1
func_list.append(DynamicalSystem([3*x**3 - QQ(9)/2*x**2*y + y**3, y**3]))
# (13) -z^3 + 3/2z^2 + 1
func_list.append(DynamicalSystem([-x**3 + QQ(3)/2*x**2*y + y**3, y**3]))
# (14) -1/4z^3 + 3/2z + 2
func_list.append(DynamicalSystem([-QQ(1)/4*x**3 + QQ(3)/2*x*y**2 + 2*y**3, y**3]))
# (15) -1/28z^3 - 3/4z + 7/2
func_list.append(DynamicalSystem([-QQ(1)/28*x**3 - QQ(3)/4*x*y**2 + QQ(7)/2*y**3, y**3]))

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
#postcritically finite (PCF) monic centered cubic polynomials z^3 + Az + B over QQ
#Ingram, A finiteness result for post-critically finite polynomials (Ingram2012),
#Section 4. The two (-3/4, +-3/4) maps are conjugate; all seven are among the
#AMT2020 classes above.
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['Ingram2012']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# (A, B) = (-3, 0)
func_list.append(DynamicalSystem([x**3 - 3*x*y**2, y**3]))
# (A, B) = (-3/2, 0)
func_list.append(DynamicalSystem([x**3 - QQ(3)/2*x*y**2, y**3]))
# (A, B) = (-3/4, 3/4)
func_list.append(DynamicalSystem([x**3 - QQ(3)/4*x*y**2 + QQ(3)/4*y**3, y**3]))
# (A, B) = (-3/4, -3/4)
func_list.append(DynamicalSystem([x**3 - QQ(3)/4*x*y**2 - QQ(3)/4*y**3, y**3]))
# (A, B) = (0, 0)
func_list.append(DynamicalSystem([x**3, y**3]))
# (A, B) = (3/2, 0)
func_list.append(DynamicalSystem([x**3 + QQ(3)/2*x*y**2, y**3]))
# (A, B) = (3, 0)
func_list.append(DynamicalSystem([x**3 + 3*x*y**2, y**3]))

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
