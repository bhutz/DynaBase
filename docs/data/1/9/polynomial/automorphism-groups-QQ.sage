# Dynabase (https://dynabase.org): dimension 1, degree 9, polynomial maps, Automorphism Groups, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^9, y^9], domain=P), '1.3d72adff.f501313b.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.7b05c466.f7c38225.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9 + x^5*y^4, y^9], domain=P), '1.f19293aa.19a13510.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9 + x^3*y^6, y^9], domain=P), '1.dd26a3f3.8eb7c9e7.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
