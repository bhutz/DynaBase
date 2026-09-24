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
#quadratic rational functions phi(w) = N(w)/D(w) over QQ
#Benedetto-Chen-Hyde-Kovacheva-White Examples
#https://rlbenedetto.people.amherst.edu/quadratdata/
#Each file PerXLenY lists maps for which inf has a QQ-rational forward orbit
#of length Y ending in a cycle of period X.  Only the maps are recorded here
#(not the orbits); the first 10 maps of each file are included (all of them
#when a file has fewer than 10).  Period 2, Length 6 is omitted from the
#source itself.
#Entries whose rational preperiodic graph (over the entry's own field) is
#already realized by an earlier entry in the same table - same degree,
#polynomial/rational, and base field degree - are commented out and
#marked DUPLICATE, so each table holds one function per graph structure.
cites = ['BCHKW2014']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# Period 2, Length 8 (Per2Len8): first 10 listed
# Per2Len8 #1: phi(w) = (-1540*w^2 + 24815*w - 23275)/(-1540*w^2 + 5549*w + 2660)
func_list.append(DynamicalSystem([-1540*x**2 + 24815*x*y - 23275*y**2, -1540*x**2 + 5549*x*y + 2660*y**2]))

# Per2Len8 #2: phi(w) = (308*w^2 + 19292*w - 19600)/(308*w^2 + 1937*w + 7700)
func_list.append(DynamicalSystem([308*x**2 + 19292*x*y - 19600*y**2, 308*x**2 + 1937*x*y + 7700*y**2]))

# DUPLICATE - conjugate to Per2Len8 #2, already in this table - commented out
# Per2Len8 #3: phi(w) = (7752*w^2 - 3417*w - 4335)/(7752*w^2 + 25508*w + 12240)
#func_list.append(DynamicalSystem([7752*x**2 - 3417*x*y - 4335*y**2, 7752*x**2 + 25508*x*y + 12240*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #4: phi(w) = (-13*w^2 + 1872*w - 1859)/(-13*w^2 + 178*w + 143)
#func_list.append(DynamicalSystem([-13*x**2 + 1872*x*y - 1859*y**2, -13*x**2 + 178*x*y + 143*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #5: phi(w) = (700*w^2 - 95*w - 605)/(700*w^2 + 1336*w + 880)
#func_list.append(DynamicalSystem([700*x**2 - 95*x*y - 605*y**2, 700*x**2 + 1336*x*y + 880*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #6: phi(w) = (21*w^2 - 560*w + 539)/(21*w^2 - 10*w - 231)
#func_list.append(DynamicalSystem([21*x**2 - 560*x*y + 539*y**2, 21*x**2 - 10*x*y - 231*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #7: phi(w) = (-9009*w^2 + 17094*w - 8085)/(-9009*w^2 + 18454*w + 10395)
#func_list.append(DynamicalSystem([-9009*x**2 + 17094*x*y - 8085*y**2, -9009*x**2 + 18454*x*y + 10395*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #8: phi(w) = (468*w^2 + 4284*w - 4752)/(468*w^2 + 1369*w + 1188)
#func_list.append(DynamicalSystem([468*x**2 + 4284*x*y - 4752*y**2, 468*x**2 + 1369*x*y + 1188*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #9: phi(w) = (-784*w^2 + 416*w + 368)/(-784*w^2 - 3885*w - 644)
#func_list.append(DynamicalSystem([-784*x**2 + 416*x*y + 368*y**2, -784*x**2 - 3885*x*y - 644*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len8 #1, already in this table - commented out
# Per2Len8 #10: phi(w) = (21*w^2 - 84*w + 63)/(21*w^2 - 16*w - 21)
#func_list.append(DynamicalSystem([21*x**2 - 84*x*y + 63*y**2, 21*x**2 - 16*x*y - 21*y**2]))


# Period 3, Length 8 (Per3Len8): first 10 listed
# Per3Len8 #1: phi(w) = (-399*w^2 + 9785*w - 9386)/(-399*w^2 + 2063*w + 1482)
func_list.append(DynamicalSystem([-399*x**2 + 9785*x*y - 9386*y**2, -399*x**2 + 2063*x*y + 1482*y**2]))

# DUPLICATE - conjugate to Per3Len8 #1, already in this table - commented out
# Per3Len8 #2: phi(w) = (330*w^2 - 187*w - 143)/(330*w^2 + 1217*w + 429)
#func_list.append(DynamicalSystem([330*x**2 - 187*x*y - 143*y**2, 330*x**2 + 1217*x*y + 429*y**2]))


# Period 1, Length 7 (Per1Len7): first 10 listed
# Per1Len7 #1: phi(w) = (4*w^2 + 508*w - 512)/(4*w^2 + 79*w + 16)
func_list.append(DynamicalSystem([4*x**2 + 508*x*y - 512*y**2, 4*x**2 + 79*x*y + 16*y**2]))

# DUPLICATE - conjugate to Per1Len7 #1, already in this table - commented out
# Per1Len7 #2: phi(w) = (-105*w^2 + 81*w + 24)/(-105*w^2 - 491*w - 108)
#func_list.append(DynamicalSystem([-105*x**2 + 81*x*y + 24*y**2, -105*x**2 - 491*x*y - 108*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len7 #1, already in this table - commented out
# Per1Len7 #3: phi(w) = (28*w^2 + 20*w - 48)/(28*w^2 - 37*w - 36)
#func_list.append(DynamicalSystem([28*x**2 + 20*x*y - 48*y**2, 28*x**2 - 37*x*y - 36*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len7 #1, already in this table - commented out
# Per1Len7 #4: phi(w) = (385*w^2 - 310*w - 75)/(385*w^2 - 802*w - 15)
#func_list.append(DynamicalSystem([385*x**2 - 310*x*y - 75*y**2, 385*x**2 - 802*x*y - 15*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len7 #1, already in this table - commented out
# Per1Len7 #5: phi(w) = (-600*w^2 + 924*w - 324)/(-600*w^2 + 965*w - 360)
#func_list.append(DynamicalSystem([-600*x**2 + 924*x*y - 324*y**2, -600*x**2 + 965*x*y - 360*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len7 #1, already in this table - commented out
# Per1Len7 #6: phi(w) = (-320*w^2 + 545*w - 225)/(-320*w^2 + 564*w - 240)
#func_list.append(DynamicalSystem([-320*x**2 + 545*x*y - 225*y**2, -320*x**2 + 564*x*y - 240*y**2]))


# Period 2, Length 7 (Per2Len7): first 10 listed
# Per2Len7 #1: phi(w) = (-238425*w^2 + 703425*w - 465000)/(-238425*w^2 + 307351*w + 153450)
func_list.append(DynamicalSystem([-238425*x**2 + 703425*x*y - 465000*y**2, -238425*x**2 + 307351*x*y + 153450*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #2: phi(w) = (-1070300*w^2 + 1180300*w - 110000)/(-1070300*w^2 + 1011619*w + 84700)
#func_list.append(DynamicalSystem([-1070300*x**2 + 1180300*x*y - 110000*y**2, -1070300*x**2 + 1011619*x*y + 84700*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #3: phi(w) = (14212*w^2 - 7678*w - 6534)/(14212*w^2 + 50597*w + 5016)
#func_list.append(DynamicalSystem([14212*x**2 - 7678*x*y - 6534*y**2, 14212*x**2 + 50597*x*y + 5016*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #4: phi(w) = (1001*w^2 + 8800*w - 9801)/(1001*w^2 + 4810*w + 9009)
#func_list.append(DynamicalSystem([1001*x**2 + 8800*x*y - 9801*y**2, 1001*x**2 + 4810*x*y + 9009*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #5: phi(w) = (-4268*w^2 + 51313*w - 47045)/(-4268*w^2 + 9208*w + 3880)
#func_list.append(DynamicalSystem([-4268*x**2 + 51313*x*y - 47045*y**2, -4268*x**2 + 9208*x*y + 3880*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #6: phi(w) = (-1995*w^2 - 16055*w + 18050)/(-1995*w^2 - 7007*w - 3990)
#func_list.append(DynamicalSystem([-1995*x**2 - 16055*x*y + 18050*y**2, -1995*x**2 - 7007*x*y - 3990*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #7: phi(w) = (12103*w^2 - 3078*w - 9025)/(12103*w^2 + 34622*w + 1995)
#func_list.append(DynamicalSystem([12103*x**2 - 3078*x*y - 9025*y**2, 12103*x**2 + 34622*x*y + 1995*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #8: phi(w) = (154090*w^2 - 190190*w + 36100)/(154090*w^2 + 699829*w - 8360)
#func_list.append(DynamicalSystem([154090*x**2 - 190190*x*y + 36100*y**2, 154090*x**2 + 699829*x*y - 8360*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #9: phi(w) = (-14136*w^2 - 103189*w + 117325)/(-14136*w^2 - 37144*w - 29640)
#func_list.append(DynamicalSystem([-14136*x**2 - 103189*x*y + 117325*y**2, -14136*x**2 - 37144*x*y - 29640*y**2]))

# DUPLICATE - same rational preperiodic graph as Per2Len7 #1, already in this table - commented out
# Per2Len7 #10: phi(w) = (-434*w^2 + 35030*w - 34596)/(-434*w^2 + 1495*w + 744)
#func_list.append(DynamicalSystem([-434*x**2 + 35030*x*y - 34596*y**2, -434*x**2 + 1495*x*y + 744*y**2]))


# Period 3, Length 7 (Per3Len7): first 10 listed
# Per3Len7 #1: phi(w) = (36036*w^2 - 123156*w + 87120)/(36036*w^2 + 147529*w - 26400)
func_list.append(DynamicalSystem([36036*x**2 - 123156*x*y + 87120*y**2, 36036*x**2 + 147529*x*y - 26400*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #2: phi(w) = (-735*w^2 + 510*w + 225)/(-735*w^2 + 224*w - 105)
#func_list.append(DynamicalSystem([-735*x**2 + 510*x*y + 225*y**2, -735*x**2 + 224*x*y - 105*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #3: phi(w) = (322*w^2 - 3262*w + 2940)/(322*w^2 - 559*w - 630)
#func_list.append(DynamicalSystem([322*x**2 - 3262*x*y + 2940*y**2, 322*x**2 - 559*x*y - 630*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #4: phi(w) = (462*w^2 - 583*w + 121)/(462*w^2 + 215*w - 33)
#func_list.append(DynamicalSystem([462*x**2 - 583*x*y + 121*y**2, 462*x**2 + 215*x*y - 33*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #5: phi(w) = (132*w^2 - 253*w + 121)/(132*w^2 + 227*w - 44)
#func_list.append(DynamicalSystem([132*x**2 - 253*x*y + 121*y**2, 132*x**2 + 227*x*y - 44*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #6: phi(w) = (495*w^2 - 858*w + 363)/(495*w^2 - 586*w - 165)
#func_list.append(DynamicalSystem([495*x**2 - 858*x*y + 363*y**2, 495*x**2 - 586*x*y - 165*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #7: phi(w) = (153*w^2 + 171*w - 324)/(153*w^2 + 655*w + 72)
#func_list.append(DynamicalSystem([153*x**2 + 171*x*y - 324*y**2, 153*x**2 + 655*x*y + 72*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #8: phi(w) = (3128*w^2 + 3757*w - 6885)/(3128*w^2 + 7272*w + 7650)
#func_list.append(DynamicalSystem([3128*x**2 + 3757*x*y - 6885*y**2, 3128*x**2 + 7272*x*y + 7650*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #9: phi(w) = (40*w^2 + 152*w - 192)/(40*w^2 + 119*w + 72)
#func_list.append(DynamicalSystem([40*x**2 + 152*x*y - 192*y**2, 40*x**2 + 119*x*y + 72*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len7 #1, already in this table - commented out
# Per3Len7 #10: phi(w) = (35*w^2 + 14*w - 49)/(35*w^2 + 113*w + 14)
#func_list.append(DynamicalSystem([35*x**2 + 14*x*y - 49*y**2, 35*x**2 + 113*x*y + 14*y**2]))


# Period 4, Length 7 (Per4Len7): first 10 listed
# Per4Len7 #1: phi(w) = (35*w^2 - 1603*w + 1568)/(35*w^2 - 64*w - 700)
func_list.append(DynamicalSystem([35*x**2 - 1603*x*y + 1568*y**2, 35*x**2 - 64*x*y - 700*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #2: phi(w) = (1470*w^2 + 555*w - 2025)/(1470*w^2 + 5131*w + 4410)
#func_list.append(DynamicalSystem([1470*x**2 + 555*x*y - 2025*y**2, 1470*x**2 + 5131*x*y + 4410*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #3: phi(w) = (-8505*w^2 + 6055*w + 2450)/(-8505*w^2 + 11313*w - 630)
#func_list.append(DynamicalSystem([-8505*x**2 + 6055*x*y + 2450*y**2, -8505*x**2 + 11313*x*y - 630*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #4: phi(w) = (-78078*w^2 + 333993*w - 255915)/(-78078*w^2 + 27976*w + 403260)
#func_list.append(DynamicalSystem([-78078*x**2 + 333993*x*y - 255915*y**2, -78078*x**2 + 27976*x*y + 403260*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #5: phi(w) = (-196*w^2 + 596*w - 400)/(-196*w^2 + 1757*w + 140)
#func_list.append(DynamicalSystem([-196*x**2 + 596*x*y - 400*y**2, -196*x**2 + 1757*x*y + 140*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #6: phi(w) = (1820*w^2 - 3020*w + 1200)/(1820*w^2 + 533*w - 780)
#func_list.append(DynamicalSystem([1820*x**2 - 3020*x*y + 1200*y**2, 1820*x**2 + 533*x*y - 780*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #7: phi(w) = (21*w^2 - 246*w + 225)/(21*w^2 + 122*w - 15)
#func_list.append(DynamicalSystem([21*x**2 - 246*x*y + 225*y**2, 21*x**2 + 122*x*y - 15*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #8: phi(w) = (-1925*w^2 + 5071*w - 3146)/(-1925*w^2 + 5305*w + 7150)
#func_list.append(DynamicalSystem([-1925*x**2 + 5071*x*y - 3146*y**2, -1925*x**2 + 5305*x*y + 7150*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #9: phi(w) = (35*w^2 + 602*w - 637)/(35*w^2 + 230*w + 455)
#func_list.append(DynamicalSystem([35*x**2 + 602*x*y - 637*y**2, 35*x**2 + 230*x*y + 455*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len7 #1, already in this table - commented out
# Per4Len7 #10: phi(w) = (10*w^2 - 185*w + 175)/(10*w^2 - 32*w - 140)
#func_list.append(DynamicalSystem([10*x**2 - 185*x*y + 175*y**2, 10*x**2 - 32*x*y - 140*y**2]))


# Period 5, Length 7 (Per5Len7): first 10 listed
# Per5Len7 #1: phi(w) = (-100*w^2 + 1350*w - 1250)/(-100*w^2 + 393*w + 400)
func_list.append(DynamicalSystem([-100*x**2 + 1350*x*y - 1250*y**2, -100*x**2 + 393*x*y + 400*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #2: phi(w) = (440*w^2 + 407*w - 847)/(440*w^2 + 1244*w + 1232)
#func_list.append(DynamicalSystem([440*x**2 + 407*x*y - 847*y**2, 440*x**2 + 1244*x*y + 1232*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #3: phi(w) = (-3630*w^2 + 4530*w - 900)/(-3630*w^2 + 3179*w + 990)
#func_list.append(DynamicalSystem([-3630*x**2 + 4530*x*y - 900*y**2, -3630*x**2 + 3179*x*y + 990*y**2]))

# DUPLICATE - conjugate to Per5Len7 #1, already in this table - commented out
# Per5Len7 #4: phi(w) = (175*w^2 - 28*w - 147)/(175*w^2 + 610*w + 315)
#func_list.append(DynamicalSystem([175*x**2 - 28*x*y - 147*y**2, 175*x**2 + 610*x*y + 315*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #5: phi(w) = (36*w^2 + 396*w - 432)/(36*w^2 + 179*w + 324)
#func_list.append(DynamicalSystem([36*x**2 + 396*x*y - 432*y**2, 36*x**2 + 179*x*y + 324*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #6: phi(w) = (66*w^2 - 48*w - 18)/(66*w^2 + 239*w - 60)
#func_list.append(DynamicalSystem([66*x**2 - 48*x*y - 18*y**2, 66*x**2 + 239*x*y - 60*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #7: phi(w) = (-315*w^2 + 490*w - 175)/(-315*w^2 + 408*w - 105)
#func_list.append(DynamicalSystem([-315*x**2 + 490*x*y - 175*y**2, -315*x**2 + 408*x*y - 105*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #8: phi(w) = (-462*w^2 + 66*w + 396)/(-462*w^2 - 989*w + 726)
#func_list.append(DynamicalSystem([-462*x**2 + 66*x*y + 396*y**2, -462*x**2 - 989*x*y + 726*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #9: phi(w) = (455*w^2 - 308*w - 147)/(455*w^2 + 2050*w - 525)
#func_list.append(DynamicalSystem([455*x**2 - 308*x*y - 147*y**2, 455*x**2 + 2050*x*y - 525*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len7 #1, already in this table - commented out
# Per5Len7 #10: phi(w) = (-2508*w^2 + 4444*w - 1936)/(-2508*w^2 + 4637*w - 2112)
#func_list.append(DynamicalSystem([-2508*x**2 + 4444*x*y - 1936*y**2, -2508*x**2 + 4637*x*y - 2112*y**2]))


# Period 6, Length 7 (Per6Len7): first 10 listed
# Per6Len7 #1: phi(w) = (-127908*w^2 + 149940*w - 22032)/(-127908*w^2 + 102365*w + 11628)
func_list.append(DynamicalSystem([-127908*x**2 + 149940*x*y - 22032*y**2, -127908*x**2 + 102365*x*y + 11628*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #2: phi(w) = (-168454*w^2 + 196042*w - 27588)/(-168454*w^2 + 165567*w + 116622)
#func_list.append(DynamicalSystem([-168454*x**2 + 196042*x*y - 27588*y**2, -168454*x**2 + 165567*x*y + 116622*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #3: phi(w) = (792*w^2 - 351*w - 441)/(792*w^2 + 1924*w + 924)
#func_list.append(DynamicalSystem([792*x**2 - 351*x*y - 441*y**2, 792*x**2 + 1924*x*y + 924*y**2]))

# Per6Len7 #4: phi(w) = (-3553*w^2 + 55176*w - 51623)/(-3553*w^2 + 24366*w + 29887)
func_list.append(DynamicalSystem([-3553*x**2 + 55176*x*y - 51623*y**2, -3553*x**2 + 24366*x*y + 29887*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #5: phi(w) = (520*w^2 + 663*w - 1183)/(520*w^2 + 782*w + 364)
#func_list.append(DynamicalSystem([520*x**2 + 663*x*y - 1183*y**2, 520*x**2 + 782*x*y + 364*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #6: phi(w) = (495*w^2 - 195*w - 300)/(495*w^2 - 917*w + 270)
#func_list.append(DynamicalSystem([495*x**2 - 195*x*y - 300*y**2, 495*x**2 - 917*x*y + 270*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #7: phi(w) = (297*w^2 - 585*w + 288)/(297*w^2 + 449*w - 108)
#func_list.append(DynamicalSystem([297*x**2 - 585*x*y + 288*y**2, 297*x**2 + 449*x*y - 108*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #8: phi(w) = (714*w^2 - 1326*w + 612)/(714*w^2 - 1859*w - 714)
#func_list.append(DynamicalSystem([714*x**2 - 1326*x*y + 612*y**2, 714*x**2 - 1859*x*y - 714*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #9: phi(w) = (-858*w^2 + 1038*w - 180)/(-858*w^2 + 3503*w + 330)
#func_list.append(DynamicalSystem([-858*x**2 + 1038*x*y - 180*y**2, -858*x**2 + 3503*x*y + 330*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len7 #10: phi(w) = (-8840*w^2 + 4165*w + 4675)/(-8840*w^2 - 7022*w - 3740)
#func_list.append(DynamicalSystem([-8840*x**2 + 4165*x*y + 4675*y**2, -8840*x**2 - 7022*x*y - 3740*y**2]))


# Period 7, Length 7 (Per7Len7): first 10 listed
# Per7Len7 #1: phi(w) = (-4655*w^2 + 4826*w - 171)/(-4655*w^2 + 8071*w - 798)
func_list.append(DynamicalSystem([-4655*x**2 + 4826*x*y - 171*y**2, -4655*x**2 + 8071*x*y - 798*y**2]))

# DUPLICATE - conjugate to Per7Len7 #1, already in this table - commented out
# Per7Len7 #2: phi(w) = (-215644*w^2 + 281644*w - 66000)/(-215644*w^2 + 349037*w - 128700)
#func_list.append(DynamicalSystem([-215644*x**2 + 281644*x*y - 66000*y**2, -215644*x**2 + 349037*x*y - 128700*y**2]))

# DUPLICATE - conjugate to Per7Len7 #1, already in this table - commented out
# Per7Len7 #3: phi(w) = (-37050*w^2 + 57875*w - 20825)/(-37050*w^2 + 80161*w - 33915)
#func_list.append(DynamicalSystem([-37050*x**2 + 57875*x*y - 20825*y**2, -37050*x**2 + 80161*x*y - 33915*y**2]))

# DUPLICATE - conjugate to Per7Len7 #1, already in this table - commented out
# Per7Len7 #4: phi(w) = (17661*w^2 - 11325*w - 6336)/(17661*w^2 - 128992*w - 3828)
#func_list.append(DynamicalSystem([17661*x**2 - 11325*x*y - 6336*y**2, 17661*x**2 - 128992*x*y - 3828*y**2]))


# Period 1, Length 6 (Per1Len6): first 10 listed
# Per1Len6 #1: phi(w) = (319*w^2 + 32351*w - 32670)/(319*w^2 + 6819*w + 1650)
func_list.append(DynamicalSystem([319*x**2 + 32351*x*y - 32670*y**2, 319*x**2 + 6819*x*y + 1650*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #2: phi(w) = (8613*w^2 - 871101*w + 862488)/(8613*w^2 + 342379*w - 139392)
#func_list.append(DynamicalSystem([8613*x**2 - 871101*x*y + 862488*y**2, 8613*x**2 + 342379*x*y - 139392*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #3: phi(w) = (836*w^2 + 103708*w - 104544)/(836*w^2 + 12333*w + 27456)
#func_list.append(DynamicalSystem([836*x**2 + 103708*x*y - 104544*y**2, 836*x**2 + 12333*x*y + 27456*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #4: phi(w) = (156940*w^2 - 6014165*w + 5857225)/(156940*w^2 + 6289049*w - 184965)
#func_list.append(DynamicalSystem([156940*x**2 - 6014165*x*y + 5857225*y**2, 156940*x**2 + 6289049*x*y - 184965*y**2]))

# Per1Len6 #5: phi(w) = (268736*w^2 + 203281*w - 472017)/(268736*w^2 + 49974*w + 155610)
func_list.append(DynamicalSystem([268736*x**2 + 203281*x*y - 472017*y**2, 268736*x**2 + 49974*x*y + 155610*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #6: phi(w) = (-137199*w^2 + 61509*w + 75690)/(-137199*w^2 + 523841*w - 72210)
#func_list.append(DynamicalSystem([-137199*x**2 + 61509*x*y + 75690*y**2, -137199*x**2 + 523841*x*y - 72210*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #7: phi(w) = (429*w^2 + 673167*w - 673596)/(429*w^2 - 80753*w + 116424)
#func_list.append(DynamicalSystem([429*x**2 + 673167*x*y - 673596*y**2, 429*x**2 - 80753*x*y + 116424*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #8: phi(w) = (11520*w^2 - 18081*w + 6561)/(11520*w^2 + 77764*w - 5184)
#func_list.append(DynamicalSystem([11520*x**2 - 18081*x*y + 6561*y**2, 11520*x**2 + 77764*x*y - 5184*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #9: phi(w) = (212036*w^2 - 2115541*w + 1903505)/(212036*w^2 + 2641099*w - 795135)
#func_list.append(DynamicalSystem([212036*x**2 - 2115541*x*y + 1903505*y**2, 212036*x**2 + 2641099*x*y - 795135*y**2]))

# DUPLICATE - same rational preperiodic graph as Per1Len6 #1, already in this table - commented out
# Per1Len6 #10: phi(w) = (-115479*w^2 + 60723*w + 54756)/(-115479*w^2 + 170348*w - 32994)
#func_list.append(DynamicalSystem([-115479*x**2 + 60723*x*y + 54756*y**2, -115479*x**2 + 170348*x*y - 32994*y**2]))


# Period 3, Length 6 (Per3Len6): first 10 listed
# Per3Len6 #1: phi(w) = (324*w^2 + 1676*w - 2000)/(324*w^2 + 477*w + 180)
func_list.append(DynamicalSystem([324*x**2 + 1676*x*y - 2000*y**2, 324*x**2 + 477*x*y + 180*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #2: phi(w) = (29106*w^2 - 58509*w + 29403)/(29106*w^2 + 9226*w - 16632)
#func_list.append(DynamicalSystem([29106*x**2 - 58509*x*y + 29403*y**2, 29106*x**2 + 9226*x*y - 16632*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #3: phi(w) = (-39520*w^2 + 48545*w - 9025)/(-39520*w^2 - 904*w + 6080)
#func_list.append(DynamicalSystem([-39520*x**2 + 48545*x*y - 9025*y**2, -39520*x**2 - 904*x*y + 6080*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #4: phi(w) = (-96330*w^2 + 195605*w - 99275)/(-96330*w^2 + 151151*w + 95095)
#func_list.append(DynamicalSystem([-96330*x**2 + 195605*x*y - 99275*y**2, -96330*x**2 + 151151*x*y + 95095*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #5: phi(w) = (-1456*w^2 + 26299*w - 24843)/(-1456*w^2 + 4164*w + 1092)
#func_list.append(DynamicalSystem([-1456*x**2 + 26299*x*y - 24843*y**2, -1456*x**2 + 4164*x*y + 1092*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #6: phi(w) = (1456*w^2 - 42861*w + 41405)/(1456*w^2 + 6540*w - 3640)
#func_list.append(DynamicalSystem([1456*x**2 - 42861*x*y + 41405*y**2, 1456*x**2 + 6540*x*y - 3640*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #7: phi(w) = (182*w^2 - 41587*w + 41405)/(182*w^2 + 1353*w - 10010)
#func_list.append(DynamicalSystem([182*x**2 - 41587*x*y + 41405*y**2, 182*x**2 + 1353*x*y - 10010*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #8: phi(w) = (-27300*w^2 + 35581*w - 8281)/(-27300*w^2 + 26792*w + 8736)
#func_list.append(DynamicalSystem([-27300*x**2 + 35581*x*y - 8281*y**2, -27300*x**2 + 26792*x*y + 8736*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #9: phi(w) = (-107800*w^2 + 84568*w + 23232)/(-107800*w^2 + 805*w - 9240)
#func_list.append(DynamicalSystem([-107800*x**2 + 84568*x*y + 23232*y**2, -107800*x**2 + 805*x*y - 9240*y**2]))

# DUPLICATE - same rational preperiodic graph as Per3Len6 #1, already in this table - commented out
# Per3Len6 #10: phi(w) = (5544*w^2 - 44264*w + 38720)/(5544*w^2 + 6675*w - 19800)
#func_list.append(DynamicalSystem([5544*x**2 - 44264*x*y + 38720*y**2, 5544*x**2 + 6675*x*y - 19800*y**2]))


# Period 4, Length 6 (Per4Len6): first 10 listed
# Per4Len6 #1: phi(w) = (-5432*w^2 + 80704*w - 75272)/(-5432*w^2 + 10249*w + 6208)
func_list.append(DynamicalSystem([-5432*x**2 + 80704*x*y - 75272*y**2, -5432*x**2 + 10249*x*y + 6208*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #2: phi(w) = (359136*w^2 - 91872*w - 267264)/(359136*w^2 - 236747*w + 80736)
#func_list.append(DynamicalSystem([359136*x**2 - 91872*x*y - 267264*y**2, 359136*x**2 - 236747*x*y + 80736*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #3: phi(w) = (7505*w^2 + 1520*w - 9025)/(7505*w^2 + 24014*w + 4085)
#func_list.append(DynamicalSystem([7505*x**2 + 1520*x*y - 9025*y**2, 7505*x**2 + 24014*x*y + 4085*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #4: phi(w) = (-52173*w^2 + 147312*w - 95139)/(-52173*w^2 + 56728*w + 11253)
#func_list.append(DynamicalSystem([-52173*x**2 + 147312*x*y - 95139*y**2, -52173*x**2 + 56728*x*y + 11253*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #5: phi(w) = (-43524*w^2 + 112716*w - 69192)/(-43524*w^2 + 60661*w + 38688)
#func_list.append(DynamicalSystem([-43524*x**2 + 112716*x*y - 69192*y**2, -43524*x**2 + 60661*x*y + 38688*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #6: phi(w) = (-205387*w^2 - 101010*w + 306397)/(-205387*w^2 - 177405*w - 249158)
#func_list.append(DynamicalSystem([-205387*x**2 - 101010*x*y + 306397*y**2, -205387*x**2 - 177405*x*y - 249158*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #7: phi(w) = (-18690*w^2 + 97900*w - 79210)/(-18690*w^2 + 34473*w + 26700)
#func_list.append(DynamicalSystem([-18690*x**2 + 97900*x*y - 79210*y**2, -18690*x**2 + 34473*x*y + 26700*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #8: phi(w) = (347130*w^2 - 203319*w - 143811)/(347130*w^2 + 2230871*w + 38019)
#func_list.append(DynamicalSystem([347130*x**2 - 203319*x*y - 143811*y**2, 347130*x**2 + 2230871*x*y + 38019*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #9: phi(w) = (650160*w^2 - 28896*w - 621264)/(650160*w^2 - 302719*w + 252840)
#func_list.append(DynamicalSystem([650160*x**2 - 28896*x*y - 621264*y**2, 650160*x**2 - 302719*x*y + 252840*y**2]))

# DUPLICATE - same rational preperiodic graph as Per4Len6 #1, already in this table - commented out
# Per4Len6 #10: phi(w) = (-245100*w^2 - 124700*w + 369800)/(-245100*w^2 - 389223*w - 322500)
#func_list.append(DynamicalSystem([-245100*x**2 - 124700*x*y + 369800*y**2, -245100*x**2 - 389223*x*y - 322500*y**2]))


# Period 5, Length 6 (Per5Len6): first 10 listed
# Per5Len6 #1: phi(w) = (-9825*w^2 - 160175*w + 170000)/(-9825*w^2 + 396133*w - 1700)
func_list.append(DynamicalSystem([-9825*x**2 - 160175*x*y + 170000*y**2, -9825*x**2 + 396133*x*y - 1700*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #2: phi(w) = (-5425*w^2 + 115425*w - 110000)/(-5425*w^2 + 35389*w + 7700)
#func_list.append(DynamicalSystem([-5425*x**2 + 115425*x*y - 110000*y**2, -5425*x**2 + 35389*x*y + 7700*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #3: phi(w) = (12425*w^2 + 727575*w - 740000)/(12425*w^2 + 189151*w + 51800)
#func_list.append(DynamicalSystem([12425*x**2 + 727575*x*y - 740000*y**2, 12425*x**2 + 189151*x*y + 51800*y**2]))

# Per5Len6 #4: phi(w) = (158100*w^2 + 1171900*w - 1330000)/(158100*w^2 + 813997*w + 226100)
func_list.append(DynamicalSystem([158100*x**2 + 1171900*x*y - 1330000*y**2, 158100*x**2 + 813997*x*y + 226100*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #5: phi(w) = (6175*w^2 + 38825*w - 45000)/(6175*w^2 + 30257*w + 8550)
#func_list.append(DynamicalSystem([6175*x**2 + 38825*x*y - 45000*y**2, 6175*x**2 + 30257*x*y + 8550*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #6: phi(w) = (85025*w^2 + 449975*w - 535000)/(85025*w^2 + 348111*w + 101650)
#func_list.append(DynamicalSystem([85025*x**2 + 449975*x*y - 535000*y**2, 85025*x**2 + 348111*x*y + 101650*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #7: phi(w) = (13756*w^2 - 171756*w + 158000)/(13756*w^2 + 63269*w - 30020)
#func_list.append(DynamicalSystem([13756*x**2 - 171756*x*y + 158000*y**2, 13756*x**2 + 63269*x*y - 30020*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #8: phi(w) = (151525*w^2 + 183475*w - 335000)/(151525*w^2 + 632911*w + 97150)
#func_list.append(DynamicalSystem([151525*x**2 + 183475*x*y - 335000*y**2, 151525*x**2 + 632911*x*y + 97150*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #9: phi(w) = (3225*w^2 + 231775*w - 235000)/(3225*w^2 + 70471*w + 101050)
#func_list.append(DynamicalSystem([3225*x**2 + 231775*x*y - 235000*y**2, 3225*x**2 + 70471*x*y + 101050*y**2]))

# DUPLICATE - same rational preperiodic graph as Per5Len6 #1, already in this table - commented out
# Per5Len6 #10: phi(w) = (315952*w^2 + 342048*w - 658000)/(315952*w^2 + 1007333*w + 322420)
#func_list.append(DynamicalSystem([315952*x**2 + 342048*x*y - 658000*y**2, 315952*x**2 + 1007333*x*y + 322420*y**2]))


# Period 6, Length 6 (Per6Len6): first 10 listed
# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #1: phi(w) = (5236*w^2 - 117887*w + 112651)/(5236*w^2 + 1633*w - 19019)
#func_list.append(DynamicalSystem([5236*x**2 - 117887*x*y + 112651*y**2, 5236*x**2 + 1633*x*y - 19019*y**2]))

# Per6Len6 #2: phi(w) = (1176637*w^2 + 3664147*w - 4840784)/(1176637*w^2 + 1468075*w + 457912)
func_list.append(DynamicalSystem([1176637*x**2 + 3664147*x*y - 4840784*y**2, 1176637*x**2 + 1468075*x*y + 457912*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #3: phi(w) = (152*w^2 + 2984*w - 3136)/(152*w^2 + 709*w + 504)
#func_list.append(DynamicalSystem([152*x**2 + 2984*x*y - 3136*y**2, 152*x**2 + 709*x*y + 504*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #4: phi(w) = (1210*w^2 - 2010*w + 800)/(1210*w^2 + 693*w - 220)
#func_list.append(DynamicalSystem([1210*x**2 - 2010*x*y + 800*y**2, 1210*x**2 + 693*x*y - 220*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #5: phi(w) = (-35090*w^2 + 29490*w + 5600)/(-35090*w^2 + 62601*w - 10780)
#func_list.append(DynamicalSystem([-35090*x**2 + 29490*x*y + 5600*y**2, -35090*x**2 + 62601*x*y - 10780*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #6: phi(w) = (-132618*w^2 + 71018*w + 61600)/(-132618*w^2 - 339667*w - 143220)
#func_list.append(DynamicalSystem([-132618*x**2 + 71018*x*y + 61600*y**2, -132618*x**2 - 339667*x*y - 143220*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #7: phi(w) = (169*w^2 + 81*w - 250)/(169*w^2 + 897*w + 260)
#func_list.append(DynamicalSystem([169*x**2 + 81*x*y - 250*y**2, 169*x**2 + 897*x*y + 260*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #8: phi(w) = (-30400*w^2 + 27873*w + 2527)/(-30400*w^2 + 76680*w - 10640)
#func_list.append(DynamicalSystem([-30400*x**2 + 27873*x*y + 2527*y**2, -30400*x**2 + 76680*x*y - 10640*y**2]))

# DUPLICATE - conjugate to Per6Len7 #1, already in this table - commented out
# Per6Len6 #9: phi(w) = (15884*w^2 - 10484*w - 5400)/(15884*w^2 + 59641*w + 6840)
#func_list.append(DynamicalSystem([15884*x**2 - 10484*x*y - 5400*y**2, 15884*x**2 + 59641*x*y + 6840*y**2]))

# DUPLICATE - same rational preperiodic graph as Per6Len7 #1, already in this table - commented out
# Per6Len6 #10: phi(w) = (66*w^2 + 130*w - 196)/(66*w^2 + 113*w + 42)
#func_list.append(DynamicalSystem([66*x**2 + 130*x*y - 196*y**2, 66*x**2 + 113*x*y + 42*y**2]))

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
#Vishkautsan Example
#personal communication, Sept 2026
#16 QQ-rational preperiodic points, two 3-cycles:
#0 -> inf -> 1 -> 0 and -10 -> 11 -> -5/11 -> -10
cites = ['Vishkautsan2026']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# f(z) = (z^2 - 21z + 20)/(z^2 + 7z)
func_list.append(DynamicalSystem([x**2 - 21*x*y + 20*y**2, x**2 + 7*x*y]))

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

# degree 2
# many 14,(6, 2): orbit [0, -1, -3, -6, -2, -4]
func_list.append(orbit_rational_system([0, -1, -3, -6, -2, -4]))
# many 14,(1, 5): orbit [0, -1, 2, 6, 4, 5]
func_list.append(orbit_rational_system([0, -1, 2, 6, 4, 5]))
# many 14,(3, 3): orbit [0, 1, -1, 3, -6, -15]
func_list.append(orbit_rational_system([0, 1, -1, 3, -6, -15]))
# many 14,(3, 3): orbit [0, 1, -1, 4, -5, -14]
func_list.append(orbit_rational_system([0, 1, -1, 4, -5, -14]))
# cycle (0, 6): orbit [0, 1, -1, -9, -14, 26]
func_list.append(orbit_rational_system([0, 1, -1, -9, -14, 26]))
# cycle (1, 5): orbit [0, -1, -4, -10, -2, 2]
func_list.append(orbit_rational_system([0, -1, -4, -10, -2, 2]))
# cycle (1, 5): orbit [0, -1, 1, 9, -3, 4]
func_list.append(orbit_rational_system([0, -1, 1, 9, -3, 4]))
# cycle (1, 5): orbit [0, 1, 3, 5, 15, -3]
func_list.append(orbit_rational_system([0, 1, 3, 5, 15, -3]))
# tail (6, 2): orbit [0, -1, -3, -6, -12, 3]
func_list.append(orbit_rational_system([0, -1, -3, -6, -12, 3]))
# tail (6, 2): orbit [0, -1, -9, 27, 3, -15]
func_list.append(orbit_rational_system([0, -1, -9, 27, 3, -15]))
# tail (6, 2): orbit [0, 1, 3, -8, -7, -11]
func_list.append(orbit_rational_system([0, 1, 3, -8, -7, -11]))

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
#postcritically finite (PCF) quadratic rational maps over QQ
#Lukas-Manes-Yap, A census of quadratic post-critically finite rational functions
#defined over Q (Lukas2014), Theorem 1: exactly twelve conjugacy classes over
#QQbar. The three polynomials (1), (3), (4) are in
#add_functions_quadratic_polys_dim_1.py. (10) as in Table 1: the theorem
#statement's layout reads ambiguously as (2z + 1)/(4z^2 - 2z), which is not PCF.
#Every class is kept, even when its rational preperiodic graph repeats one
#already in the table: this is a complete classification of PCF maps (the site
#generator still shows one function per graph). A map conjugate to one already
#in the database adds no new function, only this citation.
cites = ['Lukas2014']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

func_list = []

# (2) 1/z^2
func_list.append(DynamicalSystem([y**2, x**2]))
# (5) 1/(2(z - 1)^2)
func_list.append(DynamicalSystem([y**2, 2*(x - y)**2]))
# (6) 1/(z - 1)^2
func_list.append(DynamicalSystem([y**2, (x - y)**2]))
# (7) -1/(4z^2 - 4z)
func_list.append(DynamicalSystem([-y**2, 4*x**2 - 4*x*y]))
# (8) -4/(9z^2 - 12z)
func_list.append(DynamicalSystem([-4*y**2, 9*x**2 - 12*x*y]))
# (9) 2/(z - 1)^2
func_list.append(DynamicalSystem([2*y**2, (x - y)**2]))
# (10) (2z + 1)/(4z - 2z^2)
func_list.append(DynamicalSystem([(2*x + y)*y, 4*x*y - 2*x**2]))
# (11) -2z/(2z^2 - 4z + 1)
func_list.append(DynamicalSystem([-2*x*y, 2*x**2 - 4*x*y + y**2]))
# (12) (3z^2 - 4z + 1)/(1 - 4z)
func_list.append(DynamicalSystem([3*x**2 - 4*x*y + y**2, (y - 4*x)*y]))

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
