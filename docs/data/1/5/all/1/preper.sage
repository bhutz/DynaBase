# Dynabase (https://dynabase.org): Dimension 1, degree 5 maps over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([4*x^5 - 20*x^4*y - 5*x^3*y^2 + 95*x^2*y^3 - 14*x*y^4 - 60*y^5, 30*y^5], domain=P), '1.466dad47.cfc4fee7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 45*x^3*y^2 - 199*x*y^4, -210*y^5], domain=P), '1.c017f30b.6d97eb98.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 145*x^3*y^2 + 210*x^2*y^3 + 351*x*y^4 + 525*y^5, 210*y^5], domain=P), '1.a0f79484.ff44cdce.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^5 - 5*x^4*y - 140*x^3*y^2 + 320*x^2*y^3 + 2343*x*y^4 - 2520*y^5, -630*y^5], domain=P), '1.c6e08a19.1a263097.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^5 - 35*x^4*y + 180*x^3*y^2 - 205*x^2*y^3 - 302*x*y^4 - 240*y^5, -120*y^5], domain=P), '1.0db7347f.ddc75c3d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 45*x^3*y^2 + 30*x^2*y^3 + 56*x*y^4 - 30*y^5, 30*y^5], domain=P), '1.355f53b8.0610b4b8.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([94*x^5 - 1645*x^4*y + 8720*x^3*y^2 - 10955*x^2*y^3 - 13854*x*y^4 - 2520*y^5, -2520*y^5], domain=P), '1.cfef851e.1c4977c2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([172*x^5 - 280*x^4*y - 1175*x^3*y^2 + 1330*x^2*y^3 + 1843*x*y^4 - 1050*y^5, -420*y^5], domain=P), '1.3a84d6a0.f85236d4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([52*x^5 + 60*x^4*y - 305*x^3*y^2 - 45*x^2*y^3 - 242*x*y^4 - 465*y^5, -630*y^5], domain=P), '1.2d1a57db.e9267eb0.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^5 - 10*x^4*y - 5*x^3*y^2 + 100*x^2*y^3 + 34*x*y^4 - 120*y^5, -60*y^5], domain=P), '1.da3a68b3.1eb03349.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([181*x^5 - 3340*x^4*y + 19775*x^3*y^2 - 34460*x^2*y^3 - 22476*x*y^4 + 5040*y^5, -5040*y^5], domain=P), '1.de8ccffd.176f0d2e.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# Miasnikov2017, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.77659db6.3af5a8ff.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.141f1a9c.37bd3a33.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 25*x^3*y^2 + 26*x*y^4 + 5*y^5, -10*y^5], domain=P), '1.5356d96a.14ceb2b2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([88758966490337*x^5 + 2981527184876307*x^4*y + 11066877636602289*x^3*y^2 - 75987409403569835*x^2*y^3 - 1288812439794810*x*y^4 + 17419787236064304*y^5, 1157006057963*x^5 - 50301712572351*x^4*y - 1971337131131061*x^3*y^2 + 814941375750391*x^2*y^3 + 29505024045162162*x*y^4 + 17419787236064304*y^5], domain=P), '1.d23b671e.54ace8cd.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
