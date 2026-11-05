"""
Setup the PostgreSQL table of data versions. A version is major.minor.patch: major for a
schema change, minor for data added or newly computed, patch for a correction to existing
values. data_release/make_release.py adds the rows; extreme_examples_data/releases.jsonl
keeps them across a rebuild.
"""

# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

my_cursor.execute("""
    DROP TABLE IF EXISTS data_releases
""")

my_cursor.execute("""
CREATE TABLE data_releases (
    version varchar PRIMARY KEY,
    release_date date,
    git_commit varchar,
    sage_version varchar,
    lmfdb_date date,
    doi varchar,
    notes text,
    summary jsonb
  )""")

my_session.commit()
