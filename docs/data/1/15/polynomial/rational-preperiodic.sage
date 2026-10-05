# Dynabase (https://dynabase.org): dimension 1, degree 15, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([41*x^15 - 7380*x^14*y + 604100*x^13*y^2 - 29767920*x^12*y^3 + 985137062*x^11*y^4 - 23127063960*x^10*y^5 + 396533008300*x^9*y^6 - 5035984770960*x^8*y^7 + 47529555226153*x^7*y^8 - 331368195898740*x^6*y^9 + 1680182681686600*x^5*y^10 - 6029166612225120*x^4*y^11 + 14653631890929744*x^3*y^12 - 22451626097881920*x^2*y^13 + 19048387680000000*x*y^14 - 6585448117248000*y^15, 1307674368000*y^15], domain=P), '1.231a24d2.127a62ff.1'])

print("Dynabase: 1 dynamical system in dynabase_systems")
