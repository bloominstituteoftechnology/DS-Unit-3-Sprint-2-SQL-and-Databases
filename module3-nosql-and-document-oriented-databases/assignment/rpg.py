import psycopg2
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")

# Connect to Database
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                           password=DB_PASS, host=DB_HOST)

# Need a cursor to execute queries
pg_curs = pg_conn.cursor()

# Create a table - SERIAL = database will enumerate counting up, data = can be null
create_table_statement = '''
CREATE TABLE test_table2 (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
'''

# Inserting into the table - JSON (JavaScript Object Notation) not supported by sqlite3 = can be passed into PostgreSQL key-value pairs
insert_statement = '''
INSERT INTO test_table2 (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
'''
# The next four lines were already executed and therefore, will cause the script to fail if ran again
# pg_curs.execute(create_table_statement)
# pg_conn.commit()
# pg_curs.execute(insert_statement)
# pg_conn.commit()

# Query time! I messed up 'test_table' so I had to make it 'test_table2'
query = '''
SELECT * FROM test_table2;
'''
pg_curs.execute(query)

# Printing ALL from test_table2
print('---------------------------------------------------------------------------------------')
print(pg_curs.fetchall())

# SQLite connection
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# # Using charactercreator_character table
row_count = """
        SELECT COUNT(*)
        FROM charactercreator_character
"""
print('---------------------------------------------------------------------------------------')
print(sl_curs.execute(row_count).fetchall())

# copy characters table from SQLite to PostgreSQL using Python
# Step 1 - Get the characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()
print(characters[:5])
print(len(characters))

# Step 2 - Transform - SQL to SQL
# To load into PostgreSQL we need... a TABLE!!

# Make a new table w/ appropriate schema
print('--------------------------------------------------------------------------------------')
print(sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())

# Yields:
[(0, 'character_id', 'integer', 1, None, 1),
(1, 'name', 'varchar(30)', 1, None, 0),
(2, 'level', 'integer', 1, None, 0),
(3, 'exp', 'integer', 1, None, 0),
(4, 'hp', 'integer', 1, None, 0),
(5, 'strength', 'integer', 1, None, 0),
(6, 'intelligence', 'integer', 1, None, 0),
(7, 'dexterity', 'integer', 1, None, 0),
(8, 'wisdom', 'integer', 1, None, 0)]

create_character_table = '''
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
'''
# pg_curs.execute(create_character_table)
# pg_conn.commit()

# Optional - showing postgresql intervals
show_tables = '''
SELECT
    *
FROM
    pg_catalog.pg_tables
WHERE
    schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
'''

pg_curs.execute(show_tables)
table = pg_curs.fetchall()

# For 1 character (character[0])
# example_insert = '''
# INSERT INTO charactercreator_character
# (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
# VALUES ''' + str(characters[0][1:]) + ';'

# For ALL characters
for character in characters:
  insert_character = '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES ''' + str(character[1:]) + ';'
  pg_curs.execute(insert_character)
# pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
print('--------------------------------------------------------------------------------------')
print(pg_curs.fetchall())
breakpoint()
