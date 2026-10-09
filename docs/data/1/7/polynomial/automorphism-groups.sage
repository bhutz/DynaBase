# Dynabase (https://dynabase.org): dimension 1, degree 7, polynomial maps, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.6c5154c1.84c0eaef.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.e614ceae.cc96fc25.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x^4*y^3, y^7], domain=P), '1.567e3af6.0eb4f200.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x^3*y^4, y^7], domain=P), '1.796eda56.b6dd4150.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
