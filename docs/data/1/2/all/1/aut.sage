# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ, Automorphism Groups
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Lukas2014, CV2017, dFH2018, BS2026
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])

print("Dynabase: 2 dynamical systems in dynabase_systems")
