import sqlite3
import os

# Construct a path to where your DB exists 
# if DB IS IN "DATA" DIR AND THIS FILE IS IN THE 'APP' DIR
# DB_FILEPATH = "chinook.db"
# NOw we can run file from anywhere in our directory and also run w/o using '/'
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # let's treat our results like object/dict 
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = """
SELECT 
avg(weapon_count) as avg_weapons_per_char
FROM (
    SELECT 
      c.character_id
      ,c.name 
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory i ON c.character_id = i.character_id
    LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
    GROUP BY c.character_id
) subq
"""

result = cursor.execute(query).fetchall()
for row in result:
    print(row[0])


 