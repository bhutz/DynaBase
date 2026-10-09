# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Automorphism Groups
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
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^2*y + y^3, x^3 + 2*x*y^2], domain=P), '1.f3cb63c5.12dbaacc.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.6a61ce14.c0adc3ec.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3 - x*y^2], domain=P), '1.fa448265.8d0f1905.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
