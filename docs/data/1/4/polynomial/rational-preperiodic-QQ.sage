# Dynabase (https://dynabase.org): dimension 1, degree 4, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^3*y - 13*x^2*y^2 + 14*x*y^3 - 48*y^4, 24*y^4], domain=P), '1.9f08598a.0f7c5a09.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^4 - 14*x^3*y - 63*x^2*y^2 + 314*x*y^3, -120*y^4], domain=P), '1.a0dac219.26bee824.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^3*y - 31*x^2*y^2 + 98*x*y^3 + 60*y^4, -60*y^4], domain=P), '1.d831da0b.27b10d8c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 14*x^3*y - 49*x^2*y^2 - 206*x*y^3 + 240*y^4, 120*y^4], domain=P), '1.3e4a84b2.906ea779.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 30*x^3*y + 215*x^2*y^2 + 210*x*y^3 - 96*y^4, -120*y^4], domain=P), '1.e916c3cb.0dde0877.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 - 122*x^3*y + 289*x^2*y^2 + 302*x*y^3 - 240*y^4, 120*y^4], domain=P), '1.5de8db86.70c58f11.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 + 30*x^3*y - 95*x^2*y^2 - 150*x*y^3 + 84*y^4, 60*y^4], domain=P), '1.431f1b4f.6f6ebffb.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^4 + 6*x^3*y - 67*x^2*y^2 - 186*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.3387dead.7b560bfc.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.880302df.903704ba.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.024ac6d7.76c4de71.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.770c2622.7cef54b3.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.5457b5e3.e9909514.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.e029f05a.0d52105e.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.8e57877c.24b4743f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.a2324809.3fbf9eac.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.f2147436.53db7cc0.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
