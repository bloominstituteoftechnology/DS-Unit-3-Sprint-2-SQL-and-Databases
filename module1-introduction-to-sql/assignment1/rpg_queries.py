import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
#print('CONNECTION: ', connection)
cursor = connection.cursor()
#print('CURSOR: ', cursor)

#
### QUESTIONS 
# 

# Question 1: 
print('QUESTION 1: How many total characters?')
query = """SELECT
	count(DISTINCT character_id) as character_count
FROM
	charactercreator_character;"""

# result = cursor.execute(query)
# print('RESULT: ', result)
result2 = cursor.execute(query).fetchall()
print('Total characters: ', result2)

# Question 2: How many of each subclass?
print('QUESTION 2: How many of each subclass?')
query = """SELECT
	count(DISTINCT character_ptr_id) as cleric_count
FROM
	charactercreator_cleric;"""

result2 = cursor.execute(query).fetchall()
print('Total clerics: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as fighter_count
FROM
	charactercreator_fighter;"""

result2 = cursor.execute(query).fetchall()
print('Total fighters: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as mage_count
FROM
	charactercreator_mage;"""

result2 = cursor.execute(query).fetchall()
print('Total mages: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as thief_count
FROM
	charactercreator_thief;"""

result2 = cursor.execute(query).fetchall()
print('Total thieves: ', result2)

query = """SELECT
	count(DISTINCT mage_ptr_id) as necromancer_count
FROM
	charactercreator_necromancer;"""

result2 = cursor.execute(query).fetchall()
print('Total necromancers: ', result2)

# Question 3: How many total items?

query = """SELECT
	count(DISTINCT item_id) as total_items
FROM
	armory_item;"""

result2 = cursor.execute(query).fetchall()
print('Total items: ', result2)

# Question 4: How many of the Items are weapons? How many are not?

#weapons
query = """SELECT
	count(DISTINCT item_id) as total_weapons
FROM
	armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_ptr_id IS NOT NULL;"""

result2 = cursor.execute(query).fetchall()
print('Total weapons: ', result2)

#non-weapons
query = """SELECT
	count(DISTINCT item_id) as total_weapons
FROM
	armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_ptr_id IS NULL;"""

result2 = cursor.execute(query).fetchall()
print('Total non-weapons: ', result2)


# Question 5: How many Items does each character have? (Return first 20 rows)

query = """SELECT
	character_id, count(DISTINCT item_id) as item_count
FROM
	charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;"""

result2 = cursor.execute(query).fetchall()
print('First 20 character_ids and # of items they have: ', result2)

# How many Weapons does each character have? (Return first 20 rows)
query = """SELECT
	character_id, count(item_ptr_id) as weapon_count
	FROM
		charactercreator_character_inventory
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY character_id
    LIMIT 20;"""

result2 = cursor.execute(query).fetchall()
print('First 20 characters and the number of weapons they have:', result2)

# On average, how many Items does each Character have?

query = """SELECT AVG(item_count)
FROM (SELECT
	*, count(DISTINCT item_id)as item_count
FROM
	charactercreator_character_inventory
GROUP BY character_id);"""

result2 = cursor.execute(query).fetchall()
print('Number of items each character has on average: ', result2)


# On average, how many Weapons does each character have?
query = """SELECT AVG(weapon_count)
	FROM (
	SELECT
		character_id, count(item_ptr_id) as weapon_count
	FROM
		charactercreator_character_inventory
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY character_id);"""

result2 = cursor.execute(query).fetchall()
print('Number of weapons each character has on average: ', result2)