# Dynabase (https://dynabase.org): Summary of Extreme Examples, long rational tails, rational maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# BCHKW2014
dynabase_systems.append([DynamicalSystem([264*x^2 + 291*x*y - 285*y^2, -121*x^2 + 268*x*y + 285*y^2], domain=P), '1.76567776.1f5edaf9.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^3 - 61*x^2*y - 83*x*y^2 + 90*y^3, -40*x^3 + 15*x^2*y - 5*x*y^2 + 30*y^3], domain=P), '1.f786e132.47eb7e99.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([222*x^4 + 85*x^3*y - 369*x^2*y^2 - 298*x*y^3 - 60*y^4, 4*x^4 + 258*x^3*y + 93*x^2*y^2 - 185*x*y^3 - 30*y^4], domain=P), '1.dc43b25d.a6ee6b7e.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
