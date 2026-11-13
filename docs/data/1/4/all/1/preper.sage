# Dynabase (https://dynabase.org): Dimension 1, degree 4 maps over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 48*y^4, 7*x^3*y - 28*x*y^3], domain=P), '1.e9a7d5d9.535c299c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 3*x^2*y^2 + 4*y^4, 14*x^3*y - 14*x*y^3], domain=P), '1.23ec9100.aa83fd0c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([14*x^3*y - 14*x*y^3, 4*x^4 - 3*x^2*y^2 + 4*y^4], domain=P), '1.0b0566a7.aa83fd0c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 7*x^2*y^2 + 16*y^4, 8*x^3*y - 32*x*y^3], domain=P), '1.bd7d6b5e.9431e5ce.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x^2*y^2 + 4*y^4, -32*x^3*y + 32*x*y^3], domain=P), '1.a0e72262.9431e5ce.1'])
# DoHy2025
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^3*y - 13*x^2*y^2 + 14*x*y^3 - 48*y^4, 24*y^4], domain=P), '1.d7abafe1.ada3eacd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^4 - 14*x^3*y - 63*x^2*y^2 + 314*x*y^3, -120*y^4], domain=P), '1.51fa5c1f.3135fa52.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([148*x^4 + 384*x^3*y - 447*x^2*y^2 - 261*x*y^3 + 20*y^4, -52*x^4 - 134*x^3*y + 38*x^2*y^2 - 184*x*y^3 + 20*y^4], domain=P), '1.7c28ca44.71354757.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([12*x^4 + 5*x^3*y + 321*x^2*y^2 + 126*x*y^3 - 104*y^4, -18*x^4 + 6*x^3*y + 98*x^2*y^2 + 80*x*y^3 + 104*y^4], domain=P), '1.e1bc189c.600110e2.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([22*x^4 + 9*x^3*y - 109*x^2*y^2 + 234*x*y^3 + 144*y^4, 8*x^4 - 74*x^3*y - 80*x^2*y^2 + 92*x*y^3 - 96*y^4], domain=P), '1.2e5a49aa.1289e911.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^3*y - 31*x^2*y^2 + 98*x*y^3 + 60*y^4, -60*y^4], domain=P), '1.e5948466.fc4998fd.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([88*x^4 + 827*x^3*y + 332*x^2*y^2 - 1877*x*y^3 + 630*y^4, -14*x^4 - 122*x^3*y - 121*x^2*y^2 - 433*x*y^3 - 630*y^4], domain=P), '1.e27743a5.b699119f.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([245*x^4 - 134*x^3*y - 2879*x^2*y^2 - 2164*x*y^3 + 576*y^4, 59*x^4 + 73*x^3*y - 812*x^2*y^2 - 922*x*y^3 - 576*y^4], domain=P), '1.1b2039e1.05b1cba4.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([222*x^4 + 85*x^3*y - 369*x^2*y^2 - 298*x*y^3 - 60*y^4, 4*x^4 + 258*x^3*y + 93*x^2*y^2 - 185*x*y^3 - 30*y^4], domain=P), '1.c7d197d4.c41d521c.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([40*x^4 - 153*x^3*y - 67*x^2*y^2 + 558*x*y^3 + 72*y^4, 8*x^4 - 20*x^3*y + 34*x^2*y^2 - 100*x*y^3 - 72*y^4], domain=P), '1.67df48b5.07673f24.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([12*x^4 - 9*x^2*y^2 + 12*y^4, 2*x^3*y - 32*x*y^3], domain=P), '1.faa06ece.6915f4b8.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 15*x^2*y^2 + 48*y^4, 5*x^3*y - 32*x*y^3], domain=P), '1.c05dd9b1.6e53d50b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 15*x^2*y^2 + 48*y^4, 8*x^3*y - 20*x*y^3], domain=P), '1.af14f5ef.512bf9ce.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 14*x^3*y - 49*x^2*y^2 - 206*x*y^3 + 240*y^4, 120*y^4], domain=P), '1.fb163bc9.5fcbff70.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([x^4 + 30*x^3*y + 215*x^2*y^2 + 210*x*y^3 - 96*y^4, -120*y^4], domain=P), '1.b0ccbef7.1360fd95.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 - 122*x^3*y + 289*x^2*y^2 + 302*x*y^3 - 240*y^4, 120*y^4], domain=P), '1.f521ae59.cdcf15a3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([7*x^3*y - 7*x*y^3, -x^4 - x^2*y^2 - y^4], domain=P), '1.aaab356d.5f4406bc.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([7*x^3*y - 7*x*y^3, x^4 + x^2*y^2 + y^4], domain=P), '1.6aa10d04.5f4406bc.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 + 2*x^2*y^2 + 2*y^4, 7*x^3*y - 7*x*y^3], domain=P), '1.2f412b5a.d0dead90.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.5c998972.db1b6b2d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^3*y - 6*x*y^3, 2*x^4 - x^2*y^2 + 2*y^4], domain=P), '1.70f344d4.db1b6b2d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - x^2*y^2 + 2*y^4, 3*x^3*y + 3*x*y^3], domain=P), '1.2d84a12a.bd8193e6.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, 6*x^3*y - 9*x*y^3], domain=P), '1.c73dae0e.6876a801.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 2*x^2*y^2 + 4*y^4, -6*x^3*y + 9*x*y^3], domain=P), '1.a67b71e9.6876a801.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^2*y^2 + 16*y^4, 9*x*y^3], domain=P), '1.9a5ade3a.2648e62c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 8*x^2*y^2 + 16*y^4, -9*x*y^3], domain=P), '1.10143af4.2648e62c.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 8*x^2*y^2 + 4*y^4, x^3*y + 14*x*y^3], domain=P), '1.eebfd08d.7e8f9ea5.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^4 + 16*x^3*y + 8*x^2*y^2 + 13*x*y^3 + 21*y^4, 4*x^3*y + 12*x^2*y^2 - 13*x*y^3 - 21*y^4], domain=P), '1.c5c1c622.f44787a2.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 16*x^2*y^2 + 32*y^4, 12*x^3*y - 3*x*y^3], domain=P), '1.458881d5.fb903ca9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + 14*x*y^3, 2*x^4 - 4*x^2*y^2 + 2*y^4], domain=P), '1.222f9154.b6d290ba.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + 14*x*y^3, -2*x^4 + 4*x^2*y^2 - 2*y^4], domain=P), '1.10626fa9.b6d290ba.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 + 2*x^2*y^2 + 6*y^4, 16*x^3*y - 9*x*y^3], domain=P), '1.ee829e04.57ce422a.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3*y + x*y^3, x^4 - 3*x^2*y^2 + y^4], domain=P), '1.d976e1d2.c499eb01.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 2*x^3*y - 3*x*y^3], domain=P), '1.0985cc31.0c8d46fd.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 3*x^2*y^2 + y^4, -x^3*y - x*y^3], domain=P), '1.71b294f6.c499eb01.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -2*x^3*y + 3*x*y^3], domain=P), '1.69897651.0c8d46fd.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.d2a6e9aa.b987b518.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, 4*x^3*y - x*y^3], domain=P), '1.ea865c92.55d9e8bf.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, 3*x^3*y - 2*x*y^3], domain=P), '1.bc79209c.eab2bb20.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 6*x^2*y^2 + 2*y^4, -3*x^3*y + 2*x*y^3], domain=P), '1.6ea61bd7.eab2bb20.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, 4*x^3*y - x*y^3], domain=P), '1.bd35529d.989e2ca9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 - 9*x^2*y^2 + 3*y^4, -4*x^3*y + x*y^3], domain=P), '1.ef0e711b.989e2ca9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([6*x^4 - 18*x^2*y^2 + 6*y^4, x^3*y - 4*x*y^3], domain=P), '1.a24c217f.7aeec491.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([9*x^4 - 12*x^2*y^2 + 9*y^4, 8*x^3*y - 2*x*y^3], domain=P), '1.18280773.071b74c7.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 - 5*x^2*y^2 + 4*y^4, -5*x^3*y + 8*x*y^3], domain=P), '1.6a7e241a.3cbdd493.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([11*x^4 + 30*x^3*y - 95*x^2*y^2 - 150*x*y^3 + 84*y^4, 60*y^4], domain=P), '1.5b167a70.d13145b7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^4 + 6*x^3*y - 67*x^2*y^2 - 186*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.4c2ad5bb.1fa09beb.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.ef32d183.12ccf81e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([17*x*y^3, -4*x^4 - 4*y^4], domain=P), '1.4c81fec1.ffd15634.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 8*x*y^3, -8*x^3*y - y^4], domain=P), '1.4b06563b.80d720a9.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 5*x*y^3, -5*x^3*y + 2*y^4], domain=P), '1.baa23f7b.02a85231.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - x^3*y + 5*x^2*y^2 + 23*x*y^3 - 14*y^4, 2*x^4 - 4*x^3*y + 13*x^2*y^2 - 11*x*y^3], domain=P), '1.c272d291.84f766fa.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 11*x*y^3, 11*x^3*y + 4*y^4], domain=P), '1.4b16004a.d6b2e89b.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, x^3*y - 4*x*y^3], domain=P), '1.ce27f5ac.859ac4e3.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([5*x^3*y - 3*x*y^3, x^4 + y^4], domain=P), '1.3f68a21e.12edb8ea.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 3*y^4, 2*x^3*y - 8*x*y^3], domain=P), '1.59a09e45.21dfc846.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + y^4, -x^3*y - 5*x*y^3], domain=P), '1.7d55e404.2e89cab7.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 9*x*y^3], domain=P), '1.6a29d4c4.a1df6037.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 3*x^3*y - 5*x^2*y^2 - 14*x*y^3 + 9*y^4, x^3*y + 3*x^2*y^2 + 2*x*y^3], domain=P), '1.7630eef3.81ab8ed2.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + 2*y^4, 2*x^3*y - 5*x*y^3], domain=P), '1.4d639824.641c8248.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x^2*y^2 + 16*y^4, 9*x^3*y - 18*x*y^3], domain=P), '1.651c3aae.43f2f91e.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([3*x^4 + 24*x*y^3, 4*x^3*y - 3*y^4], domain=P), '1.288ea69b.80d74562.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([36*x^4 + 50*x*y^3, -15*x^3*y - 36*y^4], domain=P), '1.6690104d.6ae6cc52.1'])
# FN1997, GHJSX2021, Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.9e054174.3f0eaf7a.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.14995048.fcc23423.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.68938348.14eb3256.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.3c83e548.afd51a11.2'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, -x^3*y + y^4], domain=P), '1.2ead3891.699f945f.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([4*x^4 + 7*x*y^3, 2*x^3*y - 4*y^4], domain=P), '1.c699e693.90ce647d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, x^3*y - x*y^3], domain=P), '1.7fa13ba6.9269e1fa.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, x*y^3], domain=P), '1.4c3f8bcd.d64e0b4a.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.7a816f28.3f0eaf7a.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.d5469f32.478a246b.1'])
# FN1997, dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + x*y^3, y^4], domain=P), '1.80c8620b.21534f8d.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + 1/2*x*y^3, y^4], domain=P), '1.de48a9ac.b16d29ae.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^4 + y^4, -x^3*y], domain=P), '1.9c1286ea.6f9092da.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 - 112*x^3*y + 291*x^2*y^2 + 172*x*y^3 + 120*y^4, 120*y^4], domain=P), '1.5e8dcb6e.41954f0a.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([9*x^4 + 4*x^3*y + 123*x^2*y^2 - 604*x*y^3 - 132*y^4, -10*x^4 - 14*x^3*y + 262*x^2*y^2 + 14*x*y^3 - 132*y^4], domain=P), '1.dd20a767.b08ba5a7.1'])

print("Dynabase: 83 dynamical systems in dynabase_systems")
