# Dynabase (https://dynabase.org): Summary of Extreme Examples, postcritically finite maps (all of them, for each row), rational maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.f87176de.3b08f253.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.4cc4fb80.ef9cb8b5.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.fbfd6fd4.9888ce4b.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.c346226f.0c3c179e.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.170a93ef.0fdf09c7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.89eb0e1e.d90eecb7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.095ed92d.7e1406dd.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.366a39dc.7475b914.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.56d48bcf.b239edf6.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

print("Dynabase: 17 dynamical systems in dynabase_systems")
