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
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.96cf3896.0738b144.1'])
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.420f870e.c9b64d6b.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.92710271.448de5df.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])
# Poonen1998, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.49ef408f.a255b42e.1'])
# Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 7/4*y^2, y^2], domain=P), '1.01981c7d.8230c5b3.1'])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])
# Morton1992, Poonen1998, Doyle2014, Doyle2018, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.991c99ac.68df8ef0.1'])

print("Dynabase: 12 dynamical systems in dynabase_systems")
