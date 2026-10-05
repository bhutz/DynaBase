# Dynabase (https://dynabase.org): dimension 1, degree 5, polynomial maps, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
