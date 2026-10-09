# Dynabase (https://dynabase.org): dimension 1, degree 2, rational maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 0.00046574
dynabase_systems.append([DynamicalSystem([592*x^2 - 3424*x*y + 1024*y^2, 173*x^2 - 536*x*y - 1024*y^2], domain=P), '1.3b026e07.265dfbb0.1', P(0, 1)])
# Hutz2026; height ratio 0.001183
dynabase_systems.append([DynamicalSystem([285*x^2 + 2085*x*y + 990*y^2, -79*x^2 - 351*x*y + 990*y^2], domain=P), '1.0a9b4372.2927b5eb.1', P(0, 1)])
# Lukas2014; height ratio 0.25075
dynabase_systems.append([DynamicalSystem([4*y^2, -9*x^2 + 12*x*y], domain=P), '1.c346226f.0c3c179e.1', P(2, 1)])
# Lukas2014; height ratio 0.34634
dynabase_systems.append([DynamicalSystem([2*x*y, -2*x^2 + 4*x*y - y^2], domain=P), '1.095ed92d.7e1406dd.1', P(1, 1)])
# Milnor1993; height ratio 0.39403
dynabase_systems.append([DynamicalSystem([x^2 + y^2, x*y], domain=P), '1.d3259bab.d36dd573.1', P(-1, 1)])
# Lukas2014; height ratio 0.51349
dynabase_systems.append([DynamicalSystem([y^2, -4*x^2 + 4*x*y], domain=P), '1.fbfd6fd4.9888ce4b.1', P(-1, 2)])

print("Dynabase: 6 dynamical systems in dynabase_systems")
