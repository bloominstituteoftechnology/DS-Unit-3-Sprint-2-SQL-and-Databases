import sqlite3
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME2 = os.getenv("DB_NAME3")
DB_USER2 = os.getenv("DB_USER3")
DB_PASS2 = os.getenv("DB_PASS3")
DB_HOST2 = os.getenv("DB_HOST3")

conn = psycopg2.connect(dbname=DB_NAME2, 
                        user=DB_USER2,
                        password=DB_PASS2, 
                        host=DB_HOST2)

cursor = conn.cursor()

sl_conn = sqlite3.connect("rpg_db.sqlite3")
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10').fetchall()
print(characters)

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
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
'''

cursor.execute(create_character_table_query)
conn.commit()

for character in characters:

    insert_query = f''' INSERT INTO rpg_characters 
        (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
        {character}
    '''
    cursor.execute(insert_query)

conn.commit()
cursor.close()
conn.close()
