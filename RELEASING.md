# Making a data version

Versions of the data are numbered `major.minor.patch`:

- **major**: a change to the database schema
- **minor**: data added or newly computed
- **patch**: a correction to existing values

`data_release/make_release.py` compares the database with the previous version and refuses a number that doesn't match the changes. Labels are permanent from v1.0.0 on, so it also refuses a release in which a recorded label changed or disappeared.

Run everything from the repo root with sage in your path.

The driver runs its computations in parallel on half of the CPUs by default. Set
`DYNABASE_CPUS` to change that; `DYNABASE_CPUS=1` skips the parallel step. If the driver is interrupted during the parallel step, its results are lost. Maps already written to the database are skipped on a rerun.

# 

## Making the next version

This assumes something has been updated since the last version. The database is updated in place;
don't run `setup_all.sage` unless the schema change requires it (see step 1).

1. Make the change in the way that fits it:
   
   | Change                         | What to do                                                                                | Version |
   | ------------------------------ | ----------------------------------------------------------------------------------------- | ------- |
   | New maps                       | Add them to a data file, and any new source to `add_citations.py`                         | minor   |
   | A new citation on a stored map | Add the map's entry with that citation to a data file                                     | minor   |
   | A value that was missing       | Call the step's helper directly, e.g. `add_smallest_height`. The driver skips stored maps | minor   |
   | A wrong value                  | Fix the cause, then update the stored row. The driver won't overwrite it                  | patch   |
   | A schema change                | Update the setup file and `ALTER` the database                                            | major   |
   
   A rebuild after v1.0.0 keeps labels through `labels.jsonl` and the version history through`releases.jsonl`. 

2. Commit the code and data changes. The release helper refuses uncommitted ones.

3. Back up the database:
   
   ```bash
   pg_dump -h localhost -U dad_user --no-owner dad | gzip > ~/dad-before-next-version.sql.gz
   ```

4. If data files changed, run the driver. Stored maps are skipped apart from attaching citations, so it only computes what's new:
   
   ```bash
   sage extreme_examples_data/extreme_examples.sage
   ```

5. Check the last line of the output. It should report `0 changed, 0 missing`, plus the number of
   new maps:
   
   ```
   label check: 0 changed, 0 missing, 12 new since the last release
   ```
   
   A changed or missing label has to be fixed before releasing, as labels are permanent.

6. Make sure the previous version's package is in `releases/`, as the comparison needs its
   `exports/` and `schema.sql`. That folder isn't in git, so if it's gone, download that version
   from Zenodo and add `--previous <folder>` to the commands below.

7. Do a dry run with the number you expect, here 1.1.0. It lists the changes and, if the number is
   wrong, says which one they call for:
   
   ```bash
   python3 data_release/make_release.py 1.1.0 --lmfdb-date YYYY-MM-DD --notes "What changed." --dry-run
   ```
   
   `--lmfdb-date` is the date of the load in step 4, or of the last load if the driver didn't run.

8. Make the release. This updates `labels.jsonl` and `releases.jsonl`, builds
   `releases/dynabase-v1.1.0/` and its `.zip`, and regenerates `docs/`:
   
   ```bash
   python3 data_release/make_release.py 1.1.0 --lmfdb-date YYYY-MM-DD --notes "What changed."
   ```

9. Check `releases/dynabase-v1.1.0/zenodo.json`, then upload the `.zip` with "New version" on the
   existing Zenodo record, so the versions stay linked. If you reserve the DOI beforehand, pass it
   to step 8 with `--doi` and skip step 11.

10. Commit and tag. Pushing is what publishes the site:
    
    ```bash
    git add extreme_examples_data/labels.jsonl extreme_examples_data/releases.jsonl docs
    ```
    
    ```bash
    git commit -m "data version 1.1.0" && git tag data-v1.1.0
    ```

11. Record the DOI, regenerate the site so the changelog shows it, and commit
    `extreme_examples_data/releases.jsonl` and `docs`:
    
    ```bash
    python3 data_release/make_release.py 1.1.0 --set-doi <DOI>
    ```
    
    ```bash
    python3 site_generator/generate_site.py
    ```
