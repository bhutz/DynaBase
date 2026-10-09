# Dynabase (https://dynabase.org): dimension 1, degree 3, rational maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.bb44cfba.16d54f50.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^3 + 94*x^2*y + 118*x*y^2 - 84*y^3, 33*x^3 + 122*x^2*y - 43*x*y^2 - 42*y^3], domain=P), '1.161ac27f.6ad71bd1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([24*x^3 + 12*x^2*y - 39*x*y^2 + 3*y^3, 4*x^3 + 28*x^2*y - 20*x*y^2 + 6*y^3], domain=P), '1.f857410f.edf1d3b1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([180*x^3 - 564*x^2*y - 48*x*y^2 + 332*y^3, -270*x^3 + 543*x^2*y - 169*x*y^2 - 254*y^3], domain=P), '1.e9500b5e.676e33f1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 7*x^2*y - 63*x*y^2 + 20*y^3, 9*x^3 - 62*x^2*y + 33*x*y^2 + 20*y^3], domain=P), '1.77979ce5.f41a47d3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 8*x^2*y + 2*x*y^2 - 4*y^3, 3*x^3 + 13*x^2*y + 2*x*y^2], domain=P), '1.e848265f.05b2f134.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, -5*x^2*y + 9*y^3], domain=P), '1.adcffdac.f375f64a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 + 4*x^2*y - 17*x*y^2 - 4*y^3, -4*x^3 - 17*x^2*y + 4*x*y^2 + 8*y^3], domain=P), '1.63d1b9a4.21e5764c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 + 4*x^2*y - 17*x*y^2 - 4*y^3, 4*x^3 + 17*x^2*y - 4*x*y^2 - 8*y^3], domain=P), '1.df2779ce.bbc25f82.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^3 - 61*x^2*y - 83*x*y^2 + 90*y^3, -40*x^3 + 15*x^2*y - 5*x*y^2 + 30*y^3], domain=P), '1.f786e132.47eb7e99.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([78*x^3 + 72*x^2*y - 182*x*y^2 - 28*y^3, -3*x^3 + 107*x^2*y + 100*x*y^2 - 84*y^3], domain=P), '1.6eb32f83.c841c711.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^3 - 13*x*y^2, -6*x^2*y + 12*y^3], domain=P), '1.90112a34.6ec17956.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 9*x*y^2, -3*x^2*y + 16*y^3], domain=P), '1.46531c98.d2b27f19.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 10*x*y^2, -7*x^2*y + 4*y^3], domain=P), '1.6d4e8f2a.b5107965.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([25*x^3 - 9*x*y^2, 20*x^2*y + 4*y^3], domain=P), '1.05ea98b1.802705c5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 - 17*x*y^2, 7*x^2*y + 2*y^3], domain=P), '1.8924090a.20fea5d8.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^2*y + 4*y^3, 4*x^3 - 9*x*y^2], domain=P), '1.b5a57894.84ad272e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([10*x^2*y - 4*y^3, -4*x^3 + 7*x*y^2], domain=P), '1.0c07fb92.191cdb5b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([18*x^2*y - 8*y^3, -8*x^3 + 23*x*y^2], domain=P), '1.2dc59329.1a7010e3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([137*x^3 + 28*x^2*y - 203*x*y^2 + 38*y^3, -9*x^3 + 139*x^2*y + 6*x*y^2 - 76*y^3], domain=P), '1.01cf4253.f091e4fc.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.05af5145.a779cc92.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - y^3, -x^3 + 4*x*y^2], domain=P), '1.11868901.d872feca.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, -8*x^3 + 17*x*y^2], domain=P), '1.f49ab18a.ded145b3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, -2*x^3 + 3*x*y^2], domain=P), '1.75f37810.5a376865.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, 2*x^3 - 3*x*y^2], domain=P), '1.ee2edc14.5a376865.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, 8*x^3 - 17*x*y^2], domain=P), '1.ee2edc14.ded145b3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, -x^2*y + 4*y^3], domain=P), '1.6d70e7f6.70c2844a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 7*x*y^2, 2*x^2*y + y^3], domain=P), '1.d4c4d3c3.66ae8c60.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 6*x*y^2, -11*x^2*y + 9*y^3], domain=P), '1.aea4aa27.6eefe708.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^3 - 6*x*y^2, -x^2*y + 4*y^3], domain=P), '1.497f03ff.dfc6ef2d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^3 - 5*x*y^2, -11*x^2*y + 20*y^3], domain=P), '1.860f981f.c864f6c7.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, 11*x^2*y + y^3], domain=P), '1.520d3755.6a0f93b9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 + 2*x^2*y - 5*x*y^2 - 4*y^3, -x^2*y - x*y^2 + 2*y^3], domain=P), '1.6b4abd60.b3201afa.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, -21*x^2*y + 9*y^3], domain=P), '1.349aff16.637cbba3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 - 7*x^2*y - x*y^2 + 6*y^3, 4*x^3 - 6*x^2*y - 10*x*y^2 + 6*y^3], domain=P), '1.65347037.992f24d6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([14*x^3 + 25*x^2*y - 31*x*y^2 - 10*y^3, 10*x^3 + 31*x^2*y - 25*x*y^2 - 14*y^3], domain=P), '1.5544b0b9.9470101a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 + 4*x^2*y - 49*x*y^2 - 4*y^3, 4*x^3 + 49*x^2*y - 4*x*y^2 - 4*y^3], domain=P), '1.2fc8ec87.ac4bdf3a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 9*x*y^2, x^2*y + y^3], domain=P), '1.bbec1fb0.02a23e7d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, -x^2*y + 4*y^3], domain=P), '1.75be8cf8.f79b3f74.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 - 5*x*y^2, -2*x^2*y + 2*y^3], domain=P), '1.46956e6a.3206b021.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 + 14*x^2*y + x*y^2 - 13*y^3, -2*x^2*y - 4*x*y^2 + 2*y^3], domain=P), '1.85d9b82f.d70a56ec.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 7*x*y^2, 2*x^2*y + 4*y^3], domain=P), '1.4c831a59.ba1b717f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 - 14*x*y^2, -11*x^2*y + 8*y^3], domain=P), '1.8ccc5226.9a9dc720.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 + x*y^2], domain=P), '1.00f334b7.3bfa9eee.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^2*y - 2*y^3, -2*x^3 + 5*x*y^2], domain=P), '1.b763cf05.1590483d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 - 11*x*y^2], domain=P), '1.28d1e01b.3526473c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 + 5*x^2*y - 4*x*y^2 - 7*y^3, -4*x^3 - 6*x^2*y + 12*x*y^2 + 7*y^3], domain=P), '1.85f08b95.514ba404.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^2*y + 4*y^3, 4*x^3 - 7*x*y^2], domain=P), '1.2485bc1c.9c8ddc05.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^2*y + y^3, x^3 - 4*x*y^2], domain=P), '1.655ef22b.e4e0bc81.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([16*x^2*y + 10*y^3, 10*x^3 - 13*x*y^2], domain=P), '1.e25ef012.630593f2.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([342*x^3 + y^3, 343*x^2*y], domain=P), '1.353486f4.2b9249fa.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.ee2edc14.3d72adff.2'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3 - x*y^2], domain=P), '1.fa448265.8d0f1905.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.6a61ce14.c0adc3ec.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 + y^3, x^2*y], domain=P), '1.b5ec72c5.b0479528.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([39*x^2*y - 15*y^3, -15*x^3 + 13*x*y^2], domain=P), '1.c87db2d5.8182f050.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([658*x^3 - 1545*x^2*y - 3442*x*y^2 + 2025*y^3, 201*x^3 - 215*x^2*y + 541*x*y^2 - 675*y^3], domain=P), '1.1825f5a3.a46ef689.1'])

print("Dynabase: 59 dynamical systems in dynabase_systems")
