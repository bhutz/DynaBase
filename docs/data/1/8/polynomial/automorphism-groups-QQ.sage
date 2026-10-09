# Dynabase (https://dynabase.org): dimension 1, degree 8, polynomial maps, Automorphism Groups, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^8, y^8], domain=P), '1.a2cb972c.bc5e6238.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^8 + x*y^7, y^8], domain=P), '1.27e72460.98bcfef1.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
