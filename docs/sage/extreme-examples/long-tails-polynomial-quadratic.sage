# Dynabase (https://dynabase.org): Summary of Extreme Examples, long rational tails, polynomial maps over quadratic fields
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 13/16))*y^2, y^2], domain=P), '1.67b1e39b.485999fa.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
