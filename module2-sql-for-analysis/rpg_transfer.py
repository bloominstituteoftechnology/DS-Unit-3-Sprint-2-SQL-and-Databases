"""
Take RPG data from sqlite3 to out elephant sql DB
"""

import psycopg2
import sqlite3

dbname = 'zgexitff'
user = 'zgexitff'
password = 'N-rZTbhw5RUyDylzQH6Cmai2wSD4SGtr'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

"""
Create function to run queries 
"""


# Query for getting the table
get_characters = "SELECT * FROM charactercreator_character;"

sl_curs.execute(get_characters)

characters = sl_curs.fetchall()

create_character_table = """
DROP TABLE IF EXISTS charactercreator_character;
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

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_conn.commit()

if __name__ == '__main__':
    pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
    print(pg_curs.fetchall())
