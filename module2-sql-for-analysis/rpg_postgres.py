import psycopg2
import sqlite3
from .password import password


FILE_PATH = 'rpg_db_raw.sqlite3'

USER = 'ssiictbn'
DB_NAME = 'ssiictbn'
PASSWORD = password()
HOST = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = DB_NAME,
                           user = USER,
                          password = PASSWORD,
                          host = HOST)

sl_conn = sqlite3.connect(FILE_PATH)

pg_cur = pg_conn.cursor()
sl_cur = sl_conn.cursor()

def refresh():
    command = 'DROP TABLE IF EXISTS charactercreator_character'
    pg_cur.execute(command)

refresh()

create_char_table = """CREATE TABLE charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT);"""

pg_cur.execute(create_char_table)

chars = sl_cur.execute('SELECT * from charactercreator_character').fetchall()

for char in chars:
    insert_char = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(char[1:]) + ";"
    pg_cur.execute(insert_char)

pg_cur.close()
pg_conn.commit()







