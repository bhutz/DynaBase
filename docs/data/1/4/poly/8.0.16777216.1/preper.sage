# Dynabase (https://dynabase.org): Dimension 1, degree 4 polynomials over 8.0.16777216.1, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^8 + 1)  # 8.0.16777216.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^4 + ((-a^4 - 1))*y^4, y^4], domain=P), '1.cb2f009d.2c88a168.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
