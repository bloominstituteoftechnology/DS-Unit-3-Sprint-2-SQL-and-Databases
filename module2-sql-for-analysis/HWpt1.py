#import what we need
import psycopg2 
import sqlite3

#List creds
dbname = 'ensbdkiv'
user =  'ensbdkiv'
password = 's2-dWAkXkoJhwcZe1PQfHN9Tx6i7clv9'
host = 'salt.db.elephantsql.com'

#Set up psycopg connection to postgres
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

#Test connection
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall() #Must be a separate line in postgres

#Set up sqlite connection
sl_conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
#Test Connection
sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()

#Look at data types
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()


#The columns' Data types
"""
[(0, 'character_id', 'integer', 1, None, 1),
(1, 'name', 'varchar(30)', 1, None, 0),
(2, 'level', 'integer', 1, None, 0),
(3, 'exp', 'integer', 1, None, 0),
(4, 'hp', 'integer', 1, None, 0),
(5, 'strength', 'integer', 1, None, 0),
(6, 'intelligence', 'integer', 1, None, 0),
(7, 'dexterity', 'integer', 1, None, 0),
(8, 'wisdom', 'integer', 1, None, 0)]
"""

#Create a table in postgres 
pg_curs.execute(
    """
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
)

#Test the query
pg_curs.execute("""
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
""")
pg_curs.fetchall()

#Pull Characters from the sqlite table
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()

#Test
len(characters)
str(characters[0])

#For loop to inject the characters into the postgres table
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  pg_curs.execute(insert_character)

#Test insertion
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()
pg_characters

#Test that they are the same
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

#Close and Commit changes to postgres db
pg_curs.close()
pg_conn.commit()