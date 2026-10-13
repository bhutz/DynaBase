# Dynabase (https://dynabase.org): Dimension 1, degree 2 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.de450653.9e174cad.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.05f9cf28.88243c92.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# Poonen1998, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.13a1af67.7eb43a7f.1'])
# Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 7/4*y^2, y^2], domain=P), '1.751d2996.7bc729ec.1'])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.8f2b16a9.99353b99.1'])
# Morton1992, Poonen1998, Doyle2014, Doyle2018, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.1a2a6bbf.1ed2bf82.1'])

print("Dynabase: 12 dynamical systems in dynabase_systems")
