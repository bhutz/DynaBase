# Dynabase (https://dynabase.org): dimension 1, degree 2, polynomial maps, Small Height Ratio
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label, point] triples in table order: the map as a DynamicalSystem over the
# field of its table row, its Dynabase label (dimension.sigma1.sigma2.ordinal), and the
# point of smallest known height ratio, a point of the map's domain.
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Hutz2026; height ratio 0.0066042
dynabase_systems.append([DynamicalSystem([x^2 - 7*x*y - 12*y^2, 6*y^2], domain=P), '1.98c91caa.4cf50642.1', P(0, 1)])
# Hutz2026; height ratio 0.01102
dynabase_systems.append([DynamicalSystem([x^2 + 17*x*y - 6*y^2, -6*y^2], domain=P), '1.55c16ffb.e4dc7fdb.1', P(0, 1)])
# Hutz2026; height ratio 0.013458
dynabase_systems.append([DynamicalSystem([5*x^2 - 97*x*y - 756*y^2, -42*y^2], domain=P), '1.5fab3ba3.dc35593e.1', P(0, 1)])
# Doyle2014, Poonen1998; height ratio 0.13902
dynabase_systems.append([DynamicalSystem([9*x^2 - 13*y^2, 9*y^2], domain=P), '1.05f9cf28.88243c92.1', P(-2, 3)])
# Doyle2014, Poonen1998; height ratio 0.14692
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.1a2a6bbf.1ed2bf82.1', P(0, 1)])
# Doyle2014, Poonen1998; height ratio 0.14891
dynabase_systems.append([DynamicalSystem([9*x^2 - 10*y^2, 9*y^2], domain=P), '1.de450653.9e174cad.1', P(-1, 3)])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998; height ratio 0.33333
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1', P(-1, 2)])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998; height ratio 0.37357
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1', P(-2, 1)])
# Doyle2014, Poonen1998; height ratio 0.63093
dynabase_systems.append([DynamicalSystem([4*x^2 - 3*y^2, 4*y^2], domain=P), '1.13a1af67.7eb43a7f.1', P(0, 1)])
# Doyle2014, Poonen1998; height ratio 0.67619
dynabase_systems.append([DynamicalSystem([4*x^2 + y^2, 4*y^2], domain=P), '1.8f2b16a9.99353b99.1', P(-3, 2)])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997; height ratio 1
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1', P(-1, 2)])

print("Dynabase: 11 dynamical systems in dynabase_systems")
