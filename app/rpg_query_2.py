import os
import sqlite3
from pprint import pprint
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import sqlite3
import pandas as pd
import numpy as np

DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..','data', 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv()

RPG_NAME = os.getenv("RPG_NAME")
RPG_USER = os.getenv("RPG_USER")
RPG_PASSWORD = os.getenv("RPG_PASSWORD")
RPG_HOST = os.getenv("RPG_HOST")

connection = psycopg2.connect(dbname=RPG_NAME, user=RPG_USER, password=RPG_PASSWORD, host=RPG_HOST)
print(type(connection))

cursor = connection.cursor()
print("CURSOR", cursor)



connection = psycopg2.connect(dbname=RPG_NAME, user=RPG_USER, password=RPG_PASSWORD, host=RPG_HOST)

cursor = connection.cursor()
print(type(cursor))

queries = [
    """SELECT count (DISTINCT character_id) 
        FROM charactercreator_character;""",
    """SELECT COUNT(DISTINCT character_ptr_id) 
        FROM charactercreator_mage;""",
    """SELECT COUNT(DISTINCT character_ptr_id) 
        FROM charactercreator_thief;""",
    """SELECT COUNT(DISTINCT character_ptr_id) 
        FROM charactercreator_cleric;"""

]
for query in queries:
    print("--------------")
    #print(f"QUERY: '{query}'")
    results = cursor.execute(query).fetchall()
    #print("RESULTS:", type(results))
    print(results)

    print(type(results[0])) 

# QUERIES BELOW ARE WORKING ON TABLE PLUS, BUT GETTING ERROR HERE

#SELECT COUNT(DISTINCT character_ptr_id)
#FROM charactercreator_fighter  
# 
# SELECT count (item_id)
#FROM armory_item
# 
# SELECT count(item_ptr_id)
#FROM armory_weapon
# 
# SELECT c.name, COUNT(i.item_id) as item_count
#FROM charactercreator_character c
#LEFT JOIN charactercreator_character_inventory i
#ON i.character_id = c.character_id
#GROUP BY c.character_id
#LIMIT 20  

#SELECT c.name as c_name, COUNT(w.item_ptr_id) as w_count
#FROM charactercreator_character c
#LEFT JOIN charactercreator_character_inventory i
#ON i.character_id = c.character_id
#LEFT JOIN armory_weapon w 
#ON i.item_id = w.item_ptr_id
#GROUP BY c.character_id
#LIMIT 20

connection.commit()