# Dynabase (https://dynabase.org): dimension 1, degree 10, polynomial maps, Postcritically Finite, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^10, y^10], domain=P), '1.f0bbe529.7d4a3a0d.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
