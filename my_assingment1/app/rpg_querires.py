import sqlite3
import os

DB_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")



conn = sqlite3.connect(DB_filepath)


curs1 = conn.cursor()

# query for finding out the total number of characters in the 
# game
totalChars_query = """
                    SELECT 
	count(distinct(character_id))
FROM charactercreator_character_inventory;
"""
numThiefs = """
    SELECT
	count(DISTINCT(charactercreator_thief.character_ptr_id))
FROM charactercreator_thief
"""
numClerics = """
    SELECT
	count(DISTINCT(charactercreator_cleric.character_ptr_id))
FROM charactercreator_cleric
"""
numMage = """
    SELECT
	count(DISTINCT(charactercreator_mage.character_ptr_id))
FROM charactercreator_mage
"""

numFighter = """
    SELECT
	count(DISTINCT(charactercreator_fighter.character_ptr_id))
FROM charactercreator_fighter
"""

numItems = """
    SELECT
	count(DISTINCT(armory_item.item_id))
FROM armory_item
"""

nunItems_with_weapons = """
    SELECT
	
	
	count(distinct(armory_item.item_id)) as armory_id
	,armory_weapon.power as weapon_power
FROM armory_item 
LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
group by weapon_power
"""


numItems_per_char = """
    SELECT
	
	
	charactercreator_character_inventory.character_id
	,count(DISTINCT(charactercreator_character_inventory.item_id)) as num_items
FROM 
	charactercreator_character_inventory
group by charactercreator_character_inventory.character_id
LIMIT 20
"""

numWeapons_per_character = """
    SELECT
	
	
	charactercreator_character_inventory.character_id
	,count(DISTINCT(armory_weapon.power)) as num_weapons
FROM 
	charactercreator_character_inventory
LEFT JOIN armory_item on armory_item.item_id = charactercreator_character_inventory.item_id
LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
group by charactercreator_character_inventory.character_id
LIMIT 20
"""


average_num_weapons = """
	SELECT 
	count(DISTINCT armory_weapon.item_ptr_id)/
	count(distinct charactercreator_character.character_id) --as Average_weapons_per_char
	
	
from  charactercreator_character
inner JOIN charactercreator_character_inventory on
	charactercreator_character.character_id = 
	charactercreator_character_inventory.character_id
LEFT JOIN armory_item on 
	charactercreator_character_inventory.character_id = 
	armory_item.item_id
Left Join armory_weapon on 
	armory_item.item_id = armory_weapon.item_ptr_id
"""

average_items_per_char = """

	SELECT --*
	count(DISTINCT armory_item.item_id)/
	count(distinct charactercreator_character.character_id) --as Average_weapons_per_char
	
	
from  charactercreator_character
inner JOIN charactercreator_character_inventory on
	charactercreator_character.character_id = 
	charactercreator_character_inventory.character_id
LEFT JOIN armory_item on 
	charactercreator_character_inventory.character_id = 
	armory_item.item_id
Left Join armory_weapon on 
	armory_item.item_id = armory_weapon.item_ptr_id	
"""

result1 = curs1.execute(totalChars_query).fetchall()
print("First Query", result1)

result2 = curs1.execute(numThiefs).fetchall()
print("Total Thieves:", result2)

result3 = curs1.execute(numClerics).fetchall()
print("Total Clerics:", result3)

result4 = curs1.execute(numMage).fetchall()
print("Total Mage", result4)

result5 = curs1.execute(numFighter).fetchall()
print("Total Fighter:", result5)

result6 = curs1.execute(numItems).fetchall()
print("Number of items: ", result6)

results7 = curs1.execute(nunItems_with_weapons).fetchall()
print("Number of items that are weapons and not: ",results7)

results8 = curs1.execute(numItems_per_char).fetchall()
print("Number of items per character:  ", results8)


result9 = curs1.execute(numWeapons_per_character).fetchall()
print("Number of Weapons per character:  ", result9)

result10 = curs1.execute(average_items_per_char).fetchall()
print("Average number of items per character: ", result10)

result11 = curs.execute(average_num_weapons).fetchall()
print("Average number of weapons per character: ", result11)