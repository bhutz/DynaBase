# Dynabase (https://dynabase.org): Summary of Extreme Examples, many rational preperiodic points, rational maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Vishkautsan2026
dynabase_systems.append([DynamicalSystem([x^2 + 5*x*y - 6*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.51af6b72.2a948ef0.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.bb44cfba.16d54f50.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([148*x^4 + 384*x^3*y - 447*x^2*y^2 - 261*x*y^3 + 20*y^4, -52*x^4 - 134*x^3*y + 38*x^2*y^2 - 184*x*y^3 + 20*y^4], domain=P), '1.b31b924e.d130ecb7.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
