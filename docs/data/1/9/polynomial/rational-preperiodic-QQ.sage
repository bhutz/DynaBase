# Dynabase (https://dynabase.org): dimension 1, degree 9, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([16*x^9 - 696*x^7*y^2 + 9849*x^5*y^4 - 49219*x^3*y^6 + 57060*x*y^8 - 5670*y^9, 11340*y^9], domain=P), '1.154dea1c.6bbc505d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([272*x^9 + 384*x^8*y - 4536*x^7*y^2 - 4704*x^6*y^3 + 26481*x^5*y^4 + 17976*x^4*y^5 - 60269*x^3*y^6 - 19326*x^2*y^7 + 36162*x*y^8 - 3780*y^9, -7560*y^9], domain=P), '1.10f82472.ce6ee4fc.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([19*x^9 - 326*x^8*y + 1027*x^7*y^2 + 8440*x^6*y^3 - 43145*x^5*y^4 - 57044*x^4*y^5 + 370923*x^3*y^6 + 215250*x^2*y^7 - 162504*x*y^8 - 332640*y^9, 332640*y^9], domain=P), '1.271df9ee.1e432275.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([1520*x^9 + 6768*x^8*y - 7080*x^7*y^2 - 55944*x^6*y^3 - 4305*x^5*y^4 + 144207*x^4*y^5 + 35335*x^3*y^6 - 100701*x^2*y^7 + 2880*x*y^8 - 11340*y^9, -22680*y^9], domain=P), '1.dc0f2e54.6c011cd6.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.7b05c466.f7c38225.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2393*x^9 + 34641*x^8*y - 118608*x^7*y^2 - 2930256*x^6*y^3 + 203847*x^5*y^4 + 79332939*x^4*y^5 + 31916368*x^3*y^6 - 685395324*x^2*y^7 - 71694000*x*y^8 + 129729600*y^9, 129729600*y^9], domain=P), '1.777af730.f2167d91.1'])

print("Dynabase: 6 dynamical systems in dynabase_systems")
