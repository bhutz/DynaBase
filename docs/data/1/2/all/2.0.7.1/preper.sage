# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ(&radic;&minus;7) (2.0.7.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t + 2)  # 2.0.7.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 5/16*y^2, y^2], domain=P), '1.1796db64.60e7b117.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + 3/16*y^2, y^2], domain=P), '1.7c61fa3f.6fc59844.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 5/16))*y^2, y^2], domain=P), '1.82a2d649.2aa4c45a.1'])
# Doyle2014, Doyle2018, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 13/16*y^2, y^2], domain=P), '1.24c682c5.dd0783cf.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.8f2b16a9.99353b99.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
