# Dynabase (https://dynabase.org): dimension 1, degree 2, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.de450653.9e174cad.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.05f9cf28.88243c92.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.13a1af67.7eb43a7f.1'])
# Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 7/4*y^2, y^2], domain=P), '1.751d2996.7bc729ec.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.8f2b16a9.99353b99.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.1a2a6bbf.1ed2bf82.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.5b15356e.43983826.1'])
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])

K.<a> = NumberField(t^2 - t - 18)  # 2.2.73.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 15/8*y^2, y^2], domain=P), '1.0488c20d.302f679d.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 13/16*y^2, y^2], domain=P), '1.24c682c5.dd0783cf.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 45/16*y^2, y^2], domain=P), '1.73d85ba8.9eb32d83.1'])

K.<a> = NumberField(t^2 - t - 26)  # 2.2.105.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 95/48*y^2, y^2], domain=P), '1.059fb1f3.24824224.1'])

K.<a> = NumberField(t^2 - t + 4)  # 2.0.15.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 31/48*y^2, y^2], domain=P), '1.b6d3146a.3d1df7b5.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 71/48*y^2, y^2], domain=P), '1.e2965d3f.1dd287fe.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.de450653.9e174cad.1'])

K.<a> = NumberField(t^2 - t - 48)  # 2.2.193.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])

K.<a> = NumberField(t^2 - t - 84)  # 2.2.337.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])

K.<a> = NumberField(t^2 - t - 10)  # 2.2.41.1
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])

K.<a> = NumberField(t^2 - t - 14)  # 2.2.57.1
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])

K.<a> = NumberField(t^2 - t + 2)  # 2.0.7.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + 3/16*y^2, y^2], domain=P), '1.7c61fa3f.6fc59844.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 13/16))*y^2, y^2], domain=P), '1.67b1e39b.485999fa.1'])

K.<a> = NumberField(t^2 - t - 18)  # 2.2.73.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + ((1/9*a - 205/144))*y^2, y^2], domain=P), '1.99beb1a1.365246dc.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 273/64*y^2, y^2], domain=P), '1.1ae932e0.c99dfb89.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])

K.<a> = NumberField(t^2 - 10)  # 2.2.40.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.05f9cf28.88243c92.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# DH2025, Doyle2014, Hutz2026, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.7009e2bc.27fbdf16.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 289/144*y^2, y^2], domain=P), '1.0030b10b.d2337b68.1'])
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 40/9*y^2, y^2], domain=P), '1.4c8eac65.66631cbf.1'])
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 37/9*y^2, y^2], domain=P), '1.08dcdb1a.ab8de2eb.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 12*y^2, y^2], domain=P), '1.c885471f.8474b089.1'])

K.<a> = NumberField(t^2 - 10)  # 2.2.40.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 155/72*y^2, y^2], domain=P), '1.2f68bb2c.6da77c52.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])

K.<a> = NumberField(t^2 - 3)  # 2.2.12.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.13a1af67.7eb43a7f.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.e5f33c31.5bededd8.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 3*y^2, y^2], domain=P), '1.a34189c0.fa08537d.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.e9464d8c.638cd9c2.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + 1/5*y^2, y^2], domain=P), '1.a2ec8083.b1a8ea2c.1'])
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 - 4/5*y^2, y^2], domain=P), '1.22725afe.4113354a.1'])

K.<a> = NumberField(t^2 - 3)  # 2.2.12.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Doyle2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.1a2a6bbf.1ed2bf82.1'])

print("Dynabase: 55 dynamical systems in dynabase_systems")
