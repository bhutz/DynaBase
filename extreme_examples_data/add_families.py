# ****************************************************************************
#       Copyright (C) 2023 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

path_to_log = "/home/ben/dynabase/families_log.txt"
log_file = open(path_to_log, 'w', 1)

from functions.families_dim_1_helpers_NF import add_family_NF
from functions.families_dim_1_helpers_NF import add_citations_family_NF

#########################

R=PolynomialRing(QQ,1,'c')
c = R.gen()
P=ProjectiveSpace(R,1,'x,y')
x,y = P.gens()

F=DynamicalSystem([x**2+c*y**2,y**2])
family_id = add_family_NF(F, my_cursor, is_poly=True, num_crit=int(2), num_aut=int(1), aut_iso_type='1', name='poly_deg_2', log_file=log_file)

my_cursor.execute("""SELECT
        id
         FROM citations
        WHERE label=%s
        """,['Poonen1998'])
cites = my_cursor.fetchone()
add_citations_family_NF(family_id, cites, my_cursor, log_file=log_file)


for d in range(3,16):
    F=DynamicalSystem([x**d+c*y**d,y**d])
    fam_name = 'unicritical_poly_deg_' + str(d)
    family_id = add_family_NF(F, my_cursor, is_poly=True, num_crit=int(2), num_aut=int(1), aut_iso_type='1', name=fam_name, log_file=log_file)


###########################


my_session.commit()
my_session.close()
log_file.close()
