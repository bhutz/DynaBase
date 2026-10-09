# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 3.079e-06
dynabase_systems.append([DynamicalSystem([1115*x^3 - 2405*x^2*y - 37855*x*y^2 + 3465*y^3, 201*x^3 + 173*x^2*y + 1907*x*y^2 - 3465*y^3], domain=P), '1.1825f5a3.a46ef689.1', P(0, 1)])
# Hutz2026; height ratio 3.2586e-06
dynabase_systems.append([DynamicalSystem([183*x^3 - 3203*x^2*y + 15445*x*y^2 + 5775*y^3, 57*x^3 - 1117*x^2*y + 6107*x*y^2 - 5775*y^3], domain=P), '1.0aba1c76.ac22b7ff.1', P(0, 1)])
# Hutz2026; height ratio 3.2984e-06
dynabase_systems.append([DynamicalSystem([21*x^3 + 312*x^2*y + 579*x*y^2 - 72*y^3, 26*x^3 + 47*x^2*y - 141*x*y^2 - 72*y^3], domain=P), '1.50b47f1a.f7f950f2.1', P(0, 1)])
# GHJSX2021; height ratio 0.014248
dynabase_systems.append([DynamicalSystem([36*x^3 - 64*x*y^2, -189*x^2*y + 36*y^3], domain=P), '1.349aff16.637cbba3.1', P(-2, 1)])
# GHJSX2021; height ratio 0.018211
dynabase_systems.append([DynamicalSystem([9*x^3 - 9*x*y^2, -25*x^2*y + 9*y^3], domain=P), '1.6b4abd60.b3201afa.1', P(-1, 3)])
# Hutz2026; height ratio 0.021818
dynabase_systems.append([DynamicalSystem([2*x^2*y - 26*x*y^2 + 12*y^3, -x^3 - x^2*y + 8*x*y^2 - 12*y^3], domain=P), '1.e848265f.05b2f134.1', P(6, 1)])
# GHJSX2021; height ratio 0.025866
dynabase_systems.append([DynamicalSystem([8*x^2*y + 4*y^3, 4*x^3 - 7*x*y^2], domain=P), '1.2485bc1c.9c8ddc05.1', P(-1, 1)])
# GHJSX2021; height ratio 0.027235
dynabase_systems.append([DynamicalSystem([9*x^3 - 57*x*y^2, -25*x^2*y + 9*y^3], domain=P), '1.63d1b9a4.21e5764c.1', P(-5, 1)])
# GHJSX2021; height ratio 0.027804
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 - 11*x*y^2], domain=P), '1.28d1e01b.3526473c.1', P(-3, 2)])
# GHJSX2021; height ratio 0.029906
dynabase_systems.append([DynamicalSystem([8*x^3 - 14*x*y^2, -11*x^2*y + 8*y^3], domain=P), '1.8ccc5226.9a9dc720.1', P(-1, 2)])
# GHJSX2021; height ratio 0.029971
dynabase_systems.append([DynamicalSystem([2*x^3 - 2*x*y^2, -5*x^2*y + 2*y^3], domain=P), '1.46956e6a.3206b021.1', P(-2, 1)])
# GHJSX2021; height ratio 0.034688
dynabase_systems.append([DynamicalSystem([2*x^3 + x*y^2, -14*x^2*y + 2*y^3], domain=P), '1.d4c4d3c3.66ae8c60.1', P(-2, 1)])
# GHJSX2021; height ratio 0.036947
dynabase_systems.append([DynamicalSystem([36*x^3 - 45*x*y^2, -64*x^2*y + 36*y^3], domain=P), '1.adcffdac.f375f64a.1', P(-1, 6)])
# GHJSX2021; height ratio 0.03889
dynabase_systems.append([DynamicalSystem([4*x^3 + 8*x*y^2, -7*x^2*y + 4*y^3], domain=P), '1.4c831a59.ba1b717f.1', P(-1, 1)])
# GHJSX2021; height ratio 0.039313
dynabase_systems.append([DynamicalSystem([4*x^3 - 4*x*y^2, -x^2*y + 4*y^3], domain=P), '1.75be8cf8.f79b3f74.1', P(-1, 2)])
# GHJSX2021; height ratio 0.041824
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.6a61ce14.c0adc3ec.1', P(-1, 1)])
# GHJSX2021; height ratio 0.042676
dynabase_systems.append([DynamicalSystem([4*x^3 - 10*x*y^2, -7*x^2*y + 4*y^3], domain=P), '1.6d4e8f2a.b5107965.1', P(-2, 5)])
# GHJSX2021; height ratio 0.044123
dynabase_systems.append([DynamicalSystem([4*x^3 + 11*x*y^2, -64*x^2*y + 4*y^3], domain=P), '1.520d3755.6a0f93b9.1', P(-5, 2)])
# GHJSX2021; height ratio 0.046869
dynabase_systems.append([DynamicalSystem([39*x^2*y - 15*y^3, -15*x^3 + 13*x*y^2], domain=P), '1.c87db2d5.8182f050.1', P(-2, 1)])
# GHJSX2021; height ratio 0.047074
dynabase_systems.append([DynamicalSystem([y^3, x^3 + x*y^2], domain=P), '1.fa448265.8d0f1905.2', P(-1, 1)])
# GHJSX2021; height ratio 0.048112
dynabase_systems.append([DynamicalSystem([9*x^2*y - 4*y^3, -4*x^3 + 64*x*y^2], domain=P), '1.5544b0b9.9470101a.1', P(-2, 1)])
# GHJSX2021; height ratio 0.048142
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 + 13*x*y^2], domain=P), '1.65347037.992f24d6.1', P(-7, 2)])
# GHJSX2021; height ratio 0.049024
dynabase_systems.append([DynamicalSystem([4*x^3 - 4*x*y^2, -13*x^2*y + 4*y^3], domain=P), '1.6d70e7f6.70c2844a.1', P(-2, 5)])
# GHJSX2021; height ratio 0.051238
dynabase_systems.append([DynamicalSystem([45*x^2*y - 45*y^3, -45*x^3 + 77*x*y^2], domain=P), '1.2fc8ec87.ac4bdf3a.1', P(-3, 5)])
# GHJSX2021; height ratio 0.051964
dynabase_systems.append([DynamicalSystem([18*x^2*y - 8*y^3, -8*x^3 + 23*x*y^2], domain=P), '1.2dc59329.1a7010e3.1', P(-1, 2)])
# GHJSX2021; height ratio 0.052899
dynabase_systems.append([DynamicalSystem([20*x^3 - 5*x*y^2, -44*x^2*y + 20*y^3], domain=P), '1.860f981f.c864f6c7.1', P(-2, 1)])
# GHJSX2021; height ratio 0.053495
dynabase_systems.append([DynamicalSystem([18*x^3 - 27*x*y^2, -2*x^2*y + 18*y^3], domain=P), '1.497f03ff.dfc6ef2d.1', P(-4, 3)])
# GHJSX2021; height ratio 0.054114
dynabase_systems.append([DynamicalSystem([4*x^3 - 2*x*y^2, -15*x^2*y + 4*y^3], domain=P), '1.85d9b82f.d70a56ec.1', P(-3, 2)])
# GHJSX2021; height ratio 0.054199
dynabase_systems.append([DynamicalSystem([8*x^3 + 7*x*y^2, -68*x^2*y + 8*y^3], domain=P), '1.8924090a.20fea5d8.1', P(-2, 1)])
# GHJSX2021; height ratio 0.055916
dynabase_systems.append([DynamicalSystem([2*x^2*y + y^3, x^3 - 4*x*y^2], domain=P), '1.655ef22b.e4e0bc81.1', P(-1, 2)])
# GHJSX2021; height ratio 0.056525
dynabase_systems.append([DynamicalSystem([20*x^3 + 16*x*y^2, -45*x^2*y + 20*y^3], domain=P), '1.05ea98b1.802705c5.1', P(-2, 5)])
# GHJSX2021; height ratio 0.05842
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 + x*y^2], domain=P), '1.00f334b7.3bfa9eee.1', P(-2, 1)])
# GHJSX2021; height ratio 0.059097
dynabase_systems.append([DynamicalSystem([2*x^2*y - 4*y^3, -4*x^3 + 15*x*y^2], domain=P), '1.85f08b95.514ba404.1', P(-1, 1)])
# GHJSX2021; height ratio 0.059497
dynabase_systems.append([DynamicalSystem([2*x^2*y - 2*y^3, -2*x^3 + 5*x*y^2], domain=P), '1.b763cf05.1590483d.1', P(-1, 2)])
# GHJSX2021; height ratio 0.059793
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, -8*x^3 + 17*x*y^2], domain=P), '1.f49ab18a.ded145b3.1', P(-3, 4)])
# GHJSX2021; height ratio 0.06046
dynabase_systems.append([DynamicalSystem([16*x^2*y + 10*y^3, 10*x^3 - 13*x*y^2], domain=P), '1.e25ef012.630593f2.1', P(-5, 2)])
# GHJSX2021; height ratio 0.064882
dynabase_systems.append([DynamicalSystem([57*x^2*y - 9*y^3, -9*x^3 + 25*x*y^2], domain=P), '1.df2779ce.bbc25f82.1', P(-11, 3)])
# GHJSX2021; height ratio 0.066801
dynabase_systems.append([DynamicalSystem([342*x^3 + 343*y^3, 343*x^2*y], domain=P), '1.353486f4.2b9249fa.1', P(-7, 6)])
# GHJSX2021; height ratio 0.066962
dynabase_systems.append([DynamicalSystem([12*x^3 - 24*x*y^2, -13*x^2*y + 12*y^3], domain=P), '1.90112a34.6ec17956.1', P(-3, 2)])
# GHJSX2021; height ratio 0.072359
dynabase_systems.append([DynamicalSystem([6*x^2*y + 4*y^3, 4*x^3 - 9*x*y^2], domain=P), '1.b5a57894.84ad272e.1', P(-8, 3)])
# GHJSX2021; height ratio 0.072954
dynabase_systems.append([DynamicalSystem([16*x^3 - 48*x*y^2, -9*x^2*y + 16*y^3], domain=P), '1.46531c98.d2b27f19.1', P(-4, 1)])
# GHJSX2021; height ratio 0.073691
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, -2*x^3 + 3*x*y^2], domain=P), '1.75f37810.5a376865.1', P(-3, 4)])
# GHJSX2021; height ratio 0.075002
dynabase_systems.append([DynamicalSystem([10*x^2*y - 4*y^3, -4*x^3 + 7*x*y^2], domain=P), '1.0c07fb92.191cdb5b.1', P(-5, 2)])
# GHJSX2021; height ratio 0.096198
dynabase_systems.append([DynamicalSystem([4*x^2*y - y^3, -x^3 + 4*x*y^2], domain=P), '1.11868901.d872feca.1', P(-1, 3)])
# GHJSX2021; height ratio 0.097198
dynabase_systems.append([DynamicalSystem([12*x^3 - 8*x*y^2, -33*x^2*y + 12*y^3], domain=P), '1.aea4aa27.6eefe708.1', P(-3, 4)])
# GHJSX2021; height ratio 0.10807
dynabase_systems.append([DynamicalSystem([2*x^3 + y^3, x^2*y], domain=P), '1.b5ec72c5.b0479528.1', P(1, 1)])
# GHJSX2021; height ratio 0.10815
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1', P(1, 1)])
# GHJSX2021; height ratio 0.11532
dynabase_systems.append([DynamicalSystem([y^3, x^3 - x*y^2], domain=P), '1.fa448265.8d0f1905.1', P(-2, 1)])
# GHJSX2021; height ratio 0.11766
dynabase_systems.append([DynamicalSystem([2*x^2*y + y^3, x^3 + 2*x*y^2], domain=P), '1.f3cb63c5.12dbaacc.1', P(-1, 2)])
# GHJSX2021; height ratio 0.12095
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2, -9*x^2*y + y^3], domain=P), '1.bbec1fb0.02a23e7d.1', P(-1, 1)])
# GHJSX2021; height ratio 0.12161
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, 2*x^3 - 3*x*y^2], domain=P), '1.ee2edc14.5a376865.1', P(-3, 4)])
# GHJSX2021; height ratio 0.13521
dynabase_systems.append([DynamicalSystem([2*x^2*y - y^3, x^3 - 2*x*y^2], domain=P), '1.ee2edc14.12dbaacc.1', P(-1, 2)])
# GHJSX2021; height ratio 0.13862
dynabase_systems.append([DynamicalSystem([x^3 + y^3, x^2*y], domain=P), '1.b970fbd1.f98cedf9.1', P(1, 1)])
# dFH2018, GHJSX2021; height ratio 0.14804
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1', P(-1, 2)])
# GHJSX2021; height ratio 0.14804
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.ee2edc14.3d72adff.2', P(-1, 2)])
# GHJSX2021; height ratio 0.17352
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, 8*x^3 - 17*x*y^2], domain=P), '1.ee2edc14.ded145b3.1', P(-3, 4)])

print("Dynabase: 56 dynamical systems in dynabase_systems")
