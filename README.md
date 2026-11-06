# DYNABASE

Database of Arithmetic Dynamics

This database collects arithmetic information on algebraic dynamical systems.
The database in implemented in PSQL, while the computations are done in Python/SageMath.
The code/functionality is written to be run under a SageMath kernel.

# Dynabase.org

A static rendering of some of the data can be found on https://dynabase.org This is a static rendering served through github pages.

# Data versions

Versions of the data are numbered `major.minor.patch`:

- **major**: a change to the database schema
- **minor**: data added or newly computed
- **patch**: a correction to existing values

See the changelog at https://dynabase.org/changelog.html. `data_release/make_release.py` compares
the database with the previous version and refuses a number that doesn't match the changes. Labels are permanent from v1.0.0 on, so it also refuses a release in which a recorded label changed or disappeared.

Run everything from the repo root with sage in your path.

The driver runs its computations in parallel on half of the CPUs by default. Set
`DYNABASE_CPUS` to change that; `DYNABASE_CPUS=1` skips the parallel step. If the driver is interrupted during the parallel step, its results are lost. Maps already written to the database are skipped on a rerun.

Each computation has a time limit, 30 seconds unless a data file asks for longer (120 for the
automorphisms file, 300 for `x^2 + 1/4` over quadratic fields). Set `DYNABASE_TIMEOUT` to a whole
number of seconds to override all of them for a build; 0 means no limit. It only affects maps
computed in that build, as stored maps are skipped.

## Making the next version

This assumes something has been updated since the last version. The database is updated in place;
don't run `setup_all.sage` unless the schema change requires it (see step 1). The first version,
1.0.0, follows a full rebuild and starts from step 6, with no earlier version to compare with.

1. Make the change in the way that fits it:
   
   | Change                         | What to do                                                                                | Version |
   | ------------------------------ | ----------------------------------------------------------------------------------------- | ------- |
   | New maps                       | Add them to a data file, and any new source to `add_citations.py`                         | minor   |
   | A new citation on a stored map | Add the map's entry with that citation to a data file                                     | minor   |
   | A value that was missing       | Call the step's helper directly, e.g. `add_smallest_height`. The driver skips stored maps | minor   |
   | A wrong value                  | Fix the cause, then update the stored row. The driver won't overwrite it                  | patch   |
   | A schema change                | Update the setup file and `ALTER` the database                                            | major   |
   
   A rebuild after v1.0.0 keeps labels through `labels.jsonl` and the version history through
   `releases.jsonl`.

2. Commit the code and data changes. The release helper refuses uncommitted ones.

3. Back up the database:
   
   ```bash
   pg_dump -h localhost -U [username] --no-owner [databasename] | gzip > ~/data-before-next-version.sql.gz
   ```

4. If data files changed, run the driver. Stored maps are skipped apart from attaching citations,
   so it only computes what's new:
   
   ```bash
   sage extreme_examples_data/extreme_examples.sage
   ```

5. Check the last line of the output. It should report `0 changed, 0 missing`, plus the number of
   new maps:
   
   ```
   label check: 0 changed, 0 missing, 12 new since the last release
   ```
   
   A changed or missing label has to be fixed before releasing, as labels are permanent.

6. Do a dry run with the number you expect, here 1.1.0. It lists the changes and, if the number is wrong, says which one they call for:
   
   ```bash
   python3 data_release/make_release.py 1.1.0 --notes "What changed." --dry-run
   ```

7. Make the release. This updates `labels.jsonl`, `releases.jsonl` and `data_release/latest/` (the
   exports the next version is compared with), and regenerates `docs/`:
   
   ```bash
   python3 data_release/make_release.py 1.1.0 --notes "What changed."
   ```

8. Commit and tag. Pushing is what publishes the site:
   
   ```bash
   git add data_release/latest extreme_examples_data/labels.jsonl extreme_examples_data/releases.jsonl docs
   ```
   
   ```bash
   git commit -m "data version 1.1.0" && git tag data-v1.1.0
   ```

# Pre-requisites and Set-up

On an existing 20.02 ubunutu install with release sage built from sage github
(https://github.com/sagemath/sage.git)

# Install PostGreSQL

sudo apt update
sudo apt upgrade
sudo apt install postgresql

# start it

sudo systemctl start postgresql

# check its status

sudo systemctl status postgresql

# From a terminal

# create database and user

sudo su - postgres
psql
postgres=# CREATE USER [username] WITH PASSWORD '[password]';
postgres=# CREATE DATABASE [db name];
postgres=# GRANT ALL PRIVILEGES ON DATABASE [db name] to [user];
postgres=# \q

# Install a GUI client

# Beekeeper community edition

# Get link from readme in: https://github.com/beekeeper-studio/beekeeper-studio

# download .deb and install with

sudo dpkg -i [filename]

# Connecting via python needs the dependencies

sudo apt-get install python3-dev
sudo apt-get install libpq-dev

# Sage needs psql interface

sage -pip install psycopg2

# Sage uses the LMFDB-lite interface for number field data

sage --pip install -U "lmfdb-lite[pgbinary] @ git+https://github.com/roed314/lmfdb-lite.git"

# Connect to the DAD github project

# log in to you github account

# navigate to database page

https://github.com/bhutz/DAD.git

Click on "Fork" to create your personal fork of the project

# this creates your own person DAD repository. e.g., https://github.com/alice/DAD.git

# clone the repository

git clone git clone https://github.com/alice/Dynabase.git
cd DAD
git remote -v

# add the remote as the upstream

git remote add upstream https://github.com/bhutz/Dynabase.git
git remote -v

# disable pushes to upstream instead of origin

git remote set-url --push upstream DISABLE

# If you are using SSH for github, then you would do the following instead:

# create local directory for the project

# initialize as a git repository

git init

# add the remotes

git remote add origin git@github.com:alice/Dynabase.git
git remote add upstream git@github.com:bhutz/Dynabase.git
git remote -v

# pull the repository

git pull origin main

# set tracking so you don't have to specify origin/main everytime

git branch --set-upstream-to=origin/main

# to load the .oy files in Sage. It assumes you've added the root of

# the project to the load_attach_path

sage: load_attach_path('[path]')
