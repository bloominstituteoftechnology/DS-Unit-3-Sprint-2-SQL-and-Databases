#!/usr/bin/env python3

import psycopg2

dbname = 'nhworfxj'
user = 'nhworfxj'
password = 'kP5yE4IqyZ80aWYuhHUkPzrTCrvetxgP'
host = 'balarama.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
        password = password, host = host)

pg_curs = pg_conn.cursor()

import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
print(sl_curs.execute(row_count).fetchall())

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

print(characters[:5])

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

print(str(characters[0][1:]))

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

pg_curs.execute('SELECT * FROM charactercreator_character')
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()