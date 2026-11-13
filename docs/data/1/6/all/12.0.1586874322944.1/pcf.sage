# Dynabase (https://dynabase.org): Dimension 1, degree 6 maps over 12.0.1586874322944.1, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^12 - t^6 + 1)  # 12.0.1586874322944.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^6 + ((a^6 - 1))*y^6, y^6], domain=P), '1.275bdd4f.35ca43c0.1'])
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^6 - y^6, y^6], domain=P), '1.ba915b5b.12b6001c.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
