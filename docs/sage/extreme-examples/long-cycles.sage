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
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.cd59cbfd.2bdca34d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^4 - 14*x^3*y - 63*x^2*y^2 + 314*x*y^3, -120*y^4], domain=P), '1.51fa5c1f.3135fa52.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([172*x^5 - 280*x^4*y - 1175*x^3*y^2 + 1330*x^2*y^3 + 1843*x*y^4 - 1050*y^5, -420*y^5], domain=P), '1.3a84d6a0.f85236d4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([37*x^6 + 699*x^5*y + 3955*x^4*y^2 + 3345*x^3*y^3 - 24152*x^2*y^4 - 29244*x*y^5 + 5040*y^6, 5040*y^6], domain=P), '1.ba7ac639.1dcad66b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([17*x^7 - 70*x^6*y - 469*x^5*y^2 + 1610*x^4*y^3 + 3668*x^3*y^4 - 7840*x^2*y^5 - 6996*x*y^6 + 2520*y^7, 2520*y^7], domain=P), '1.9f7084a5.a8286a79.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^8 + 21*x^7*y - 161*x^6*y^2 - 651*x^5*y^3 + 2611*x^4*y^4 + 5754*x^3*y^5 - 17574*x^2*y^6 - 10164*x*y^7 + 20160*y^8, 5040*y^8], domain=P), '1.4e61e3fb.dbd77aff.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([16*x^9 - 160*x^8*y + 520*x^7*y^2 - 224*x^6*y^3 - 1799*x^5*y^4 + 2170*x^4*y^5 - 135*x^3*y^6 + 1994*x^2*y^7 + 3918*x*y^8 - 7560*y^9, -2520*y^9], domain=P), '1.bde3b2b5.fd8f0170.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([74*x^10 - 238*x^9*y - 52401*x^8*y^2 - 618552*x^7*y^3 - 699552*x^6*y^4 + 17285898*x^5*y^5 + 37024291*x^4*y^6 - 138284468*x^3*y^7 - 36272412*x^2*y^8 - 8112240*x*y^9 - 129729600*y^10, -129729600*y^10], domain=P), '1.8492f5e2.72686618.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([257*x^11 + 9331*x^10*y + 120130*x^9*y^2 + 579300*x^8*y^3 - 229479*x^7*y^4 - 11442417*x^6*y^5 - 52169780*x^5*y^6 - 128719150*x^4*y^7 + 428342072*x^3*y^8 + 2215246536*x^2*y^9 - 1413900000*x*y^10 - 1037836800*y^11, -518918400*y^11], domain=P), '1.9c7f83c2.66f67e8f.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6847*x^12 - 246252*x^11*y + 2861183*x^10*y^2 - 4657620*x^9*y^3 - 133640139*x^8*y^4 + 716294124*x^7*y^5 + 1338002189*x^6*y^6 - 14257305420*x^5*y^7 + 2892624592*x^4*y^8 + 88929820128*x^3*y^9 - 36791713872*x^2*y^10 - 129870336960*x*y^11 - 108972864000*y^12, -21794572800*y^12], domain=P), '1.385cc0eb.bdd4ef44.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([860*x^13 + 61685*x^12*y + 1906138*x^11*y^2 + 33008833*x^10*y^3 + 347125350*x^9*y^4 + 2213680755*x^8*y^5 + 7633125214*x^7*y^6 + 5859546979*x^6*y^7 - 52599293890*x^5*y^8 - 171757668940*x^4*y^9 - 108558503352*x^3*y^10 + 204127005888*x^2*y^11 + 181197233280*x*y^12 + 6227020800*y^13, -6227020800*y^13], domain=P), '1.647c5692.b6e4705c.1'])
# DoHy2025
dynabase_systems.append([DynamicalSystem([34*x^14 - 5474*x^13*y + 397033*x^12*y^2 - 17145856*x^11*y^3 + 490911421*x^10*y^4 - 9820782972*x^9*y^5 + 140949659279*x^8*y^6 - 1466929231768*x^7*y^7 + 11059905517661*x^6*y^8 - 59702976487154*x^5*y^9 + 225313258722188*x^4*y^10 - 570881108919576*x^3*y^11 + 907090218753984*x^2*y^12 - 796573394467200*x*y^13 + 285901205990400*y^14, 43589145600*y^14], domain=P), '1.73beca44.f064b266.1'])
# DoHy2025
dynabase_systems.append([DynamicalSystem([41*x^15 - 7380*x^14*y + 604100*x^13*y^2 - 29767920*x^12*y^3 + 985137062*x^11*y^4 - 23127063960*x^10*y^5 + 396533008300*x^9*y^6 - 5035984770960*x^8*y^7 + 47529555226153*x^7*y^8 - 331368195898740*x^6*y^9 + 1680182681686600*x^5*y^10 - 6029166612225120*x^4*y^11 + 14653631890929744*x^3*y^12 - 22451626097881920*x^2*y^13 + 19048387680000000*x*y^14 - 6585448117248000*y^15, 1307674368000*y^15], domain=P), '1.470ab850.3e5a5275.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.50d6ba67.3704ee8d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.288635eb.05a208df.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.e1bc189c.600110e2.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.77659db6.f4c36872.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.43808372.c2bd952a.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.9190add3.023ff0b9.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.4dbdab6d.d8496994.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Stoll2008, Hutz2013, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 71/48*y^2, y^2], domain=P), '1.b63253c2.79c27641.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^4 + y^4, y^4], domain=P), '1.ae35600b.b0c27808.1'])
# DoHi2025
dynabase_systems.append([DynamicalSystem([x^6 + ((a - 1))*y^6, y^6], domain=P), '1.9781d019.d2e02e20.1'])

print("Dynabase: 24 dynamical systems in dynabase_systems")
