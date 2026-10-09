# Dynabase (https://dynabase.org): Summary of Extreme Examples, many rational preperiodic points
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
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])
# Benedetto2009, DH2025
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 8*x*y^2 - 6*y^3, 3*y^3], domain=P), '1.8559ffe5.347dee9d.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^3*y - 13*x^2*y^2 + 14*x*y^3 - 48*y^4, 24*y^4], domain=P), '1.9f08598a.0f7c5a09.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([4*x^5 - 20*x^4*y - 5*x^3*y^2 + 95*x^2*y^3 - 14*x*y^4 - 60*y^5, 30*y^5], domain=P), '1.7189638a.d745bb69.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^6 + 21*x^5*y + 115*x^4*y^2 - 105*x^3*y^3 - 1556*x^2*y^4 + 84*x*y^5 - 720*y^6, 720*y^6], domain=P), '1.4958edb5.8af16663.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([8*x^7 - 28*x^6*y - 154*x^5*y^2 + 455*x^4*y^3 + 1022*x^3*y^4 - 2002*x^2*y^5 - 2451*x*y^6 + 1890*y^7, 630*y^7], domain=P), '1.b22ecd74.c9c5de79.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^8 + 20*x^7*y + 70*x^6*y^2 - 700*x^5*y^3 - 3731*x^4*y^4 + 6440*x^3*y^5 + 33900*x^2*y^6 - 36000*x*y^7 - 20160*y^8, 20160*y^8], domain=P), '1.ca09c537.11e402ba.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([16*x^9 - 696*x^7*y^2 + 9849*x^5*y^4 - 49219*x^3*y^6 + 57060*x*y^8 - 5670*y^9, 11340*y^9], domain=P), '1.154dea1c.6bbc505d.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^10 + 5*x^9*y - 210*x^8*y^2 - 870*x^7*y^3 + 15393*x^6*y^4 + 49245*x^5*y^5 - 450640*x^4*y^6 - 984380*x^3*y^7 + 4064256*x^2*y^8 + 4564800*x*y^9 - 1814400*y^10, 1814400*y^10], domain=P), '1.a85d22d5.df507810.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^11 - 205*x^9*y^2 + 14883*x^7*y^4 - 451795*x^5*y^6 + 4987516*x^3*y^8 - 8179200*x*y^10 + 3628800*y^11, -3628800*y^11], domain=P), '1.51b560b0.e0f41b07.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^12 - 126*x^11*y + 7049*x^10*y^2 - 230790*x^9*y^3 + 4906023*x^8*y^4 - 70986258*x^7*y^5 + 712405427*x^6*y^6 - 4956342930*x^5*y^7 + 23477770876*x^4*y^8 - 72861245016*x^3*y^9 + 138251771424*x^2*y^10 - 140949607680*x*y^11 + 57131827200*y^12, 43545600*y^12], domain=P), '1.65b18f53.f836f322.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([x^13 - 143*x^12*y + 9178*x^11*y^2 - 349206*x^10*y^3 + 8761753*x^9*y^4 - 152522799*x^8*y^5 + 1886334164*x^7*y^6 - 16681595788*x^6*y^7 + 104670816536*x^5*y^8 - 455629039008*x^4*y^9 + 1320045298208*x^3*y^10 - 2370430947456*x^2*y^11 + 2315049903360*x*y^12 - 907588281600*y^13, -518918400*y^13], domain=P), '1.b40a6a5b.972ad06e.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([34*x^14 - 5474*x^13*y + 397033*x^12*y^2 - 17145856*x^11*y^3 + 490911421*x^10*y^4 - 9820782972*x^9*y^5 + 140949659279*x^8*y^6 - 1466929231768*x^7*y^7 + 11059905517661*x^6*y^8 - 59702976487154*x^5*y^9 + 225313258722188*x^4*y^10 - 570881108919576*x^3*y^11 + 907090218753984*x^2*y^12 - 796573394467200*x*y^13 + 285901205990400*y^14, 43589145600*y^14], domain=P), '1.1a8d2917.bb444830.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([41*x^15 - 7380*x^14*y + 604100*x^13*y^2 - 29767920*x^12*y^3 + 985137062*x^11*y^4 - 23127063960*x^10*y^5 + 396533008300*x^9*y^6 - 5035984770960*x^8*y^7 + 47529555226153*x^7*y^8 - 331368195898740*x^6*y^9 + 1680182681686600*x^5*y^10 - 6029166612225120*x^4*y^11 + 14653631890929744*x^3*y^12 - 22451626097881920*x^2*y^13 + 19048387680000000*x*y^14 - 6585448117248000*y^15, 1307674368000*y^15], domain=P), '1.231a24d2.127a62ff.1'])
# Vishkautsan2026
dynabase_systems.append([DynamicalSystem([x^2 + 5*x*y - 6*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.51af6b72.2a948ef0.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.bb44cfba.16d54f50.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 48*y^4, 7*x^3*y - 28*x*y^3], domain=P), '1.500a8360.2e13b69c.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])

print("Dynabase: 22 dynamical systems in dynabase_systems")
