# Dynabase (https://dynabase.org): Dimension 1, degree 5 polynomials over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.05e343fb.f4c36872.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.141f1a9c.37bd3a33.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5 + x^3*y^2, y^5], domain=P), '1.38a9c050.7707a7b4.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
