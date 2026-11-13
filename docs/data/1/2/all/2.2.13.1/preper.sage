# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;13) (2.2.13.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.420f870e.c9b64d6b.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 289/144*y^2, y^2], domain=P), '1.be487703.7a8d3331.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 40/9*y^2, y^2], domain=P), '1.5ee5410e.67a5d387.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 37/9*y^2, y^2], domain=P), '1.b5662713.812bd674.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
