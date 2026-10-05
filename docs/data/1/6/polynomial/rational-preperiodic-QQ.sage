# Dynabase (https://dynabase.org): dimension 1, degree 6, polynomial maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025
dynabase_systems.append([DynamicalSystem([x^6 + 21*x^5*y + 115*x^4*y^2 - 105*x^3*y^3 - 1556*x^2*y^4 + 84*x*y^5 - 720*y^6, 720*y^6], domain=P), '1.4958edb5.8af16663.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^6 + 153*x^5*y + 275*x^4*y^2 - 3105*x^3*y^3 - 7846*x^2*y^4 + 15552*x*y^5 + 20160*y^6, -5040*y^6], domain=P), '1.9cb99077.f6e8139d.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 - 102*x^5*y + 545*x^4*y^2 + 390*x^3*y^3 - 6850*x^2*y^4 + 3492*x*y^5 + 2520*y^6, -2520*y^6], domain=P), '1.01a75594.4b1e061e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 18*x^5*y + 100*x^4*y^2 + 120*x^3*y^3 - 731*x^2*y^4 - 2028*x*y^5 + 1260*y^6, 1260*y^6], domain=P), '1.6b7fa4b1.1a0cf570.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 + 33*x^5*y - 415*x^4*y^2 - 1185*x^3*y^3 + 7250*x^2*y^4 + 7992*x*y^5 - 15120*y^6, -5040*y^6], domain=P), '1.015510fb.36f2eb61.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 15*x^5*y + 55*x^4*y^2 - 75*x^3*y^3 - 416*x^2*y^4 - 300*x*y^5 - 720*y^6, -720*y^6], domain=P), '1.57a89876.65bc5558.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 29*x^5*y + 225*x^4*y^2 + 155*x^3*y^3 - 2386*x^2*y^4 - 664*x*y^5 - 1680*y^6, 1680*y^6], domain=P), '1.e759a42f.f95d1922.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^6 + 13*x^5*y + 25*x^4*y^2 - 205*x^3*y^3 - 506*x^2*y^4 + 672*x*y^5 + 480*y^6, 240*y^6], domain=P), '1.b135bc96.0778470f.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^6 + 49*x^5*y + 185*x^4*y^2 - 365*x^3*y^3 - 1868*x^2*y^4 + 1156*x*y^5 + 840*y^6, -840*y^6], domain=P), '1.528048f3.f9472d55.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([19*x^6 + 27*x^5*y - 725*x^4*y^2 - 835*x^3*y^3 + 6586*x^2*y^4 + 3328*x*y^5 - 8400*y^6, -1680*y^6], domain=P), '1.eb941176.6a76c7c8.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([13*x^6 + 289*x^5*y + 2035*x^4*y^2 + 3875*x^3*y^3 - 5408*x^2*y^4 - 4164*x*y^5 + 3360*y^6, 3360*y^6], domain=P), '1.6634aaf5.9a0da828.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x^6 - x^5*y - 125*x^4*y^2 + 5*x^3*y^3 + 720*x^2*y^4 + 116*x*y^5 - 720*y^6, -240*y^6], domain=P), '1.d9db9953.1172d213.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([397*x^6 + 12822*x^5*y + 103285*x^4*y^2 - 259470*x^3*y^3 - 3933002*x^2*y^4 + 1913808*x*y^5 + 2162160*y^6, 1081080*y^6], domain=P), '1.1dbf5dff.1958fc3c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([23*x^6 - 61*x^5*y - 740*x^4*y^2 + 1255*x^3*y^3 + 6057*x^2*y^4 - 3414*x*y^5 - 7560*y^6, 2520*y^6], domain=P), '1.7a21bd00.fd515d2c.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^6 + x*y^5, y^6], domain=P), '1.ab5c2018.5ec8e92f.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([4*x^6 - 55*x^5*y + 170*x^4*y^2 + 95*x^3*y^3 + 666*x^2*y^4 - 2560*x*y^5 - 1680*y^6, 1680*y^6], domain=P), '1.c8900699.e39a2a24.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
