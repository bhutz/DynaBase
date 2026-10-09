# Dynabase (https://dynabase.org): Summary of Extreme Examples, postcritically finite maps (all of them, for each row)
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K = QQ
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.b5876aa4.6951d87f.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998, FN1997
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.a68cf1ff.024ac6d7.1'])
# Doyle2014, Ingram2012, Lukas2014, Poonen1998
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.a6935bbd.880302df.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - y^3, -y^3], domain=P), '1.7e36c441.20e2ac14.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 + 2*y^3, 2*y^3], domain=P), '1.5ac401c2.34c3c88c.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.5b621046.0e8d94e9.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([3*x^3 - 9*x*y^2 + 2*y^3, 4*y^3], domain=P), '1.6502de33.969c7b25.1'])
# AMT2020, Benedetto2009, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3], domain=P), '1.9fcfd25c.91fd0195.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y - 4*y^3, -4*y^3], domain=P), '1.194ce1a9.8660b31e.1'])
# AMT2020, Benedetto2009
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, -y^3], domain=P), '1.e8bb745c.fe98c06c.1'])
# AMT2020, Ingram2012, FN1997
dynabase_systems.append([DynamicalSystem([x^3, y^3], domain=P), '1.5fe37194.3d72adff.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([x^3 + 3*x^2*y, 3*x*y^2 + y^3], domain=P), '1.ad8ccd97.61cd033e.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x^2*y + 2*y^3, -2*y^3], domain=P), '1.3e20f681.046df03c.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 + 3*x^2*y - y^3, y^3], domain=P), '1.354addff.61cd033e.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([3*x^3, -2*x^3 + 6*x^2*y + 3*x*y^2 - 4*y^3], domain=P), '1.b40fd63f.4b09c087.1'])
# AMT2020, Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3*x*y^2, y^3], domain=P), '1.4b199b71.fe98c06c.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([2*x^3 - 3*x*y^2 - 2*y^3, -2*y^3], domain=P), '1.31ca8b83.56a37501.1'])
# AMT2020
dynabase_systems.append([DynamicalSystem([4*x^3 + 3*x^2*y + 6*x*y^2 - 3*y^3, -7*y^3], domain=P), '1.170955e6.895e6900.1'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 - 3/2*x*y^2, y^3], domain=P), '1.354addff.61cd033e.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3/2*x*y^2, y^3], domain=P), '1.ad8ccd97.61cd033e.2'])
# Ingram2012
dynabase_systems.append([DynamicalSystem([x^3 + 3*x*y^2, y^3], domain=P), '1.e8bb745c.fe98c06c.2'])
# Fraser2024, GHJSX2021, FN1997
dynabase_systems.append([DynamicalSystem([x^4, y^4], domain=P), '1.024ac6d7.76c4de71.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - y^4, y^4], domain=P), '1.770c2622.7cef54b3.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([2*x^4 - y^4, -y^4], domain=P), '1.5457b5e3.e9909514.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4, 4*x*y^3 + 3*y^4], domain=P), '1.d445c2f7.72c00a36.1'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([3*x^4 - 4*x^3*y + y^4, y^4], domain=P), '1.a48ef78e.703b5deb.1'])
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
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2, 2*y^4], domain=P), '1.e029f05a.0d52105e.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 4*y^4, 2*y^4], domain=P), '1.5457b5e3.e9909514.2'])
# Fraser2024
dynabase_systems.append([DynamicalSystem([x^4 - 4*x^2*y^2 + 2*y^4, y^4], domain=P), '1.880302df.903704ba.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^5, y^5], domain=P), '1.6f752b35.d8e415c3.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^6, y^6], domain=P), '1.d60c7e5d.aa38682f.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^7, y^7], domain=P), '1.6c5154c1.84c0eaef.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^8, y^8], domain=P), '1.a2cb972c.bc5e6238.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^9, y^9], domain=P), '1.3d72adff.f501313b.1'])
# FN1997
dynabase_systems.append([DynamicalSystem([x^10, y^10], domain=P), '1.f0bbe529.7d4a3a0d.1'])
# dFH2018, Lukas2014
dynabase_systems.append([DynamicalSystem([y^2, x^2], domain=P), '1.a35a25cc.024ac6d7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*x*y - y^2, -x^2 + 2*x*y - y^2], domain=P), '1.f87176de.3b08f253.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2], domain=P), '1.4cc4fb80.ef9cb8b5.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - y^2, -x^2 - y^2], domain=P), '1.fbfd6fd4.9888ce4b.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 - 2*y^2], domain=P), '1.c346226f.0c3c179e.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, -x^2], domain=P), '1.170a93ef.0fdf09c7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 - 2*y^2, -x^2 + 2*x*y - 2*y^2], domain=P), '1.89eb0e1e.d90eecb7.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([2*x^2 + 2*x*y, -x^2 - y^2], domain=P), '1.095ed92d.7e1406dd.1'])
# Lukas2014
dynabase_systems.append([DynamicalSystem([x^2 + 2*y^2, x^2 - y^2], domain=P), '1.366a39dc.7475b914.1'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, x^3], domain=P), '1.ee2edc14.3d72adff.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([x^3 - 3*y^3, -3*x^2*y], domain=P), '1.ee2edc14.06479f56.1'])
# GHJSX2021
dynabase_systems.append([DynamicalSystem([y^3, -x^3], domain=P), '1.ee2edc14.3d72adff.2'])
# dFH2018, GHJSX2021
dynabase_systems.append([DynamicalSystem([y^4, x^4], domain=P), '1.71005f25.76c4de71.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^5, x^5], domain=P), '1.56d48bcf.d8e415c3.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^5 - 5*x*y^4, -5*x^4*y + y^5], domain=P), '1.56d48bcf.b239edf6.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^6, x^6], domain=P), '1.61329c7f.aa38682f.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([y^7, x^7], domain=P), '1.2b775e9a.84c0eaef.1'])
# dFH2018
dynabase_systems.append([DynamicalSystem([x^11 + 66*x^6*y^5 - 11*x*y^10, -11*x^10*y - 66*x^5*y^6 + y^11], domain=P), '1.936da2cf.8bf2f4e6.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.e9464d8c.638cd9c2.1'])

print("Dynabase: 62 dynamical systems in dynabase_systems")
