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

import psycopg2
import psycopg2.extras

from config import load_config

config = load_config()
try:
    # connecting to the PostgreSQL server
    my_session = psycopg2.connect(**config)
    print('Connected to the PostgreSQL server.')

except (psycopg2.DatabaseError, Exception) as error:
    print(error)


my_cursor = my_session.cursor(cursor_factory=psycopg2.extras.DictCursor)


