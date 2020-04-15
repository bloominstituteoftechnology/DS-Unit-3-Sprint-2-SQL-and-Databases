import os
import psycopg2
import json
import sqlite3
from dotenv import load_dotenv
from psycopg2.extras import execute_values

# adds contents of the .env file to our enviornment
# looking in the .env file for env variables
load_dotenv()

### Connect to ElephantSQL-hosted PostgreSQL

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
conn_pg = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
conn_sql = sqlite3.connect('rpg_db.sqlite3')

curr_pg = conn_pg.cursor()
curr_sql = conn_sql.cursor()

armory_item_query = "SELECT * FROM armory_item;"
# armory_item_results = curr_sql.execute(armory_item_query).fetchall()

armory_item_schema = ('''
CREATE TABLE armory_item(
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    value INTEGER,
    weight INTEGER
);
''')

# charactercreator_character_query = "SELECT * FROM charactercreator_character;"
# charactercreator_character_results = curr_sql.execute(charactercreator_character_query).fetchall()
# charactercreator_character_schema = ('''
# CREATE TABLE charactercreator_character(
#     character_id SERIAL PRIMARY KEY,
#     name VARCHAR(30),
#     level INTEGER,
#     exp INTEGER,
#     hp INTEGER,
#     strength INTEGER,
#     intelligence INTEGER,
#     dexterity INTEGER,
#     wisdom INTEGER
# );
# ''')

# curr_pg.execute(table_schema)
# conn_pg.commit()

# change columns to charactercreator_character and its columns
insertion_query = f"INSERT INTO armory_item (item_id, name, value, weight) VALUES %s"

execute_values(curr_pg, insertion_query, charactercreator_character_results)
conn_pg.commit()
