import psycopg2
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")

pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)
pg_curs = pg_conn.cursor()
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

print(sl_curs.execute(
        'PRAGMA table_info(charactercreator_character);'
        ).fetchall())

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

# pg_curs.execute(create_character_table)
# pg_conn.commit()

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)
pg_conn.commit()