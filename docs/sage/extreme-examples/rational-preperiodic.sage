# Dynabase (https://dynabase.org): Summary of Extreme Examples, rational preperiodic points
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
# Hutz2026
dynabase_systems.append([DynamicalSystem([148*x^4 + 384*x^3*y - 447*x^2*y^2 - 261*x*y^3 + 20*y^4, -52*x^4 - 134*x^3*y + 38*x^2*y^2 - 184*x*y^3 + 20*y^4], domain=P), '1.b31b924e.d130ecb7.1'])
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
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.f087c4af.5b9da8c6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.05af5145.a779cc92.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.273dc9f6.ddfc6e2a.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 71/48*y^2, y^2], domain=P), '1.e2965d3f.1dd287fe.1'])

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 10*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.d5b21280.a4b7fd53.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^4 + 6*x^3*y - 67*x^2*y^2 - 186*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.3387dead.7b560bfc.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([52*x^5 + 60*x^4*y - 305*x^3*y^2 - 45*x^2*y^3 - 242*x*y^4 - 465*y^5, -630*y^5], domain=P), '1.903f8f48.32194ee6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^6 + 49*x^5*y + 185*x^4*y^2 - 365*x^3*y^3 - 1868*x^2*y^4 + 1156*x*y^5 + 840*y^6, -840*y^6], domain=P), '1.528048f3.f9472d55.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^7 - 35*x^6*y + 161*x^5*y^2 + 70*x^4*y^3 - 1477*x^3*y^4 + 2485*x^2*y^5 - 3726*x*y^6, 2520*y^7], domain=P), '1.75e098ac.5edff4e1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^8 - 140*x^7*y + 434*x^6*y^2 + 2296*x^5*y^3 - 10759*x^4*y^4 - 11900*x^3*y^5 + 50636*x^2*y^6 + 90384*x*y^7 - 80640*y^8, -40320*y^8], domain=P), '1.30a427de.0d23e4e3.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([19*x^9 - 326*x^8*y + 1027*x^7*y^2 + 8440*x^6*y^3 - 43145*x^5*y^4 - 57044*x^4*y^5 + 370923*x^3*y^6 + 215250*x^2*y^7 - 162504*x*y^8 - 332640*y^9, 332640*y^9], domain=P), '1.271df9ee.1e432275.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([848*x^10 + 7920*x^9*y - 15400*x^8*y^2 - 154440*x^7*y^3 + 94149*x^6*y^4 + 980595*x^5*y^5 - 255200*x^4*y^6 - 2280960*x^3*y^7 + 353353*x^2*y^8 + 1550835*x*y^9 - 177750*y^10, 207900*y^10], domain=P), '1.337868e8.c6e45913.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2076*x^11 + 66177*x^10*y + 718525*x^9*y^2 + 2134860*x^8*y^3 - 13169922*x^7*y^4 - 90177339*x^6*y^5 - 36287115*x^5*y^6 + 681611190*x^4*y^7 + 1044667796*x^3*y^8 - 853094088*x^2*y^9 - 2812145760*x*y^10 + 2075673600*y^11, -518918400*y^11], domain=P), '1.b6b8895a.3e7242d7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([16391*x^12 - 673482*x^11*y + 10411807*x^10*y^2 - 67309050*x^9*y^3 + 35206113*x^8*y^4 + 1753977834*x^7*y^5 - 7131900059*x^6*y^6 - 4268681790*x^5*y^7 + 73986295796*x^4*y^8 - 74922917352*x^3*y^9 - 197667466848*x^2*y^10 + 164683895040*x*y^11 - 130767436800*y^12, -43589145600*y^12], domain=P), '1.230c5630.2a3260b6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([8354*x^13 + 48151*x^12*y - 1206332*x^11*y^2 - 6298093*x^10*y^3 + 66314652*x^9*y^4 + 304427913*x^8*y^5 - 1745126036*x^7*y^6 - 6746939239*x^6*y^7 + 22669801274*x^5*y^8 + 67817345236*x^4*y^9 - 132792152232*x^3*y^10 - 235725166368*x^2*y^11 + 242569797120*x*y^12, 43589145600*y^13], domain=P), '1.e8d5184a.0f99e138.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([264*x^2 + 291*x*y - 285*y^2, -121*x^2 + 268*x*y + 285*y^2], domain=P), '1.76567776.1f5edaf9.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^3 - 61*x^2*y - 83*x*y^2 + 90*y^3, -40*x^3 + 15*x^2*y - 5*x*y^2 + 30*y^3], domain=P), '1.f786e132.47eb7e99.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([222*x^4 + 85*x^3*y - 369*x^2*y^2 - 298*x*y^3 - 60*y^4, 4*x^4 + 258*x^3*y + 93*x^2*y^2 - 185*x*y^3 - 30*y^4], domain=P), '1.dc43b25d.a6ee6b7e.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 13/16))*y^2, y^2], domain=P), '1.67b1e39b.485999fa.1'])

print("Dynabase: 54 dynamical systems in dynabase_systems")
