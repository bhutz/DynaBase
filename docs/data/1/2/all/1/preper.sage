# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Vishkautsan2026
dynabase_systems.append([DynamicalSystem([x^2 + 5*x*y - 6*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.f990fc06.6562ad8f.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([264*x^2 + 291*x*y - 285*y^2, -121*x^2 + 268*x*y + 285*y^2], domain=P), '1.e1302513.eb5bf8e4.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([166*x^2 - 4*x*y - 162*y^2, -21*x^2 + 271*x*y + 36*y^2], domain=P), '1.5e0c1572.308b1bbd.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.50d6ba67.3704ee8d.1'])
# BCE2015
dynabase_systems.append([DynamicalSystem([37*x^2 + 29287*x*y - 13794*y^2, -443*x*y - 32802*y^2], domain=P), '1.3c0d0130.2c2c2d8b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([39*x^2 - x*y - 40*y^2, 66*x^2 - 34*x*y - 30*y^2], domain=P), '1.80955150.230d117a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x*y - 5*y^2, x^2 - 2*x*y - 5*y^2], domain=P), '1.e40ed237.6fa525a3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^2 - 7*x*y - 6*y^2, -4*x*y + 2*y^2], domain=P), '1.0dbfa3c0.fea2b8cc.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([6*x^2 + 19*x*y - 25*y^2, 6*x^2 + 19*x*y + 10*y^2], domain=P), '1.88428e98.c8e9493d.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([36*x^2 + 47*x*y - 50*y^2, 48*x^2 + 15*x*y - 30*y^2], domain=P), '1.5213697c.76dcd0f9.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([3099*x^2 - 1875*x*y - 4596*y^2, 3522*x^2 + 6310*x*y + 2382*y^2], domain=P), '1.249ed031.1fb79274.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([111*x^2 - 688*x*y - 963*y^2, -609*x^2 - 43*x*y + 722*y^2], domain=P), '1.b7d636e5.a7017af6.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([6*x^2 + 7*x*y - 5*y^2, -3*x^2 + 6*x*y + 9*y^2], domain=P), '1.13461466.22f3e54f.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([12*x^2 + 26*x*y - 30*y^2, -x^2 + 29*x*y + 30*y^2], domain=P), '1.a02c28c2.0579aeeb.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([137*x^2 - 1957*x*y - 1470*y^2, 127*x^2 + 103*x*y - 1050*y^2], domain=P), '1.d387f629.c0167d3f.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([x^2 - 11*x*y - 12*y^2, -2*x^2 - 2*x*y + 12*y^2], domain=P), '1.a7bd668d.0e5d8386.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([6*x^2 - 7*x*y - 6*y^2, 6*x^2 + 7*x*y - 6*y^2], domain=P), '1.6b9173f4.0a44ed51.1'])
# CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([6*x^2 - x*y - 5*y^2, 6*x^2 - x*y], domain=P), '1.0652a132.c763afa2.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 + 7*x*y - 9*y^2, 2*x^2 + 7*x*y + 6*y^2], domain=P), '1.88736f04.489254af.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([145*x^2 - 256*x*y - 9*y^2, 169*x*y + 39*y^2], domain=P), '1.61b166ba.7aee76d4.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([12*x^2 - 94*x*y + 147*y^2, -32*x^2 - 149*x*y - 174*y^2], domain=P), '1.acd32b8c.b8099b9d.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([150*x^2 + 60*x*y - 210*y^2, -117*x^2 + 101*x*y + 210*y^2], domain=P), '1.8806e48a.9f84c1a8.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([5100*x^2 - 4030*x*y - 9512*y^2, -5440*x^2 - 16743*x*y - 10505*y^2], domain=P), '1.2d8d5ff2.5059373c.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([x^2 - x*y - 2*y^2, -2*x^2 - 2*x*y + 2*y^2], domain=P), '1.d256e977.82f03437.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([4*x^2 + 5*x*y - 9*y^2, 3*x*y + 3*y^2], domain=P), '1.30bddb74.2f10ffa3.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.96cf3896.0738b144.1'])
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])
# CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([2*x^2 + x*y - 3*y^2, 2*x^2 + x*y], domain=P), '1.85899dfb.043eab8a.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([4*x^2 - 4*x*y + y^2, -x*y + 2*y^2], domain=P), '1.a0a9bd15.0d00d582.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([8*x^2 - x*y, x^2 + 27*x*y - 28*y^2], domain=P), '1.d13da0ca.97b57198.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 - 3*x*y - 2*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.92ce04ab.bf36a025.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([3*x*y, x^2 - y^2], domain=P), '1.360df9a4.9406c17e.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([x^2 - y^2, 3*x*y], domain=P), '1.089ed394.9406c17e.1'])
# Manes2008
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, 3*x*y], domain=P), '1.62bb12c7.99373c00.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.420f870e.c9b64d6b.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.92710271.448de5df.1'])
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])
# CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([4*x^2 + 3*x*y - y^2, x*y + 2*y^2], domain=P), '1.739430cc.ed805d0a.1'])
# CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([2*x^2 + 3*x*y - 5*y^2, 2*x^2 + 3*x*y], domain=P), '1.49f644a8.7d56d942.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([x^2 - 2*x*y + y^2, x*y + y^2], domain=P), '1.a19ef251.ad614fbd.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([6*y^2, x^2 - x*y], domain=P), '1.ebff540d.9ed2f405.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([3*x^2 + x*y - 2*y^2, -x*y + 2*y^2], domain=P), '1.55f773eb.bb3584ed.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([x^2 + 3*x*y - 4*y^2, -4*x^2 - 3*x*y + 4*y^2], domain=P), '1.1d452eb4.0c2369ce.1'])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.1e41a745.8bc476bb.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.49146aab.c4a4d949.1'])
# BS2026
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y, -2*x*y - y^2], domain=P), '1.db03b80b.9e054174.3'])
# BS2026
dynabase_systems.append([DynamicalSystem([2*x*y + y^2, x^2 - y^2], domain=P), '1.db03b80b.9e054174.5'])
# Manes2008
dynabase_systems.append([DynamicalSystem([2*x^2 - y^2, -x*y], domain=P), '1.6a1ffbc1.19afc26b.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.2a6bd967.16210f77.1'])
# Poonen1998, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.49ef408f.a255b42e.1'])
# Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 7/4*y^2, y^2], domain=P), '1.01981c7d.8230c5b3.1'])
# CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([2*y^2, x^2 - x*y - 2*y^2], domain=P), '1.13b277e2.d503772e.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([x*y - 2*y^2, -x^2], domain=P), '1.963f06ad.c4b661be.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*x*y + 2*y^2, x^2 - x*y - 2*y^2], domain=P), '1.f826034b.88904e0c.1'])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# Lukas2014, CV2017, Vishkautsan2019
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.7caff06c.b29c4e61.1'])
# Lukas2014, CV2017
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.a8c6b910.e0fda4e1.1'])
# Lukas2014, CV2017, dFH2018, BS2026
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.db03b80b.9e054174.2'])
# BS2026
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -2*x*y], domain=P), '1.db03b80b.9e054174.4'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.e585768f.4eff1f14.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.dbdf4212.adc49165.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([x*y + y^2, x^2], domain=P), '1.7fd7d429.624111b4.1'])
# CV2017
dynabase_systems.append([DynamicalSystem([2*y^2, x^2], domain=P), '1.db03b80b.9e054174.1'])
# Milnor1993, Manes2008
dynabase_systems.append([DynamicalSystem([x^2 + y^2, x*y], domain=P), '1.c8bf74dc.02e668ff.1'])
# Morton1992, Poonen1998, Doyle2014, Doyle2018, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.991c99ac.68df8ef0.1'])
# BCHKW2014, Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^2 - x*y - 6*y^2, -x^2 + 9*x*y + 6*y^2], domain=P), '1.842872ee.9614550e.1'])

print("Dynabase: 69 dynamical systems in dynabase_systems")
