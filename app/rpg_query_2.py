import os
import sqlite3
from pprint import pprint
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

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