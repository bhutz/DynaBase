# Dynabase (https://dynabase.org): dimension 1, degree 2, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 0.0066042
dynabase_systems.append([DynamicalSystem([x^2 - 7*x*y - 12*y^2, 6*y^2], domain=P), '1.98c91caa.4cf50642.1', P(0, 1)])
# Hutz2026; height ratio 0.01102
dynabase_systems.append([DynamicalSystem([x^2 + 17*x*y - 6*y^2, -6*y^2], domain=P), '1.55c16ffb.e4dc7fdb.1', P(0, 1)])
# Hutz2026; height ratio 0.013458
dynabase_systems.append([DynamicalSystem([5*x^2 - 97*x*y - 756*y^2, -42*y^2], domain=P), '1.5fab3ba3.dc35593e.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
