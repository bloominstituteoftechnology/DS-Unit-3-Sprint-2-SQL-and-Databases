# pipenv shell
# pipenv install psycopg2-binary
!pip install psycopg2-binary

import psycopg2
import sqlite3


sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# List of Tuples
get_characters = "SELECT * FROM charactercreator_character;"
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()
print(len(characters))
characters[:5]

# Transform
sl_curs.execute('PRAGMA table_info(charactercreator_character);')
sl_curs.fetchall()

# Create Statement
create_character_table = """
CREATE TABLE charactercreator_character (
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
dbname = 'aozsohiy'
user = 'aozsohiy'  
password = '1q4lTsuwMLB-JndNWIMzj7jjHwmd-6Ze'  
host = 'isilo.db.elephantsql.com'

# Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
  curs.close()
  conn.close()
  pg_conn = psycopg2.connect(dbname=dbname, user=user,
                             password=password, host=host)
  pg_curs = pg_conn.cursor()
  return pg_conn, pg_curs

pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)

### IF FUNCTION DOESN'T WORK
# pg_conn = psycopg2.connect(dbname=dbname, user=user,
# password=password, host=host)
# pg_curs = pg_conn.cursor()

# Execute the create table
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
pg_curs.execute(show_tables)
pg_curs.fetchall()

# Load
characters[0]


characters[0][1:]

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)  

# Insert Loop
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)



pg_conn.commit()

# Check
pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
pg_curs.fetchall()


pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

# Spot checks
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

# Closing cursor/connection
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()