# Dynabase (https://dynabase.org): dimension 1, degree 2, rational maps, Automorphism Groups, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# Milnor1993
dynabase_systems.append([DynamicalSystem([x^2 + y^2, x*y], domain=P), '1.d3259bab.d36dd573.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
