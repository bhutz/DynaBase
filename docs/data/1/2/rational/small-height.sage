# Dynabase (https://dynabase.org): dimension 1, degree 2, rational maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 0.00046574
dynabase_systems.append([DynamicalSystem([592*x^2 - 3424*x*y + 1024*y^2, 173*x^2 - 536*x*y - 1024*y^2], domain=P), '1.3b026e07.265dfbb0.1', P(0, 1)])
# Hutz2026; height ratio 0.001183
dynabase_systems.append([DynamicalSystem([285*x^2 + 2085*x*y + 990*y^2, -79*x^2 - 351*x*y + 990*y^2], domain=P), '1.0a9b4372.2927b5eb.1', P(0, 1)])

print("Dynabase: 2 dynamical systems in dynabase_systems")
