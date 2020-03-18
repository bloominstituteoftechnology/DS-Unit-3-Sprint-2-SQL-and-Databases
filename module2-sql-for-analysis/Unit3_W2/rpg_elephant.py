import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import sqlite3


load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

DB_FILEPATH = 'rpg_db.sqlite3'
connect = sqlite3.connect('rpg_db.sqlite3')
print("CONNECT:", connect)

rpg_db = connect.cursor()
print("CURSOR", rpg_db)

armor_item = """
SELECT
	*
FROM 
	armory_item
"""
leet_items = rpg_db.execute(armor_item).fetchall()

#
# TABLE CREATION
#

query = """
CREATE TABLE IF NOT EXISTS rpg_items (
  item_id SERIAL PRIMARY KEY,
  name varchar(30) NOT NULL,
  value integer,
  weight integer
);
"""

cursor.execute(query)

cursor.execute("SELECT * from rpg_items;")
result = cursor.fetchall()
print("RESULT:", len(result))

#
# DATA INSERTION
#

# APPROACH 1 (hard-coded)
for i in leet_items:
    insertion_query =f"""
    INSERT INTO rpg_items (item_id, name, value, weight)
    VALUES
    {i}
    """
    cursor.execute(insertion_query)

cursor.execute("Select * from rpg_items;")
result = cursor.fetchall()
print("RESULT:", len(result))


# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()