import os
import sqlite3
import pandas as pd


DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

conn = sqlite3.connect(DATABASE_FILEPATH)
conn.row_factory = sqlite3.Row
#print(type(conn))
cursor = conn.cursor()

#This query is to get a total number of characters.

char_query = """


"""



#This query is to get the total number of each subclass from the characters
query = """ 
SELECT count(rage) AS fighter_count,
	   count(charactercreator_cleric.using_shield) as cleric_count,
	   count(charactercreator_mage.has_pet) as mage_count,
	   count(charactercreator_thief.is_sneaking) as thief_count

FROM charactercreator_character
LEFT JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
LEFT JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
LEFT JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
LEFT JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
where rage IS NOT NULL 
or charactercreator_cleric.using_shield IS NOT NULL 
or charactercreator_mage.has_pet IS NOT NULL
or charactercreator_thief.is_sneaking IS NOT NULL"""

result = cursor.execute(query)
for row in result:
    print(row[:])
# (fighter, cleric, mage thief)

#prints the total amount of items in the game
items_query = """
SELECT
	count(armory_item.item_id) as total_items
	FROM armory_item
"""

item_result = cursor.execute(items_query).fetchall()
print('The total number of items is: ' + str(item_result[0][0]) + '.')


# Getting the number of items that are not weapons
non_weapons_query = """
SELECT count(armory_item.item_id) as total_items
	 FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id IS NULL"""


non_weapons_result = cursor.execute(non_weapons_query).fetchall()
print('Total number of non-weapon items: ' + str((non_weapons_result[0][0])))

#Getting the number of weapons in the game.
weapons_query = """
SELECT count(armory_weapon.item_ptr_id) as total_weapons
FROM armory_weapon"""

weapons_result = cursor.execute(weapons_query).fetchall()
print('The total number of weapons is: ' + str(weapons_result[0][0]))

#showing the amount of items owned by the first 20 characters.
items_per_char_query = """
SELECT charactercreator_character_inventory.character_id,
	   count(armory_item.item_id) as item_count
FROM charactercreator_character_inventory
LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20"""

items_per_char_result = cursor.execute(items_per_char_query)
for row in items_per_char_result:
    print('Character number ' + str(row[0]) + ' has ' + str(row[1]) + ' items in their inventory.')

#shows the amount of weapons the first 20 characters has.
weps_per_char_query = """
SELECT charactercreator_character_inventory.character_id,
	   count(armory_weapon.item_ptr_id) as wep_count
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20"""

weps_per_char_result = cursor.execute(weps_per_char_query)
for row in weps_per_char_result:
    print('Character number ' + str(row[0]) + ' has ' + str(row[0]) + ' weapons in their inventory.')

#Shows the average items owned by all characters
av_items_query = """SELECT AVG(item_count)
FROM (SELECT charactercreator_character_inventory.character_id,
	   count(armory_item.item_id) as item_count
FROM charactercreator_character_inventory
LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
GROUP BY charactercreator_character_inventory.character_id
)"""

av_items_result = cursor.execute(av_items_query).fetchall()
print('The average items owned per character is ' + str(av_items_result[0][0]) + '.')


#Shows the average amount of weapons owned by all characters.
av_weps_query = """SELECT AVG(wep_count)
FROM (SELECT charactercreator_character_inventory.character_id,
	   count(armory_weapon.item_ptr_id) as wep_count
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
)"""
av_weps_result = cursor.execute(av_weps_query).fetchall()
print('The average weapon per character comes out to ' + str(av_weps_result[0][0]))