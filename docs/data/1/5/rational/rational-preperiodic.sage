# Dynabase (https://dynabase.org): dimension 1, degree 5, rational maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.56d48bcf.b239edf6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([88758966490337*x^5 + 2981527184876307*x^4*y + 11066877636602289*x^3*y^2 - 75987409403569835*x^2*y^3 - 1288812439794810*x*y^4 + 17419787236064304*y^5, 1157006057963*x^5 - 50301712572351*x^4*y - 1971337131131061*x^3*y^2 + 814941375750391*x^2*y^3 + 29505024045162162*x*y^4 + 17419787236064304*y^5], domain=P), '1.92f49ee7.789f9313.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
