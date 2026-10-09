# Dynabase (https://dynabase.org): dimension 1, degree 6, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 1.8372e-09
dynabase_systems.append([DynamicalSystem([29*x^6 + 639*x^5*y + 4925*x^4*y^2 + 15345*x^3*y^3 + 12686*x^2*y^4 - 23544*x*y^5 - 5040*y^6, -5040*y^6], domain=P), '1.3ae91201.688c90c9.1', P(0, 1)])
# Hutz2026; height ratio 2.056e-09
dynabase_systems.append([DynamicalSystem([4*x^6 + 137*x^5*y + 1810*x^4*y^2 + 11295*x^3*y^3 + 32386*x^2*y^4 + 34528*x*y^5 - 1680*y^6, 1680*y^6], domain=P), '1.c8900699.e39a2a24.1', P(0, 1)])
# Hutz2026; height ratio 2.1833e-09
dynabase_systems.append([DynamicalSystem([11*x^6 + 246*x^5*y + 1955*x^4*y^2 + 6570*x^3*y^3 + 6854*x^2*y^4 - 10596*x*y^5 - 2520*y^6, -2520*y^6], domain=P), '1.25af66d3.72e1d34b.1', P(0, 1)])
# Hutz2026; height ratio 2.3063e-09
dynabase_systems.append([DynamicalSystem([7*x^6 + 127*x^5*y + 805*x^4*y^2 + 1965*x^3*y^3 + 748*x^2*y^4 - 2452*x*y^5 - 240*y^6, -240*y^6], domain=P), '1.f4ae4239.237a939c.1', P(0, 1)])

print("Dynabase: 4 dynamical systems in dynabase_systems")
