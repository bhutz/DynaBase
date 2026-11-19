# ****************************************************************************
#       Copyright (C) 2026 Ben Hutz <benjamin.hutz@slu.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

import os
import sys
# the repository: DYNABASE_ROOT if set, else the directory above this script when it is run as
# `sage extreme_examples_data/extreme_examples.sage`, else the working directory.
# The files loaded from here read DYNABASE_ROOT.
_script = globals().get('__file__', '')
if not os.environ.get('DYNABASE_ROOT'):
    os.environ['DYNABASE_ROOT'] = (os.path.dirname(os.path.dirname(os.path.abspath(_script)))
                                   if os.path.basename(_script) == 'extreme_examples.sage.py' else os.getcwd())
DYNABASE_ROOT = os.environ['DYNABASE_ROOT']
if not os.path.isfile(os.path.join(DYNABASE_ROOT, 'connect.py')):
    raise RuntimeError(DYNABASE_ROOT + ' is not the Dynabase repository: run from its root, or set DYNABASE_ROOT')
load_attach_path(DYNABASE_ROOT)
sys.path.append(DYNABASE_ROOT)

from functions.function_dim_1_helpers_generic import build_cpus, build_timeout, build_compute_missing

# Build settings. Every data file reads the environment variables
# when it adds its maps (functions/parallel_load.py),
# so a data file loaded on its own uses them too. Each is an environment variable: set it for
# one run (DYNABASE_TIMEOUT=600 sage extreme_examples_data/extreme_examples.sage), for the
# terminal (export DYNABASE_TIMEOUT=600), or here by uncommenting its line (which overrides
# an environment variable setting).
#
# To run an individual file with the non-default setting, you must specify
# the value when running: e.g.,
#DYNABASE_TIMEOUT=1800 sage -c 'load("extreme_examples_data/add_functions_cubic_polys_dim_1.py")'
# (from the repository root, or with DYNABASE_ROOT set to it)
# (not `sage filename`: sage runs a .py file as plain Python, without QQ, load, etc.)
#
# DYNABASE_CPUS: the number of processes computing at once, half of the available CPUs by
#   default; 1 computes serially. Each can start child processes of its own, so a build can
#   use more CPUs than this.
# DYNABASE_TIMEOUT: the limit, in seconds, of every computation, overriding each file's own
#   (30 s by default, 120 for the automorphisms file, 300 for x^2 + 1/4 over quadratic
#   fields); 0 means no limit.
# DYNABASE_COMPUTE_MISSING: 1 to rerun the missing steps (a column still null, e.g. it timed
#   out) of each map already in the database; 0, the default, gives a stored map only its
#   citations. To fill in what timed out with a longer limit:
#   DYNABASE_COMPUTE_MISSING=1 DYNABASE_TIMEOUT=1800 sage extreme_examples_data/extreme_examples.sage

os.environ['DYNABASE_CPUS'] = '4'
os.environ['DYNABASE_TIMEOUT'] = '1800'
os.environ['DYNABASE_COMPUTE_MISSING'] = '1'

# a bad value stops here, before any computing
print('build settings: cpus', build_cpus(), ' timeout', build_timeout(int(30)),
      ' compute missing', build_compute_missing())

# data versions already released (setup_all drops them)
# for label continuity
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

# functions data: each file compiles its maps and adds them, its computations in parallel
function_files = ["extreme_examples_data/add_functions_quadratic_polys_dim_1.py",
                  "extreme_examples_data/add_functions_cubic_polys_dim_1.py",
                  "extreme_examples_data/add_functions_quadratic_rational_dim_1.py",
                  "extreme_examples_data/add_functions_special_cases_dim_1.py",
                  "extreme_examples_data/add_functions_higher_degree_polys_dim_1.py",
                  "extreme_examples_data/add_functions_higher_degree_rational_dim_1.py",
                  "extreme_examples_data/add_functions_small_height_dim_1.py",
                  "extreme_examples_data/add_functions_automorphisms_dim_1.py"]

for function_file in function_files:
    print(function_file)
    load("connect.py")
    load(function_file)

# every label in the label file should have survived the load
load("connect.py")
load("extreme_examples_data/check_labels.py")
