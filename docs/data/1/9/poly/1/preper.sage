# Dynabase (https://dynabase.org): Dimension 1, degree 9 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([16*x^9 - 696*x^7*y^2 + 9849*x^5*y^4 - 49219*x^3*y^6 + 57060*x*y^8 - 5670*y^9, 11340*y^9], domain=P), '1.cd5461f2.e933e62b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([272*x^9 + 384*x^8*y - 4536*x^7*y^2 - 4704*x^6*y^3 + 26481*x^5*y^4 + 17976*x^4*y^5 - 60269*x^3*y^6 - 19326*x^2*y^7 + 36162*x*y^8 - 3780*y^9, -7560*y^9], domain=P), '1.0f6ec33a.fefd096b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([16*x^9 - 160*x^8*y + 520*x^7*y^2 - 224*x^6*y^3 - 1799*x^5*y^4 + 2170*x^4*y^5 - 135*x^3*y^6 + 1994*x^2*y^7 + 3918*x*y^8 - 7560*y^9, -2520*y^9], domain=P), '1.bde3b2b5.fd8f0170.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([19*x^9 - 326*x^8*y + 1027*x^7*y^2 + 8440*x^6*y^3 - 43145*x^5*y^4 - 57044*x^4*y^5 + 370923*x^3*y^6 + 215250*x^2*y^7 - 162504*x*y^8 - 332640*y^9, 332640*y^9], domain=P), '1.295e4546.0fec5b9e.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9, y^9], domain=P), '1.790bef87.083b88f1.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.f4ddead6.588b0522.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2393*x^9 + 34641*x^8*y - 118608*x^7*y^2 - 2930256*x^6*y^3 + 203847*x^5*y^4 + 79332939*x^4*y^5 + 31916368*x^3*y^6 - 685395324*x^2*y^7 - 71694000*x*y^8 + 129729600*y^9, 129729600*y^9], domain=P), '1.a845382f.865ec852.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
