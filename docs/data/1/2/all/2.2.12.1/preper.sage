# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;3) (2.2.12.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - 3)  # 2.2.12.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
