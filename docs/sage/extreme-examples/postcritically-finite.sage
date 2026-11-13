# Dynabase (https://dynabase.org): Summary of Extreme Examples, postcritically finite maps (all of them, for each row)
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
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

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.71dc0491.720d92b7.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^6 + ((a - 1))*y^6, y^6], domain=P), '1.9781d019.d2e02e20.1'])

print("Dynabase: 67 dynamical systems in dynabase_systems")
