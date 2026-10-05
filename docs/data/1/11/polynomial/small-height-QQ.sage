# Dynabase (https://dynabase.org): dimension 1, degree 11, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 7.3446e-17
dynabase_systems.append([DynamicalSystem([141*x^11 + 9219*x^10*y + 251060*x^9*y^2 + 3656820*x^8*y^3 + 30154233*x^7*y^4 + 133154847*x^6*y^5 + 223258230*x^5*y^6 - 332540670*x^4*y^7 - 1468215824*x^3*y^8 - 1620494616*x^2*y^9 - 1639499040*x*y^10 - 518918400*y^11, 518918400*y^11], domain=P), '1.10b0df19.494435eb.1', P(0, 1)])
# Hutz2026; height ratio 7.8702e-17
dynabase_systems.append([DynamicalSystem([5937*x^11 + 432149*x^10*y + 13281680*x^9*y^2 + 223637970*x^8*y^3 + 2232505821*x^7*y^4 + 13246556757*x^6*y^5 + 43106192730*x^5*y^6 + 53723887780*x^4*y^7 - 57754095608*x^3*y^8 - 154372805856*x^2*y^9 + 55991255040*x*y^10 + 14529715200*y^11, 14529715200*y^11], domain=P), '1.c3674a51.db20218e.1', P(0, 1)])
# Hutz2026; height ratio 9.7411e-17
dynabase_systems.append([DynamicalSystem([2*x^11 - 7991*x^10*y - 399915*x^9*y^2 - 7981350*x^8*y^3 - 79345404*x^7*y^4 - 377896743*x^6*y^5 - 389297015*x^5*y^6 + 3506418500*x^4*y^7 + 11992668252*x^3*y^8 + 6219998784*x^2*y^9 - 14637136320*x*y^10 + 1556755200*y^11, -1556755200*y^11], domain=P), '1.104367ec.d6774a05.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
