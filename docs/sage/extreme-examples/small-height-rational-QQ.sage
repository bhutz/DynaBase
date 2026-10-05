# Dynabase (https://dynabase.org): Summary of Extreme Examples, small canonical heights, rational maps over QQ
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
# Hutz2026; height ratio 3.079e-06
dynabase_systems.append([DynamicalSystem([1115*x^3 - 2405*x^2*y - 37855*x*y^2 + 3465*y^3, 201*x^3 + 173*x^2*y + 1907*x*y^2 - 3465*y^3], domain=P), '1.1825f5a3.a46ef689.1', P(0, 1)])
# Hutz2026; height ratio 2.1843e-08
dynabase_systems.append([DynamicalSystem([49*x^4 + 844*x^3*y + 4499*x^2*y^2 + 7364*x*y^3 - 660*y^4, -10*x^4 - 174*x^3*y - 866*x^2*y^2 - 1122*x*y^3 + 660*y^4], domain=P), '1.0efc460c.908765ce.1', P(0, 1)])
# Hutz2026; height ratio 3.6941e-10
dynabase_systems.append([DynamicalSystem([88758966490337*x^5 + 2981527184876307*x^4*y + 11066877636602289*x^3*y^2 - 75987409403569835*x^2*y^3 - 1288812439794810*x*y^4 + 17419787236064304*y^5, 1157006057963*x^5 - 50301712572351*x^4*y - 1971337131131061*x^3*y^2 + 814941375750391*x^2*y^3 + 29505024045162162*x*y^4 + 17419787236064304*y^5], domain=P), '1.92f49ee7.789f9313.1', P(0, 1)])
# dFH2018; height ratio 0.010205
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1', P(-1, 1)])

print("Dynabase: 5 dynamical systems in dynabase_systems")
