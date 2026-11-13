# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;10) (2.2.40.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - 10)  # 2.2.40.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.92710271.448de5df.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 155/72*y^2, y^2], domain=P), '1.cfe3a31c.40f65747.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
