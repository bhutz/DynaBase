# Dynabase (https://dynabase.org): dimension 1, degree 2, polynomial maps, Postcritically Finite, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])

print("Dynabase: 3 dynamical systems in dynabase_systems")
