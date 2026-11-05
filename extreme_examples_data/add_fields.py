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

path_to_log = "/home/ben/dynabase/fields_log.txt"
log_file = open(path_to_log, 'w', 1)


from fields.field_helpers_FF import add_field_FF


#########################
###########################

# Finite Fields

for p in primes(2,20):
    for n in range(1,5):
        add_field_FF(GF(p**n), my_cursor)


my_session.commit()
log_file.close()
my_session.close()
