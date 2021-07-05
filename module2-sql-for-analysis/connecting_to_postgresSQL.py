import psycopg2
import sqlite3

dbname = 'xindmaoa'
user = 'xindmaoa'
password = 'Xw7UVM2_zcJIP7td-LIHWNDMceV2JeKp'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
                           password = password, host = host)
pg_curs = pg_conn.cursor()

pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall())

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;')
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
print(len(characters))

create_character_table = """
                         CREATE TABLE charactercreator_character
                         (character_id SERIAL PRIMARY KEY,
                          name VARCHAR(30),
                          level INT,
                          exp INT,
                          hp INT,
                          strength INT,
                          intelligence INT,
                          dexterity INT,
                          wisdom INT)
                         """
# pg_curs.execute(create_character_table)

attempted_insert = """
                   INSERT INTO charactercreator_character
                   VALUES
                   """ + str(characters[0])
# pg_curs.execute(attempted_insert)

# pg_conn.commit() 

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

print(pg_characters)

for character in characters[1:]:
    insert_character = """
                       INSERT INTO charactercreator_character
                       VALUES
                       """ + str(character)
    pg_curs.execute(insert_character)

pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
print(pg_characters)