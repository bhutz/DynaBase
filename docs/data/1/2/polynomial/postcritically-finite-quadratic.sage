# Dynabase (https://dynabase.org): dimension 1, degree 2, polynomial maps, Postcritically Finite, over quadratic fields
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.e9464d8c.638cd9c2.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
