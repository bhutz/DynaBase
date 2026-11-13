# Dynabase (https://dynabase.org): Dimension 1, degree 4 polynomials over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 2.9015e-06
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.5e8dcb6e.41954f0a.1', P(0, 1)])
# Hutz2026; height ratio 2.9568e-06
dynabase_systems.append([DynamicalSystem([11*x^4 - 246*x^3*y + 2101*x^2*y^2 - 6906*x*y^3 - 840*y^4, -840*y^4], domain=P), '1.f5ef2f2b.e5a7f2ff.1', P(0, 1)])
# Hutz2026; height ratio 3.0905e-06
dynabase_systems.append([DynamicalSystem([7*x^4 + 33*x^3*y - 58*x^2*y^2 - 222*x*y^3 + 60*y^4, 60*y^4], domain=P), '1.6f0e407b.23fa2201.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
