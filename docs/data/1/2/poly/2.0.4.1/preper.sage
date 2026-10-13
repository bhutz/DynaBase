# Dynabase (https://dynabase.org): Dimension 1, degree 2 polynomials over QQ(i) (2.0.4.1), Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + ((3/8*a - 1/4))*y^2, y^2], domain=P), '1.91587f96.0b5d852d.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.8f2b16a9.99353b99.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.e9464d8c.638cd9c2.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
