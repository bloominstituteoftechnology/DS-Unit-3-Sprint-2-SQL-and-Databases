# ETL - Extract Transform Load
# Step1 - Extract, get data out of SQLITE
# Lets focus on character data

import sqlite3
import psycopg2

dbname = 'ppezxvjc'
user = 'ppezxvjc'
password = 't0tlBYAiZvucD-MTqJAG2SPT87DZbVnS'  # Don't commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = "SELECT * FROM charactercreator_character;"
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()
print(len(characters))

# Slice the first five rows
print(f'characters {characters[:5]}')

# Step 1 complete, we have a tuple with all our character data

# Step 2 - Transform
# Our goal is to make a schema to define a table that fits the data
sl_curs.execute('PRAGMA table_info(charactercreator_character);')
print(sl_curs.fetchall())

create_character_table = """
CREATE TABLE if not exists charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
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
print(create_character_table)

# Execute the created table
pg_curs.execute(create_character_table)
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
print(characters[0])
print(characters[0][1:])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_conn.commit()

# Let's look at what we've done
print(pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;'))
print(pg_curs.fetchall())

# Now the data looks the same! But let's check it systematically
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

# We could do more spot checks, but let's loop and check them all
# TODO/afternoon task - consider making this a more formal test
for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

# No complaints - which means they're all the same!
# Closing out cursor/connection to wrap up
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()
