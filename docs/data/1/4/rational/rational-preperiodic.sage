# Dynabase (https://dynabase.org): dimension 1, degree 4, rational maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026
dynabase_systems.append([DynamicalSystem([148*x^4 + 384*x^3*y - 447*x^2*y^2 - 261*x*y^3 + 20*y^4, -52*x^4 - 134*x^3*y + 38*x^2*y^2 - 184*x*y^3 + 20*y^4], domain=P), '1.b31b924e.d130ecb7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.273dc9f6.ddfc6e2a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([22*x^4 + 9*x^3*y - 109*x^2*y^2 + 234*x*y^3 + 144*y^4, 8*x^4 - 74*x^3*y - 80*x^2*y^2 + 92*x*y^3 - 96*y^4], domain=P), '1.5f6c3257.9610aaf4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([309*x^4 - 1290*x^3*y - 2109*x^2*y^2 + 1794*x*y^3 + 2304*y^4, 161*x^4 - 432*x^3*y - 1679*x^2*y^2 + 870*x*y^3 + 576*y^4], domain=P), '1.4e082e6b.9f635f09.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([245*x^4 - 134*x^3*y - 2879*x^2*y^2 - 2164*x*y^3 + 576*y^4, 59*x^4 + 73*x^3*y - 812*x^2*y^2 - 922*x*y^3 - 576*y^4], domain=P), '1.71cbf504.843422aa.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([222*x^4 + 85*x^3*y - 369*x^2*y^2 - 298*x*y^3 - 60*y^4, 4*x^4 + 258*x^3*y + 93*x^2*y^2 - 185*x*y^3 - 30*y^4], domain=P), '1.dc43b25d.a6ee6b7e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^4 - 153*x^3*y - 67*x^2*y^2 + 558*x*y^3 + 72*y^4, 8*x^4 - 20*x^3*y + 34*x^2*y^2 - 100*x*y^3 - 72*y^4], domain=P), '1.9d32fd4e.6cd17e03.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 + 4*x^3*y + 123*x^2*y^2 - 604*x*y^3 - 132*y^4, -10*x^4 - 14*x^3*y + 262*x^2*y^2 + 14*x*y^3 - 132*y^4], domain=P), '1.0efc460c.908765ce.1'])

print("Dynabase: 9 dynamical systems in dynabase_systems")
