# Dynabase (https://dynabase.org): dimension 1, degree 3, polynomial maps, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, y^3], domain=P), '1.9554125a.42669779.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
