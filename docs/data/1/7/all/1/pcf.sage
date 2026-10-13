# Dynabase (https://dynabase.org): Dimension 1, degree 7 maps over QQ, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.6c5154c1.84c0eaef.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
