import psycopg2

dbname = 'taymbqyq'
user = 'taymbqyq'
password = 'JOslYoz4AmPe2QkmWYVlOpHUWziadEzM'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall(), '\n')

 
import sqlite3
 
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
sl_curs.execute("""
    SELECT COUNT(*) 
    FROM charactercreator_character;
    """)
rows = sl_curs.fetchall()
print(rows)

sl_curs.execute("""
    SELECT COUNT(DISTINCT name) 
    FROM charactercreator_character;
    """)
unique = sl_curs.fetchall()
print(unique)

sl_curs.execute('SELECT * FROM charactercreator_character;')
characters = sl_curs.fetchall()
print(characters[0])
print(characters[-1])
print(len(characters))

sl_curs.execute('PRAGMA table_info(charactercreator_character);')
print(sl_curs.fetchall(), '\n')


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
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
print(pg_curs.fetchall())
print(characters[0])
print(str(characters[0][1:]))

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"
print(example_insert)

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)
pg_curs.execute('SELECT * from charactercreator_character;')
pg_characters = pg_curs.fetchall()
print(characters[0:3], '\n')
print(pg_characters[0:3])

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

pg_curs.close()
pg_conn.commit()