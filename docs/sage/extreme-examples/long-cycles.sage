# Dynabase (https://dynabase.org): Summary of Extreme Examples, long rational cycles
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.1da98dda.1cfac040.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^4 - 14*x^3*y - 63*x^2*y^2 + 314*x*y^3, -120*y^4], domain=P), '1.a0dac219.26bee824.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([172*x^5 - 280*x^4*y - 1175*x^3*y^2 + 1330*x^2*y^3 + 1843*x*y^4 - 1050*y^5, -420*y^5], domain=P), '1.a813d7bb.9d684b8b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([37*x^6 + 699*x^5*y + 3955*x^4*y^2 + 3345*x^3*y^3 - 24152*x^2*y^4 - 29244*x*y^5 + 5040*y^6, 5040*y^6], domain=P), '1.28559cc1.c4578bdd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([17*x^7 - 70*x^6*y - 469*x^5*y^2 + 1610*x^4*y^3 + 3668*x^3*y^4 - 7840*x^2*y^5 - 6996*x*y^6 + 2520*y^7, 2520*y^7], domain=P), '1.a116d3bd.871dfac8.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^8 + 21*x^7*y - 161*x^6*y^2 - 651*x^5*y^3 + 2611*x^4*y^4 + 5754*x^3*y^5 - 17574*x^2*y^6 - 10164*x*y^7 + 20160*y^8, 5040*y^8], domain=P), '1.1b32f8a3.b7900ec8.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([272*x^9 + 384*x^8*y - 4536*x^7*y^2 - 4704*x^6*y^3 + 26481*x^5*y^4 + 17976*x^4*y^5 - 60269*x^3*y^6 - 19326*x^2*y^7 + 36162*x*y^8 - 3780*y^9, -7560*y^9], domain=P), '1.10f82472.ce6ee4fc.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([74*x^10 - 238*x^9*y - 52401*x^8*y^2 - 618552*x^7*y^3 - 699552*x^6*y^4 + 17285898*x^5*y^5 + 37024291*x^4*y^6 - 138284468*x^3*y^7 - 36272412*x^2*y^8 - 8112240*x*y^9 - 129729600*y^10, -129729600*y^10], domain=P), '1.1d4c2bf4.a2235824.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([257*x^11 + 9331*x^10*y + 120130*x^9*y^2 + 579300*x^8*y^3 - 229479*x^7*y^4 - 11442417*x^6*y^5 - 52169780*x^5*y^6 - 128719150*x^4*y^7 + 428342072*x^3*y^8 + 2215246536*x^2*y^9 - 1413900000*x*y^10 - 1037836800*y^11, -518918400*y^11], domain=P), '1.0cca5889.247cf2ab.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6847*x^12 - 246252*x^11*y + 2861183*x^10*y^2 - 4657620*x^9*y^3 - 133640139*x^8*y^4 + 716294124*x^7*y^5 + 1338002189*x^6*y^6 - 14257305420*x^5*y^7 + 2892624592*x^4*y^8 + 88929820128*x^3*y^9 - 36791713872*x^2*y^10 - 129870336960*x*y^11 - 108972864000*y^12, -21794572800*y^12], domain=P), '1.ccc4811b.487121f5.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([860*x^13 + 61685*x^12*y + 1906138*x^11*y^2 + 33008833*x^10*y^3 + 347125350*x^9*y^4 + 2213680755*x^8*y^5 + 7633125214*x^7*y^6 + 5859546979*x^6*y^7 - 52599293890*x^5*y^8 - 171757668940*x^4*y^9 - 108558503352*x^3*y^10 + 204127005888*x^2*y^11 + 181197233280*x*y^12 + 6227020800*y^13, -6227020800*y^13], domain=P), '1.9333086c.415680ad.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([34*x^14 - 5474*x^13*y + 397033*x^12*y^2 - 17145856*x^11*y^3 + 490911421*x^10*y^4 - 9820782972*x^9*y^5 + 140949659279*x^8*y^6 - 1466929231768*x^7*y^7 + 11059905517661*x^6*y^8 - 59702976487154*x^5*y^9 + 225313258722188*x^4*y^10 - 570881108919576*x^3*y^11 + 907090218753984*x^2*y^12 - 796573394467200*x*y^13 + 285901205990400*y^14, 43589145600*y^14], domain=P), '1.1a8d2917.bb444830.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([41*x^15 - 7380*x^14*y + 604100*x^13*y^2 - 29767920*x^12*y^3 + 985137062*x^11*y^4 - 23127063960*x^10*y^5 + 396533008300*x^9*y^6 - 5035984770960*x^8*y^7 + 47529555226153*x^7*y^8 - 331368195898740*x^6*y^9 + 1680182681686600*x^5*y^10 - 6029166612225120*x^4*y^11 + 14653631890929744*x^3*y^12 - 22451626097881920*x^2*y^13 + 19048387680000000*x*y^14 - 6585448117248000*y^15, 1307674368000*y^15], domain=P), '1.231a24d2.127a62ff.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.f087c4af.5b9da8c6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.05af5145.a779cc92.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.273dc9f6.ddfc6e2a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 71/48*y^2, y^2], domain=P), '1.e2965d3f.1dd287fe.1'])

print("Dynabase: 22 dynamical systems in dynabase_systems")
