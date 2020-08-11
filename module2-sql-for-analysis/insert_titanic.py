# Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
# thinking about the schema to make sure it is appropriate for the columns.
# [Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
# be useful. Once it is set up, write a `insert_titanic.py` script that uses
# `psycopg2` to connect to and upload the data from the csv, and add the file to
# our repo. Then start writing PostgreSQL queries to explore the data!

import psycopg2
import pandas as pd
import csv

# Looks similar to sqlite3, but needs auth/host info to connect
# Note - this is sensitive info (particularly password)
# and shouldn't be checked into git! More on how to handle next week

dbname = "ajkuvccu"
user = "ajkuvccu"  # ElephantSQL happens to use same name for db and user
password = "FBOFpSpFdAFrxYUG-DBqN39wDQ0Mjc4V"  # Sensitive! Don't share/commit
host = "isilo.db.elephantsql.com"

def create_type_class():
    type_class_statement = """
    CREATE TYPE class as ENUM ('1', '2', '3');
    """

    pg_curs.execute(type_class_statement)
    pg_conn.commit()  # "Save" by committing

def drop():
    pg_curs.execute("DROP TABLE titanic")
    pg_conn.commit()  # "Save" by committing

# Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

if __name__ == "__main__":
    # If we make too many connections, the database complains! Be sure to close
    # cursors and connections
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    pg_curs = pg_conn.cursor()  # Works the same as SQLite!

    # We're connected, but db is empty
    # Let's run a simple example to populate (from the tk)
    create_table_statement = """
    CREATE TABLE titanic (
    survived boolean,
    pclass class,
    name varchar(100),
    sex varchar(6),
    age float,
    siblings_spouses_aboard integer,
    parents_children_aboard integer,
    fare float
    );
    """
    # NOTE - these types are PostgreSQL specific. This won't work in SQLite!

    pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)

    #pg_curs.execute(create_table_statement)
    pg_conn.commit()  # "Save" by committing

    with open('titanic.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skipe the header row.
        for row in reader:
            pg_curs.execute(
            "INSERT INTO titanic VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
    pg_conn.commit()

    pg_curs.execute("SELECT * FROM 'public'.'titanic' LIMIT 100")
    pg_conn.commit()  # "Save" by committing