"""Import data from titanic.csv file to PostgreSQL database."""

import psycopg2
import csv

# Username and password to be set by user.
username = "TODO"
default_db = "TODO"
new_db = "TODO"
password = "TODO"
host = "TODO"

# Create titanic database if needed.
conn = psycopg2.connect(host=host, dbname=default_db,
                        user=username, password=password)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("""SELECT datname
            FROM pg_database
            WHERE datistemplate = false;""")
if new_db not in [X[0] for X in list(cur.fetchall())]:
    cur.execute('CREATE DATABASE {};'.format(new_db))
    conn.commit()
conn.close()

# Connect to titanic database.
conn = psycopg2.connect(host=host, dbname=new_db,
                        user=username, password=password)
cur = conn.cursor()

# Open titanic.csv and read through.
f = open('titanic.csv', 'r')
reader = csv.reader(f)
for i, row in enumerate(reader):
    if i == 0:
        # Create titanic table if needed.
        cur.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public';""")
        if 'titanic' in [X[0] for X in list(cur.fetchall())]:
            cur.execute("DROP TABLE titanic;")
        cur.execute("""CREATE TABLE titanic(
            id serial PRIMARY KEY,
            survived boolean,
            pclass integer,
            name text,
            sex_male boolean,
            age float,
            siblings_spouses integer,
            parents_children integer,
            fare float
        );""")
    else:
        # Add row from csv.
        surv = None
        if row[0] == "0":
            surv = "f"
        elif row[0] == "1":
            surv = "t"
        sex = None
        if row[3] == "male":
            sex = "t"
        elif row[3] == "female":
            sex = "f"
        format_row = (surv, row[1], row[2], sex,
                      row[4], row[5], row[6], row[7])
        cur.execute(
            """INSERT INTO titanic (survived, pclass, name, sex_male,
                age, siblings_spouses, parents_children, fare)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            format_row
        )
# Commit and close connection.
conn.commit()
conn.close()
