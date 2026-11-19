# ****************************************************************************
#       Copyright (C) 2024 Ben Hutz <benjamin.hutz@slu.edu>
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
# `sage setup_tables/setup_all.sage`, else the working directory.
# The files loaded from here read DYNABASE_ROOT.
_script = globals().get('__file__', '')
if not os.environ.get('DYNABASE_ROOT'):
    os.environ['DYNABASE_ROOT'] = (os.path.dirname(os.path.dirname(os.path.abspath(_script)))
                                   if os.path.basename(_script) == 'setup_all.sage.py' else os.getcwd())
DYNABASE_ROOT = os.environ['DYNABASE_ROOT']
if not os.path.isfile(os.path.join(DYNABASE_ROOT, 'connect.py')):
    raise RuntimeError(DYNABASE_ROOT + ' is not the Dynabase repository: run from its root, or set DYNABASE_ROOT')
load_attach_path(DYNABASE_ROOT)
sys.path.append(DYNABASE_ROOT)

# set up tables
load("connect.py")
load("setup_tables/setup_all.py")

