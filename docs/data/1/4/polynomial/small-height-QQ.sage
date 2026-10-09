# Dynabase (https://dynabase.org): dimension 1, degree 4, polynomial maps, Small Height Ratio, over QQ
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
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.f2147436.53db7cc0.1', P(0, 1)])
# Hutz2026; height ratio 2.9568e-06
dynabase_systems.append([DynamicalSystem([11*x^4 - 246*x^3*y + 2101*x^2*y^2 - 6906*x*y^3 - 840*y^4, -840*y^4], domain=P), '1.9e5d8556.ae91e74b.1', P(0, 1)])
# Hutz2026; height ratio 3.0905e-06
dynabase_systems.append([DynamicalSystem([7*x^4 + 33*x^3*y - 58*x^2*y^2 - 222*x*y^3 + 60*y^4, 60*y^4], domain=P), '1.84307af0.41a6c807.1', P(0, 1)])
# GHJSX2021; height ratio 0.03589
dynabase_systems.append([DynamicalSystem([2*x^4, x^3*y + 2*y^4], domain=P), '1.d20ab877.52739882.1', P(-1, 1)])
# Fraser2024; height ratio 0.074074
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.5457b5e3.e9909514.1', P(-1, 2)])
# dFH2018, GHJSX2021, FN1997; height ratio 0.10082
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.a2324809.3fbf9eac.1', P(1, 1)])
# Fraser2024; height ratio 0.12209
dynabase_systems.append([DynamicalSystem([x^4 - y^4, -y^4], domain=P), '1.770c2622.7cef54b3.1', P(-2, 1)])
# Fraser2024; height ratio 0.30931
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.8e57877c.24b4743f.1', P(2, 1)])

print("Dynabase: 8 dynamical systems in dynabase_systems")
