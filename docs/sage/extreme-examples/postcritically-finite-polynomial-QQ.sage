# Dynabase (https://dynabase.org): Summary of Extreme Examples, postcritically finite maps (all of them, for each row), polynomial maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.ad88b95b.f2825a1c.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.2142a8dc.f10f2f86.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.48280c35.4e1a6268.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.3204476a.7fdfbb3b.1'])
# Benedetto2009, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.8d1d75ce.14532702.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.fe349f2e.400608e6.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.da2b6adb.6af3bd89.1'])
# FN1997, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.34726b93.790bef87.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 3*x*y^2 + y^3], domain=P), '1.1629b8e6.58109c1f.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y + 2*y^3, -2*y^3], domain=P), '1.19c8476f.c14935ce.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - y^3, y^3], domain=P), '1.0a11425e.58109c1f.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3, -2*x^3 + 6*x^2*y + 3*x*y^2 - 4*y^3], domain=P), '1.3e1e6f0e.924ace90.1'])
# Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, y^3], domain=P), '1.5d5bc592.6af3bd89.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.e8b4d7b9.76f410c3.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([4*x^3 + 3*x^2*y + 6*x*y^2 - 3*y^3, -7*y^3], domain=P), '1.a3b69891.7b115b3c.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/2*x*y^2, y^3], domain=P), '1.0a11425e.58109c1f.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3/2*x*y^2, y^3], domain=P), '1.1629b8e6.58109c1f.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3*x*y^2, y^3], domain=P), '1.da2b6adb.6af3bd89.2'])
# FN1997, GHJSX2021, Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.9e054174.3f0eaf7a.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.14995048.fcc23423.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.68938348.14eb3256.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, 4*x*y^3 + 3*y^4], domain=P), '1.82a47d29.57db8a86.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 4*x^3*y + y^4, y^4], domain=P), '1.22037e2d.4a60706e.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 - 8/27*x*y^3 + 26/27*y^4, y^4], domain=P), '1.2da9e4fc.f7288834.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 + 8/27*x*y^3 - 19/27*y^4, y^4], domain=P), '1.a84822fb.ce008426.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 + 4*x^3*y - 6*x^2*y^2 - 12*x*y^3 + 5*y^4, 6*y^4], domain=P), '1.60a85381.e4844273.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 8*x^3*y, -6*y^4], domain=P), '1.b328a709.67009066.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, y^4], domain=P), '1.14995048.fcc23423.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + y^4, y^4], domain=P), '1.3c83e548.afd51a11.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2, y^4], domain=P), '1.b3ee860d.dc17dde7.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.d5469f32.478a246b.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.3c83e548.afd51a11.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 4*y^4, 2*y^4], domain=P), '1.68938348.14eb3256.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.ef32d183.12ccf81e.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.05e343fb.f4c36872.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^6, y^6], domain=P), '1.46c82190.c2bd952a.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.4b1ca9ed.023ff0b9.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^8, y^8], domain=P), '1.00faa61e.83bed86d.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9, y^9], domain=P), '1.790bef87.083b88f1.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10, y^10], domain=P), '1.500c00a0.a04b9cb7.1'])

print("Dynabase: 43 dynamical systems in dynabase_systems")
