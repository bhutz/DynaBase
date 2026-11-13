# Dynabase (https://dynabase.org): Summary of Extreme Examples, automorphism groups (smallest degree for each group)
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.343beeba.c008598d.1'])
# FN1997, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.34726b93.790bef87.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x*y^3, -4*x^4 - 4*y^4], domain=P), '1.4c81fec1.ffd15634.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.99d40459.e75b5525.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.48690a94.9c571960.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*y^2, x^2], domain=P), '1.db03b80b.9e054174.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^8 + x*y^7, y^8], domain=P), '1.7f8ca563.27c82941.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.f4ddead6.588b0522.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.fcc3f607.790bef87.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10 + x*y^9, y^10], domain=P), '1.32c02398.5289177c.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.7a816f28.3f0eaf7a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.fcc3f607.78dde912.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.43808372.c2bd952a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.9190add3.023ff0b9.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10, y^10], domain=P), '1.500c00a0.a04b9cb7.1'])
# Miasnikov2017, dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.77659db6.3af5a8ff.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.4dbdab6d.d8496994.1'])

print("Dynabase: 19 dynamical systems in dynabase_systems")
