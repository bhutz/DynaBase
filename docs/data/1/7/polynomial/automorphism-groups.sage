# Dynabase (https://dynabase.org): dimension 1, degree 7, polynomial maps, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.e614ceae.cc96fc25.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
