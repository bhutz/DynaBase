# Dynabase (https://dynabase.org): Dimension 1, degree 3 polynomials over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.5fe37194.3d72adff.1'])
# FN1997, dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, y^3], domain=P), '1.9554125a.42669779.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
