# Dynabase (https://dynabase.org): dimension 1, degree 5, polynomial maps, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.6f752b35.d8e415c3.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5 + x^3*y^2, y^5], domain=P), '1.91738bc3.f35ae2c4.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
