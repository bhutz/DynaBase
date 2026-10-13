# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;17) (2.2.17.1), Rational Preperiodic
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
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])
# Doyle2014, Doyle2018, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 13/16*y^2, y^2], domain=P), '1.24c682c5.dd0783cf.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 13/16))*y^2, y^2], domain=P), '1.67b1e39b.485999fa.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 273/64*y^2, y^2], domain=P), '1.1ae932e0.c99dfb89.1'])

print("Dynabase: 5 dynamical systems in dynabase_systems")
