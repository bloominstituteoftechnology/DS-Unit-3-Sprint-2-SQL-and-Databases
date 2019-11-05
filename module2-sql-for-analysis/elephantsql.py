import psycopg2
import sqlite3

dbname = 'yjbbntkp'
user = 'yjbbntkp'
password = 'euAG1JE7Wa6Fb_K9FVhQaU1Y3uLPgj9B'
host = 'salt.db.elephantsql.com'


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()

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
WHERE schemaname <> 'pg_catalog'
and schemaname <> 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES
        """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)


pg_curs.execute('SELECT * FROM charactercreator_character;')
print(pg_curs.fetchall())
pg_curs.close()
pg_curs.commit()



