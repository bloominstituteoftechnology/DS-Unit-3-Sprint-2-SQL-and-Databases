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
) subq;

SELECT
  CASE
  WHEN cl.character_ptr_id is not null THEN "cleric"
  WHEN f.character_ptr_id is not null THEN "fighter"
  WHEN n.mage_ptr_id is not null THEN "mage-necro"
  WHEN m.character_ptr_id is not null THEN "mage"
  WHEN th.character_ptr_id is not null THEN "thief"
  ELSE "todo"
  END as char_type
  ,count(distinct ch.character_id) as char_count
from charactercreator_character as ch
left join charactercreator_cleric as cl on ch.character_id = cl.character_ptr_id
left join charactercreator_fighter as f on ch.character_id = f.character_ptr_id
left join charactercreator_mage as m on ch.character_id = m.character_ptr_id
left join charactercreator_thief as th on ch.character_id = th.character_ptr_id
-- left join charactercreator_necromancer as n on ch.character_id = n.character_ptr_id
left join charactercreator_necromancer as n on m.character_ptr_id = n.mage_ptr_id
group by char_type

"""

result = cursor.execute(query).fetchall()
for row in result:
    print(row[0])


 