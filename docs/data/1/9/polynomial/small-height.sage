# Dynabase (https://dynabase.org): dimension 1, degree 9, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 1.7173e-14
dynabase_systems.append([DynamicalSystem([2393*x^9 + 120789*x^8*y + 2368272*x^7*y^2 + 22132656*x^6*y^3 + 91367367*x^5*y^4 + 43987671*x^4*y^5 - 669797792*x^3*y^6 - 974348316*x^2*y^7 + 1094978160*x*y^8 - 129729600*y^9, 129729600*y^9], domain=P), '1.777af730.f2167d91.1', P(0, 1)])
# Hutz2026; height ratio 5.5356e-14
dynabase_systems.append([DynamicalSystem([1822*x^9 + 83421*x^8*y + 1418448*x^7*y^2 + 10411674*x^6*y^3 + 23261238*x^5*y^4 - 58134531*x^4*y^5 - 94356628*x^3*y^6 + 696287436*x^2*y^7 + 199404720*x*y^8 + 259459200*y^9, -259459200*y^9], domain=P), '1.5b63efb4.618cfb4f.1', P(0, 1)])
# Hutz2026; height ratio 7.5618e-14
dynabase_systems.append([DynamicalSystem([1153*x^9 + 66303*x^8*y + 1518918*x^7*y^2 + 17259102*x^6*y^3 + 95397897*x^5*y^4 + 171771327*x^4*y^5 - 387903808*x^3*y^6 - 1123149852*x^2*y^7 + 187202160*x*y^8 - 103783680*y^9, 103783680*y^9], domain=P), '1.5ca93c2d.c003711d.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
