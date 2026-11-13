# Dynabase (https://dynabase.org): Dimension 1, degree 9 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^9, y^9], domain=P), '1.790bef87.083b88f1.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.f4ddead6.588b0522.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9 + x^5*y^4, y^9], domain=P), '1.7b81e06a.0fabe57c.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9 + x^3*y^6, y^9], domain=P), '1.cc20f300.bf01317f.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
