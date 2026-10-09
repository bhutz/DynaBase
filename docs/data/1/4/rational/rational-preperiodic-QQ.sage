# Dynabase (https://dynabase.org): dimension 1, degree 4, rational maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 48*y^4, 7*x^3*y - 28*x*y^3], domain=P), '1.500a8360.2e13b69c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 3*x^2*y^2 + 4*y^4, 14*x^3*y - 14*x*y^3], domain=P), '1.4aa5dfac.996dac4d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([14*x^3*y - 14*x*y^3, 4*x^4 - 3*x^2*y^2 + 4*y^4], domain=P), '1.6cbefbf4.996dac4d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 7*x^2*y^2 + 16*y^4, 8*x^3*y - 32*x*y^3], domain=P), '1.60bb54a9.c83a38e2.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x^2*y^2 + 4*y^4, -32*x^3*y + 32*x*y^3], domain=P), '1.6b2d80ad.c83a38e2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([148*x^4 + 384*x^3*y - 447*x^2*y^2 - 261*x*y^3 + 20*y^4, -52*x^4 - 134*x^3*y + 38*x^2*y^2 - 184*x*y^3 + 20*y^4], domain=P), '1.b31b924e.d130ecb7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.273dc9f6.ddfc6e2a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([22*x^4 + 9*x^3*y - 109*x^2*y^2 + 234*x*y^3 + 144*y^4, 8*x^4 - 74*x^3*y - 80*x^2*y^2 + 92*x*y^3 - 96*y^4], domain=P), '1.5f6c3257.9610aaf4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([309*x^4 - 1290*x^3*y - 2109*x^2*y^2 + 1794*x*y^3 + 2304*y^4, 161*x^4 - 432*x^3*y - 1679*x^2*y^2 + 870*x*y^3 + 576*y^4], domain=P), '1.4e082e6b.9f635f09.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([245*x^4 - 134*x^3*y - 2879*x^2*y^2 - 2164*x*y^3 + 576*y^4, 59*x^4 + 73*x^3*y - 812*x^2*y^2 - 922*x*y^3 - 576*y^4], domain=P), '1.71cbf504.843422aa.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([222*x^4 + 85*x^3*y - 369*x^2*y^2 - 298*x*y^3 - 60*y^4, 4*x^4 + 258*x^3*y + 93*x^2*y^2 - 185*x*y^3 - 30*y^4], domain=P), '1.dc43b25d.a6ee6b7e.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^4 - 153*x^3*y - 67*x^2*y^2 + 558*x*y^3 + 72*y^4, 8*x^4 - 20*x^3*y + 34*x^2*y^2 - 100*x*y^3 - 72*y^4], domain=P), '1.9d32fd4e.6cd17e03.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([12*x^4 - 9*x^2*y^2 + 12*y^4, 2*x^3*y - 32*x*y^3], domain=P), '1.358ef8b3.946d8ee8.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 15*x^2*y^2 + 48*y^4, 5*x^3*y - 32*x*y^3], domain=P), '1.121aed3a.2520a088.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 15*x^2*y^2 + 48*y^4, 8*x^3*y - 20*x*y^3], domain=P), '1.21cb1754.1d57781b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([7*x^3*y - 7*x*y^3, -x^4 - x^2*y^2 - y^4], domain=P), '1.af2622c4.bf66e92a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([7*x^3*y - 7*x*y^3, x^4 + x^2*y^2 + y^4], domain=P), '1.cd42d8e8.bf66e92a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 + 2*x^2*y^2 + 2*y^4, 7*x^3*y - 7*x*y^3], domain=P), '1.3bbb75a6.230302f6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.12538736.b2ce03ca.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^3*y - 6*x*y^3, 2*x^4 - x^2*y^2 + 2*y^4], domain=P), '1.89109d01.b2ce03ca.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 3*x^3*y + 3*x*y^3], domain=P), '1.59cccd26.79baa0b4.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.3718719e.e6f4a08d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, -6*x^3*y + 9*x*y^3], domain=P), '1.7888bb95.e6f4a08d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^2*y^2 + 16*y^4, 9*x*y^3], domain=P), '1.fafe1b17.4d3f6fcb.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^2*y^2 + 16*y^4, -9*x*y^3], domain=P), '1.e4ffa78b.4d3f6fcb.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, x^3*y + 14*x*y^3], domain=P), '1.6de954c6.1338f81c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^4 + 16*x^3*y + 8*x^2*y^2 + 13*x*y^3 + 21*y^4, 4*x^3*y + 12*x^2*y^2 - 13*x*y^3 - 21*y^4], domain=P), '1.f42cf9b6.cbf33a43.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 16*x^2*y^2 + 32*y^4, 12*x^3*y - 3*x*y^3], domain=P), '1.4ea30318.d65b1f28.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + 14*x*y^3, 2*x^4 - 4*x^2*y^2 + 2*y^4], domain=P), '1.198c8857.e4f64de5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + 14*x*y^3, -2*x^4 + 4*x^2*y^2 - 2*y^4], domain=P), '1.aed903b9.e4f64de5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 + 2*x^2*y^2 + 6*y^4, 16*x^3*y - 9*x*y^3], domain=P), '1.8aa8f55f.004d3689.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + x*y^3, x^4 - 3*x^2*y^2 + y^4], domain=P), '1.f2dcc3c9.d757e35b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 2*x^3*y - 3*x*y^3], domain=P), '1.32472edd.2666fe40.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 3*x^2*y^2 + y^4, -x^3*y - x*y^3], domain=P), '1.e3ea824f.d757e35b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -2*x^3*y + 3*x*y^3], domain=P), '1.829772e7.2666fe40.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.c0038ecf.279cf350.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, 4*x^3*y - x*y^3], domain=P), '1.f5411a05.0c03828b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 3*x^3*y - 2*x*y^3], domain=P), '1.4d73e1db.dc52989b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -3*x^3*y + 2*x*y^3], domain=P), '1.ecae62ce.dc52989b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, 4*x^3*y - x*y^3], domain=P), '1.5f57b4f3.d1087fd5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, -4*x^3*y + x*y^3], domain=P), '1.2723d613.d1087fd5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, x^3*y - 4*x*y^3], domain=P), '1.821069b9.2ba5042d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^4 - 12*x^2*y^2 + 9*y^4, 8*x^3*y - 2*x*y^3], domain=P), '1.37aeafa2.f9359303.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 5*x^2*y^2 + 4*y^4, -5*x^3*y + 8*x*y^3], domain=P), '1.88fcc1f7.94e3619d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x*y^3, -4*x^4 - 4*y^4], domain=P), '1.9b2c8616.14c83dd2.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 8*x*y^3, -8*x^3*y - y^4], domain=P), '1.16ec9a5a.c342a6d9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 5*x*y^3, -5*x^3*y + 2*y^4], domain=P), '1.fe12a0a5.46354713.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - x^3*y + 5*x^2*y^2 + 23*x*y^3 - 14*y^4, 2*x^4 - 4*x^3*y + 13*x^2*y^2 - 11*x*y^3], domain=P), '1.c5501a61.6ac9e05c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 11*x*y^3, 11*x^3*y + 4*y^4], domain=P), '1.32e85428.b2963fd5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.25a234f7.9d083e3e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^3*y - 3*x*y^3, x^4 + y^4], domain=P), '1.4529be27.09bcaf9f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, 2*x^3*y - 8*x*y^3], domain=P), '1.b8a1712a.9c337ce8.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + y^4, -x^3*y - 5*x*y^3], domain=P), '1.dd747faf.06790b53.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 9*x*y^3], domain=P), '1.9b232cfe.b342f2fd.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 3*x^3*y - 5*x^2*y^2 - 14*x*y^3 + 9*y^4, x^3*y + 3*x^2*y^2 + 2*x*y^3], domain=P), '1.0d5a00f6.efe3ae44.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 2*x^3*y - 5*x*y^3], domain=P), '1.85e22016.d2b8d77d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + 16*y^4, 9*x^3*y - 18*x*y^3], domain=P), '1.48e5db6b.4e21c9bb.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 24*x*y^3, 4*x^3*y - 3*y^4], domain=P), '1.e9032acd.ef9d4b14.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([36*x^4 + 50*x*y^3, -15*x^3*y - 36*y^4], domain=P), '1.d1af118d.860b388d.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, 2*x^3*y], domain=P), '1.9f4b8995.c1399402.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, -x^3*y + y^4], domain=P), '1.07bff554.9ff476b6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 3*x*y^3, x^3*y - y^4], domain=P), '1.01973d29.9891742e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x*y^3, 2*x^3*y - 4*y^4], domain=P), '1.fea306ba.afe5fc79.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x^3*y - x*y^3], domain=P), '1.66a11a01.35767842.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, x*y^3], domain=P), '1.30134287.d1fc13ce.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, -x^3*y], domain=P), '1.bec3eb46.3f16aab2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 + 4*x^3*y + 123*x^2*y^2 - 604*x*y^3 - 132*y^4, -10*x^4 - 14*x^3*y + 262*x^2*y^2 + 14*x*y^3 - 132*y^4], domain=P), '1.0efc460c.908765ce.1'])

print("Dynabase: 68 dynamical systems in dynabase_systems")
