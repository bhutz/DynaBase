# Dynabase (https://dynabase.org): Summary of Extreme Examples, long rational tails, polynomial maps over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

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
# DH2025
dynabase_systems.append([DynamicalSystem([34*x^14 - 5474*x^13*y + 397033*x^12*y^2 - 17145856*x^11*y^3 + 490911421*x^10*y^4 - 9820782972*x^9*y^5 + 140949659279*x^8*y^6 - 1466929231768*x^7*y^7 + 11059905517661*x^6*y^8 - 59702976487154*x^5*y^9 + 225313258722188*x^4*y^10 - 570881108919576*x^3*y^11 + 907090218753984*x^2*y^12 - 796573394467200*x*y^13 + 285901205990400*y^14, 43589145600*y^14], domain=P), '1.1a8d2917.bb444830.1'])
# DH2025
dynabase_systems.append([DynamicalSystem([41*x^15 - 7380*x^14*y + 604100*x^13*y^2 - 29767920*x^12*y^3 + 985137062*x^11*y^4 - 23127063960*x^10*y^5 + 396533008300*x^9*y^6 - 5035984770960*x^8*y^7 + 47529555226153*x^7*y^8 - 331368195898740*x^6*y^9 + 1680182681686600*x^5*y^10 - 6029166612225120*x^4*y^11 + 14653631890929744*x^3*y^12 - 22451626097881920*x^2*y^13 + 19048387680000000*x*y^14 - 6585448117248000*y^15, 1307674368000*y^15], domain=P), '1.231a24d2.127a62ff.1'])

print("Dynabase: 14 dynamical systems in dynabase_systems")
