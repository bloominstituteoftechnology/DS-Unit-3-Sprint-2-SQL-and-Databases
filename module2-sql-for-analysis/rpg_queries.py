import os
import psycopg2
import sqlite3
from psycopg2.extras import execute_values
import json
import pandas as pd
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

## Setting up PostgreSQL Connection

load_dotenv()

DB_NAME = os.getenv('DB_NAME1', default='Check env variables')
DB_USER = os.getenv('DB_USER1', default='Check env variables')
DB_PASSWORD = os.getenv('DB_PASSWORD1', default='Check env variables')
DB_HOST = os.getenv('DB_HOST1', default='Check env variables')

connection = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                                password = DB_PASSWORD, host = DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("CURSOR:", cursor)

create_table = """CREATE TABLE IF NOT EXISTS rpg_data (character_id SERIAL PRIMARY KEY, 
name varchar(30) NOT NULL, 
level int, 
exp int, 
hp int, 
strength int, 
intelligence int, 
dexterity int, 
wisdom int);
"""

table_query = "SELECT * FROM rpg_data"

cursor.execute(create_table)
cursor.execute(table_query)
connection.commit()
result = cursor.fetchall()
print("RESULT:", type(result))
# print(result)

# Connecting to SQLite3 DB for RPG Data

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_conn.execute('SELECT * FROM charactercreator_character').fetchall()
print(characters)

## Inserting SQLite data into PostgreSQL DB

for character in characters:
  insert_query_pg = f"""INSERT INTO rpg_data (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES 
  {character}"""

  print(insert_query_pg)

  cursor.execute(insert_query_pg)

connection.commit()