# Dynabase (https://dynabase.org): Dimension 1, degree 2 polynomials over QQ(&radic;&minus;455) (2.0.455.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t + 114)  # 2.0.455.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + 199/720*y^2, y^2], domain=P), '1.2d03ec80.3b33feef.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
