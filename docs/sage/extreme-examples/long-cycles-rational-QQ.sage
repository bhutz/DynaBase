# Dynabase (https://dynabase.org): Summary of Extreme Examples, long rational cycles, rational maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.f087c4af.5b9da8c6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.05af5145.a779cc92.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.273dc9f6.ddfc6e2a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
