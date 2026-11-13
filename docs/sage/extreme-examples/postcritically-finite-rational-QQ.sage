# Dynabase (https://dynabase.org): Summary of Extreme Examples, postcritically finite maps (all of them, for each row), non-polynomial maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Lukas2014, CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.7caff06c.b29c4e61.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.a8c6b910.e0fda4e1.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.1e41a745.8bc476bb.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.49146aab.c4a4d949.1'])
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
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.2a6bd967.16210f77.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.e585768f.4eff1f14.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.dbdf4212.adc49165.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.834cba9d.77c499dc.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.fcc3f607.790bef87.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.fcc3f607.790bef87.2'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.fcc3f607.78dde912.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.7a816f28.3f0eaf7a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# Miasnikov2017, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.77659db6.3af5a8ff.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.43808372.c2bd952a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.9190add3.023ff0b9.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.4dbdab6d.d8496994.1'])

print("Dynabase: 22 dynamical systems in dynabase_systems")
