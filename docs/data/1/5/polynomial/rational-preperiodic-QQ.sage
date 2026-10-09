# Dynabase (https://dynabase.org): dimension 1, degree 5, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([4*x^5 - 20*x^4*y - 5*x^3*y^2 + 95*x^2*y^3 - 14*x*y^4 - 60*y^5, 30*y^5], domain=P), '1.7189638a.d745bb69.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 45*x^3*y^2 - 199*x*y^4, -210*y^5], domain=P), '1.fd72ba6e.52563e6e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 145*x^3*y^2 + 210*x^2*y^3 + 351*x*y^4 + 525*y^5, 210*y^5], domain=P), '1.ef45669f.812a9ef2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^5 - 5*x^4*y - 140*x^3*y^2 + 320*x^2*y^3 + 2343*x*y^4 - 2520*y^5, -630*y^5], domain=P), '1.a86b32dc.6a1bd5a6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^5 - 35*x^4*y + 180*x^3*y^2 - 205*x^2*y^3 - 302*x*y^4 - 240*y^5, -120*y^5], domain=P), '1.a12e0f3a.3994cb76.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 45*x^3*y^2 + 30*x^2*y^3 + 56*x*y^4 - 30*y^5, 30*y^5], domain=P), '1.fe3e030e.4b3a1f41.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([94*x^5 - 1645*x^4*y + 8720*x^3*y^2 - 10955*x^2*y^3 - 13854*x*y^4 - 2520*y^5, -2520*y^5], domain=P), '1.bf1a9a87.f0139e12.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([172*x^5 - 280*x^4*y - 1175*x^3*y^2 + 1330*x^2*y^3 + 1843*x*y^4 - 1050*y^5, -420*y^5], domain=P), '1.a813d7bb.9d684b8b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([52*x^5 + 60*x^4*y - 305*x^3*y^2 - 45*x^2*y^3 - 242*x*y^4 - 465*y^5, -630*y^5], domain=P), '1.903f8f48.32194ee6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^5 - 10*x^4*y - 5*x^3*y^2 + 100*x^2*y^3 + 34*x*y^4 - 120*y^5, -60*y^5], domain=P), '1.94385621.861dda79.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([181*x^5 - 3340*x^4*y + 19775*x^3*y^2 - 34460*x^2*y^3 - 22476*x*y^4 + 5040*y^5, -5040*y^5], domain=P), '1.da478ea6.b84e5437.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.6f752b35.d8e415c3.1'])
# dFH2018, FN1997
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^5 - 25*x^3*y^2 + 26*x*y^4 + 5*y^5, -10*y^5], domain=P), '1.96a4ba66.02556abd.1'])

print("Dynabase: 14 dynamical systems in dynabase_systems")
