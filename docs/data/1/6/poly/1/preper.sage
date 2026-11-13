# Dynabase (https://dynabase.org): Dimension 1, degree 6 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([x^6 + 21*x^5*y + 115*x^4*y^2 - 105*x^3*y^3 - 1556*x^2*y^4 + 84*x*y^5 - 720*y^6, 720*y^6], domain=P), '1.5b4c543b.5e467fb2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^6 + 153*x^5*y + 275*x^4*y^2 - 3105*x^3*y^3 - 7846*x^2*y^4 + 15552*x*y^5 + 20160*y^6, -5040*y^6], domain=P), '1.c6450b5a.b2756a15.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 - 102*x^5*y + 545*x^4*y^2 + 390*x^3*y^3 - 6850*x^2*y^4 + 3492*x*y^5 + 2520*y^6, -2520*y^6], domain=P), '1.2a9b4176.028a2d8e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 18*x^5*y + 100*x^4*y^2 + 120*x^3*y^3 - 731*x^2*y^4 - 2028*x*y^5 + 1260*y^6, 1260*y^6], domain=P), '1.e9f0aabb.5272ae6d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 + 33*x^5*y - 415*x^4*y^2 - 1185*x^3*y^3 + 7250*x^2*y^4 + 7992*x*y^5 - 15120*y^6, -5040*y^6], domain=P), '1.b708150c.9a7f93da.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 15*x^5*y + 55*x^4*y^2 - 75*x^3*y^3 - 416*x^2*y^4 - 300*x*y^5 - 720*y^6, -720*y^6], domain=P), '1.97c26816.0823ad2c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 29*x^5*y + 225*x^4*y^2 + 155*x^3*y^3 - 2386*x^2*y^4 - 664*x*y^5 - 1680*y^6, 1680*y^6], domain=P), '1.b0d30df6.18285eff.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 13*x^5*y + 25*x^4*y^2 - 205*x^3*y^3 - 506*x^2*y^4 + 672*x*y^5 + 480*y^6, 240*y^6], domain=P), '1.1fc1a008.b79eb35b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^6 + 49*x^5*y + 185*x^4*y^2 - 365*x^3*y^3 - 1868*x^2*y^4 + 1156*x*y^5 + 840*y^6, -840*y^6], domain=P), '1.091720b9.2933c009.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([37*x^6 + 699*x^5*y + 3955*x^4*y^2 + 3345*x^3*y^3 - 24152*x^2*y^4 - 29244*x*y^5 + 5040*y^6, 5040*y^6], domain=P), '1.ba7ac639.1dcad66b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([13*x^6 + 289*x^5*y + 2035*x^4*y^2 + 3875*x^3*y^3 - 5408*x^2*y^4 - 4164*x*y^5 + 3360*y^6, 3360*y^6], domain=P), '1.f29915b2.d8ddbeae.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 - x^5*y - 125*x^4*y^2 + 5*x^3*y^3 + 720*x^2*y^4 + 116*x*y^5 - 720*y^6, -240*y^6], domain=P), '1.c32f0bf3.8f696ebb.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([742*x^6 - 19230*x^5*y + 131395*x^4*y^2 + 117540*x^3*y^3 - 2371517*x^2*y^4 - 1359570*x*y^5 + 617760*y^6, -360360*y^6], domain=P), '1.c2054d9e.c70e8919.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([23*x^6 - 61*x^5*y - 740*x^4*y^2 + 1255*x^3*y^3 + 6057*x^2*y^4 - 3414*x*y^5 - 7560*y^6, 2520*y^6], domain=P), '1.04b36a9c.57cc8036.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^6, y^6], domain=P), '1.46c82190.c2bd952a.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.99d40459.e75b5525.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([29*x^6 + 117*x^5*y - 745*x^4*y^2 - 1905*x^3*y^3 + 3236*x^2*y^4 - 732*x*y^5 + 15120*y^6, -5040*y^6], domain=P), '1.1cf30720.ffda36f2.1'])

print("Dynabase: 17 dynamical systems in dynabase_systems")
