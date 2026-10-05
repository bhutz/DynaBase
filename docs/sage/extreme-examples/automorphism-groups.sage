# Dynabase (https://dynabase.org): Summary of Extreme Examples, automorphism groups (smallest degree for each group)
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# dFH2018
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, y^3], domain=P), '1.9554125a.42669779.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.a2324809.3fbf9eac.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.ab5c2018.5ec8e92f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.e614ceae.cc96fc25.1'])
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^8 + x*y^7, y^8], domain=P), '1.27e72460.98bcfef1.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^9 + x*y^8, y^9], domain=P), '1.7b05c466.f7c38225.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.56d48bcf.b239edf6.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
