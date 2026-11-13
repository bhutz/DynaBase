# Dynabase (https://dynabase.org): Dimension 1, degree 8 maps over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([x^8 + 20*x^7*y + 70*x^6*y^2 - 700*x^5*y^3 - 3731*x^4*y^4 + 6440*x^3*y^5 + 33900*x^2*y^6 - 36000*x*y^7 - 20160*y^8, 20160*y^8], domain=P), '1.844efd6c.ba0bf677.1'])
# DoHy2025
dynabase_systems.append([DynamicalSystem([x^8 + 36*x^7*y + 490*x^6*y^2 + 3024*x^5*y^3 + 5929*x^4*y^4 - 25956*x^3*y^5 - 127380*x^2*y^6 + 22896*x*y^7 + 80640*y^8, 40320*y^8], domain=P), '1.8515efe3.633ae152.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^8 + 21*x^7*y - 161*x^6*y^2 - 651*x^5*y^3 + 2611*x^4*y^4 + 5754*x^3*y^5 - 17574*x^2*y^6 - 10164*x*y^7 + 20160*y^8, 5040*y^8], domain=P), '1.4e61e3fb.dbd77aff.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^8 + 48*x^7*y + 14*x^6*y^2 - 756*x^5*y^3 - 1855*x^4*y^4 - 3948*x^3*y^5 + 11916*x^2*y^6 + 55056*x*y^7 - 20160*y^8, -20160*y^8], domain=P), '1.7a17a714.e191fb3b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^8 + 28*x^7*y + 14*x^6*y^2 - 1232*x^5*y^3 - 3493*x^4*y^4 + 12292*x^3*y^5 + 23636*x^2*y^6 + 9072*x*y^7 + 80640*y^8, 40320*y^8], domain=P), '1.e364f5ca.b7f6f1ca.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([31*x^8 - 580*x^7*y + 2182*x^6*y^2 + 12848*x^5*y^3 - 72521*x^4*y^4 - 73180*x^3*y^5 + 493668*x^2*y^6 + 242352*x*y^7 - 241920*y^8, 120960*y^8], domain=P), '1.8a10e3e4.fb6d9f96.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^8 - 140*x^7*y + 434*x^6*y^2 + 2296*x^5*y^3 - 10759*x^4*y^4 - 11900*x^3*y^5 + 50636*x^2*y^6 + 90384*x*y^7 - 80640*y^8, -40320*y^8], domain=P), '1.aca4a50d.203d96c4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([413*x^8 + 13232*x^7*y + 152754*x^6*y^2 + 742392*x^5*y^3 + 1278837*x^4*y^4 + 334488*x^3*y^5 - 988484*x^2*y^6 - 13065152*x*y^7 + 15523200*y^8, -3991680*y^8], domain=P), '1.ed5b8d5a.a4654013.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^8, y^8], domain=P), '1.00faa61e.83bed86d.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^8 + x*y^7, y^8], domain=P), '1.7f8ca563.27c82941.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([55*x^8 - 2114*x^7*y + 26992*x^6*y^2 - 90986*x^5*y^3 - 524825*x^4*y^4 + 2604784*x^3*y^5 + 3741018*x^2*y^6 - 1430604*x*y^7 + 4324320*y^8, -2162160*y^8], domain=P), '1.2e3cf036.c24221e7.1'])

print("Dynabase: 11 dynamical systems in dynabase_systems")
