import psycopg2
import sqlite3

# Postgresql login credentials
dbname = 'xgbbacwp'
user = 'xgbbacwp'
password = ''
host = 'raja.db.elephantsql.com'

# Create a connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

# Create a cursor and query table
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

# Create a connection to rpg_db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Count number of characters
sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()

# Select character data
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
len(characters)

# Add character table to postgresql database
# Create new table and create the character schema
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
)
"""
pg_curs.execute(create_character_table)

# Insert table into database
insert = """
    INSERT INTO charactercreator_character
    VALUES """ + str(characters[0])
pg_curs.execute(insert)

# Commit changes so the new table/data shows up in database
pg_conn.commit()

# Create a new cursor and query data
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
pg_characters[0]
len(pg_characters)

# Insert the rest of the characters
for character in characters[1:]:
    insert_character = """
    INSERT INTO charactercreator_character
    VALUES """ + str(character)
    pg_curs.execute(insert_character)
pg_conn.commit()

# Create new cursor and inspect data
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
len(pg_characters)
