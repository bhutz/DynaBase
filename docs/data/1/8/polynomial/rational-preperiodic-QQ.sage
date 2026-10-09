# Dynabase (https://dynabase.org): dimension 1, degree 8, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^8 + 20*x^7*y + 70*x^6*y^2 - 700*x^5*y^3 - 3731*x^4*y^4 + 6440*x^3*y^5 + 33900*x^2*y^6 - 36000*x*y^7 - 20160*y^8, 20160*y^8], domain=P), '1.ca09c537.11e402ba.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^8 + 36*x^7*y + 490*x^6*y^2 + 3024*x^5*y^3 + 5929*x^4*y^4 - 25956*x^3*y^5 - 127380*x^2*y^6 + 22896*x*y^7 + 80640*y^8, 40320*y^8], domain=P), '1.b9d2c449.eadf5ac7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^8 + 21*x^7*y - 161*x^6*y^2 - 651*x^5*y^3 + 2611*x^4*y^4 + 5754*x^3*y^5 - 17574*x^2*y^6 - 10164*x*y^7 + 20160*y^8, 5040*y^8], domain=P), '1.1b32f8a3.b7900ec8.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^8 + 48*x^7*y + 14*x^6*y^2 - 756*x^5*y^3 - 1855*x^4*y^4 - 3948*x^3*y^5 + 11916*x^2*y^6 + 55056*x*y^7 - 20160*y^8, -20160*y^8], domain=P), '1.1ae30b50.177faf2c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^8 + 28*x^7*y + 14*x^6*y^2 - 1232*x^5*y^3 - 3493*x^4*y^4 + 12292*x^3*y^5 + 23636*x^2*y^6 + 9072*x*y^7 + 80640*y^8, 40320*y^8], domain=P), '1.639cb7d1.7aa51b98.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([31*x^8 - 580*x^7*y + 2182*x^6*y^2 + 12848*x^5*y^3 - 72521*x^4*y^4 - 73180*x^3*y^5 + 493668*x^2*y^6 + 242352*x*y^7 - 241920*y^8, 120960*y^8], domain=P), '1.1b1f8eec.8988c609.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^8 - 140*x^7*y + 434*x^6*y^2 + 2296*x^5*y^3 - 10759*x^4*y^4 - 11900*x^3*y^5 + 50636*x^2*y^6 + 90384*x*y^7 - 80640*y^8, -40320*y^8], domain=P), '1.30a427de.0d23e4e3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([413*x^8 + 13232*x^7*y + 152754*x^6*y^2 + 742392*x^5*y^3 + 1278837*x^4*y^4 + 334488*x^3*y^5 - 988484*x^2*y^6 - 13065152*x*y^7 + 15523200*y^8, -3991680*y^8], domain=P), '1.a6bf8bf0.026133d3.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^8, y^8], domain=P), '1.a2cb972c.bc5e6238.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^8 + x*y^7, y^8], domain=P), '1.27e72460.98bcfef1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([55*x^8 - 2114*x^7*y + 26992*x^6*y^2 - 90986*x^5*y^3 - 524825*x^4*y^4 + 2604784*x^3*y^5 + 3741018*x^2*y^6 - 1430604*x*y^7 + 4324320*y^8, -2162160*y^8], domain=P), '1.4e7307c9.5ac37621.1'])

print("Dynabase: 11 dynamical systems in dynabase_systems")
