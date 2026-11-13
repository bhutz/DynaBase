# Dynabase (https://dynabase.org): Dimension 1, degree 3 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.fcc3f607.78dde912.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.fcc3f607.790bef87.1'])
# FN1997, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.34726b93.790bef87.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.343beeba.c008598d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3 - x*y^2], domain=P), '1.0cf9b7d5.e6c6bfb3.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
