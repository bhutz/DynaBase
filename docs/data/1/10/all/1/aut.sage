# Dynabase (https://dynabase.org): Dimension 1, degree 10 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^10, y^10], domain=P), '1.500c00a0.a04b9cb7.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10 + x*y^9, y^10], domain=P), '1.32c02398.5289177c.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10 + x^4*y^6, y^10], domain=P), '1.b73ae813.561abc2a.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
