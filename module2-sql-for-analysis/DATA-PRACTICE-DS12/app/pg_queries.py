import psycopg2
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME= os.getenv("DB_NAME", default="oops")
DB_USER= os.getenv("DB_USER", default="oops")
DB_PASSWORD= os.getenv("DB_PASSWORD", default="oops")
DB_HOST= os.getenv("DB_HOST", default="oops")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
print("CONNECTION:", connection)

# cursor.execute('SELECT * from test_table;')
# print("CURSOR:", cursor)

rpg_connection = sqlite3.connect("rpg_db.sqlite3")
rpg_cursor = rpg_connection.cursor()

query = """
SELECT
*
FROM armory_item
"""

item_result = rpg_cursor.execute(query).fetchall()

#
# Table created
#

query= """
CREATE TABLE IF NOT EXISTS armory_item (
  item_id        SERIAL PRIMARY KEY,
  name  varchar(30) NOT NULL,
  value    integer,
  weight   integer
);
"""

cursor.execute(query)

cursor.execute("SELECT * from armory_item;")

result = cursor.fetchall()
print("RESULT:", len(result))


#
# Data insertion
#
for item_obj in item_result:
  insertion_query = f"""
  INSERT INTO armory_item (item_id, name, value, weight)
  VALUES
  {item_obj}
  """
  cursor.execute(insertion_query)


cursor.execute("SELECT * from armory_item;")
result = cursor.fetchall()
print("RESULT:", len(result))

connection.commit()
connection.close()