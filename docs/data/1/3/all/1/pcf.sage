# Dynabase (https://dynabase.org): Dimension 1, degree 3 maps over QQ, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.fcc3f607.78dde912.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.e8b4d7b9.76f410c3.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y + 2*y^3, -2*y^3], domain=P), '1.19c8476f.c14935ce.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.2142a8dc.f10f2f86.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.48280c35.4e1a6268.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.da2b6adb.6af3bd89.1'])
# Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, y^3], domain=P), '1.5d5bc592.6af3bd89.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([4*x^3 + 3*x^2*y + 6*x*y^2 - 3*y^3, -7*y^3], domain=P), '1.a3b69891.7b115b3c.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3*x*y^2, y^3], domain=P), '1.da2b6adb.6af3bd89.2'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.3204476a.7fdfbb3b.1'])
# Benedetto2009, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.8d1d75ce.14532702.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.fe349f2e.400608e6.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3, -2*x^3 + 6*x^2*y + 3*x*y^2 - 4*y^3], domain=P), '1.3e1e6f0e.924ace90.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.ad88b95b.f2825a1c.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 3*x*y^2 + y^3], domain=P), '1.1629b8e6.58109c1f.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - y^3, y^3], domain=P), '1.0a11425e.58109c1f.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/2*x*y^2, y^3], domain=P), '1.0a11425e.58109c1f.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3/2*x*y^2, y^3], domain=P), '1.1629b8e6.58109c1f.2'])
# FN1997, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.34726b93.790bef87.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.fcc3f607.790bef87.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.fcc3f607.790bef87.2'])

print("Dynabase: 21 dynamical systems in dynabase_systems")
