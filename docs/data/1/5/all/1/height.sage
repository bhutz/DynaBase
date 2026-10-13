# Dynabase (https://dynabase.org): Dimension 1, degree 5 maps over QQ, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 3.6941e-10
dynabase_systems.append([DynamicalSystem([88758966490337*x^5 + 2981527184876307*x^4*y + 11066877636602289*x^3*y^2 - 75987409403569835*x^2*y^3 - 1288812439794810*x*y^4 + 17419787236064304*y^5, 1157006057963*x^5 - 50301712572351*x^4*y - 1971337131131061*x^3*y^2 + 814941375750391*x^2*y^3 + 29505024045162162*x*y^4 + 17419787236064304*y^5], domain=P), '1.92f49ee7.789f9313.1', P(0, 1)])
# Hutz2026; height ratio 3.7088e-10
dynabase_systems.append([DynamicalSystem([360307694*x^5 - 24850051494*x^4*y + 445661486158*x^3*y^2 + 1287816130714*x^2*y^3 - 68914533709032*x*y^4 + 4016025536600*y^5, 224318693*x^5 - 5595423774*x^4*y - 29944225157*x^3*y^2 + 974275081474*x^2*y^3 - 441448123596*x*y^4 + 4016025536600*y^5], domain=P), '1.e6b10276.dc6b6c83.1', P(0, 1)])
# Hutz2026; height ratio 3.7574e-10
dynabase_systems.append([DynamicalSystem([410868324212067295*x^5 - 214908806651361490*x^4*y - 123140623561248668490*x^3*y^2 - 423945106692483245240*x^2*y^3 + 966459488711406110795*x*y^4 - 3269779023770435670*y^5, -31058519941648543*x^5 - 315256851535218746*x^4*y + 8446975942617674502*x^3*y^2 + 16273986690252479876*x^2*y^3 - 3156194582136401159*x*y^4 + 3269779023770435670*y^5], domain=P), '1.8cfc84c3.570110b4.1', P(0, 1)])
# Hutz2026; height ratio 9.1519e-09
dynabase_systems.append([DynamicalSystem([x^5 + 20*x^4*y + 135*x^3*y^2 + 340*x^2*y^3 + 184*x*y^4 + 40*y^5, -40*y^5], domain=P), '1.96a4ba66.02556abd.1', P(0, 1)])
# Hutz2026; height ratio 1.6874e-08
dynabase_systems.append([DynamicalSystem([2*x^5 + 35*x^4*y + 200*x^3*y^2 + 385*x^2*y^3 + 38*x*y^4 + 60*y^5, -60*y^5], domain=P), '1.7578ba72.e29751ce.1', P(0, 1)])
# Hutz2026; height ratio 2.8227e-08
dynabase_systems.append([DynamicalSystem([13*x^5 + 355*x^4*y + 2935*x^3*y^2 + 11405*x^2*y^3 + 64252*x*y^4 - 18480*y^5, 18480*y^5], domain=P), '1.edbe4aa0.f2385e77.1', P(0, 1)])
# FN1997; height ratio 0.021485
dynabase_systems.append([DynamicalSystem([x^5 + x^3*y^2, y^5], domain=P), '1.91738bc3.f35ae2c4.1', P(-1, 1)])
# FN1997, dFH2018; height ratio 0.061259
dynabase_systems.append([DynamicalSystem([x^5 + x*y^4, y^5], domain=P), '1.9583af2a.e586d7b9.1', P(-1, 1)])
# Miasnikov2017, dFH2018; height ratio 0.091155
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.56d48bcf.b239edf6.1', P(-1, 3)])

print("Dynabase: 9 dynamical systems in dynabase_systems")
