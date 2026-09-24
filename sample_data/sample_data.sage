load_attach_path('/home/ben/dynabase')
import sys
sys.path.append("/home/ben/dynabase")

# citations
load("connect.py")
load("sample_data/add_citations.py")

# field data
load("connect.py")
load("sample_data/add_fields.py")

# family data
load("connect.py")
load("sample_data/add_families.py")

# functions data
load("connect.py")
load("sample_data/add_functions_quadratic_polys_dim_1.py")

load("connect.py")
load("sample_data/add_functions_cubic_polys_dim_1.py")

load("connect.py")
load("sample_data/add_functions_quadratic_rational_dim_1.py")

load("connect.py")
load("sample_data/add_functions_higher_degree_polys_dim_1.py")

load("connect.py")
load("sample_data/add_functions_higher_degree_rational_dim_1.py")
