# Dynabase (https://dynabase.org): Summary of Extreme Examples, small canonical heights
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 0.0066042
dynabase_systems.append([DynamicalSystem([x^2 - 7*x*y - 12*y^2, 6*y^2], domain=P), '1.98c91caa.4cf50642.1', P(0, 1)])
# Hutz2026; height ratio 9.2099e-05
dynabase_systems.append([DynamicalSystem([2*x^3 + 21*x^2*y + 25*x*y^2 - 12*y^3, -12*y^3], domain=P), '1.4f511a5c.f031a661.1', P(0, 1)])
# Hutz2026; height ratio 2.9015e-06
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.f2147436.53db7cc0.1', P(0, 1)])
# Hutz2026; height ratio 9.1519e-09
dynabase_systems.append([DynamicalSystem([x^5 + 20*x^4*y + 135*x^3*y^2 + 340*x^2*y^3 + 184*x*y^4 + 40*y^5, -40*y^5], domain=P), '1.96a4ba66.02556abd.1', P(0, 1)])
# Hutz2026; height ratio 2.056e-09
dynabase_systems.append([DynamicalSystem([4*x^6 + 137*x^5*y + 1810*x^4*y^2 + 11295*x^3*y^3 + 32386*x^2*y^4 + 34528*x*y^5 - 1680*y^6, 1680*y^6], domain=P), '1.c8900699.e39a2a24.1', P(0, 1)])
# Hutz2026; height ratio 1.0564e-10
dynabase_systems.append([DynamicalSystem([215*x^7 - 7601*x^6*y + 100973*x^5*y^2 - 610445*x^4*y^3 + 1535960*x^3*y^4 - 546194*x^2*y^5 - 2468748*x*y^6 + 166320*y^7, -166320*y^7], domain=P), '1.f4bd3027.b70022ba.1', P(0, 1)])
# Hutz2026; height ratio 8.771e-13
dynabase_systems.append([DynamicalSystem([55*x^8 + 1846*x^7*y + 18550*x^6*y^2 + 15988*x^5*y^3 - 502775*x^4*y^4 - 21686*x^3*y^5 + 9132810*x^2*y^6 - 12969108*x*y^7 - 2162160*y^8, -2162160*y^8], domain=P), '1.4e7307c9.5ac37621.1', P(0, 1)])
# Hutz2026; height ratio 1.7173e-14
dynabase_systems.append([DynamicalSystem([2393*x^9 + 120789*x^8*y + 2368272*x^7*y^2 + 22132656*x^6*y^3 + 91367367*x^5*y^4 + 43987671*x^4*y^5 - 669797792*x^3*y^6 - 974348316*x^2*y^7 + 1094978160*x*y^8 - 129729600*y^9, 129729600*y^9], domain=P), '1.777af730.f2167d91.1', P(0, 1)])
# Hutz2026; height ratio 9.9368e-16
dynabase_systems.append([DynamicalSystem([947*x^10 - 64921*x^9*y + 1852872*x^8*y^2 - 28455834*x^7*y^3 + 253612359*x^6*y^4 - 1317059289*x^5*y^5 + 3771140518*x^4*y^6 - 4957186196*x^3*y^7 - 134718696*x^2*y^8 + 8118980640*x*y^9 - 518918400*y^10, 518918400*y^10], domain=P), '1.83fffd60.85ed5cc4.1', P(0, 1)])
# Hutz2026; height ratio 7.3446e-17
dynabase_systems.append([DynamicalSystem([141*x^11 + 9219*x^10*y + 251060*x^9*y^2 + 3656820*x^8*y^3 + 30154233*x^7*y^4 + 133154847*x^6*y^5 + 223258230*x^5*y^6 - 332540670*x^4*y^7 - 1468215824*x^3*y^8 - 1620494616*x^2*y^9 - 1639499040*x*y^10 - 518918400*y^11, 518918400*y^11], domain=P), '1.10b0df19.494435eb.1', P(0, 1)])
# Hutz2026; height ratio 5.9715e-19
dynabase_systems.append([DynamicalSystem([1592279639*x^12 + 3158737074*x^11*y - 642202438277*x^10*y^2 + 1327021417038*x^9*y^3 + 74225487274905*x^8*y^4 - 344961191466810*x^7*y^5 - 2329858471035263*x^6*y^6 + 16712209649304162*x^5*y^7 - 14142180837380044*x^4*y^8 - 57001311415764264*x^3*y^9 + 55257305950787040*x^2*y^10 - 27370257381331200*x*y^11 + 9714712879872000*y^12, 9714712879872000*y^12], domain=P), '1.31a79e92.1ce88c1b.1', P(0, 1)])
# Hutz2026; height ratio 0.00046574
dynabase_systems.append([DynamicalSystem([592*x^2 - 3424*x*y + 1024*y^2, 173*x^2 - 536*x*y - 1024*y^2], domain=P), '1.3b026e07.265dfbb0.1', P(0, 1)])
# Hutz2026; height ratio 3.079e-06
dynabase_systems.append([DynamicalSystem([1115*x^3 - 2405*x^2*y - 37855*x*y^2 + 3465*y^3, 201*x^3 + 173*x^2*y + 1907*x*y^2 - 3465*y^3], domain=P), '1.1825f5a3.a46ef689.1', P(0, 1)])
# Hutz2026; height ratio 2.1843e-08
dynabase_systems.append([DynamicalSystem([49*x^4 + 844*x^3*y + 4499*x^2*y^2 + 7364*x*y^3 - 660*y^4, -10*x^4 - 174*x^3*y - 866*x^2*y^2 - 1122*x*y^3 + 660*y^4], domain=P), '1.0efc460c.908765ce.1', P(0, 1)])
# Hutz2026; height ratio 3.6941e-10
dynabase_systems.append([DynamicalSystem([88758966490337*x^5 + 2981527184876307*x^4*y + 11066877636602289*x^3*y^2 - 75987409403569835*x^2*y^3 - 1288812439794810*x*y^4 + 17419787236064304*y^5, 1157006057963*x^5 - 50301712572351*x^4*y - 1971337131131061*x^3*y^2 + 814941375750391*x^2*y^3 + 29505024045162162*x*y^4 + 17419787236064304*y^5], domain=P), '1.92f49ee7.789f9313.1', P(0, 1)])
# dFH2018; height ratio 0.010205
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1', P(-1, 1)])

print("Dynabase: 16 dynamical systems in dynabase_systems")
