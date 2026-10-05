# Dynabase (https://dynabase.org): dimension 1, degree 4, polynomial maps, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.880302df.903704ba.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.e029f05a.0d52105e.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 4*y^4, 2*y^4], domain=P), '1.5457b5e3.e9909514.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.5457b5e3.e9909514.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 - 8/27*x*y^3 + 26/27*y^4, y^4], domain=P), '1.8af865e4.2d8ff491.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 + 8/27*x*y^3 - 19/27*y^4, y^4], domain=P), '1.9da62374.0f726d75.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 + 4*x^3*y - 6*x^2*y^2 - 12*x*y^3 + 5*y^4, 6*y^4], domain=P), '1.a70750b0.c07be85c.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 8*x^3*y, -6*y^4], domain=P), '1.da89c05a.4e01541d.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, y^4], domain=P), '1.770c2622.7cef54b3.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + y^4, y^4], domain=P), '1.e029f05a.0d52105e.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2, y^4], domain=P), '1.6951d87f.f9bbe0ed.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.8e57877c.24b4743f.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.770c2622.7cef54b3.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, 4*x*y^3 + 3*y^4], domain=P), '1.d445c2f7.72c00a36.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 4*x^3*y + y^4, y^4], domain=P), '1.a48ef78e.703b5deb.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.024ac6d7.76c4de71.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
