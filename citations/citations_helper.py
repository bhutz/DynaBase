"""
Functions to help working with the citations table

AUTHORS:

- Ben Hutz (2026-9): initial version

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

import sys

path_to_log = "/home/ben/dynabase/functions_log.txt"
log_file = open(path_to_log, 'w', 1)


def citation_in_database(label, my_cursor, log_file=sys.stdout):
    """
    Check whether a citation with the given label is already in the
    citations table.

    returns (True, id) if found, (False, 0) if not
    """
    my_cursor.execute("""SELECT id FROM citations WHERE label=%s""", [label])
    row = my_cursor.fetchone()
    if row is None:
        log_file.write('citation not found: ' + str(label) + '\n')
        return False, 0
    log_file.write('citation found: ' + str(label) + ' as ' + str(row['id']) + '\n')
    return True, row['id']


def add_citation(label, authors, journal, year, citation, mathscinet, my_cursor, log_file=sys.stdout):
    """
    Check if a citation (by label) is already in the citations table, and
    add it if it is not.

    (the `citation` parameter is the one long human-readable citation string -
    the table's own `citation` column - not to be confused with the citations
    table as a whole, or with this function's own name.)

    returns (is_new, citation_id):
        is_new is True if a new row was inserted, False if the label was
        already present (matching add_function_NF's own return convention in
        functions/function_dim_1_helpers_NF.py); citation_id is that row's
        `id` either way, so callers (e.g. building a functions_dim_1_NF
        .citations array) get a usable id regardless of which case it was.
    """
    found, existing_id = citation_in_database(label, my_cursor, log_file=log_file)
    if found:
        log_file.write('citation already in db: ' + str(label) + '\n')
        return False, existing_id

    row = {
        'label': label,
        'authors': authors,
        'journal': journal,
        'year': year,
        'citation': citation,
        'mathscinet': mathscinet,
    }
    my_cursor.execute("""INSERT INTO citations
        (label, authors, journal, year, citation, mathscinet)
        VALUES
        (%(label)s, %(authors)s, %(journal)s, %(year)s, %(citation)s, %(mathscinet)s)
        RETURNING id
        """, row)
    if my_cursor.rowcount == 0:
        log_file.write('add_citation failure: ' + str(label) + ' not inserted \n')
        raise ValueError('add_citation insert failure on ' + str(label))
    new_id = my_cursor.fetchone()['id']
    log_file.write('citation inserted: ' + str(label) + ' as ' + str(new_id) + '\n')
    return True, new_id



