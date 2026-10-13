# Dynabase (https://dynabase.org): Summary of Extreme Examples, many rational preperiodic points, polynomial maps over quadratic fields
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^4 + y^4, y^4], domain=P), '1.72e71605.c7592b35.1'])
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^6 + ((a - 1))*y^6, y^6], domain=P), '1.98d006bc.2368dbfa.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
