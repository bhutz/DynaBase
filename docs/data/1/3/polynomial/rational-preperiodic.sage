# Dynabase (https://dynabase.org): dimension 1, degree 3, polynomial maps, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Benedetto2009, DH2025
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 8*x*y^2 - 6*y^3, 3*y^3], domain=P), '1.8559ffe5.347dee9d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 8*x*y^2 - 3*y^3, -3*y^3], domain=P), '1.cd902a24.347dee9d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 37*x*y^2, 12*y^3], domain=P), '1.79ee5a65.0f4c28a2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 24*x^2*y + 11*x*y^2 - 18*y^3, -12*y^3], domain=P), '1.d780f2b1.0f4c28a2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 73*x*y^2, 24*y^3], domain=P), '1.7a8d9186.ba7e61ef.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 36*x^2*y + 35*x*y^2 - 39*y^3, -24*y^3], domain=P), '1.863416b3.ba7e61ef.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 169*x*y^2, 120*y^3], domain=P), '1.0914e46b.014962df.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 15*x^2*y - 94*x*y^2 - 120*y^3, -120*y^3], domain=P), '1.ff7fdce9.014962df.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 151*x*y^2 + 30*y^3, 60*y^3], domain=P), '1.cc9dd188.453dbf8b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 5*x*y^2 - 3*y^3, 3*y^3], domain=P), '1.d4e1d9bd.b6030427.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y - 5*x*y^2, -3*y^3], domain=P), '1.3c3b4962.9789849b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 31*x*y^2 + 6*y^3, 12*y^3], domain=P), '1.94bd291c.95d1a964.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y - 11*x*y^2 - 18*y^3, 12*y^3], domain=P), '1.2c40cb6c.bc0790b1.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 15*x^2*y + 13*x*y^2 - 30*y^3, 30*y^3], domain=P), '1.7b36f59a.95831402.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 15*x^2*y + 13*x*y^2 - 30*y^3, -30*y^3], domain=P), '1.d17acb7c.63e986f1.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 88*x*y^2, 20*y^3], domain=P), '1.ee12426a.efb26159.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, 6*y^3], domain=P), '1.00a8d209.fb578664.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 13*x*y^2, 12*y^3], domain=P), '1.eda89b36.4c6458de.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 10*x*y^2, -12*y^3], domain=P), '1.f8b704d7.4c6458de.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 49*x*y^2, 24*y^3], domain=P), '1.7cfe5367.3d07bd2a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([30*x^3 + 10*x^2*y - 73*x*y^2 - 51*y^3, -51*x^3 - 73*x^2*y + 10*x*y^2 + 30*y^3], domain=P), '1.52685069.30202a88.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 289*x*y^2, 120*y^3], domain=P), '1.c9377ea5.ffb2a57a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 72*x^2*y + 143*x*y^2 - 150*y^3, -120*y^3], domain=P), '1.aca30c10.ffb2a57a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2, 6*y^3], domain=P), '1.2f943509.9f423aad.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 5*x*y^2 - 12*y^3, -6*y^3], domain=P), '1.74f13bd4.f40f7ed9.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 10*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.d5b21280.a4b7fd53.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 12*x^2*y - x*y^2 - 21*y^3, -12*y^3], domain=P), '1.296d565f.20c33639.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 9*x^2*y + x*y^2, -6*y^3], domain=P), '1.9c94c3be.8f280c56.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 19*x*y^2 + 6*y^3, 12*y^3], domain=P), '1.c953bd66.ebeb7ac0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 + 12*x^2*y - 61*x*y^2 - 69*y^3, 24*y^3], domain=P), '1.e61d8484.65d4dcaa.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 21*x^2*y + 56*x*y^2 + 54*y^3, -30*y^3], domain=P), '1.e2ccbdf8.be93fd76.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 21*x^2*y + 116*x*y^2 - 84*y^3, -60*y^3], domain=P), '1.2bd9f383.ea9751b0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y - 71*x*y^2, 60*y^3], domain=P), '1.5d99de76.000c31d9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y - 82*x*y^2 + 72*y^3, -24*y^3], domain=P), '1.54fc67f0.1e4b51b9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, 3*y^3], domain=P), '1.596006ca.582041e4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 5*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.d073ed60.88a37e20.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.e25e3e69.bbc2e348.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.062d6fd4.8aa6fecd.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y + 3*x*y^2 - 9*y^3, 5*y^3], domain=P), '1.8b819948.3ed81102.1'])
# Benedetto2009, Hutz2026
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2 - 6*y^3, 6*y^3], domain=P), '1.1da98dda.1cfac040.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - 11*x*y^2, 6*y^3], domain=P), '1.8873a09e.feb3ffc2.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 11*x*y^2 + 12*y^3, -12*y^3], domain=P), '1.96253f25.4f70736a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 76*x*y^2 - 78*y^3, 30*y^3], domain=P), '1.39cb5615.d8266ebf.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 15*x^2*y - 47*x*y^2, -60*y^3], domain=P), '1.3e7c18e1.86a5f1f4.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 15*x^2*y - 53*x*y^2, -15*y^3], domain=P), '1.127b28ef.d2895030.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 130*x*y^2 - 72*y^3, 48*y^3], domain=P), '1.58e0e473.30035c41.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2 - 4*y^3, -2*y^3], domain=P), '1.6767275a.82516cf9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, 24*y^3], domain=P), '1.5c0a726d.766edf39.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2, -24*y^3], domain=P), '1.c8db720a.766edf39.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 25*x*y^2, 12*y^3], domain=P), '1.184d863d.9f8684f6.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 25*x*y^2, 24*y^3], domain=P), '1.c9f75935.05cf79d3.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 34*x*y^2, 15*y^3], domain=P), '1.1e2b5cc3.42692a0a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 14*x*y^2 + 12*y^3, -15*y^3], domain=P), '1.9f549580.42692a0a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2, 3*y^3], domain=P), '1.930d87c7.62a84f51.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2 - 6*y^3, -6*y^3], domain=P), '1.ae26dd44.18f135b8.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 7/4*x*y^2 + 1/4*y^3, y^3], domain=P), '1.c1e1ae4b.d73171c9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x^2*y - 4*x*y^2, -4*y^3], domain=P), '1.143c76d8.2e93d8f3.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*x*y^2, 12*y^3], domain=P), '1.cd6f9660.7873c9dd.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 12*x^2*y + 32*x*y^2, -15*y^3], domain=P), '1.1e4d1273.5dc5464a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y - 10*x*y^2, -12*y^3], domain=P), '1.7e1c6f61.f94f3b7b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x^2*y + 11*x*y^2 + 12*y^3, -6*y^3], domain=P), '1.57c6ed2f.aa46601a.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 49*x*y^2 + 6*y^3, 30*y^3], domain=P), '1.90fab641.c4a4a8a3.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 18*x^2*y + 35*x*y^2 + 30*y^3, -24*y^3], domain=P), '1.6e125599.2bc4970f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 67*x*y^2, 30*y^3], domain=P), '1.8aa5e8e4.fa972e5e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 118*x*y^2 - 30*y^3, 30*y^3], domain=P), '1.ba669632.1388f678.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 15*x^2*y + 4*x*y^2 + 20*y^3, -20*y^3], domain=P), '1.56efb0a4.f101c3f5.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 18*x^2*y - 43*x*y^2 - 60*y^3, 30*y^3], domain=P), '1.bd2a8de2.6265c653.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.5ac401c2.34c3c88c.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.5b621046.0e8d94e9.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - x*y^2 - 3*y^3, 3*y^3], domain=P), '1.bd42efc7.6176739e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - x*y^2, 3*y^3], domain=P), '1.8aeb464f.0c20066b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2, -3*y^3], domain=P), '1.4f2ccba6.7a3e142f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y + x*y^2 - 3*y^3, -3*y^3], domain=P), '1.9f695940.aa1b7dc0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9/4*x*y^2 + 1/2*y^3, y^3], domain=P), '1.daf0cc02.21d9e611.1'])
# AMT2020, Benedetto2009, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.9fcfd25c.91fd0195.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 9*x^2*y + x*y^2 - 6*y^3, 6*y^3], domain=P), '1.9722bcc8.3f1e1a77.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y - 7*x*y^2 - 30*y^3, -30*y^3], domain=P), '1.3e6c85c6.a07c0a70.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 + 6*x^2*y - 41*x*y^2, 15*y^3], domain=P), '1.e21821ae.66818176.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 55*x*y^2 + 18*y^3, 24*y^3], domain=P), '1.a8de819c.37accabd.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.e8bb745c.fe98c06c.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 5*x*y^2, 2*y^3], domain=P), '1.86af38cb.639acb45.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + 2*y^3, 2*y^3], domain=P), '1.cb051a84.cd6fab67.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.d4a34d4b.6a79bec0.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y + 2*x*y^2, 3*y^3], domain=P), '1.5aac8d61.852d660b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([2*x^3 - 5*x*y^2 - 3*y^3, -3*y^3], domain=P), '1.7c4d9da4.cf052ce5.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 9*x^2*y + 16*x*y^2 - 6*y^3, -10*y^3], domain=P), '1.43a9b821.d0442390.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.6502de33.969c7b25.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.194ce1a9.8660b31e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([7*x^3 + 21*x^2*y - 4*x*y^2 - 18*y^3, 6*y^3], domain=P), '1.10af2e63.d5d4442d.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 10*y^3], domain=P), '1.8f2b80e6.c0500433.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 12*x*y^2 + 4*y^3, 5*y^3], domain=P), '1.9f5ab3b9.1d588276.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 9*x*y^2, -10*y^3], domain=P), '1.56de700a.098d271b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 9*x^2*y + 10*y^3, -10*y^3], domain=P), '1.44d31e0e.f2c2067f.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - x*y^2 + y^3, y^3], domain=P), '1.b00ed9b9.04728702.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -y^3], domain=P), '1.7131a09e.8573ce82.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([4*x^3 - 5*x*y^2 - 4*y^3, -4*y^3], domain=P), '1.34f852bb.e2925272.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.0e5bf0af.6c3e1388.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 2*x*y^2, 2*y^3], domain=P), '1.721c6bfd.9ba98839.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 6*x^2*y + 13*x*y^2, -10*y^3], domain=P), '1.7b2113e3.48912438.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.7e36c441.20e2ac14.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x^2*y, -y^3], domain=P), '1.facf0049.688d3315.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 2*x*y^2 + 2*y^3, y^3], domain=P), '1.f1d8a4f8.0c07551b.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + x*y^2 + y^3, y^3], domain=P), '1.0055c590.ed64de1e.1'])
# Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + y^3, y^3], domain=P), '1.9a82bd54.3667f7d9.1'])

print("Dynabase: 104 dynamical systems in dynabase_systems")
