
from fields.field_helpers_NF import normalize_field_NF
from fields.field_helpers_NF import lmfdb_field_label_NF

from functions.function_dim_1_helpers_NF import model_in_database_NF
from functions.function_dim_1_helpers_NF import add_function_all_NF
from functions.function_dim_1_helpers_NF import normalize_function_NF

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

path_to_log = "/home/ben/dynabase/functions_log.txt"
log_file = open(path_to_log, 'w', 1)

#x^2 + c
#Poonen's Examples
cites = ['Poonen1998']
P = ProjectiveSpace(QQ,1,'x,y')
x,y = P.gens()

F = DynamicalSystem([x**2+y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2+QQ(1/4)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]: 
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2+0*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-2*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(3/4)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(7/4)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(10/9)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(13/9)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(21/16)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(301/144)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)

F = DynamicalSystem([x**2-QQ(29/16)*y**2,y**2])
if not model_in_database_NF(F, my_cursor)[0]:
        label = add_function_all_NF(F, my_cursor, 
        citations=cites, log_file=log_file)


my_session.commit()




#Some number field examples
#for d in range(2,6):
#    if ZZ(d).is_squarefree():
#        K = QuadraticField(d,'v')
#        K,phi = normalize_field_NF(K)
#        print(lmfdb_field_label_NF(K))
#        P=ProjectiveSpace(K,1,'x,y')
#        x,y = P.gens()
#        for c in 
#K.elements_of_bounded_height(bound=ZZ(4)):
#            #print(c)
#            F,phi = 
#normalize_function_NF(DynamicalSystem([x**2+c*y**2,y**2])) 
#polys
#            label = add_function_all_NF(F, my_cursor, citations=['Poonen1998'], log_file=log_file)
#update citations
#    my_session.commit()

#my_session.commit()

log_file.close()

#my_session.close()
