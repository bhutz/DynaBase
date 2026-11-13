# Dynabase (https://dynabase.org): Dimension 1, degree 2 polynomials over quadratic fields, Rational Preperiodic
#
# Load in Sage with load("<this file>"). It defines dynabase_systems, a list of
# [map, label] pairs in table order: the map as a DynamicalSystem over the field of
# its table row, and its Dynabase label (dimension.sigma1.sigma2.ordinal).
# Loading also (re)defines K, a, P, x, y, R, t.

R.<t> = QQ[]
dynabase_systems = []

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 21/16*y^2, y^2], domain=P), '1.96cf3896.0738b144.1'])
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])

K.<a> = NumberField(t^2 - t - 18)  # 2.2.73.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Stoll2008, Hutz2013, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 71/48*y^2, y^2], domain=P), '1.b63253c2.79c27641.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 15/8*y^2, y^2], domain=P), '1.0b9d1367.ec14c47e.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 13/16*y^2, y^2], domain=P), '1.c54b8f3f.756bd15c.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 45/16*y^2, y^2], domain=P), '1.66a737e7.ba20c451.1'])

K.<a> = NumberField(t^2 - t - 26)  # 2.2.105.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 95/48*y^2, y^2], domain=P), '1.ea60287f.20733fcb.1'])

K.<a> = NumberField(t^2 - t + 4)  # 2.0.15.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 31/48*y^2, y^2], domain=P), '1.7f55f532.309a74eb.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 10/9*y^2, y^2], domain=P), '1.420f870e.c9b64d6b.1'])

K.<a> = NumberField(t^2 - t - 48)  # 2.2.193.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])

K.<a> = NumberField(t^2 - t - 84)  # 2.2.337.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])

K.<a> = NumberField(t^2 - t - 10)  # 2.2.41.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])

K.<a> = NumberField(t^2 - t - 14)  # 2.2.57.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])

K.<a> = NumberField(t^2 - t + 2)  # 2.0.7.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + 3/16*y^2, y^2], domain=P), '1.47e02d0b.8c09d28d.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + ((-1/2*a - 13/16))*y^2, y^2], domain=P), '1.746227db.7d7b25f5.1'])

K.<a> = NumberField(t^2 - t - 18)  # 2.2.73.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + ((1/9*a - 205/144))*y^2, y^2], domain=P), '1.4e71ff9d.500b5808.1'])

K.<a> = NumberField(t^2 - t - 4)  # 2.2.17.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 273/64*y^2, y^2], domain=P), '1.022ad844.22a44656.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])

K.<a> = NumberField(t^2 - 10)  # 2.2.40.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 13/9*y^2, y^2], domain=P), '1.92710271.448de5df.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Hutz2013, Doyle2014, Doyle2018, Doyle2020, DoHy2025, Hutz2026
dynabase_systems.append([DynamicalSystem([x^2 - 29/16*y^2, y^2], domain=P), '1.2799614f.68d04ee2.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 289/144*y^2, y^2], domain=P), '1.be487703.7a8d3331.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 40/9*y^2, y^2], domain=P), '1.5ee5410e.67a5d387.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 37/9*y^2, y^2], domain=P), '1.b5662713.812bd674.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 12*y^2, y^2], domain=P), '1.ce2ee6ce.40d0399a.1'])

K.<a> = NumberField(t^2 - 10)  # 2.2.40.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 155/72*y^2, y^2], domain=P), '1.cfe3a31c.40f65747.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])

K.<a> = NumberField(t^2 - 3)  # 2.2.12.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 3/4*y^2, y^2], domain=P), '1.49ef408f.a255b42e.1'])

K.<a> = NumberField(t^2 - t - 8)  # 2.2.33.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 301/144*y^2, y^2], domain=P), '1.58d642f9.9c223710.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 3*y^2, y^2], domain=P), '1.65eba62c.ade2f71d.1'])

K.<a> = NumberField(t^2 - 2)  # 2.2.8.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])

K.<a> = NumberField(t^2 - t - 3)  # 2.2.13.1
P.<x,y> = ProjectiveSpace(K, 1)
# WR1994, Poonen1998, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 - 2*y^2, y^2], domain=P), '1.1e4552d5.ef32d183.1'])

K.<a> = NumberField(t^2 + 1)  # 2.0.4.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + (a)*y^2, y^2], domain=P), '1.71dc0491.720d92b7.1'])

K.<a> = NumberField(t^2 - t + 1)  # 2.0.3.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 + 1/5*y^2, y^2], domain=P), '1.416b374b.839be271.1'])
# Doyle2014, Doyle2018
dynabase_systems.append([DynamicalSystem([x^2 - 4/5*y^2, y^2], domain=P), '1.bc23abeb.ac82301a.1'])

K.<a> = NumberField(t^2 - 3)  # 2.2.12.1
P.<x,y> = ProjectiveSpace(K, 1)
# Poonen1998, Ingram2012, Doyle2014, Lukas2014, CV2017, Doyle2018, Doyle2020, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 - y^2, y^2], domain=P), '1.9521dd83.b3ee860d.1'])

K.<a> = NumberField(t^2 - t - 1)  # 2.2.5.1
P.<x,y> = ProjectiveSpace(K, 1)
# Morton1992, FN1997, Poonen1998, Manes2008, Ingram2012, Doyle2014, Lukas2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2, y^2], domain=P), '1.8a010b19.9e054174.1'])
# Poonen1998, Doyle2014, Doyle2018, Doyle2020
dynabase_systems.append([DynamicalSystem([x^2 + 1/4*y^2, y^2], domain=P), '1.5123e4a4.77ccce17.1'])
# Morton1992, Poonen1998, Doyle2014, Doyle2018, DoHi2025
dynabase_systems.append([DynamicalSystem([x^2 + y^2, y^2], domain=P), '1.991c99ac.68df8ef0.1'])

print("Dynabase: 46 dynamical systems in dynabase_systems")
