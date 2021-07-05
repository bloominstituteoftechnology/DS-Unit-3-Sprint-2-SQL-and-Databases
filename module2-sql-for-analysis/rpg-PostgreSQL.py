import psycopg2
import sqlite3


dbname = 'bxqrunlw'
user = 'bxqrunlw'
password = 'elThsh7qzZ9c6FByBC7M_EY-3SLq4pRB'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)

pg_curs = pg_conn.cursor()

rpg_db = '/Users/josephbell/Desktop/rpg_db.sqlite3'

sl_connection = sqlite3.connect(rpg_db)
sl_curs = sl_connection.cursor()

get_characters = "SELECT * FROM charactercreator_character"
characters = sl_curs.execute(get_characters).fetchall()

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

pg_conn.commit()
