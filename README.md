# DYNABASE

Database of Arithmetic Dynamics

This database collects arithmetic information on algebraic dynamical systems.
The data is stored in a PostgreSQL database, and the computations are done in SageMath.
The code is written to be run under SageMath.

# Dynabase.org

A static rendering of the data is at https://dynabase.org, served through GitHub Pages from `docs/`.

# License

The code is licensed under the GNU General Public License, version 3 or later (see `LICENSE`).
The data is licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0,
https://creativecommons.org/licenses/by/4.0/); see `LICENSE-DATA` for which files that covers.

# Citing Dynabase

See `CITATION.cff` (GitHub's "Cite this repository" button reads it). Please cite the article and
give the data version you used, as listed on the website and in its changelog. Each map also
lists the published sources it comes from.

# Data versions

Versions of the data are numbered `major.minor.patch`:

- **major**: a change to the database schema
- **minor**: data added or newly computed
- **patch**: a correction to existing values

See the changelog at https://dynabase.org/changelog.html. `data_release/make_release.py` compares
the database with the previous version and refuses a number that doesn't match the changes. Labels are permanent from v1.0.0 on, so it also refuses a release in which a recorded label changed or disappeared.

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
   exports the next version is compared with), sets the version and release date in
   `CITATION.cff`, and regenerates `docs/`. It runs SageMath to record its version and to build the
   site: the `sage` on your path, or the one given by `--sage` or the `DYNABASE_SAGE` environment
   variable:
   
   ```bash
   python3 data_release/make_release.py 1.1.0 --notes "What changed."
   ```

8. Commit and tag. Pushing is what publishes the site:
   
   ```bash
   git add data_release/latest extreme_examples_data/labels.jsonl extreme_examples_data/releases.jsonl docs CITATION.cff
   ```
   
   ```bash
   git commit -m "data version 1.1.0" && git tag data-v1.1.0
   ```

9. Package the version for Zenodo. This builds `releases/dynabase-v1.1.0.zip` (not in git) from
   the tag: the database dump, schema, table exports, labels, version history, the source at the
   tag, a README and a manifest of checksums. The dump is only made while the database still holds
   exactly this version; once it has moved on, add `--no-database` to package the exports alone.

   ```bash
   python3 data_release/package_zenodo.py 1.1.0
   ```

10. On zenodo.org, upload the `.zip` with "New version" on the existing record, so the versions
    share one concept DOI (for 1.0.0, "New upload"). Fill in the form from
    `releases/dynabase-v1.1.0.zenodo.json`, then publish. After the first upload, add the concept
    DOI to `CITATION.cff` (`doi: "10.5281/zenodo.NNNNNNN"`), once.

# Setting up a copy

These are the steps to build the database and the website yourself. Dynabase was developed and
its data computed with:

| Software          | Version                                           |
| ----------------- | ------------------------------------------------- |
| Ubuntu            | 22.04 (under the Windows Subsystem for Linux)     |
| SageMath          | 10.4 (its Python 3.10, PARI 2.15.4, GAP 4.12.2)   |
| PostgreSQL        | 14                                                |
| psycopg2          | 2.9.9                                             |
| lmfdb-lite        | from GitHub, commit `4c4262b`                     |
| Jinja2            | 3.1.4 (included with SageMath)                    |

Building the database also needs network access to the LMFDB, which `lmfdb-lite` queries for
number field labels.

## 1. Install SageMath

Follow https://doc.sagemath.org/html/en/installation/ and make sure `sage` is on your path.

## 2. Install PostgreSQL and create a database

```bash
sudo apt update
sudo apt install postgresql
sudo systemctl start postgresql
```

Create a user and a database:

```bash
sudo -u postgres psql
```

```sql
CREATE USER [username] WITH PASSWORD '[password]';
CREATE DATABASE [databasename] OWNER [username];
\q
```

A GUI client is optional, e.g. Beekeeper Studio (https://github.com/beekeeper-studio/beekeeper-studio).

## 3. Install the Python packages

```bash
sudo apt install python3-dev libpq-dev
sage -pip install psycopg2
sage -pip install -U "lmfdb-lite[pgbinary] @ git+https://github.com/roed314/lmfdb-lite.git"
```

The release scripts in `data_release/` run under plain Python 3, which needs psycopg2 too
(`sudo apt install python3-psycopg2`).

## 4. Get the code

Fork https://github.com/bhutz/DynaBase on GitHub, then clone your fork:

```bash
git clone https://github.com/[your account]/DynaBase.git dynabase
cd dynabase
git remote add upstream https://github.com/bhutz/DynaBase.git
git remote set-url --push upstream DISABLE
```

The repository can be anywhere. `config.py` reads `database.ini` from the repository root, and
`setup_all.sage` and the driver find the root from their own location (or from the
`DYNABASE_ROOT` environment variable, if set) and pass it on to the files they load. A data file
run on its own uses `DYNABASE_ROOT`, else the working directory, so run it from the repository
root. The log files are written to the repository root.

## 5. Configure the database connection

Create `database.ini` in the repository root. It holds passwords, so it is not tracked by git:

```ini
[postgresql]
host=localhost
port=5432
database=[databasename]
user=[username]
password=[password]

[postgresql_local]
host=localhost
port=5432
database=[databasename]
user=[username]
password=[password]
```

`connect.py`, which every setup and data file loads, uses the `[postgresql]` section. The site
generator and the release scripts default to `[postgresql_local]` and take `--section` to choose
another. To build and publish from the same database, give both sections the same values. For a
hosted server that closes idle transactions (Neon closes them after 5 minutes), add
`options=-c idle_in_transaction_session_timeout=0` to its section, as computations can keep a
transaction idle for longer.

## 6. Create the tables

```bash
sage setup_tables/setup_all.sage
```

This drops and recreates every table, so don't run it against a database you want to keep.

## 7. Compute the data

Run everything from the repository root:

```bash
sage extreme_examples_data/extreme_examples.sage
```

The driver loads the citations, fields, families and every data file in order. Three settings
control it, each an environment variable (e.g. `DYNABASE_TIMEOUT=600 sage
extreme_examples_data/extreme_examples.sage`) or a line near the top of `extreme_examples.sage`,
which overrides the environment. Check those lines before a build:

- `DYNABASE_CPUS`: how many maps are computed at once, half of the CPUs by default. `1` computes
  serially.
- `DYNABASE_TIMEOUT`: the time limit in seconds of every computation, overriding each file's own
  (30 seconds, 120 for the automorphisms file, 300 for `x^2 + 1/4` over quadratic fields). `0`
  means no limit.
- `DYNABASE_COMPUTE_MISSING`: `1` reruns the missing steps (a property left unset, e.g. by a
  timeout) of maps already in the database; `0`, the default, only adds new citations to them.

A full build took about 2 days with 8 processes and a 7200 second limit; most properties finish
within 300 seconds. A computation that reaches its limit leaves the property unset, and a later
run with `DYNABASE_COMPUTE_MISSING=1` and a longer limit fills it in. A stopped build keeps what
it has written, map by map. A single data file can also be run on its own, against what is
already in the database:

```bash
sage -c 'load("extreme_examples_data/add_functions_cubic_polys_dim_1.py")'
```

(Not `sage [file].py`, which runs a `.py` file as plain Python, without SageMath's names.)

## 8. Build the website

```bash
sage -python site_generator/generate_site.py
```

This rewrites `docs/` from the database, using `[postgresql_local]` unless given `--section`.
It runs under SageMath, and needs the LMFDB, for the SageMath exports of maps over fields of
degree 3 or more. The About page has the licence and how to cite Dynabase, linked from every page's footer,
and every SageMath export states the licence in its header.

## 9. Use the code in SageMath

To load the helper files in a SageMath session, add the repository root to the load path:

```python
sage: load_attach_path('[path to the repository]')
sage: import sys; sys.path.append('[path to the repository]')
sage: load("connect.py")
```
