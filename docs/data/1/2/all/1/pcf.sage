# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.dbdf4212.adc49165.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.834cba9d.77c499dc.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.1e41a745.8bc476bb.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.49146aab.c4a4d949.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.2a6bd967.16210f77.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.a8c6b910.e0fda4e1.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.e585768f.4eff1f14.1'])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])
# Lukas2014, CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.7caff06c.b29c4e61.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*y^2, x^2], domain=P), '1.db03b80b.9e054174.1'])
# Lukas2014, CV2017, dFH2018, BS2026
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.db03b80b.9e054174.2'])
# BS2026
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y, -2*x*y - y^2], domain=P), '1.db03b80b.9e054174.3'])
# BS2026
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -2*x*y], domain=P), '1.db03b80b.9e054174.4'])
# BS2026
dynabase_systems.append([DynamicalSystem([2*x*y + y^2, x^2 - y^2], domain=P), '1.db03b80b.9e054174.5'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
