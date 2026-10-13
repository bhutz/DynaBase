# Dynabase (https://dynabase.org): Dimension 1, degree 6 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^6, y^6], domain=P), '1.d60c7e5d.aa38682f.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.ab5c2018.5ec8e92f.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
