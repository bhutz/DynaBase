# Dynabase (https://dynabase.org): Dimension 1, degree 7 maps over fields of degree 6, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^6 - t^3 + 1)  # 6.0.19683.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^7 + ((-a^4))*y^7, y^7], domain=P), '1.6c4e5c28.c3612aca.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
