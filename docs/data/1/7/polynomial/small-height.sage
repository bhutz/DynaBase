# Dynabase (https://dynabase.org): dimension 1, degree 7, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 1.0564e-10
dynabase_systems.append([DynamicalSystem([215*x^7 - 7601*x^6*y + 100973*x^5*y^2 - 610445*x^4*y^3 + 1535960*x^3*y^4 - 546194*x^2*y^5 - 2468748*x*y^6 + 166320*y^7, -166320*y^7], domain=P), '1.f4bd3027.b70022ba.1', P(0, 1)])
# Hutz2026; height ratio 1.4693e-10
dynabase_systems.append([DynamicalSystem([71*x^7 - 11383*x^6*y + 390449*x^5*y^2 - 5367805*x^4*y^3 + 31958744*x^3*y^4 - 68134252*x^2*y^5 + 6569616*x*y^6 - 8648640*y^7, -8648640*y^7], domain=P), '1.c1314b2f.331e2e8e.1', P(0, 1)])
# Hutz2026; height ratio 1.5717e-10
dynabase_systems.append([DynamicalSystem([203*x^7 - 10751*x^6*y + 217193*x^5*y^2 - 2060945*x^4*y^3 + 8904932*x^3*y^4 - 12342704*x^2*y^5 - 7680888*x*y^6 - 1441440*y^7, -1441440*y^7], domain=P), '1.52b0cbfc.77fe76fb.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
