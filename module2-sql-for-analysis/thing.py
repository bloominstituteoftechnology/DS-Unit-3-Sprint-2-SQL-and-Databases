import psycopg2

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

create_char_table = """
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

try:
    pg_curs.execute(create_char_table)

    characters = sl_curs.execute('SELECT * from charactercreator_character').fetchall()

    for char in characters:
        insert_character = """
            INSERT INTO charactercreator_character
            (name, level, exp, hp ,strength, intelligence, dexterity, wisdom)
            VALUES """ + str(char[1:])+";"
        pg_curs.execute(insert_character)
except:
    pass

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
print(pg_characters)

pg_curs.close()
pg_conn.commit()