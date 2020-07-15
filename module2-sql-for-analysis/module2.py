
import psycopg2
import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

# sqlite specific 
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall() 
# We need to make a create statement for PostgreSQL that captures these types
SQL_CREATE_TABLE = """
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
params = {"dbname": "rtnktynj",
        'user': 'rtnktynj',
        'password': 'UDZgOFVupQwhuoyRcHtjVt9q1GK-XDtO',  ##need something better
        'host': 'ruby.db.elephantsql.com',
        'port': 5432}


with psycopg2.connect(**params) as conn:     
    with conn.cursor() as curs:            # this code will auto commit if no exception
        curs.execute("DROP TABLE IF EXISTS charactercreator_character;")
        curs.execute(SQL_CREATE_TABLE)
        for character in characters:
            SQL_INSERT_ONE_ROW = """
                                INSERT INTO charactercreator_character
                                (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
                                VALUES """ + str(character[1:]) + ";"
            curs.execute(SQL_INSERT_ONE_ROW)                   # create table

conn.close()