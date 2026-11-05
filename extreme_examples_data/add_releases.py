from psycopg2.extras import Json

from functions.release_files import read_release_file

###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

#########################

#setup_all drops data_releases: put back the versions already released
for r in read_release_file():
    my_cursor.execute("""INSERT INTO data_releases
        (version, release_date, git_commit, sage_version, lmfdb_date, doi, notes, summary)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (version) DO NOTHING""",
        [r['version'], r['release_date'], r['git_commit'], r['sage_version'],
         r['lmfdb_date'], r.get('doi'), r['notes'], Json(r['summary'])])

my_session.commit()
