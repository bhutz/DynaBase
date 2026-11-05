# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

load_attach_path('/home/ben/dynabase')
import sys
sys.path.append("/home/ben/dynabase")

from functions.parallel_load import default_num_cpus, start_collecting, stop_collecting, precompute_jobs

# data versions already released (setup_all drops them)
load("connect.py")
load("extreme_examples_data/add_releases.py")

# citations
load("connect.py")
load("extreme_examples_data/add_citations.py")

# field data
load("connect.py")
load("extreme_examples_data/add_fields.py")

# family data
load("connect.py")
load("extreme_examples_data/add_families.py")

# functions data
function_files = ["extreme_examples_data/add_functions_quadratic_polys_dim_1.py",
                  "extreme_examples_data/add_functions_cubic_polys_dim_1.py",
                  "extreme_examples_data/add_functions_quadratic_rational_dim_1.py",
                  "extreme_examples_data/add_functions_higher_degree_polys_dim_1.py",
                  "extreme_examples_data/add_functions_higher_degree_rational_dim_1.py",
                  "extreme_examples_data/add_functions_small_height_dim_1.py",
                  "extreme_examples_data/add_functions_automorphisms_dim_1.py"]

# the computations run in parallel first (see functions/parallel_load.py); the load after
# them writes the database in order.
#
# The number of processes is half of the available CPUs by default. To change it, set the
# environment variable DYNABASE_CPUS (the exact name, in capitals) to a whole number; 1 skips
# the parallel step. Each process can start child processes of its own, so a load can use
# more CPUs than this number.
#
#   for one run:                  DYNABASE_CPUS=4 sage extreme_examples_data/extreme_examples.sage
#   for this terminal:            export DYNABASE_CPUS=4
#   for new terminals as well:    echo 'export DYNABASE_CPUS=4' >> ~/.bashrc
num_cpus = default_num_cpus()
if num_cpus > 1:
    parallel_jobs = start_collecting()
    for function_file in function_files:
        load("connect.py")
        load(function_file)
    stop_collecting()
    precompute_jobs(parallel_jobs, num_cpus)

for function_file in function_files:
    load("connect.py")
    load(function_file)

# every label in the label file should have survived the load
load("connect.py")
load("extreme_examples_data/check_labels.py")
