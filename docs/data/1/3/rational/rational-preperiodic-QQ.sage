# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.bb44cfba.16d54f50.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^3 + 94*x^2*y + 118*x*y^2 - 84*y^3, 33*x^3 + 122*x^2*y - 43*x*y^2 - 42*y^3], domain=P), '1.161ac27f.6ad71bd1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([24*x^3 + 12*x^2*y - 39*x*y^2 + 3*y^3, 4*x^3 + 28*x^2*y - 20*x*y^2 + 6*y^3], domain=P), '1.f857410f.edf1d3b1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([180*x^3 - 564*x^2*y - 48*x*y^2 + 332*y^3, -270*x^3 + 543*x^2*y - 169*x*y^2 - 254*y^3], domain=P), '1.e9500b5e.676e33f1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 7*x^2*y - 63*x*y^2 + 20*y^3, 9*x^3 - 62*x^2*y + 33*x*y^2 + 20*y^3], domain=P), '1.77979ce5.f41a47d3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 8*x^2*y + 2*x*y^2 - 4*y^3, 3*x^3 + 13*x^2*y + 2*x*y^2], domain=P), '1.e848265f.05b2f134.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^3 - 61*x^2*y - 83*x*y^2 + 90*y^3, -40*x^3 + 15*x^2*y - 5*x*y^2 + 30*y^3], domain=P), '1.f786e132.47eb7e99.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([78*x^3 + 72*x^2*y - 182*x*y^2 - 28*y^3, -3*x^3 + 107*x^2*y + 100*x*y^2 - 84*y^3], domain=P), '1.6eb32f83.c841c711.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([137*x^3 + 28*x^2*y - 203*x*y^2 + 38*y^3, -9*x^3 + 139*x^2*y + 6*x*y^2 - 76*y^3], domain=P), '1.01cf4253.f091e4fc.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.05af5145.a779cc92.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([658*x^3 - 1545*x^2*y - 3442*x*y^2 + 2025*y^3, 201*x^3 - 215*x^2*y + 541*x*y^2 - 675*y^3], domain=P), '1.1825f5a3.a46ef689.1'])

print("Dynabase: 13 dynamical systems in dynabase_systems")
