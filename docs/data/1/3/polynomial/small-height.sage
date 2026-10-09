# Dynabase (https://dynabase.org): dimension 1, degree 3, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 9.2099e-05
dynabase_systems.append([DynamicalSystem([2*x^3 + 21*x^2*y + 25*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.4f511a5c.f031a661.1', P(0, 1)])
# Hutz2026; height ratio 0.00016547
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y - 37*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.53ae6e59.415bb16f.1', P(0, 1)])
# Hutz2026; height ratio 0.00016738
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2 - 6*y^3, -6*y^3], domain=P), '1.fa2ce9d2.c2b4dc06.1', P(0, 1)])
# Benedetto2009; height ratio 0.014622
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 - 6*y^3, -6*y^3], domain=P), '1.4f2ccba6.7a3e142f.1', P(3, 1)])
# Benedetto2009; height ratio 0.020499
dynabase_systems.append([DynamicalSystem([4*x^3 - 7*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.d073ed60.88a37e20.1', P(2, 1)])
# AMT2020; height ratio 0.023368
dynabase_systems.append([DynamicalSystem([x^3 - 6*x*y^2 - 8*y^3, -4*y^3], domain=P), '1.31ca8b83.56a37501.1', P(0, 1)])
# Benedetto2009; height ratio 0.023414
dynabase_systems.append([DynamicalSystem([16*x^3 - 16*x*y^2 - 15*y^3, -15*y^3], domain=P), '1.1e4d1273.5dc5464a.1', P(-1, 4)])
# Benedetto2009; height ratio 0.025431
dynabase_systems.append([DynamicalSystem([4*x^3 - 5*x*y^2 - 4*y^3, -4*y^3], domain=P), '1.34f852bb.e2925272.1', P(0, 1)])
# Benedetto2009; height ratio 0.026174
dynabase_systems.append([DynamicalSystem([x^3 - 7*x*y^2 + 6*y^3, 6*y^3], domain=P), '1.e25e3e69.bbc2e348.1', P(-4, 1)])
# Benedetto2009; height ratio 0.029285
dynabase_systems.append([DynamicalSystem([4*x^3 - 4*x*y^2 + 3*y^3, 3*y^3], domain=P), '1.8aeb464f.0c20066b.1', P(-1, 2)])
# Benedetto2009; height ratio 0.035085
dynabase_systems.append([DynamicalSystem([x^3 - 4*x*y^2 + 3*y^3, 3*y^3], domain=P), '1.bd42efc7.6176739e.1', P(-3, 1)])
# Benedetto2009; height ratio 0.038051
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + 3*y^3, 3*y^3], domain=P), '1.5aac8d61.852d660b.1', P(2, 1)])
# Benedetto2009; height ratio 0.038625
dynabase_systems.append([DynamicalSystem([x^3 - 7*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.062d6fd4.8aa6fecd.1', P(4, 1)])
# AMT2020, Benedetto2009; height ratio 0.040902
dynabase_systems.append([DynamicalSystem([9*x^3 - 12*x*y^2 - 16*y^3, -16*y^3], domain=P), '1.194ce1a9.8660b31e.1', P(2, 1)])
# Benedetto2009; height ratio 0.040959
dynabase_systems.append([DynamicalSystem([2*x^3 - 5*x*y^2 - 3*y^3, -3*y^3], domain=P), '1.7c4d9da4.cf052ce5.1', P(-2, 1)])
# Benedetto2009; height ratio 0.046869
dynabase_systems.append([DynamicalSystem([9*x^3 - 5*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.721c6bfd.9ba98839.1', P(0, 1)])
# Benedetto2009; height ratio 0.047227
dynabase_systems.append([DynamicalSystem([4*x^3 - x*y^2 - 6*y^3, -6*y^3], domain=P), '1.ae26dd44.18f135b8.1', P(-3, 2)])
# Benedetto2009; height ratio 0.0477
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - y^3, -y^3], domain=P), '1.facf0049.688d3315.1', P(0, 1)])
# Benedetto2009; height ratio 0.048093
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + 6*y^3, 6*y^3], domain=P), '1.930d87c7.62a84f51.1', P(3, 1)])
# Benedetto2009; height ratio 0.056296
dynabase_systems.append([DynamicalSystem([9*x^3 - 13*x*y^2, 6*y^3], domain=P), '1.00a8d209.fb578664.1', P(-5, 3)])
# Benedetto2009; height ratio 0.059038
dynabase_systems.append([DynamicalSystem([x^3 - 9*x*y^2 + 4*y^3, 4*y^3], domain=P), '1.daf0cc02.21d9e611.1', P(4, 1)])
# Benedetto2009; height ratio 0.06391
dynabase_systems.append([DynamicalSystem([4*x^3 - 7*x*y^2 + 6*y^3, 6*y^3], domain=P), '1.2f943509.9f423aad.1', P(2, 1)])
# AMT2020, Benedetto2009; height ratio 0.065634
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.7e36c441.20e2ac14.1', P(-1, 1)])
# Benedetto2009; height ratio 0.071524
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.0e5bf0af.6c3e1388.1', P(-1, 1)])
# Benedetto2009; height ratio 0.074771
dynabase_systems.append([DynamicalSystem([x^3 - 7*x*y^2 + 3*y^3, 3*y^3], domain=P), '1.596006ca.582041e4.1', P(-4, 1)])
# Benedetto2009; height ratio 0.08155
dynabase_systems.append([DynamicalSystem([x^3 - 28*x*y^2 + 16*y^3, 16*y^3], domain=P), '1.c1e1ae4b.d73171c9.1', P(0, 1)])
# AMT2020, Benedetto2009; height ratio 0.084124
dynabase_systems.append([DynamicalSystem([3*x^3 - 36*x*y^2 + 16*y^3, 16*y^3], domain=P), '1.6502de33.969c7b25.1', P(0, 1)])
# Benedetto2009; height ratio 0.091641
dynabase_systems.append([DynamicalSystem([4*x^3 - 5*x*y^2, 2*y^3], domain=P), '1.86af38cb.639acb45.1', P(-3, 2)])
# AMT2020; height ratio 0.092627
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y + 2*y^3, -2*y^3], domain=P), '1.3e20f681.046df03c.1', P(2, 1)])
# Benedetto2009; height ratio 0.098903
dynabase_systems.append([DynamicalSystem([4*x^3 - 3*x*y^2 - y^3, -y^3], domain=P), '1.7131a09e.8573ce82.1', P(-1, 1)])
# AMT2020, Benedetto2009, Ingram2012; height ratio 0.10291
dynabase_systems.append([DynamicalSystem([9*x^3 - 12*x*y^2 + 16*y^3, 16*y^3], domain=P), '1.9fcfd25c.91fd0195.1', P(2, 1)])
# Benedetto2009; height ratio 0.10443
dynabase_systems.append([DynamicalSystem([4*x^3 - x*y^2 - 2*y^3, -2*y^3], domain=P), '1.d4a34d4b.6a79bec0.1', P(-1, 1)])
# AMT2020; height ratio 0.1117
dynabase_systems.append([DynamicalSystem([x^3 + 21*x*y^2 - 98*y^3, -28*y^3], domain=P), '1.170955e6.895e6900.1', P(7, 1)])
# Benedetto2009; height ratio 0.12666
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + 2*y^3, 2*y^3], domain=P), '1.cb051a84.cd6fab67.1', P(2, 1)])
# AMT2020, Benedetto2009; height ratio 0.13013
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.5ac401c2.34c3c88c.1', P(-3, 1)])
# AMT2020, Benedetto2009; height ratio 0.17378
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.5b621046.0e8d94e9.1', P(3, 1)])
# Benedetto2009; height ratio 0.21005
dynabase_systems.append([DynamicalSystem([4*x^3 - 7*x*y^2, -2*y^3], domain=P), '1.6767275a.82516cf9.1', P(-2, 1)])
# AMT2020; height ratio 0.21031
dynabase_systems.append([DynamicalSystem([6*x^3 - 9*x^2*y, -2*y^3], domain=P), '1.b40fd63f.4b09c087.1', P(1, 2)])
# AMT2020, Benedetto2009; height ratio 0.21031
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.e8bb745c.fe98c06c.1', P(-1, 2)])
# dFH2018, GHJSX2021, FN1997; height ratio 0.23321
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, y^3], domain=P), '1.9554125a.42669779.1', P(-1, 1)])
# Benedetto2009; height ratio 0.28712
dynabase_systems.append([DynamicalSystem([x^3 - 28*x*y^2 - 16*y^3, -16*y^3], domain=P), '1.143c76d8.2e93d8f3.1', P(0, 1)])
# AMT2020; height ratio 0.55769
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y, -y^3], domain=P), '1.ad8ccd97.61cd033e.1', P(-1, 1)])

print("Dynabase: 42 dynamical systems in dynabase_systems")
