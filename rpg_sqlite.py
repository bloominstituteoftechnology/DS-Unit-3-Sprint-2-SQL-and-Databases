import sqlite3 as sql
""" import sqlite3 as sql"""

conn = sql.connect('rpg_db.sqlite3')
""" connect is like loading data to be able to work on it """
curs = conn.cursor()
""" cursor is an object that actually let's us work on out data """
# that's how we create a query
cleric_query = """SELECT character.character_id, character.name, cleric.using_shield
FROM charactercreator_character AS character,
charactercreator_cleric AS cleric
WHERE character.character_id = cleric.character_ptr_id
AND character.character_id = 166;"""
# pirnt the query
print(cleric_query)
# executing the query
curs.execute(cleric_query)
# don't know why we stored it result while we never use result for anything
result = curs.execute(cleric_query)
# fetchone fetches the first row of the query result it's more like .head() in pandas
print(curs.fetchone())

""" Need to rerun/re-execute cleric_query (query) to be able to fetch again """
curs
curs.execute(cleric_query)
print(curs.fetchall())

""" Question1. How many total Characters are there? """

total_char_query = """SELECT character.name
FROM charactercreator_character AS character;"""
curs.execute(total_char_query)
result = curs.execute(total_char_query)
print(curs.fetchall())

""" Question 2: How many of each specific subclass?"""
specific_class_query = ("""SELECT
                (SELECT COUNT(*) FROM charactercreator_cleric) AS Clerics,
                (SELECT COUNT(*) FROM charactercreator_fighter) AS Fighters,
                (SELECT COUNT(*) FROM  charactercreator_mage) AS Mages,
                (SELECT COUNT(*) FROM  charactercreator_thief) AS Thieves,
                (SELECT COUNT(*) FROM  charactercreator_necromancer) AS Necromancers""")
curs.execute(specific_class_query)
result = curs.execute(specific_class_query)
print(curs.fetchall())

""" Question 3: How many total Items? """
total_items_query = """SELECT COUNT(armory_item.item_id)
FROM armory_item;"""
curs.execute(total_items_query)
result = curs.execute(total_items_query)
print(curs.fetchall())

""" Question 4: How many of the Items are weapons? How many are not?
Part A:  """

no_of_weapon_items_query = """SELECT COUNT(*)
FROM armory_item
WHERE item_id IN (SELECT distinct item_ptr_id FROM armory_weapon)"""
curs.execute(no_of_weapon_items_query)
result = curs.execute(no_of_weapon_items_query)
print(curs.fetchall())

""" Question 4: How many of the Items are weapons? How many are not?
Part B:  """
no_of_not_weapons_items_query = """SELECT COUNT(*)
FROM armory_item
WHERE item_id NOT IN (SELECT distinct item_ptr_id FROM armory_weapon)"""
curs.execute(no_of_not_weapons_items_query)
result = curs.execute(no_of_not_weapons_items_query)
print(curs.fetchall())

""" Question 5: How many Items does each character have? (Return first 20 rows) """

itmes_each_char_have_query = """SELECT character.character_id, 
COUNT (inventory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = inventory.character_id
AND armory.item_id = inventory.item_id
GROUP BY character.character_id
LIMIT 20;"""

curs.execute(itmes_each_char_have_query)
result = curs.execute(itmes_each_char_have_query)
print(curs.fetchall())


weapons_each_char_have_query = """ SELECT character.character_id, 
COUNT (armory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = armory.item_id
AND inventory.item_id = armory.item_id
GROUP BY character.character_id
LIMIT 20;"""

curs.execute(weapons_each_char_have_query)
result = curs.execute(weapons_each_char_have_query)
print(curs.fetchall())

""" On average, how many Items does each Character have? """
avg_itmes_each_char = """SELECT character.character_id, 
AVG (inventory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = inventory.character_id
AND armory.item_id = inventory.item_id
GROUP BY character.character_id"""
curs.execute(avg_itmes_each_char)
result = curs.execute(avg_itmes_each_char)
print(curs.fetchall())

""" Q8: On average, how many Weapons does each character have? """
avg_weapons_each_char = """ SELECT character.character_id, 
AVG (armory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = armory.item_id
AND inventory.item_id = armory.item_id
GROUP BY character.character_id;
"""
curs.execute(avg_weapons_each_char)
result = curs.execute(avg_weapons_each_char)
print(curs.fetchall())
