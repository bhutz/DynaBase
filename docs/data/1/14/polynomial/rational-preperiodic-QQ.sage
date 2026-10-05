# Dynabase (https://dynabase.org): dimension 1, degree 14, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([34*x^14 - 5474*x^13*y + 397033*x^12*y^2 - 17145856*x^11*y^3 + 490911421*x^10*y^4 - 9820782972*x^9*y^5 + 140949659279*x^8*y^6 - 1466929231768*x^7*y^7 + 11059905517661*x^6*y^8 - 59702976487154*x^5*y^9 + 225313258722188*x^4*y^10 - 570881108919576*x^3*y^11 + 907090218753984*x^2*y^12 - 796573394467200*x*y^13 + 285901205990400*y^14, 43589145600*y^14], domain=P), '1.1a8d2917.bb444830.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
