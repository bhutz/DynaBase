# Dynabase (https://dynabase.org): dimension 1, degree 4, rational maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 2.1843e-08
dynabase_systems.append([DynamicalSystem([49*x^4 + 844*x^3*y + 4499*x^2*y^2 + 7364*x*y^3 - 660*y^4, -10*x^4 - 174*x^3*y - 866*x^2*y^2 - 1122*x*y^3 + 660*y^4], domain=P), '1.0efc460c.908765ce.1', P(0, 1)])
# Hutz2026; height ratio 2.6346e-08
dynabase_systems.append([DynamicalSystem([91*x^4 + 428*x^3*y - 2133*x^2*y^2 - 4922*x*y^3 - 184*y^4, 60*x^4 - 236*x^3*y - 674*x^2*y^2 + 194*x*y^3 - 184*y^4], domain=P), '1.81431a6a.d4fbfcee.1', P(0, 1)])
# Hutz2026; height ratio 2.9735e-08
dynabase_systems.append([DynamicalSystem([182*x^4 + 1323*x^3*y + 2023*x^2*y^2 + 717*x*y^3 + 1755*y^4, -15*x^4 - 36*x^3*y - 30*x^2*y^2 - 1284*x*y^3 - 1755*y^4], domain=P), '1.d1d120cf.91c81eac.1', P(0, 1)])
# GHJSX2021; height ratio 0.016999
dynabase_systems.append([DynamicalSystem([12*x^4 - 15*x^2*y^2 + 12*y^4, 32*x^3*y - 20*x*y^3], domain=P), '1.21cb1754.1d57781b.1', P(-1, 1)])
# GHJSX2021; height ratio 0.020631
dynabase_systems.append([DynamicalSystem([4*x^4 + x^2*y^2 + 4*y^4, 36*x^3*y - 18*x*y^3], domain=P), '1.48e5db6b.4e21c9bb.1', P(-2, 1)])
# GHJSX2021; height ratio 0.020784
dynabase_systems.append([DynamicalSystem([12*x^4 - 15*x^2*y^2 + 12*y^4, 20*x^3*y - 32*x*y^3], domain=P), '1.121aed3a.2520a088.1', P(-1, 1)])
# GHJSX2021; height ratio 0.021616
dynabase_systems.append([DynamicalSystem([x^4 + y^4, -x^3*y], domain=P), '1.bec3eb46.3f16aab2.1', P(-1, 1)])
# GHJSX2021; height ratio 0.023346
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 9*x*y^3], domain=P), '1.9b232cfe.b342f2fd.1', P(-1, 2)])
# GHJSX2021; height ratio 0.0234
dynabase_systems.append([DynamicalSystem([36*x^4 - 15*x*y^3, -50*x^3*y + 36*y^4], domain=P), '1.d1af118d.860b388d.1', P(-1, 2)])
# GHJSX2021; height ratio 0.024629
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, x^3*y - 4*x*y^3], domain=P), '1.821069b9.2ba5042d.1', P(-3, 2)])
# GHJSX2021; height ratio 0.025856
dynabase_systems.append([DynamicalSystem([6*x^4 + 2*x^2*y^2 + 6*y^4, 16*x^3*y - 9*x*y^3], domain=P), '1.8aa8f55f.004d3689.1', P(-3, 1)])
# GHJSX2021; height ratio 0.026425
dynabase_systems.append([DynamicalSystem([12*x^4 - 9*x^2*y^2 + 12*y^4, 28*x^3*y - 28*x*y^3], domain=P), '1.500a8360.2e13b69c.1', P(-1, 4)])
# GHJSX2021; height ratio 0.02817
dynabase_systems.append([DynamicalSystem([4*x^4 - 3*x^2*y^2 + 4*y^4, 14*x^3*y - 14*x*y^3], domain=P), '1.4aa5dfac.996dac4d.1', P(-1, 4)])
# GHJSX2021; height ratio 0.029228
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, 4*x^3*y - x*y^3], domain=P), '1.f5411a05.0c03828b.1', P(-2, 3)])
# GHJSX2021; height ratio 0.030736
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, 4*x^3*y - x*y^3], domain=P), '1.5f57b4f3.d1087fd5.1', P(-3, 1)])
# GHJSX2021; height ratio 0.031919
dynabase_systems.append([DynamicalSystem([12*x^4 - 9*x^2*y^2 + 12*y^4, 2*x^3*y - 32*x*y^3], domain=P), '1.358ef8b3.946d8ee8.1', P(-2, 1)])
# GHJSX2021; height ratio 0.033285
dynabase_systems.append([DynamicalSystem([10*x^4 - 17*x*y^3, -17*x^3*y + 10*y^4], domain=P), '1.c5501a61.6ac9e05c.1', P(-2, 5)])
# GHJSX2021; height ratio 0.034519
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x*y^3], domain=P), '1.e79e32b0.e63120a1.1', P(-1, 1)])
# GHJSX2021; height ratio 0.035255
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, -4*x^3*y + x*y^3], domain=P), '1.2723d613.d1087fd5.1', P(-3, 1)])
# GHJSX2021; height ratio 0.036063
dynabase_systems.append([DynamicalSystem([4*x^4 - 3*x^2*y^2 + 4*y^4, -14*x^3*y + 14*x*y^3], domain=P), '1.6cbefbf4.996dac4d.1', P(-1, 4)])
# GHJSX2021; height ratio 0.036756
dynabase_systems.append([DynamicalSystem([9*x^4 - 12*x^2*y^2 + 9*y^4, 8*x^3*y - 2*x*y^3], domain=P), '1.37aeafa2.f9359303.1', P(-2, 1)])
# GHJSX2021; height ratio 0.039059
dynabase_systems.append([DynamicalSystem([4*x^4 + 4*y^4, -17*x^3*y], domain=P), '1.9b2c8616.14c83dd2.1', P(-1, 1)])
# GHJSX2021; height ratio 0.039516
dynabase_systems.append([DynamicalSystem([8*x^4 - 16*x^2*y^2 + 8*y^4, 48*x^3*y - 3*x*y^3], domain=P), '1.4ea30318.d65b1f28.1', P(-4, 1)])
# GHJSX2021; height ratio 0.039835
dynabase_systems.append([DynamicalSystem([4*x^4 + 2*x*y^3, -7*x^3*y + 4*y^4], domain=P), '1.fea306ba.afe5fc79.1', P(1, 2)])
# GHJSX2021; height ratio 0.040699
dynabase_systems.append([DynamicalSystem([4*x^4 - 5*x^2*y^2 + 4*y^4, -5*x^3*y + 8*x*y^3], domain=P), '1.88fcc1f7.94e3619d.1', P(-3, 2)])
# GHJSX2021; height ratio 0.041602
dynabase_systems.append([DynamicalSystem([2*x^4 + 2*x^2*y^2 + 2*y^4, 7*x^3*y - 7*x*y^3], domain=P), '1.3bbb75a6.230302f6.1', P(-1, 3)])
# GHJSX2021; height ratio 0.042333
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, -14*x^3*y - x*y^3], domain=P), '1.aed903b9.e4f64de5.1', P(-1, 4)])
# GHJSX2021; height ratio 0.043013
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x^2*y^2 + 4*y^4, 32*x^3*y - 32*x*y^3], domain=P), '1.60bb54a9.c83a38e2.1', P(-2, 7)])
# GHJSX2021; height ratio 0.045888
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -3*x^3*y + 2*x*y^3], domain=P), '1.ecae62ce.dc52989b.1', P(-2, 3)])
# GHJSX2021; height ratio 0.046004
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 2*x^3*y - 5*x*y^3], domain=P), '1.85e22016.d2b8d77d.1', P(-2, 1)])
# GHJSX2021; height ratio 0.047328
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 14*x^3*y + x*y^3], domain=P), '1.198c8857.e4f64de5.1', P(-1, 4)])
# GHJSX2021; height ratio 0.047332
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, x^3*y + 14*x*y^3], domain=P), '1.6de954c6.1338f81c.1', P(-1, 2)])
# GHJSX2021; height ratio 0.048293
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.c0038ecf.279cf350.1', P(-1, 3)])
# GHJSX2021; height ratio 0.051136
dynabase_systems.append([DynamicalSystem([3*x^4 + 4*x*y^3, -24*x^3*y + 3*y^4], domain=P), '1.e9032acd.ef9d4b14.1', P(2, 1)])
# GHJSX2021; height ratio 0.051917
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -2*x^3*y + 3*x*y^3], domain=P), '1.829772e7.2666fe40.1', P(-3, 2)])
# GHJSX2021; height ratio 0.053382
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + y^4, 7*x^3*y - 7*x*y^3], domain=P), '1.af2622c4.bf66e92a.1', P(-1, 3)])
# GHJSX2021; height ratio 0.053669
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, 4*x^3*y - x*y^3], domain=P), '1.0d5a00f6.efe3ae44.1', P(-2, 1)])
# GHJSX2021; height ratio 0.053785
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x^2*y^2 + 4*y^4, -32*x^3*y + 32*x*y^3], domain=P), '1.6b2d80ad.c83a38e2.1', P(-2, 7)])
# GHJSX2021; height ratio 0.054324
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 3*x^3*y - 2*x*y^3], domain=P), '1.4d73e1db.dc52989b.1', P(-2, 3)])
# GHJSX2021; height ratio 0.061166
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.25a234f7.9d083e3e.1', P(-1, 2)])
# GHJSX2021; height ratio 0.061936
dynabase_systems.append([DynamicalSystem([4*x^4 + 11*x*y^3, 11*x^3*y + 4*y^4], domain=P), '1.32e85428.b2963fd5.1', P(-1, 4)])
# GHJSX2021; height ratio 0.062037
dynabase_systems.append([DynamicalSystem([x^4 - 8*x*y^3, -8*x^3*y + y^4], domain=P), '1.16ec9a5a.c342a6d9.1', P(-2, 5)])
# GHJSX2021; height ratio 0.063153
dynabase_systems.append([DynamicalSystem([5*x^4 - 10*x^2*y^2 + 5*y^4, 4*x^3*y - 25*x*y^3], domain=P), '1.f42cf9b6.cbf33a43.1', P(-1, 2)])
# GHJSX2021; height ratio 0.06381
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + y^4, -7*x^3*y + 7*x*y^3], domain=P), '1.cd42d8e8.bf66e92a.1', P(-1, 3)])
# GHJSX2021; height ratio 0.06918
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, 2*x^3*y - 8*x*y^3], domain=P), '1.b8a1712a.9c337ce8.1', P(-3, 1)])
# GHJSX2021; height ratio 0.071287
dynabase_systems.append([DynamicalSystem([x^4 - 3*x^2*y^2 + y^4, x^3*y + x*y^3], domain=P), '1.f2dcc3c9.d757e35b.1', P(-1, 3)])
# GHJSX2021; height ratio 0.076458
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 2*x^3*y - 3*x*y^3], domain=P), '1.32472edd.2666fe40.1', P(-3, 2)])
# GHJSX2021; height ratio 0.077314
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x^3*y], domain=P), '1.44b04e71.3f16aab2.1', P(-1, 1)])
# GHJSX2021; height ratio 0.078198
dynabase_systems.append([DynamicalSystem([x^4 + y^4, -3*x^3*y + 5*x*y^3], domain=P), '1.4529be27.09bcaf9f.1', P(-2, 1)])
# GHJSX2021; height ratio 0.080008
dynabase_systems.append([DynamicalSystem([x^4 - 3*x^2*y^2 + y^4, -x^3*y - x*y^3], domain=P), '1.e3ea824f.d757e35b.1', P(-1, 3)])
# GHJSX2021; height ratio 0.08189
dynabase_systems.append([DynamicalSystem([2*x^4 - 5*x*y^3, -5*x^3*y + 2*y^4], domain=P), '1.fe12a0a5.46354713.1', P(2, 3)])
# GHJSX2021; height ratio 0.081937
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.12538736.b2ce03ca.1', P(-3, 1)])
# GHJSX2021; height ratio 0.086754
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + y^4, -x^3*y - 5*x*y^3], domain=P), '1.dd747faf.06790b53.1', P(-4, 1)])
# GHJSX2021; height ratio 0.089502
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, x*y^3], domain=P), '1.30134287.d1fc13ce.1', P(-1, 2)])
# GHJSX2021; height ratio 0.094403
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, -6*x^3*y + 9*x*y^3], domain=P), '1.7888bb95.e6f4a08d.1', P(-1, 4)])
# GHJSX2021; height ratio 0.10723
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, -6*x^3*y + 9*x*y^3], domain=P), '1.89109d01.b2ce03ca.1', P(-3, 1)])
# GHJSX2021; height ratio 0.11127
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, 9*x*y^3], domain=P), '1.fafe1b17.4d3f6fcb.1', P(-3, 2)])
# GHJSX2021; height ratio 0.13901
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, -9*x*y^3], domain=P), '1.e4ffa78b.4d3f6fcb.1', P(-3, 2)])
# GHJSX2021; height ratio 0.1488
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 3*x^3*y + 3*x*y^3], domain=P), '1.59cccd26.79baa0b4.1', P(-1, 3)])
# GHJSX2021; height ratio 0.1709
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.3718719e.e6f4a08d.1', P(-1, 4)])
# GHJSX2021; height ratio 0.23426
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, -3*x^3*y + y^4], domain=P), '1.01973d29.9891742e.1', P(1, 2)])
# GHJSX2021; height ratio 0.34251
dynabase_systems.append([DynamicalSystem([x^4 + y^4, 2*x^3*y], domain=P), '1.9f4b8995.c1399402.1', P(-1, 2)])
# GHJSX2021; height ratio 0.59664
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, -x^3*y + y^4], domain=P), '1.07bff554.9ff476b6.1', P(1, 2)])
# GHJSX2021; height ratio 0.64575
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x^3*y - x*y^3], domain=P), '1.66a11a01.35767842.1', P(-1, 2)])

print("Dynabase: 64 dynamical systems in dynabase_systems")
