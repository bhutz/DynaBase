# Dynabase (https://dynabase.org): dimension 1, degree 2, rational maps, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.89eb0e1e.d90eecb7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.095ed92d.7e1406dd.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.f87176de.3b08f253.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.c346226f.0c3c179e.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.366a39dc.7475b914.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.fbfd6fd4.9888ce4b.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.170a93ef.0fdf09c7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.4cc4fb80.ef9cb8b5.1'])
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])

print("Dynabase: 9 dynamical systems in dynabase_systems")
