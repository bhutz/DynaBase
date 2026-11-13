# Dynabase (https://dynabase.org): Dimension 1, degree 7 polynomials over fields of degree 4, Postcritically Finite
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
dynabase_systems.append([DynamicalSystem([x^7 + ((a^3 - a))*y^7, y^7], domain=P), '1.3899370b.7a1d8320.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
