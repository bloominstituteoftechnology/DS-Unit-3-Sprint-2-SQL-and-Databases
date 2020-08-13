import sqlite3
import psycopg2

# Establish Connection W/ DataBase
dbname = 'ppezxvjc'
user = 'ppezxvjc'
password = 't0tlBYAiZvucD-MTqJAG2SPT87DZbVnS'  # Don't commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Get Data Out of SQLite
sl_conn = sqlite3.connect('Titanic3.db')
sl_curs = sl_conn.cursor()

# Extract All Desired Observations/Rows
get_people = "SELECT * FROM TITANIC"
sl_curs.execute(get_people)
people = sl_curs.fetchall()
# Check Length
print(len(people))

# Print first 5 Rows
print(f'people {people[:5]}')

# Step1 - Completed, we have data in people

# Step2 - Transform
# Goal is to make a schema to define a table that fits the data
sl_curs.execute('PRAGMA table_info(TITANIC);')
print(sl_curs.fetchall())

create_TITANIC_table = """
DROP TABLE if exists TITANIC;
CREATE TABLE if not exists TITANIC (
    Survived INT ,
    Pclass INT,
    Name VARCHAR(100),
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
pg_curs.execute(create_TITANIC_table)
pg_conn.commit()

pg_curs.execute('DROP TABLE if exists TITANIC3,TITANIC4,TITANIC5,TITANIC6')
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
print('tables', pg_curs.execute(show_tables))
print(pg_curs.fetchall())

# Done with step 2 (transform)
# Step 3 - Load!
print(people[0])
print(people[0][1:])
example_insert = """
INSERT INTO TITANIC
(Survived, Pclass, Name, Sex, Age, Siblings_Spouses, Parents_Children,Fare)
VALUES """ + str(people[0][0:]) + ";"

for person in people:
    if "'" in person[2]:
        person = list(person)
        person[2] = person[2].replace("'", "")
        person = tuple(person)
    insert_person = """
    INSERT INTO TITANIC
    (Survived, Pclass,Name, Sex, Age, Siblings_Spouses, Parents_Children, Fare)
    VALUES """ + str(person[0:]) + ";"
    pg_curs.execute(insert_person)

pg_conn.commit()

# Let's look at what we've done first
print(pg_curs.execute('SELECT * FROM TITANIC LIMIT 10;'))
pg_curs.fetchall()

# Now the data looks the same! But let's check it systematically
pg_curs.execute('SELECT * FROM TITANIC;')
pg_people = pg_curs.fetchall()

# TESTS
# We could do more spot checks, but let's loop and check them all
# # TODO/afternoon task - consider making this a more formal test
# for person, pg_person in zip(people, pg_people):
#     assert person == pg_person

# No complaints - which means they're all the same!
# Closing out cursor/connection to wrap up
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()
