# Dynabase (https://dynabase.org): Dimension 1, degree 4 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# FN1997, GHJSX2021, Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.024ac6d7.76c4de71.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, -x^3*y], domain=P), '1.bec3eb46.3f16aab2.1'])
# FN1997, dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.a2324809.3fbf9eac.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x^3*y - x*y^3], domain=P), '1.66a11a01.35767842.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
