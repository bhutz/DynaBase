# Dynabase (https://dynabase.org): dimension 1, degree 12, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 5.9715e-19
dynabase_systems.append([DynamicalSystem([1592279639*x^12 + 3158737074*x^11*y - 642202438277*x^10*y^2 + 1327021417038*x^9*y^3 + 74225487274905*x^8*y^4 - 344961191466810*x^7*y^5 - 2329858471035263*x^6*y^6 + 16712209649304162*x^5*y^7 - 14142180837380044*x^4*y^8 - 57001311415764264*x^3*y^9 + 55257305950787040*x^2*y^10 - 27370257381331200*x*y^11 + 9714712879872000*y^12, 9714712879872000*y^12], domain=P), '1.31a79e92.1ce88c1b.1', P(0, 1)])
# Hutz2026; height ratio 1.5221e-18
dynabase_systems.append([DynamicalSystem([9849455*x^12 + 105767010*x^11*y - 1373074466*x^10*y^2 - 16841221215*x^9*y^3 + 39874768095*x^8*y^4 + 782892762660*x^7*y^5 + 671008281412*x^6*y^6 - 9411053466555*x^5*y^7 - 12145321075600*x^4*y^8 + 36409735953780*x^3*y^9 + 36074565801504*x^2*y^10 - 34804486810080*x*y^11 + 3519823507200*y^12, -3519823507200*y^12], domain=P), '1.e6e99cfb.f3d6f968.1', P(0, 1)])
# Hutz2026; height ratio 1.7538e-18
dynabase_systems.append([DynamicalSystem([92474035*x^12 + 1913144020*x^11*y - 10253614901*x^10*y^2 - 330265297020*x^9*y^3 + 257992893765*x^8*y^4 + 17994948682620*x^7*y^5 - 4977871704823*x^6*y^6 - 316529046772180*x^5*y^7 + 51234803117300*x^4*y^8 + 1947923012482560*x^3*y^9 - 149752919376576*x^2*y^10 - 3610775530252800*x*y^11 + 206496312422400*y^12, -206496312422400*y^12], domain=P), '1.fc4b78f0.a6c52987.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
