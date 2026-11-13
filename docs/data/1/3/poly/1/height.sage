# Dynabase (https://dynabase.org): Dimension 1, degree 3 polynomials over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Benedetto2009, Hutz2026; height ratio 9.2099e-05
dynabase_systems.append([DynamicalSystem([2*x^3 + 21*x^2*y + 25*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.979dd007.9848a21a.1', P(0, 1)])
# Hutz2026; height ratio 0.00016547
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y - 37*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.a8ef183d.99db83a1.1', P(0, 1)])
# Hutz2026; height ratio 0.00016738
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2 - 6*y^3, -6*y^3], domain=P), '1.cc1bb839.97c4f4cc.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
