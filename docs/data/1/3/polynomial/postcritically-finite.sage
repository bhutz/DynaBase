# Dynabase (https://dynabase.org): dimension 1, degree 3, polynomial maps, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.31ca8b83.56a37501.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y + 2*y^3, -2*y^3], domain=P), '1.3e20f681.046df03c.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.5ac401c2.34c3c88c.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.5b621046.0e8d94e9.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.e8bb745c.fe98c06c.1'])
# AMT2020, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, y^3], domain=P), '1.4b199b71.fe98c06c.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([4*x^3 + 3*x^2*y + 6*x*y^2 - 3*y^3, -7*y^3], domain=P), '1.170955e6.895e6900.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3*x*y^2, y^3], domain=P), '1.e8bb745c.fe98c06c.2'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.6502de33.969c7b25.1'])
# AMT2020, Benedetto2009, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.9fcfd25c.91fd0195.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.194ce1a9.8660b31e.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3, -2*x^3 + 6*x^2*y + 3*x*y^2 - 4*y^3], domain=P), '1.b40fd63f.4b09c087.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.7e36c441.20e2ac14.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 3*x*y^2 + y^3], domain=P), '1.ad8ccd97.61cd033e.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - y^3, y^3], domain=P), '1.354addff.61cd033e.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/2*x*y^2, y^3], domain=P), '1.354addff.61cd033e.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3/2*x*y^2, y^3], domain=P), '1.ad8ccd97.61cd033e.2'])
# AMT2020, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.5fe37194.3d72adff.1'])

print("Dynabase: 18 dynamical systems in dynabase_systems")
