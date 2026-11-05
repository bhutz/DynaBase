# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from functions.release_files import LABEL_ROWS_QUERY, compare_labels, read_label_file

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

#every label is permanent from v1.0.0 on: report any that didn't survive this load
label_entries = read_label_file()
if not label_entries:
    print('label check: no label file yet, make_release.py writes it')
else:
    my_cursor.execute(LABEL_ROWS_QUERY)
    label_check = compare_labels(label_entries, my_cursor.fetchall())
    for old, new in label_check['changed']:
        print('LABEL CHANGED: ' + old + ' is now ' + new)
    for old in label_check['missing']:
        print('LABEL MISSING: ' + old + ' is not in the database')
    print('label check: ' + str(len(label_check['changed'])) + ' changed, '
          + str(len(label_check['missing'])) + ' missing, '
          + str(len(label_check['new'])) + ' new since the last release')
