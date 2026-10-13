# Dynabase (https://dynabase.org): Dimension 1, degree 2 maps over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# BCHKW2014, Hutz2026; height ratio 0.00046574
dynabase_systems.append([DynamicalSystem([592*x^2 - 3424*x*y + 1024*y^2, 173*x^2 - 536*x*y - 1024*y^2], domain=P), '1.3b026e07.265dfbb0.1', P(0, 1)])
# Hutz2026; height ratio 0.001183
dynabase_systems.append([DynamicalSystem([285*x^2 + 2085*x*y + 990*y^2, -79*x^2 - 351*x*y + 990*y^2], domain=P), '1.0a9b4372.2927b5eb.1', P(0, 1)])
# BCHKW2014, Hutz2026; height ratio 0.0066042
dynabase_systems.append([DynamicalSystem([x^2 - 7*x*y - 12*y^2, 6*y^2], domain=P), '1.98c91caa.4cf50642.1', P(0, 1)])
# Hutz2026; height ratio 0.01102
dynabase_systems.append([DynamicalSystem([x^2 + 17*x*y - 6*y^2, -6*y^2], domain=P), '1.55c16ffb.e4dc7fdb.1', P(0, 1)])
# Hutz2026; height ratio 0.013458
dynabase_systems.append([DynamicalSystem([5*x^2 - 97*x*y - 756*y^2, -42*y^2], domain=P), '1.5fab3ba3.dc35593e.1', P(0, 1)])
# CV2017; height ratio 0.092981
dynabase_systems.append([DynamicalSystem([2*y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.2', P(-1, 1)])
# CV2017; height ratio 0.095631
dynabase_systems.append([DynamicalSystem([3*x^2 + x*y - 2*y^2, 3*x^2], domain=P), '1.fb83e34d.c7184a61.1', P(1, 3)])
# Manes2008; height ratio 0.13102
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, 3*x*y], domain=P), '1.ac8cf792.942e5495.1', P(-1, 4)])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020; height ratio 0.13902
dynabase_systems.append([DynamicalSystem([9*x^2 - 13*y^2, 9*y^2], domain=P), '1.05f9cf28.88243c92.1', P(-2, 3)])
# CV2017; height ratio 0.14218
dynabase_systems.append([DynamicalSystem([5*x*y - 2*y^2, 3*x^2], domain=P), '1.e22974b1.a9cc00d0.1', P(-2, 1)])
# Morton1992, Poonen1998, Doyle2014, Doyle2018, DoHi2025; height ratio 0.14692
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.1a2a6bbf.1ed2bf82.1', P(0, 1)])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020; height ratio 0.14891
dynabase_systems.append([DynamicalSystem([9*x^2 - 10*y^2, 9*y^2], domain=P), '1.de450653.9e174cad.1', P(-1, 3)])
# CV2017; height ratio 0.15535
dynabase_systems.append([DynamicalSystem([x*y + y^2, -6*x^2], domain=P), '1.5823545c.68655cae.1', P(1, 3)])
# CV2017, Vishkautsan2019; height ratio 0.16526
dynabase_systems.append([DynamicalSystem([2*x^2 - x*y - y^2, 2*x^2], domain=P), '1.95ae9a5a.82a8ae0e.1', P(1, 2)])
# Manes2008; height ratio 0.1672
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -3*x*y], domain=P), '1.f4fc8255.a5a6aa7f.1', P(-1, 4)])
# Manes2008; height ratio 0.17028
dynabase_systems.append([DynamicalSystem([5*x^2 - 4*y^2, -4*x*y], domain=P), '1.b44322dc.18089662.1', P(-10, 7)])
# CV2017; height ratio 0.18187
dynabase_systems.append([DynamicalSystem([7*x*y - 6*y^2, x^2], domain=P), '1.c499b77a.5dc87905.1', P(3, 1)])
# CV2017; height ratio 0.18617
dynabase_systems.append([DynamicalSystem([x*y + y^2, x^2], domain=P), '1.9f0abdc9.7ec498ce.1', P(1, 1)])
# CV2017; height ratio 0.1921
dynabase_systems.append([DynamicalSystem([x*y - 2*y^2, -x^2], domain=P), '1.b27790b8.3354fd0f.1', P(-1, 1)])
# Lukas2014, CV2017; height ratio 0.25075
dynabase_systems.append([DynamicalSystem([4*y^2, -9*x^2 + 12*x*y], domain=P), '1.c346226f.0c3c179e.1', P(2, 1)])
# Manes2008; height ratio 0.25854
dynabase_systems.append([DynamicalSystem([2*x^2 - y^2, -x*y], domain=P), '1.6aeac73a.21e09a88.1', P(-2, 3)])
# Lukas2014, CV2017, dFH2018, BS2026; height ratio 0.27894
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1', P(-1, 2)])
# Manes2008; height ratio 0.28002
dynabase_systems.append([DynamicalSystem([x^2 - y^2, 3*x*y], domain=P), '1.18fb8816.a5a6aa7f.1', P(-1, 4)])
# BS2026; height ratio 0.32384
dynabase_systems.append([DynamicalSystem([2*x*y, x^2 - y^2], domain=P), '1.a35a25cc.024ac6d7.4', P(-1, 2)])
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020; height ratio 0.33333
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1', P(-1, 2)])
# CV2017; height ratio 0.34427
dynabase_systems.append([DynamicalSystem([6*x*y - 4*y^2, 3*x^2], domain=P), '1.145e75a7.efc06602.1', P(4, 3)])
# Lukas2014; height ratio 0.34634
dynabase_systems.append([DynamicalSystem([2*x*y, -2*x^2 + 4*x*y - y^2], domain=P), '1.095ed92d.7e1406dd.1', P(1, 1)])
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025; height ratio 0.37357
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1', P(-2, 1)])
# BS2026; height ratio 0.39155
dynabase_systems.append([DynamicalSystem([6*x*y, x^2 - 3*y^2], domain=P), '1.a35a25cc.024ac6d7.3', P(-1, 3)])
# Milnor1993, Manes2008; height ratio 0.39403
dynabase_systems.append([DynamicalSystem([x^2 + y^2, x*y], domain=P), '1.d3259bab.d36dd573.1', P(-1, 1)])
# Lukas2014, CV2017; height ratio 0.51349
dynabase_systems.append([DynamicalSystem([y^2, -4*x^2 + 4*x*y], domain=P), '1.fbfd6fd4.9888ce4b.1', P(-1, 2)])
# CV2017; height ratio 0.52022
dynabase_systems.append([DynamicalSystem([3*x*y - 2*y^2, x^2], domain=P), '1.02dc5922.c81b4028.1', P(3, 2)])
# Poonen1998, Doyle2014, Doyle2018; height ratio 0.63093
dynabase_systems.append([DynamicalSystem([4*x^2 - 3*y^2, 4*y^2], domain=P), '1.13a1af67.7eb43a7f.1', P(0, 1)])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020; height ratio 0.67619
dynabase_systems.append([DynamicalSystem([4*x^2 + y^2, 4*y^2], domain=P), '1.8f2b16a9.99353b99.1', P(-3, 2)])
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020; height ratio 1
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1', P(-1, 2)])

print("Dynabase: 35 dynamical systems in dynabase_systems")
