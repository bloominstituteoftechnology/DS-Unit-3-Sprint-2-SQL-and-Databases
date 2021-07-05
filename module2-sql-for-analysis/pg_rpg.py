import sqlite3
import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values


# Create pandas dataframes from RPG database tables.
FILEPATH = os.path.dirname(__file__)
DB_FILEPATH = os.path.join(FILEPATH, "..", "module1-introduction-to-sql", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

query = 'SELECT * FROM charactercreator_character;'
character_df = pd.read_sql_query(query, connection)

query = 'SELECT * FROM armory_item;'
armory_df = pd.read_sql_query(query, connection)

cursor.close()
connection.close()

# print(df.to_json(orient='records'))

# Load dataframes onto elephantsql database

load_dotenv() 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor()

query = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
  id SERIAL PRIMARY KEY,
  character_id int,
  name varchar,
  level int,
  exp int,
  hp int,
  strenth int,
  intelligence int,
  dexterity int,
  wisdom int
);
"""

cursor.execute(query)
cursor.execute("SELECT * from charactercreator_character;")
result = cursor.fetchall()

print("Current character count:", len(result))
if len(result) == 0:
    print("No characters in database, adding from CSV.")
    rows = list(character_df.itertuples(index=False, name=None))
    insertion_query = """
    INSERT INTO charactercreator_character (character_id, name, level, exp, hp, strenth, intelligence, dexterity, wisdom) VALUES %s
    """
    execute_values(cursor, insertion_query, rows)

connection.commit()