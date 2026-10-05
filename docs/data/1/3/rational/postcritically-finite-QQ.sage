# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Postcritically Finite, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
