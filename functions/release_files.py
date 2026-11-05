"""
The two files that carry a data version's identity across database rebuilds, both
tracked in git next to the data files. Plain Python (no Sage), as the release helper
data_release/make_release.py and the Sage helpers both use them.

extreme_examples_data/labels.jsonl - one line per function: its label, the model it was
    first recorded with, and the versions that added and last changed it. A label's
    ordinal depends on load order, so add_function_NF takes it from this file to keep
    labels stable. Written by make_release.py.

extreme_examples_data/releases.jsonl - one line per data version, the rows of the
    data_releases table, which the driver reloads after setup_all drops the table.
"""
import json
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL_FILE = os.path.join(_ROOT, 'extreme_examples_data', 'labels.jsonl')
RELEASE_FILE = os.path.join(_ROOT, 'extreme_examples_data', 'releases.jsonl')

# what compare_labels needs from the database
LABEL_ROWS_QUERY = """SELECT function_id, degree, sigma_one, sigma_two, ordinal, base_field_label,
    (original_model).coeffs AS coeffs FROM functions_dim_1_NF ORDER BY function_id"""

_cache = {}


def format_label(row, dimension=1):
    return f"{dimension}.{row['sigma_one']}.{row['sigma_two']}.{row['ordinal']}"


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def _write_jsonl(entries, path):
    with open(path, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(json.dumps(entry, sort_keys=True, separators=(',', ':')) + '\n')


def read_label_file(path=None):
    """All entries of the label file, [] if there is none yet (before v1.0.0)."""
    return _read_jsonl(path or LABEL_FILE)


def write_label_file(entries, path=None):
    _write_jsonl(sorted(entries, key=lambda e: (e['degree'], e['label'])), path or LABEL_FILE)


def entries_with_hashes(degree, sigma_one, sigma_two, path=None):
    """The label file's entries for these hashes; the file is read once per change."""
    path = path or LABEL_FILE
    stamp = os.path.getmtime(path) if os.path.exists(path) else None
    if path not in _cache or _cache[path][0] != stamp:
        index = {}
        for e in read_label_file(path):
            index.setdefault((e['degree'], e['sigma_one'], e['sigma_two']), []).append(e)
        _cache[path] = (stamp, index)
    return _cache[path][1].get((degree, sigma_one, sigma_two), [])


def compare_labels(entries, rows):
    """
    Compare the label file's entries with the database's rows (LABEL_ROWS_QUERY). Returns
    {'changed': [(file label, database label)], 'missing': [file label], 'new': [database
    label]}. changed: the same model with another label. missing: a file label no database
    row has, whose model isn't stored either. new: a map the file doesn't have yet, which
    is expected until the next release adds it.
    """
    rows = [dict(r) for r in rows]
    db_labels = {format_label(r) for r in rows}
    file_labels = {e['label'] for e in entries}
    by_model = {(r['base_field_label'], json.dumps(r['coeffs'])): format_label(r) for r in rows}
    changed, missing = [], []
    for e in entries:
        if e['label'] in db_labels:
            continue
        now = by_model.get((e['field'], json.dumps(e['coeffs'])))
        if now is None:
            missing.append(e['label'])
        else:
            changed.append((e['label'], now))
    moved = {new for _, new in changed}
    return {'changed': changed, 'missing': missing,
            'new': sorted(db_labels - file_labels - moved)}


def read_release_file(path=None):
    return _read_jsonl(path or RELEASE_FILE)


def write_release_file(releases, path=None):
    _write_jsonl(sorted(releases, key=lambda r: version_key(r['version'])), path or RELEASE_FILE)


def version_key(version):
    """'1.10.0' -> (1, 10, 0), for ordering versions"""
    return tuple(int(v) for v in version.split('.'))
