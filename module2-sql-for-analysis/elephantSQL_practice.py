import psycopg2
import sqlite3
import pandas as pd

"""Also in my Colab 322 Andrea_elephant_works_assignment_part_1"""

dbname = 'kywjqhga'
user = 'kywjqhga'
password = 'Hhv61Sm9LGB5iDk1dOEDJLjKcOFIQ_pP' 
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, 
                            user=user, 
                            password=password, 
                            host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()
sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall()
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

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
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema'
"""

pg_curs.execute(show_tables)

pg_curs.fetchall()

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES""" + str(characters[0][1:] ) + ';'

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(character[1:]) + ';'
  pg_curs.execute(insert_character) 

  insert_character

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
