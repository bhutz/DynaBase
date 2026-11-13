# Dynabase (https://dynabase.org): Dimension 1, degree 3 polynomials over QQ, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Benedetto2009, DoHy2025
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 8*x*y^2 - 6*y^3, 3*y^3], domain=P), '1.a9e0d4b5.1e91cdd4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 8*x*y^2 - 3*y^3, -3*y^3], domain=P), '1.74b9543b.1e91cdd4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 37*x*y^2, 12*y^3], domain=P), '1.9eb167bd.33420087.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 24*x^2*y + 11*x*y^2 - 18*y^3, -12*y^3], domain=P), '1.9804eaa0.33420087.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 73*x*y^2, 24*y^3], domain=P), '1.33e07b79.59ec3e59.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 36*x^2*y + 35*x*y^2 - 39*y^3, -24*y^3], domain=P), '1.7ad3765d.59ec3e59.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 169*x*y^2, 120*y^3], domain=P), '1.60cf1f41.93839f3d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 15*x^2*y - 94*x*y^2 - 120*y^3, -120*y^3], domain=P), '1.d5bb2990.93839f3d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 151*x*y^2 + 30*y^3, 60*y^3], domain=P), '1.c713f014.80ec0177.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 5*x*y^2 - 3*y^3, 3*y^3], domain=P), '1.6c31920d.23659318.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y - 5*x*y^2, -3*y^3], domain=P), '1.8ed28586.c3c96ba2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 31*x*y^2 + 6*y^3, 12*y^3], domain=P), '1.5fa265ca.ad865cba.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y - 11*x*y^2 - 18*y^3, 12*y^3], domain=P), '1.d61ab607.6e78b9a4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 15*x^2*y + 13*x*y^2 - 30*y^3, 30*y^3], domain=P), '1.7333bde9.be966046.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 15*x^2*y + 13*x*y^2 - 30*y^3, -30*y^3], domain=P), '1.bd418e2c.a4db7274.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 88*x*y^2, 20*y^3], domain=P), '1.151edc71.3fd5de43.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, 6*y^3], domain=P), '1.a79bf777.e803e141.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, 12*y^3], domain=P), '1.f77ec7d5.96ba9243.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 10*x*y^2, -12*y^3], domain=P), '1.bd47ba17.96ba9243.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 49*x*y^2, 24*y^3], domain=P), '1.e6e08c6b.4de3c910.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([30*x^3 + 10*x^2*y - 73*x*y^2 - 51*y^3, -51*x^3 - 73*x^2*y + 10*x*y^2 + 30*y^3], domain=P), '1.047b178d.ca430fda.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 289*x*y^2, 120*y^3], domain=P), '1.d3322e60.fe6b480f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 72*x^2*y + 143*x*y^2 - 150*y^3, -120*y^3], domain=P), '1.5895b006.fe6b480f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2, 6*y^3], domain=P), '1.d35164de.5a2d4a89.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 5*x*y^2 - 12*y^3, -6*y^3], domain=P), '1.0af15aa5.e4860b8a.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 10*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.b8af95a9.624cfacf.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 12*x^2*y - x*y^2 - 21*y^3, -12*y^3], domain=P), '1.9311831c.cf7ad5cc.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2, -6*y^3], domain=P), '1.d6971cbf.b2200cbf.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 19*x*y^2 + 6*y^3, 12*y^3], domain=P), '1.9941e270.85003a1f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 12*x^2*y - 61*x*y^2 - 69*y^3, 24*y^3], domain=P), '1.e0cb4159.6b4adfe7.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 21*x^2*y + 56*x*y^2 + 54*y^3, -30*y^3], domain=P), '1.d2313152.1db7b367.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 21*x^2*y + 116*x*y^2 - 84*y^3, -60*y^3], domain=P), '1.1e525da7.7d85bdbd.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y - 71*x*y^2, 60*y^3], domain=P), '1.ec62e512.1527212a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y - 82*x*y^2 + 72*y^3, -24*y^3], domain=P), '1.ec9eaa2b.ae019b43.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, 3*y^3], domain=P), '1.0e0be859.9f04d392.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 5*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.c45dd638.d972c071.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.87c6ae53.890e2ac9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.d8acc9af.32df6876.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y + 3*x*y^2 - 9*y^3, 5*y^3], domain=P), '1.dddef542.8aeff7ce.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.cd59cbfd.2bdca34d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2, 6*y^3], domain=P), '1.dd5f9beb.84d0b34a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 11*x*y^2 + 12*y^3, -12*y^3], domain=P), '1.7c789043.8073331e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 76*x*y^2 - 78*y^3, 30*y^3], domain=P), '1.76f21757.09704162.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 15*x^2*y - 47*x*y^2, -60*y^3], domain=P), '1.63646942.8affd45b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 15*x^2*y - 53*x*y^2, -15*y^3], domain=P), '1.6abb72e3.f196590f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 130*x*y^2 - 72*y^3, 48*y^3], domain=P), '1.7fb8bcc3.886a30f4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 4*y^3, -2*y^3], domain=P), '1.ec71db64.0066809e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, 24*y^3], domain=P), '1.60605974.f661ff4a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, -24*y^3], domain=P), '1.afdc6092.f661ff4a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 25*x*y^2, 12*y^3], domain=P), '1.f6ace77d.6e0c8fc6.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 25*x*y^2, 24*y^3], domain=P), '1.ba05b5e1.4f9d87f6.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 34*x*y^2, 15*y^3], domain=P), '1.32d4db34.b4f711d2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 14*x*y^2 + 12*y^3, -15*y^3], domain=P), '1.a391bfe6.b4f711d2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2, 3*y^3], domain=P), '1.5666a87e.1d985361.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.55f18213.229aab61.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 7/4*x*y^2 + 1/4*y^3, y^3], domain=P), '1.30a66fa1.cce8c7aa.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x^2*y - 4*x*y^2, -4*y^3], domain=P), '1.71877eb4.a78ed56b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2, 12*y^3], domain=P), '1.c05e093e.52b59e97.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y + 32*x*y^2, -15*y^3], domain=P), '1.51d7c810.f53daa91.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y - 10*x*y^2, -12*y^3], domain=P), '1.3843fd20.387af309.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 11*x*y^2 + 12*y^3, -6*y^3], domain=P), '1.a6b1f546.aed3904d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 49*x*y^2 + 6*y^3, 30*y^3], domain=P), '1.0f580613.d8d7bb52.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 18*x^2*y + 35*x*y^2 + 30*y^3, -24*y^3], domain=P), '1.e9735421.93293a6b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 67*x*y^2, 30*y^3], domain=P), '1.7dd05d6e.90c47663.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 118*x*y^2 - 30*y^3, 30*y^3], domain=P), '1.8c34f324.ff87b2cc.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 15*x^2*y + 4*x*y^2 + 20*y^3, -20*y^3], domain=P), '1.719a1fdf.3f0bfdc6.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 18*x^2*y - 43*x*y^2 - 60*y^3, 30*y^3], domain=P), '1.50fb41f1.86a98177.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.2142a8dc.f10f2f86.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.48280c35.4e1a6268.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - x*y^2 - 3*y^3, 3*y^3], domain=P), '1.f14c2462.680953df.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - x*y^2, 3*y^3], domain=P), '1.85c067c0.6b78205b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2, -3*y^3], domain=P), '1.ae9136c5.bc06a773.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2 - 3*y^3, -3*y^3], domain=P), '1.7382ad30.12658370.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9/4*x*y^2 + 1/2*y^3, y^3], domain=P), '1.4b35d28b.633a1882.1'])
# Benedetto2009, Ingram2012, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.8d1d75ce.14532702.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y + x*y^2 - 6*y^3, 6*y^3], domain=P), '1.019f69a4.c8555179.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 7*x*y^2 - 30*y^3, -30*y^3], domain=P), '1.e3427bb2.e2beb76d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 6*x^2*y - 41*x*y^2, 15*y^3], domain=P), '1.4e671526.19a1b895.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 55*x*y^2 + 18*y^3, 24*y^3], domain=P), '1.32aa0f82.f44ebad6.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.da2b6adb.6af3bd89.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 5*x*y^2, 2*y^3], domain=P), '1.e8f34f37.b869fe93.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + 2*y^3, 2*y^3], domain=P), '1.59621430.4a780c14.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.8297d2a5.571fa648.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2, 3*y^3], domain=P), '1.8686294c.9df607e0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 5*x*y^2 - 3*y^3, -3*y^3], domain=P), '1.c44ceb4d.cf082869.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 9*x^2*y + 16*x*y^2 - 6*y^3, -10*y^3], domain=P), '1.eebc2ff8.f1d610d4.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.3204476a.7fdfbb3b.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.fe349f2e.400608e6.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([7*x^3 + 21*x^2*y - 4*x*y^2 - 18*y^3, 6*y^3], domain=P), '1.09c470ea.1adf0fba.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 10*y^3], domain=P), '1.d8f448b3.c9115a8f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x*y^2 + 4*y^3, 5*y^3], domain=P), '1.9c7c5c77.82d8f347.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 9*x*y^2, -10*y^3], domain=P), '1.02e22378.e8ed0b25.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y + 10*y^3, -10*y^3], domain=P), '1.c67b1a1f.27a80360.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + y^3, y^3], domain=P), '1.a05bf936.ba882769.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -y^3], domain=P), '1.6611fe6d.98a8f852.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 - 5*x*y^2 - 4*y^3, -4*y^3], domain=P), '1.d2ec6044.b5fa8d49.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.e5a6937e.9d1e2ff7.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 2*x*y^2, 2*y^3], domain=P), '1.8fa7c1b0.9cdf89a9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 13*x*y^2, -10*y^3], domain=P), '1.8a748cc1.13d3bf64.1'])
# Benedetto2009, AMT2020
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.ad88b95b.f2825a1c.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x^2*y, -y^3], domain=P), '1.d5e44e8e.d6b0130c.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 2*x*y^2 + 2*y^3, y^3], domain=P), '1.79a7edb3.71476f7d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2 + y^3, y^3], domain=P), '1.ecedbdf0.a703bcb0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + y^3, y^3], domain=P), '1.28588048.de1f547a.1'])

print("Dynabase: 104 dynamical systems in dynabase_systems")
