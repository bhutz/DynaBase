# Dynabase (https://dynabase.org): Dimension 1, degree 4 maps over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 2.1843e-08
dynabase_systems.append([DynamicalSystem([49*x^4 + 844*x^3*y + 4499*x^2*y^2 + 7364*x*y^3 - 660*y^4, -10*x^4 - 174*x^3*y - 866*x^2*y^2 - 1122*x*y^3 + 660*y^4], domain=P), '1.dd20a767.b08ba5a7.1', P(0, 1)])
# Hutz2026; height ratio 2.6346e-08
dynabase_systems.append([DynamicalSystem([91*x^4 + 428*x^3*y - 2133*x^2*y^2 - 4922*x*y^3 - 184*y^4, 60*x^4 - 236*x^3*y - 674*x^2*y^2 + 194*x*y^3 - 184*y^4], domain=P), '1.f45c3ed4.4bf9abc0.1', P(0, 1)])
# Hutz2026; height ratio 2.9735e-08
dynabase_systems.append([DynamicalSystem([182*x^4 + 1323*x^3*y + 2023*x^2*y^2 + 717*x*y^3 + 1755*y^4, -15*x^4 - 36*x^3*y - 30*x^2*y^2 - 1284*x*y^3 - 1755*y^4], domain=P), '1.c8cfbb8a.ce17fea0.1', P(0, 1)])
# Hutz2026; height ratio 2.9015e-06
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.5e8dcb6e.41954f0a.1', P(0, 1)])
# Hutz2026; height ratio 2.9568e-06
dynabase_systems.append([DynamicalSystem([11*x^4 - 246*x^3*y + 2101*x^2*y^2 - 6906*x*y^3 - 840*y^4, -840*y^4], domain=P), '1.f5ef2f2b.e5a7f2ff.1', P(0, 1)])
# Hutz2026; height ratio 3.0905e-06
dynabase_systems.append([DynamicalSystem([7*x^4 + 33*x^3*y - 58*x^2*y^2 - 222*x*y^3 + 60*y^4, 60*y^4], domain=P), '1.6f0e407b.23fa2201.1', P(0, 1)])

print("Dynabase: 6 dynamical systems in dynabase_systems")
