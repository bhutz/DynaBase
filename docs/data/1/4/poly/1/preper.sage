# Dynabase (https://dynabase.org): Dimension 1, degree 4 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^3*y - 13*x^2*y^2 + 14*x*y^3 - 48*y^4, 24*y^4], domain=P), '1.d7abafe1.ada3eacd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^4 - 14*x^3*y - 63*x^2*y^2 + 314*x*y^3, -120*y^4], domain=P), '1.51fa5c1f.3135fa52.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^3*y - 31*x^2*y^2 + 98*x*y^3 + 60*y^4, -60*y^4], domain=P), '1.e5948466.fc4998fd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 14*x^3*y - 49*x^2*y^2 - 206*x*y^3 + 240*y^4, 120*y^4], domain=P), '1.fb163bc9.5fcbff70.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 30*x^3*y + 215*x^2*y^2 + 210*x*y^3 - 96*y^4, -120*y^4], domain=P), '1.b0ccbef7.1360fd95.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 - 122*x^3*y + 289*x^2*y^2 + 302*x*y^3 - 240*y^4, 120*y^4], domain=P), '1.f521ae59.cdcf15a3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 + 30*x^3*y - 95*x^2*y^2 - 150*x*y^3 + 84*y^4, 60*y^4], domain=P), '1.5b167a70.d13145b7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^4 + 6*x^3*y - 67*x^2*y^2 - 186*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.4c2ad5bb.1fa09beb.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.ef32d183.12ccf81e.1'])
# FN1997, GHJSX2021, Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.9e054174.3f0eaf7a.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.14995048.fcc23423.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.68938348.14eb3256.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.3c83e548.afd51a11.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.d5469f32.478a246b.1'])
# FN1997, dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.80c8620b.21534f8d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 1/2*x*y^3, y^4], domain=P), '1.de48a9ac.b16d29ae.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.5e8dcb6e.41954f0a.1'])

print("Dynabase: 17 dynamical systems in dynabase_systems")
