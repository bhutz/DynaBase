# Dynabase (https://dynabase.org): Dimension 1, degree 7 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.9190add3.023ff0b9.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.4b1ca9ed.023ff0b9.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.48690a94.9c571960.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x^4*y^3, y^7], domain=P), '1.d10cb60c.a191ee94.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x^3*y^4, y^7], domain=P), '1.87db90d3.89dadf22.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
