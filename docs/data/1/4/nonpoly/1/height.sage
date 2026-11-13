# Dynabase (https://dynabase.org): Dimension 1, degree 4 non-polynomial maps over QQ, Small Height Ratio
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

print("Dynabase: 3 dynamical systems in dynabase_systems")
