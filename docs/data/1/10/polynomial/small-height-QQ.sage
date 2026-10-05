# Dynabase (https://dynabase.org): dimension 1, degree 10, polynomial maps, Small Height Ratio, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 9.9368e-16
dynabase_systems.append([DynamicalSystem([947*x^10 - 64921*x^9*y + 1852872*x^8*y^2 - 28455834*x^7*y^3 + 253612359*x^6*y^4 - 1317059289*x^5*y^5 + 3771140518*x^4*y^6 - 4957186196*x^3*y^7 - 134718696*x^2*y^8 + 8118980640*x*y^9 - 518918400*y^10, 518918400*y^10], domain=P), '1.83fffd60.85ed5cc4.1', P(0, 1)])
# Hutz2026; height ratio 1.3982e-15
dynabase_systems.append([DynamicalSystem([1693*x^10 - 99895*x^9*y + 2473620*x^8*y^2 - 33498870*x^7*y^3 + 271133409*x^6*y^4 - 1340481495*x^5*y^5 + 3879555830*x^4*y^6 - 5322410780*x^3*y^7 - 261276552*x^2*y^8 + 5918113440*x*y^9 + 518918400*y^10, 518918400*y^10], domain=P), '1.c09c892e.c59aad96.1', P(0, 1)])
# Hutz2026; height ratio 1.5071e-15
dynabase_systems.append([DynamicalSystem([134*x^10 - 8944*x^9*y + 251367*x^8*y^2 - 3840972*x^7*y^3 + 34202868*x^6*y^4 - 174460944*x^5*y^5 + 446397643*x^4*y^6 - 274381508*x^3*y^7 - 766257132*x^2*y^8 + 686205648*x*y^9 - 51891840*y^10, -51891840*y^10], domain=P), '1.75baf259.5930340d.1', P(0, 1)])

print("Dynabase: 3 dynamical systems in dynabase_systems")
