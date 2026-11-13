# Dynabase (https://dynabase.org): Dimension 1, degree 7 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# DoHy2025
dynabase_systems.append([DynamicalSystem([8*x^7 - 28*x^6*y - 154*x^5*y^2 + 455*x^4*y^3 + 1022*x^3*y^4 - 2002*x^2*y^5 - 2451*x*y^6 + 1890*y^7, 630*y^7], domain=P), '1.20ad6e70.d175ad8a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^7 - 35*x^6*y + 161*x^5*y^2 + 70*x^4*y^3 - 1477*x^3*y^4 + 2485*x^2*y^5 - 3726*x*y^6, 2520*y^7], domain=P), '1.25f8aeab.4609f6ef.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^7 - 14*x^6*y - 7*x^5*y^2 + 175*x^4*y^3 - 637*x^3*y^4 + 1099*x^2*y^5 + 4422*x*y^6 - 5040*y^7, -2520*y^7], domain=P), '1.6880f2dd.b715d99b.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^7 + 348*x^6*y + 850*x^5*y^2 - 15*x^4*y^3 - 1535*x^3*y^4 - 18*x^2*y^5 - 930*x*y^6 + 630*y^7, -1260*y^7], domain=P), '1.a297fa9d.e0e0d36c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^7 + 28*x^6*y - 56*x^5*y^2 - 980*x^4*y^3 + 1099*x^3*y^4 + 8512*x^2*y^5 - 8604*x*y^6 - 15120*y^7, 5040*y^7], domain=P), '1.bb3e7de0.a534c9aa.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^7 - 14*x^6*y - 14*x^5*y^2 + 490*x^4*y^3 + 49*x^3*y^4 - 2996*x^2*y^5 - 7596*x*y^6 + 5040*y^7, 5040*y^7], domain=P), '1.621d852a.7cb807b1.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^7 - 77*x^6*y - 301*x^5*y^2 + 2275*x^4*y^3 + 2534*x^3*y^4 - 17318*x^2*y^5 - 7284*x*y^6 + 20160*y^7, 5040*y^7], domain=P), '1.9e3f53d6.24899745.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^7 + 14*x^6*y + 112*x^5*y^2 + 560*x^4*y^3 - 161*x^3*y^4 - 8134*x^2*y^5 - 2472*x*y^6 + 10080*y^7, 5040*y^7], domain=P), '1.189edd9f.ff42d641.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([17*x^7 - 70*x^6*y - 469*x^5*y^2 + 1610*x^4*y^3 + 3668*x^3*y^4 - 7840*x^2*y^5 - 6996*x*y^6 + 2520*y^7, 2520*y^7], domain=P), '1.9f7084a5.a8286a79.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([22*x^7 + 511*x^6*y + 4375*x^5*y^2 + 16765*x^4*y^3 + 27223*x^3*y^4 + 10444*x^2*y^5 - 19020*x*y^6 - 5040*y^7, -5040*y^7], domain=P), '1.a3b4236b.45f9704e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([88*x^7 - 20*x^6*y - 1214*x^5*y^2 + 625*x^4*y^3 + 3382*x^3*y^4 - 3125*x^2*y^5 + 2784*x*y^6 + 2520*y^7, 2520*y^7], domain=P), '1.fc64b028.e81b4491.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([104*x^7 + 132*x^6*y - 1978*x^5*y^2 - 1605*x^4*y^3 + 8756*x^3*y^4 + 2103*x^2*y^5 - 8772*x*y^6 + 2520*y^7, -2520*y^7], domain=P), '1.5e3024cf.95f27299.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([19*x^7 + 189*x^6*y + 133*x^5*y^2 - 2415*x^4*y^3 - 644*x^3*y^4 + 14826*x^2*y^5 - 2028*x*y^6 - 5040*y^7, -5040*y^7], domain=P), '1.4578320f.c67ed8f2.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.4b1ca9ed.023ff0b9.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7 + x^4*y^3, y^7], domain=P), '1.d10cb60c.a191ee94.1'])
# FN1997, dFH2018
dynabase_systems.append([DynamicalSystem([x^7 + x*y^6, y^7], domain=P), '1.48690a94.9c571960.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([215*x^7 - 7601*x^6*y + 100973*x^5*y^2 - 610445*x^4*y^3 + 1535960*x^3*y^4 - 546194*x^2*y^5 - 2468748*x*y^6 + 166320*y^7, -166320*y^7], domain=P), '1.f57e4ba8.b8276089.1'])

print("Dynabase: 17 dynamical systems in dynabase_systems")
