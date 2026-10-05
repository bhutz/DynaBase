# Dynabase (https://dynabase.org): dimension 1, degree 10, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^10 + 5*x^9*y - 210*x^8*y^2 - 870*x^7*y^3 + 15393*x^6*y^4 + 49245*x^5*y^5 - 450640*x^4*y^6 - 984380*x^3*y^7 + 4064256*x^2*y^8 + 4564800*x*y^9 - 1814400*y^10, 1814400*y^10], domain=P), '1.a85d22d5.df507810.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([74*x^10 - 238*x^9*y - 52401*x^8*y^2 - 618552*x^7*y^3 - 699552*x^6*y^4 + 17285898*x^5*y^5 + 37024291*x^4*y^6 - 138284468*x^3*y^7 - 36272412*x^2*y^8 - 8112240*x*y^9 - 129729600*y^10, -129729600*y^10], domain=P), '1.1d4c2bf4.a2235824.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([848*x^10 + 7920*x^9*y - 15400*x^8*y^2 - 154440*x^7*y^3 + 94149*x^6*y^4 + 980595*x^5*y^5 - 255200*x^4*y^6 - 2280960*x^3*y^7 + 353353*x^2*y^8 + 1550835*x*y^9 - 177750*y^10, 207900*y^10], domain=P), '1.337868e8.c6e45913.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([947*x^10 + 20309*x^9*y + 46086*x^8*y^2 - 1515126*x^7*y^3 - 7507773*x^6*y^4 + 38688741*x^5*y^5 + 224543044*x^4*y^6 - 432649604*x^3*y^7 - 2094260544*x^2*y^8 + 1753715520*x*y^9 + 1556755200*y^10, 518918400*y^10], domain=P), '1.83fffd60.85ed5cc4.1'])

print("Dynabase: 4 dynamical systems in dynabase_systems")
