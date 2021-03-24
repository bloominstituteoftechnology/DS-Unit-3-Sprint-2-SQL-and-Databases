# app/rpg_queries.py

import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# How many total Characters are there?
query = '''
SELECT count(DISTINCT character_id)
FROM charactercreator_character
'''

# How many of each specific subclass?
total_characters = cursor.execute(query).fetchone()
print("Total Characters:", total_characters[0]) # > 302

query2 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_mage
'''
mage_characters = cursor.execute(query2).fetchone()
print("Total Mages:", mage_characters[0]) # > 108

query3 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_thief
'''
thief_characters = cursor.execute(query3).fetchone()
print("Total Thiefs:", thief_characters[0]) # > 51

query4 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_cleric
'''
cleric_characters = cursor.execute(query4).fetchone()
print("Total Clerics:", cleric_characters[0]) # > 75

query5 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_fighter
'''
fighter_characters = cursor.execute(query5).fetchone()
print("Total Fighters:", fighter_characters[0]) # > 68

# How many total Items?
query6 = '''
SELECT count(DISTINCT item_id)
FROM armory_item
'''
total_items = cursor.execute(query6).fetchone()
print("Total Items:", total_items[0]) # > 174

#How many of the Items are weapons? 
query7 = '''
SELECT count(item_ptr_id)
FROM  armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_id = item_ptr_id
'''
total_weapons = cursor.execute(query7).fetchone()
print("Total Weapons:", total_weapons[0]) # > 37

# How many are not?
query8 = '''
SELECT count(DISTINCT item_id)
FROM  armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_id < 138
'''
total_non_weapon_items = cursor.execute(query8).fetchone()
print("Total Items that aren't weapons:", total_non_weapon_items[0]) # > 137

print("How many Items does each character have? (Return first 20 rows)")
query9 = '''
SELECT character_id, COUNT(item_id) as n_items
FROM charactercreator_character_inventory as inventory
GROUP BY inventory.character_id
LIMIT 20
'''
character_items = cursor.execute(query9).fetchall()
print(character_items) 