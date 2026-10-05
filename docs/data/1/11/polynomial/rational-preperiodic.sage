# Dynabase (https://dynabase.org): dimension 1, degree 11, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^11 - 205*x^9*y^2 + 14883*x^7*y^4 - 451795*x^5*y^6 + 4987516*x^3*y^8 - 8179200*x*y^10 + 3628800*y^11, -3628800*y^11], domain=P), '1.51b560b0.e0f41b07.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([257*x^11 + 9331*x^10*y + 120130*x^9*y^2 + 579300*x^8*y^3 - 229479*x^7*y^4 - 11442417*x^6*y^5 - 52169780*x^5*y^6 - 128719150*x^4*y^7 + 428342072*x^3*y^8 + 2215246536*x^2*y^9 - 1413900000*x*y^10 - 1037836800*y^11, -518918400*y^11], domain=P), '1.0cca5889.247cf2ab.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2076*x^11 + 66177*x^10*y + 718525*x^9*y^2 + 2134860*x^8*y^3 - 13169922*x^7*y^4 - 90177339*x^6*y^5 - 36287115*x^5*y^6 + 681611190*x^4*y^7 + 1044667796*x^3*y^8 - 853094088*x^2*y^9 - 2812145760*x*y^10 + 2075673600*y^11, -518918400*y^11], domain=P), '1.b6b8895a.3e7242d7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([141*x^11 + 7668*x^10*y + 166625*x^9*y^2 + 1788870*x^8*y^3 + 8878083*x^7*y^4 + 5247984*x^6*y^5 - 117838365*x^5*y^6 - 280673970*x^4*y^7 + 302054476*x^3*y^8 + 14170248*x^2*y^9 - 971638560*x*y^10 + 1037836800*y^11, 518918400*y^11], domain=P), '1.10b0df19.494435eb.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
