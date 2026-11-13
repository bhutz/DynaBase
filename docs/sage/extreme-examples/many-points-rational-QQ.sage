# Dynabase (https://dynabase.org): Summary of Extreme Examples, many rational preperiodic points, non-polynomial maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Vishkautsan2026
dynabase_systems.append([DynamicalSystem([x^2 + 5*x*y - 6*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.f990fc06.6562ad8f.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.df73f7e3.c8b68e52.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 48*y^4, 7*x^3*y - 28*x*y^3], domain=P), '1.e9a7d5d9.535c299c.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.43808372.c2bd952a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.9190add3.023ff0b9.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.4dbdab6d.d8496994.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
