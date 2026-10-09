# Dynabase (https://dynabase.org): dimension 1, degree 5, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 9.1519e-09
dynabase_systems.append([DynamicalSystem([x^5 + 20*x^4*y + 135*x^3*y^2 + 340*x^2*y^3 + 184*x*y^4 + 40*y^5, -40*y^5], domain=P), '1.96a4ba66.02556abd.1', P(0, 1)])
# Hutz2026; height ratio 1.6874e-08
dynabase_systems.append([DynamicalSystem([2*x^5 + 35*x^4*y + 200*x^3*y^2 + 385*x^2*y^3 + 38*x*y^4 + 60*y^5, -60*y^5], domain=P), '1.7578ba72.e29751ce.1', P(0, 1)])
# Hutz2026; height ratio 2.8227e-08
dynabase_systems.append([DynamicalSystem([13*x^5 + 355*x^4*y + 2935*x^3*y^2 + 11405*x^2*y^3 + 64252*x*y^4 - 18480*y^5, 18480*y^5], domain=P), '1.edbe4aa0.f2385e77.1', P(0, 1)])
# FN1997; height ratio 0.021485
dynabase_systems.append([DynamicalSystem([x^5 + x^3*y^2, y^5], domain=P), '1.91738bc3.f35ae2c4.1', P(-1, 1)])
# dFH2018, FN1997; height ratio 0.061259
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1', P(-1, 1)])

print("Dynabase: 5 dynamical systems in dynabase_systems")
