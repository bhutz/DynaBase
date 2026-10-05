# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Small Height Ratio
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
dynabase_systems.append([DynamicalSystem([1115*x^3 - 2405*x^2*y - 37855*x*y^2 + 3465*y^3, 201*x^3 + 173*x^2*y + 1907*x*y^2 - 3465*y^3], domain=P), '1.1825f5a3.a46ef689.1', P(0, 1)])
# Hutz2026; height ratio 3.2586e-06
dynabase_systems.append([DynamicalSystem([183*x^3 - 3203*x^2*y + 15445*x*y^2 + 5775*y^3, 57*x^3 - 1117*x^2*y + 6107*x*y^2 - 5775*y^3], domain=P), '1.0aba1c76.ac22b7ff.1', P(0, 1)])
# Hutz2026; height ratio 3.2984e-06
dynabase_systems.append([DynamicalSystem([21*x^3 + 312*x^2*y + 579*x*y^2 - 72*y^3, 26*x^3 + 47*x^2*y - 141*x*y^2 - 72*y^3], domain=P), '1.50b47f1a.f7f950f2.1', P(0, 1)])
# GHJSX2021; height ratio 0.10815
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1', P(1, 1)])
# dFH2018; height ratio 0.14804
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1', P(-1, 2)])

print("Dynabase: 5 dynamical systems in dynabase_systems")
