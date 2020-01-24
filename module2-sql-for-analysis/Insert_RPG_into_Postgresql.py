import psycopg2
# print(dir(psycopg2))
dbname = 'hvvolzee'
user = 'hvvolzee'
password = 'dAKXw5LOi5bSb_IZtRP6yXMG0jddM_qD'  # Don't commit or share this for security purposes!
host = 'rajje.db.elephantsql.com'  # Port should be included or default
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
#print(pg_conn)
pg_curs = pg_conn.cursor()

import sqlite3
sl_conn  = sqlite3.connect('/Users/julie/Desktop/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
# We care about charactercreator_character table
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
a = sl_curs.execute(row_count).fetchall()
print(a)

# Our goal - copy the characters table from SQLite to PostgreSQL using Python
# Step 1 - E=Extract: Get the Characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

print(characters[:5])
print(len(characters))

# Step 2 - Transform
# In this case, we don't actually want/need to change much
# Because we want to keep all the data
# And we're going from SQL to SQL

# But what do we need to be able to load into PostgreSQL?
# We need to make a new table with the appropriate schema

# What was the old schema? We can get at this with SQLite internals
print(sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())

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
print(pg_curs.fetchall())
print(characters[0])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

# How do we do this for all characters? Loops!
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)
# pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
print(pg_curs.fetchall())

pg_conn.commit()



