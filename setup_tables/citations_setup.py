"""
Setup the PostgreSQL table for citations

AUTHORS:

- Ben Hutz (2023-10): initial version

"""

# ****************************************************************************
#       Copyright (C) 2023 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

# drop table if it already exists
my_cursor.execute("""
    DROP TABLE IF EXISTS citations
""")


############################
# create custom types


#create new types


######################################
# Create Citations table Schema

#should this have things like: base_field_type?
my_cursor.execute("""
CREATE TABLE citations (
    label varchar PRIMARY KEY,
    authors varchar[],
    journal varchar,
    year integer,
    citation varchar,
    mathscinet varchar,
    id serial
  )""")


#'https://mathscinet.ams.org/mathscinet/article?mr=MR2501344'
my_session.commit()




