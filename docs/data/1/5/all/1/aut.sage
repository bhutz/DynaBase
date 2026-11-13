# Dynabase (https://dynabase.org): Dimension 1, degree 5 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Miasnikov2017, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.77659db6.3af5a8ff.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.05e343fb.f4c36872.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.141f1a9c.37bd3a33.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5 + x^3*y^2, y^5], domain=P), '1.38a9c050.7707a7b4.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
