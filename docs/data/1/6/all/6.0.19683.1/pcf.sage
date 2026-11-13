# Dynabase (https://dynabase.org): Dimension 1, degree 6 maps over 6.0.19683.1, Postcritically Finite
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
dynabase_systems.append([DynamicalSystem([x^6 + ((a^3 - 1))*y^6, y^6], domain=P), '1.d643395e.6ec94ba8.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
