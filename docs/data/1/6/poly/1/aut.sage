# Dynabase (https://dynabase.org): Dimension 1, degree 6 polynomials over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^6, y^6], domain=P), '1.46c82190.c2bd952a.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.99d40459.e75b5525.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
