# Dynabase (https://dynabase.org): dimension 1, degree 3, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 9.2099e-05
dynabase_systems.append([DynamicalSystem([2*x^3 + 21*x^2*y + 25*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.4f511a5c.f031a661.1', P(0, 1)])
# Hutz2026; height ratio 0.00016547
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y - 37*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.53ae6e59.415bb16f.1', P(0, 1)])
# Hutz2026; height ratio 0.00016738
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2 - 6*y^3, -6*y^3], domain=P), '1.fa2ce9d2.c2b4dc06.1', P(0, 1)])
# dFH2018; height ratio 0.23321
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, y^3], domain=P), '1.9554125a.42669779.1', P(-1, 1)])

print("Dynabase: 4 dynamical systems in dynabase_systems")
