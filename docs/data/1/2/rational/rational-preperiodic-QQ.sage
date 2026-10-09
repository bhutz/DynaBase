# Dynabase (https://dynabase.org): dimension 1, degree 2, rational maps, Rational Preperiodic, over QQ
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Vishkautsan2026
dynabase_systems.append([DynamicalSystem([x^2 + 5*x*y - 6*y^2, x^2 + 3*x*y + 2*y^2], domain=P), '1.51af6b72.2a948ef0.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([264*x^2 + 291*x*y - 285*y^2, -121*x^2 + 268*x*y + 285*y^2], domain=P), '1.76567776.1f5edaf9.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([166*x^2 - 4*x*y - 162*y^2, -21*x^2 + 271*x*y + 36*y^2], domain=P), '1.3bd966d6.c0ea849d.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([380*x^2 + 913*x*y - 1878*y^2, 95*x^2 - 583*x*y - 1806*y^2], domain=P), '1.f087c4af.5b9da8c6.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([39*x^2 - x*y - 40*y^2, 66*x^2 - 34*x*y - 30*y^2], domain=P), '1.819f711c.ad6ea102.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([5*x*y - 5*y^2, x^2 - 2*x*y - 5*y^2], domain=P), '1.8c464acc.35c4d3f7.1'])
# Hutz2026
dynabase_systems.append([DynamicalSystem([3*x^2 - 7*x*y - 6*y^2, -4*x*y + 2*y^2], domain=P), '1.64eaa460.a2d15fe7.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([36*x^2 + 47*x*y - 50*y^2, 48*x^2 + 15*x*y - 30*y^2], domain=P), '1.f150f22f.e39c87ba.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([3099*x^2 - 1875*x*y - 4596*y^2, 3522*x^2 + 6310*x*y + 2382*y^2], domain=P), '1.33af6776.1e69f6d5.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([111*x^2 - 688*x*y - 963*y^2, -609*x^2 - 43*x*y + 722*y^2], domain=P), '1.90f9e3df.9b5d59ee.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([6*x^2 + 7*x*y - 5*y^2, -3*x^2 + 6*x*y + 9*y^2], domain=P), '1.3fc6e372.9f1cfbf5.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([12*x^2 + 26*x*y - 30*y^2, -x^2 + 29*x*y + 30*y^2], domain=P), '1.56bec964.82b87ac1.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([137*x^2 - 1957*x*y - 1470*y^2, 127*x^2 + 103*x*y - 1050*y^2], domain=P), '1.879d9c1a.55717e8f.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([145*x^2 - 256*x*y - 9*y^2, 169*x*y + 39*y^2], domain=P), '1.b56f5ad0.9975811c.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([12*x^2 - 94*x*y + 147*y^2, -32*x^2 - 149*x*y - 174*y^2], domain=P), '1.93fa2cae.c5977ee2.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([150*x^2 + 60*x*y - 210*y^2, -117*x^2 + 101*x*y + 210*y^2], domain=P), '1.438f4f1e.836416a0.1'])
# BCHKW2014
dynabase_systems.append([DynamicalSystem([5100*x^2 - 4030*x*y - 9512*y^2, -5440*x^2 - 16743*x*y - 10505*y^2], domain=P), '1.e8e98d01.8bd6f201.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.f87176de.3b08f253.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.c346226f.0c3c179e.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.366a39dc.7475b914.1'])
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.4cc4fb80.ef9cb8b5.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.fbfd6fd4.9888ce4b.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.170a93ef.0fdf09c7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.89eb0e1e.d90eecb7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.095ed92d.7e1406dd.1'])
# BCHKW2014, Hutz2026
dynabase_systems.append([DynamicalSystem([7*x^2 - x*y - 6*y^2, -x^2 + 9*x*y + 6*y^2], domain=P), '1.3b026e07.265dfbb0.1'])

print("Dynabase: 27 dynamical systems in dynabase_systems")
