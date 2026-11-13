# Dynabase (https://dynabase.org): Dimension 1, degree 3 maps over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 3.079e-06
dynabase_systems.append([DynamicalSystem([1115*x^3 - 2405*x^2*y - 37855*x*y^2 + 3465*y^3, 201*x^3 + 173*x^2*y + 1907*x*y^2 - 3465*y^3], domain=P), '1.3dfdcd07.d1dc886d.1', P(0, 1)])
# Hutz2026; height ratio 3.2586e-06
dynabase_systems.append([DynamicalSystem([183*x^3 - 3203*x^2*y + 15445*x*y^2 + 5775*y^3, 57*x^3 - 1117*x^2*y + 6107*x*y^2 - 5775*y^3], domain=P), '1.afae8093.c213272b.1', P(0, 1)])
# Hutz2026; height ratio 3.2984e-06
dynabase_systems.append([DynamicalSystem([21*x^3 + 312*x^2*y + 579*x*y^2 - 72*y^3, 26*x^3 + 47*x^2*y - 141*x*y^2 - 72*y^3], domain=P), '1.3918d746.4c48c8df.1', P(0, 1)])
# Benedetto2009, Hutz2026; height ratio 9.2099e-05
dynabase_systems.append([DynamicalSystem([2*x^3 + 21*x^2*y + 25*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.979dd007.9848a21a.1', P(0, 1)])
# Hutz2026; height ratio 0.00016547
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y - 37*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.a8ef183d.99db83a1.1', P(0, 1)])
# Hutz2026; height ratio 0.00016738
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2 - 6*y^3, -6*y^3], domain=P), '1.cc1bb839.97c4f4cc.1', P(0, 1)])

print("Dynabase: 6 dynamical systems in dynabase_systems")
