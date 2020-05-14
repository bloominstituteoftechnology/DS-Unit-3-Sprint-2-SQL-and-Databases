import os
from dotenv import load_dotenv
import psycopg2
import sqlite3
load_dotenv()

#Sqlite connection

SQ_DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

sq_connection = sqlite3.connect(SQ_DB_FILEPATH)

sq_cursor = sq_connection.cursor()

#row_count = 'SELECT COUNT (*) FROM charactercreator_character'
#rc = sq_cursor.execute(row_count).fetchall()
#print(rc)
#Postgre connection

RPGE_NAME = os.getenv("RPGE_NAME")
RPGE_USER = os.getenv("RPGE_USER")
RPGE_PASSWORD = os.getenv("RPGE_PASSWORD")
RPGE_HOST = os.getenv("RPGE_HOST")

pg_connection = psycopg2.connect(dbname=RPGE_NAME, user=RPGE_USER, password=RPGE_PASSWORD, host=RPGE_HOST)
#print("CONNECTION:", pg_connection)

pg_cursor = pg_connection.cursor()
#print("CURSOR:", pg_cursor)

# looking at scema

#scema = sq_cursor.execute('PRAGMA table_info(charactercreator_character);').fetchall()
#print(scema)
# creating a new table

create_character_table = """
CREATE TABLE IF NOT EXISTS charactercreator_character(
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

pg_cursor.execute(create_character_table)
pg_connection.commit()


get_character = """
SELECT * FROM charactercreator_character;
"""
characters = sq_cursor.execute(get_character).fetchall()

#print(characters[0])

# Insert
for x in characters:
    insert = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES
        """ + str(x[1:]) + ";"
        #print(insert)
    pg_cursor.execute(insert)
pg_connection.commit()