import sqlite3
import psycopg2

dbname = 'bpecpenu'
user = 'bpecpenu'
password = 'aqJWJbtfkIqQ1oloxEGdC-bEJau3JA4E'
host = 'otto.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, 
                        user=user, 
                        password=password, 
                        host=host)

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

sl_conn = sqlite3.connect('rpg_db copy.sqlite3')
sl_curs = sl_conn.cursor()
sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()
sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character;').fetchall()
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
characters[0]
characters[-1]
len(characters)

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

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
and schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

example_insert = """
INSERT INTO charactercreator_character 
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ';'

print(example_insert)

for character in characters:
    insert_chracter = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ';'
    # print(insert_chracter)\
    pg_curs.execute(insert_chracter)

pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_characters = pg_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

characters[0]
pg_characters[0]

for character, pg_character in zip(characters, pg_characters):
    assert characters == pg_character