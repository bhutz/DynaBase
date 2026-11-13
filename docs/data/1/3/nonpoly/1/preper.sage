# Dynabase (https://dynabase.org): Dimension 1, degree 3 non-polynomial maps over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026
dynabase_systems.append([DynamicalSystem([130*x^2*y - 55*x*y^2 - 60*y^3, -36*x^3 - 50*x^2*y + 176*x*y^2 - 60*y^3], domain=P), '1.df73f7e3.c8b68e52.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^3 + 94*x^2*y + 118*x*y^2 - 84*y^3, 33*x^3 + 122*x^2*y - 43*x*y^2 - 42*y^3], domain=P), '1.23310515.89828b23.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([24*x^3 + 12*x^2*y - 39*x*y^2 + 3*y^3, 4*x^3 + 28*x^2*y - 20*x*y^2 + 6*y^3], domain=P), '1.40ab661f.7675a0d5.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([180*x^3 - 564*x^2*y - 48*x*y^2 + 332*y^3, -270*x^3 + 543*x^2*y - 169*x*y^2 - 254*y^3], domain=P), '1.851044e1.1f663fe4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 7*x^2*y - 63*x*y^2 + 20*y^3, 9*x^3 - 62*x^2*y + 33*x*y^2 + 20*y^3], domain=P), '1.396d8710.4799bcbd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([6*x^3 + 8*x^2*y + 2*x*y^2 - 4*y^3, 3*x^3 + 13*x^2*y + 2*x*y^2], domain=P), '1.0cab9c65.83999d8c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, -5*x^2*y + 9*y^3], domain=P), '1.cb2ddf34.1fab61ed.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 + 4*x^2*y - 17*x*y^2 - 4*y^3, -4*x^3 - 17*x^2*y + 4*x*y^2 + 8*y^3], domain=P), '1.2e48b247.1341229c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 + 4*x^2*y - 17*x*y^2 - 4*y^3, 4*x^3 + 17*x^2*y - 4*x*y^2 - 8*y^3], domain=P), '1.e3b3304b.ef0980b0.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^3 - 61*x^2*y - 83*x*y^2 + 90*y^3, -40*x^3 + 15*x^2*y - 5*x*y^2 + 30*y^3], domain=P), '1.47754fb3.5023eca7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([78*x^3 + 72*x^2*y - 182*x*y^2 - 28*y^3, -3*x^3 + 107*x^2*y + 100*x*y^2 - 84*y^3], domain=P), '1.e6b941cb.2c8fc55f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^3 - 13*x*y^2, -6*x^2*y + 12*y^3], domain=P), '1.fe5c56c9.315156a3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 9*x*y^2, -3*x^2*y + 16*y^3], domain=P), '1.446bcc6b.914aefaf.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 10*x*y^2, -7*x^2*y + 4*y^3], domain=P), '1.30a4e40b.2e1b7ac7.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([25*x^3 - 9*x*y^2, 20*x^2*y + 4*y^3], domain=P), '1.30ca5a8e.5233bf57.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 - 17*x*y^2, 7*x^2*y + 2*y^3], domain=P), '1.ca56d2db.723fbe63.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^2*y + 4*y^3, 4*x^3 - 9*x*y^2], domain=P), '1.9e1f6a56.6602bb10.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([10*x^2*y - 4*y^3, -4*x^3 + 7*x*y^2], domain=P), '1.cacd465f.2e52bea6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([18*x^2*y - 8*y^3, -8*x^3 + 23*x*y^2], domain=P), '1.70846b75.080a4685.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([137*x^3 + 28*x^2*y - 203*x*y^2 + 38*y^3, -9*x^3 + 139*x^2*y + 6*x*y^2 - 76*y^3], domain=P), '1.03839239.106c251a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([38*x^3 + 37*x^2*y - 39*x*y^2 - 24*y^3, -8*x^3 + 7*x^2*y - 11*x*y^2 - 12*y^3], domain=P), '1.288635eb.05a208df.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - y^3, -x^3 + 4*x*y^2], domain=P), '1.b854d85b.de842186.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, -8*x^3 + 17*x*y^2], domain=P), '1.f66385b5.192ba677.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, -2*x^3 + 3*x*y^2], domain=P), '1.301a2e07.20831d8d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^2*y - 2*y^3, 2*x^3 - 3*x*y^2], domain=P), '1.fcc3f607.20831d8d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x^2*y - 8*y^3, 8*x^3 - 17*x*y^2], domain=P), '1.fcc3f607.192ba677.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, -x^2*y + 4*y^3], domain=P), '1.6abddfd7.23df4bf1.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 7*x*y^2, 2*x^2*y + y^3], domain=P), '1.83cd9ffd.18bc9b3c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 6*x*y^2, -11*x^2*y + 9*y^3], domain=P), '1.c780aac8.e0f93c0f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^3 - 6*x*y^2, -x^2*y + 4*y^3], domain=P), '1.bc986ef1.4ccf27d5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^3 - 5*x*y^2, -11*x^2*y + 20*y^3], domain=P), '1.5d755733.a40eaf39.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, 11*x^2*y + y^3], domain=P), '1.eb2954a0.12261201.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 + 2*x^2*y - 5*x*y^2 - 4*y^3, -x^2*y - x*y^2 + 2*y^3], domain=P), '1.d6eb442c.9a7037e4.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 - 16*x*y^2, -21*x^2*y + 9*y^3], domain=P), '1.e0382f52.8f41f560.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 - 7*x^2*y - x*y^2 + 6*y^3, 4*x^3 - 6*x^2*y - 10*x*y^2 + 6*y^3], domain=P), '1.6d8636fe.f08756bb.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([14*x^3 + 25*x^2*y - 31*x*y^2 - 10*y^3, 10*x^3 + 31*x^2*y - 25*x*y^2 - 14*y^3], domain=P), '1.0360ace3.4fa14039.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 + 4*x^2*y - 49*x*y^2 - 4*y^3, 4*x^3 + 49*x^2*y - 4*x*y^2 - 4*y^3], domain=P), '1.217564f3.6da5c7bc.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 9*x*y^2, x^2*y + y^3], domain=P), '1.1f9a871a.10249843.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, -x^2*y + 4*y^3], domain=P), '1.0271fc91.b96ab9e0.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 - 5*x*y^2, -2*x^2*y + 2*y^3], domain=P), '1.dc51e2fe.703ffc64.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^3 + 14*x^2*y + x*y^2 - 13*y^3, -2*x^2*y - 4*x*y^2 + 2*y^3], domain=P), '1.d69a66d8.beadd997.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 7*x*y^2, 2*x^2*y + 4*y^3], domain=P), '1.bd015b31.f618e643.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^3 - 14*x*y^2, -11*x^2*y + 8*y^3], domain=P), '1.6ac97a96.24a3f097.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 + x*y^2], domain=P), '1.eef6a2cb.410f1ef9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^2*y - 2*y^3, -2*x^3 + 5*x*y^2], domain=P), '1.63c2025b.0a583959.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^2*y - 4*y^3, -4*x^3 - 11*x*y^2], domain=P), '1.dcc47a76.3b3d4f0f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 + 5*x^2*y - 4*x*y^2 - 7*y^3, -4*x^3 - 6*x^2*y + 12*x*y^2 + 7*y^3], domain=P), '1.89345372.bbb7204f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([8*x^2*y + 4*y^3, 4*x^3 - 7*x*y^2], domain=P), '1.bbfdb589.200b5415.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^2*y + y^3, x^3 - 4*x*y^2], domain=P), '1.5503013d.f4fb9b2e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([16*x^2*y + 10*y^3, 10*x^3 - 13*x*y^2], domain=P), '1.a5ebd0b7.6c1eb7d6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([342*x^3 + y^3, 343*x^2*y], domain=P), '1.0c11f93f.bc9024d3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.fcc3f607.790bef87.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3 - x*y^2], domain=P), '1.0cf9b7d5.e6c6bfb3.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.fcc3f607.790bef87.2'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -x^2*y], domain=P), '1.343beeba.c008598d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^3 + y^3, x^2*y], domain=P), '1.0a23dabf.4a13fe3c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([39*x^2*y - 15*y^3, -15*x^3 + 13*x*y^2], domain=P), '1.3bd9b49b.218d5d8c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.fcc3f607.78dde912.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([658*x^3 - 1545*x^2*y - 3442*x*y^2 + 2025*y^3, 201*x^3 - 215*x^2*y + 541*x*y^2 - 675*y^3], domain=P), '1.3dfdcd07.d1dc886d.1'])

print("Dynabase: 59 dynamical systems in dynabase_systems")
