"""I already ran this code in my command line, so I don't need to run it again.
As such, I'm putting this in a separate file.
"""

import psycopg2
import sqlite3
from password_example import password
# For this to work, the above line instead has to be
# "from password import password." If you want the password.py
# file with my actual password, please contact me.


dbname = 'gubyurua'
user = 'gubyurua'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

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

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

pg_curs.close()
pg_conn.commit()