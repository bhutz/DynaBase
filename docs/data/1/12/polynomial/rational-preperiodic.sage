# Dynabase (https://dynabase.org): dimension 1, degree 12, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^12 - 126*x^11*y + 7049*x^10*y^2 - 230790*x^9*y^3 + 4906023*x^8*y^4 - 70986258*x^7*y^5 + 712405427*x^6*y^6 - 4956342930*x^5*y^7 + 23477770876*x^4*y^8 - 72861245016*x^3*y^9 + 138251771424*x^2*y^10 - 140949607680*x*y^11 + 57131827200*y^12, 43545600*y^12], domain=P), '1.65b18f53.f836f322.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6847*x^12 - 246252*x^11*y + 2861183*x^10*y^2 - 4657620*x^9*y^3 - 133640139*x^8*y^4 + 716294124*x^7*y^5 + 1338002189*x^6*y^6 - 14257305420*x^5*y^7 + 2892624592*x^4*y^8 + 88929820128*x^3*y^9 - 36791713872*x^2*y^10 - 129870336960*x*y^11 - 108972864000*y^12, -21794572800*y^12], domain=P), '1.ccc4811b.487121f5.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([16391*x^12 - 673482*x^11*y + 10411807*x^10*y^2 - 67309050*x^9*y^3 + 35206113*x^8*y^4 + 1753977834*x^7*y^5 - 7131900059*x^6*y^6 - 4268681790*x^5*y^7 + 73986295796*x^4*y^8 - 74922917352*x^3*y^9 - 197667466848*x^2*y^10 + 164683895040*x*y^11 - 130767436800*y^12, -43589145600*y^12], domain=P), '1.230c5630.2a3260b6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([1592279639*x^12 + 3158737074*x^11*y - 642202438277*x^10*y^2 + 1327021417038*x^9*y^3 + 74225487274905*x^8*y^4 - 344961191466810*x^7*y^5 - 2329858471035263*x^6*y^6 + 16712209649304162*x^5*y^7 - 14142180837380044*x^4*y^8 - 57001311415764264*x^3*y^9 + 55257305950787040*x^2*y^10 - 27370257381331200*x*y^11 + 9714712879872000*y^12, 9714712879872000*y^12], domain=P), '1.31a79e92.1ce88c1b.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
