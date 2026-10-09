from functions.function_dim_1_helpers_NF import add_automorphism_group_NF
from functions.function_dim_1_helpers_NF import get_sage_func_NF
from functions.function_dim_1_helpers_NF import polynomial_automorphism_group

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_log.txt"
log_file = open(path_to_log, 'a', 1)

###########################################
#Backfill automorphism_group_iso_type (added 2026-10-01) for the functions stored
#before that column existed: they have automorphism_group_cardinality but no type.
#
#- order 1 or a prime p: the group can only be trivial or cyclic, so the type is
#  '1' or 'Cp' (GAP's StructureDescription names, as add_automorphism_group_NF stores)
#  and nothing is computed;
#- any other order (e.g. 4: C4 or C2 x C2): add_automorphism_group_NF recomputes the
#  group over QQbar and stores its size and type.
#
#Functions with no automorphism_group_cardinality (their computation timed out):
#a polynomial written as one, (f(x, y) : c*y^d), gets its group from its exponents
#(polynomial_automorphism_group, through add_automorphism_group_NF - instant); any
#other is left alone rather than spend another timeout on it.
#Only rows with a null type are touched, so this can be rerun.
#On 2026-10-08: 302 functions - orders 1 (264), 2 (35), 3 (1) set directly, 4 and 6
#(one each) recomputed. z^2 (Poonen1998, order 2) is the degree 2 C_2 example.
timeout = int(120)

my_cursor.execute("""SELECT function_id, automorphism_group_cardinality FROM functions_dim_1_NF
    WHERE automorphism_group_iso_type IS NULL AND automorphism_group_cardinality IS NOT NULL
    ORDER BY function_id""")
rows = my_cursor.fetchall()
log_file.write('backfilling automorphism group types for ' + str(len(rows)) + ' functions\n')

set_directly, recomputed = 0, 0
for row in rows:
    F_id, n = row['function_id'], ZZ(row['automorphism_group_cardinality'])
    if n == 1 or n.is_prime():
        iso_type = '1' if n == 1 else 'C' + str(n)
        my_cursor.execute("""UPDATE functions_dim_1_NF SET automorphism_group_iso_type = %s
            WHERE function_id = %s""", [iso_type, F_id])
        set_directly += 1
    else:
        add_automorphism_group_NF(F_id, my_cursor, log_file=log_file, timeout=timeout)
        recomputed += 1
        my_session.commit()

my_session.commit()
log_file.write('automorphism group types: ' + str(set_directly) + ' set from the order, '
               + str(recomputed) + ' recomputed\n')

my_cursor.execute("""SELECT function_id FROM functions_dim_1_NF
    WHERE automorphism_group_cardinality IS NULL ORDER BY function_id""")
from_exponents = 0
for row in my_cursor.fetchall():
    F_id = row['function_id']
    F = get_sage_func_NF(F_id, 'original', my_cursor, log_file=log_file)
    if polynomial_automorphism_group(F) is not None:
        add_automorphism_group_NF(F_id, my_cursor, log_file=log_file, timeout=timeout)
        from_exponents += 1
my_session.commit()
log_file.write('automorphism groups of polynomials from their exponents: ' + str(from_exponents) + '\n')

log_file.close()

#my_session.close()
