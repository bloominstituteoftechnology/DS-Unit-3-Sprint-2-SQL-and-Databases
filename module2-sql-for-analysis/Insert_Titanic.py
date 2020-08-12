import sqlite3
import psycopg2

dbname = 'ppezxvjc'
user = 'ppezxvjc'
password = 't0tlBYAiZvucD-MTqJAG2SPT87DZbVnS'  # Don't commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Get Data Out of SQLite
sl_conn = sqlite3.connect('Titanic.db')
sl_curs = sl_conn.cursor()

# Create Table
get_people = "SELECT *  FROM Titanic"
sl_curs.execute(get_people)
people = sl_curs.fetchall()
# Get rows for the table
print(len(people))

# Slice the first 5 Rows
print(f'people {people[:5]}')

# Step1 - Completed, we have data in people

# Step2 - Transform
# Goal is to make a schema to define a table that fits the data
sl_curs.execute('PRAGMA table_info(TITANIC);')
print(sl_curs.fetchall())

create_TITANIC_table = """
CREATE TABLE TITANIC (
    Name INT,
    Sex VARCHAR(30),
    Age FlOAT,
    Siblings_Spouses INT,
    Parents_Children INT,
    Fare FlOAT
    );
    """


# Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)
print(create_TITANIC_table)
pg_conn.commit()

# PostgreSQL comparison to the SQLite pragma
# We can query tables if we want to check
# This is a clever optional thing, showing postgresql internals
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
print(pg_curs.execute(show_tables))
print(pg_curs.fetchall())

# Done with step 2 (transform)
# Step 3 - Load!
print(people[0])
print(people[0][1:])

example_insert = """
INSERT INTO TITANIC
(Name, Sex, Age, Siblings_Spouses, Parents_Children,Fare)
VALUES """ + str(people[0][1:]) + ";"

print(example_insert)

for person in people:
    insert_person = """
    INSERT INTO TITANIC
    (Name, Sex, Age, Siblings_Spouses, Parents_Children, Fare)
    VALUES """ + str(people[1:]) + ";"
    pg_curs.execute(insert_person)

pg_conn.commit()

# Let's look at what we've done
print(pg_curs.execute('SELECT * FROM TITANIC LIMIT 5;'))
print(pg_curs.fetchall())

# Now the data looks the same! But let's check it systematically
pg_curs.execute('SELECT * FROM TITANIC;')
pg_people = pg_curs.fetchall()

# We could do more spot checks, but let's loop and check them all
# TODO/afternoon task - consider making this a more formal test
for person, pg_person in zip(people, pg_people):
    assert person == pg_person

# No complaints - which means they're all the same!
# Closing out cursor/connection to wrap up
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()
