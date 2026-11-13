# Dynabase (https://dynabase.org): Dimension 1, degree 11 maps over 4.0.144.1, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^4 - t^2 + 1)  # 4.0.144.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^11 + ((-a^3))*y^11, y^11], domain=P), '1.07c76fd8.d755f8bf.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
