# Dynabase (https://dynabase.org): dimension 1, degree 8, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 8.771e-13
dynabase_systems.append([DynamicalSystem([55*x^8 + 1846*x^7*y + 18550*x^6*y^2 + 15988*x^5*y^3 - 502775*x^4*y^4 - 21686*x^3*y^5 + 9132810*x^2*y^6 - 12969108*x*y^7 - 2162160*y^8, -2162160*y^8], domain=P), '1.4e7307c9.5ac37621.1', P(0, 1)])
# Hutz2026; height ratio 1.1829e-12
dynabase_systems.append([DynamicalSystem([137*x^8 + 4224*x^7*y + 42434*x^6*y^2 + 107184*x^5*y^3 - 547687*x^4*y^4 - 2176944*x^3*y^5 + 1835676*x^2*y^6 + 4726656*x*y^7 - 1330560*y^8, -1330560*y^8], domain=P), '1.6fc2e0ba.762d9ad9.1', P(0, 1)])
# Hutz2026; height ratio 1.3585e-12
dynabase_systems.append([DynamicalSystem([387*x^8 + 12100*x^7*y + 113806*x^6*y^2 + 49504*x^5*y^3 - 4180757*x^4*y^4 - 13474580*x^3*y^5 + 30012484*x^2*y^6 + 108548016*x*y^7 + 17297280*y^8, -17297280*y^8], domain=P), '1.79b47ccf.8642e5ff.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
