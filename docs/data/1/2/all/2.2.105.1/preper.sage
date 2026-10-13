# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;105) (2.2.105.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t - 26)  # 2.2.105.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 95/48*y^2, y^2], domain=P), '1.059fb1f3.24824224.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
