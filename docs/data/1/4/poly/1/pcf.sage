# Dynabase (https://dynabase.org): Dimension 1, degree 4 polynomials over QQ, Postcritically Finite
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, P, x, y.

dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.ef32d183.12ccf81e.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.3c83e548.afd51a11.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 4*y^4, 2*y^4], domain=P), '1.68938348.14eb3256.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.68938348.14eb3256.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 - 8/27*x*y^3 + 26/27*y^4, y^4], domain=P), '1.2da9e4fc.f7288834.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2/3*x^2*y^2 + 8/27*x*y^3 - 19/27*y^4, y^4], domain=P), '1.a84822fb.ce008426.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 + 4*x^3*y - 6*x^2*y^2 - 12*x*y^3 + 5*y^4, 6*y^4], domain=P), '1.60a85381.e4844273.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 8*x^3*y, -6*y^4], domain=P), '1.b328a709.67009066.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2 + y^4, y^4], domain=P), '1.14995048.fcc23423.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - 4*x^2*y^2 + y^4, y^4], domain=P), '1.3c83e548.afd51a11.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 2*x^2*y^2, y^4], domain=P), '1.b3ee860d.dc17dde7.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 + 4*x*y^3, 3*y^4], domain=P), '1.d5469f32.478a246b.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.14995048.fcc23423.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, 4*x*y^3 + 3*y^4], domain=P), '1.82a47d29.57db8a86.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 4*x^3*y + y^4, y^4], domain=P), '1.22037e2d.4a60706e.1'])
# FN1997, GHJSX2021, Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.9e054174.3f0eaf7a.1'])

print("Dynabase: 16 dynamical systems in dynabase_systems")
