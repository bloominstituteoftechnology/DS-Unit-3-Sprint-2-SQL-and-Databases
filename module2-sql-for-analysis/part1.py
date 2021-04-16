
# Step 1 - Extract, getting data out of SQLite3
import sqlite3
sl_conn = sqlite3.connect('/Users/noahpovis/Desktop/Lambda Clones/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Our goal - copy the charactercreator_character table
get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

# Step 2 - Transform
# Our goal is to make a schema to define a table that fits this data in Postgres
# Can we check the old schema?
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

## We need to make a create statement for PostgreSQL that captures these types
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
#!pip install psycopg2-binary
import psycopg2
dbname = 'njskuvoi'
user = 'njskuvoi'
password = 'V4hoTmOL2IlAb_98ylcdRtErA_ERzFMo'
host = 'ruby.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor() #works the same as sqlite !

# May need to rerun the .connect to refresh
pg_curs = pg_conn.cursor()
pg_curs.execute(create_character_table)
pg_conn.commit()

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

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)  # Not running, just inspecting

# If we ran that, we'd insert the first character
# But we want them all - loops!
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

  # PostgreSQL cursor needs to fetch in separate step, unlike SQLite
pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
pg_curs.fetchall()

# It inserted, and we can query from our open cursor (because it did the insert)
# But other connections and cursors don't know about it yet - we didn't commit!
pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

# We could do more spot checks, but let's loop and check them all
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

  

