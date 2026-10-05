# Dynabase (https://dynabase.org): dimension 1, degree 13, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^13 - 143*x^12*y + 9178*x^11*y^2 - 349206*x^10*y^3 + 8761753*x^9*y^4 - 152522799*x^8*y^5 + 1886334164*x^7*y^6 - 16681595788*x^6*y^7 + 104670816536*x^5*y^8 - 455629039008*x^4*y^9 + 1320045298208*x^3*y^10 - 2370430947456*x^2*y^11 + 2315049903360*x*y^12 - 907588281600*y^13, -518918400*y^13], domain=P), '1.b40a6a5b.972ad06e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([860*x^13 + 61685*x^12*y + 1906138*x^11*y^2 + 33008833*x^10*y^3 + 347125350*x^9*y^4 + 2213680755*x^8*y^5 + 7633125214*x^7*y^6 + 5859546979*x^6*y^7 - 52599293890*x^5*y^8 - 171757668940*x^4*y^9 - 108558503352*x^3*y^10 + 204127005888*x^2*y^11 + 181197233280*x*y^12 + 6227020800*y^13, -6227020800*y^13], domain=P), '1.9333086c.415680ad.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([8354*x^13 + 48151*x^12*y - 1206332*x^11*y^2 - 6298093*x^10*y^3 + 66314652*x^9*y^4 + 304427913*x^8*y^5 - 1745126036*x^7*y^6 - 6746939239*x^6*y^7 + 22669801274*x^5*y^8 + 67817345236*x^4*y^9 - 132792152232*x^3*y^10 - 235725166368*x^2*y^11 + 242569797120*x*y^12, 43589145600*y^13], domain=P), '1.e8d5184a.0f99e138.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
