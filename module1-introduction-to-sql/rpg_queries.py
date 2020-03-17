import sqlite3
import os
import numpy as np

FILEPATH = os.path.dirname(__file__)
DB_FILEPATH = os.path.join(FILEPATH, "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

print("Question 1: How many total Characters are there?")
query = 'SELECT COUNT(*) FROM charactercreator_character;'
result = cursor.execute(query).fetchall()
print("ANSWER:", result[0][0])

print("\nQuestion: How many of each specific subclass?")
query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
cleric_count = cursor.execute(query).fetchall()[0][0]
query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
fighter_count = cursor.execute(query).fetchall()[0][0]
query = 'SELECT COUNT(*) FROM charactercreator_mage;'
mage_count = cursor.execute(query).fetchall()[0][0]
query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
necromancer_count = cursor.execute(query).fetchall()[0][0]
query = 'SELECT COUNT(*) FROM charactercreator_thief;'
thief_count = cursor.execute(query).fetchall()[0][0]
print("ANSWER:",
 cleric_count, "clerics,",
 fighter_count, "fighters,",
 mage_count, "mages,",
 necromancer_count, "necromancers,",
 thief_count, "thieves.")

print("\nQuestion: How many total Items?")
query = 'SELECT COUNT(*) FROM armory_item;'
result = cursor.execute(query).fetchall()
print("ANSWER:", result[0][0])

print("\nQuestion: How many of the Items are weapons? How many are not?")
query = 'SELECT COUNT(*) FROM armory_weapon;'
weapon_count = cursor.execute(query).fetchall()[0][0]
query = """
SELECT COUNT(armory_item.name)
FROM armory_item
LEFT JOIN armory_weapon 
ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id IS NULL
"""
non_weapon_count = cursor.execute(query).fetchall()[0][0]
print("ANSWER:", weapon_count, "weapons,", non_weapon_count, "non-weapons")

print("\nQuestion: How many Items does each character have? (Return first 20 rows)")
query = """
SELECT char.name, COUNT(inv.item_id) as item_count
FROM charactercreator_character char
LEFT JOIN charactercreator_character_inventory inv 
ON inv.character_id = char.character_id
GROUP BY char.character_id
LIMIT 20
"""
item_results = cursor.execute(query).fetchall()
print("ANSWER:")
for item in item_results:
    print(item[0], "-", item[1], "items")

print("\nQuestion: How many Weapons does each character have? (Return first 20 rows)")
query = """
SELECT char.name as char_name, count(wep.item_ptr_id) as weapon_count
FROM charactercreator_character char
LEFT JOIN charactercreator_character_inventory inv 
ON inv.character_id = char.character_id
LEFT JOIN armory_weapon wep 
ON inv.item_id = wep.item_ptr_id
GROUP BY char.character_id
LIMIT 20
"""
weapon_results = cursor.execute(query).fetchall()
for item in weapon_results:
    print(item[0], "-", item[1], "weapons")

# Had trouble doing these next two with the AVG() sql function.
# Gonna use python instead and calculate it that way.

print("\nQuestion: On average, how many Items does each Character have?")
count_list = []
for item in item_results:
    count_list.append(item[1])
print("ANSWER:", np.mean(count_list))


print("\nQuestion: On average, how many Weapons does each character have?")
count_list = []
for item in weapon_results:
    count_list.append(item[1])
print("ANSWER:", np.mean(count_list))