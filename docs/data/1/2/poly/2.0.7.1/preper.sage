# Dynabase (https://dynabase.org): Dimension 1, degree 2 polynomials over QQ(&radic;&minus;7) (2.0.7.1), Rational Preperiodic
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
dynabase_systems.append([DynamicalSystem([x^2 - 5/16*y^2, y^2], domain=P), '1.c73eeb94.b6a37976.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.96cf3896.0738b144.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + 3/16*y^2, y^2], domain=P), '1.47e02d0b.8c09d28d.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 5/16))*y^2, y^2], domain=P), '1.52e196ee.8bc0c716.1'])
# Doyle2014, Doyle2018, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 13/16*y^2, y^2], domain=P), '1.c54b8f3f.756bd15c.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])

print("Dynabase: 7 dynamical systems in dynabase_systems")
