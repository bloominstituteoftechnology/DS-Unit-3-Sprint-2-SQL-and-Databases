'''
This module includes SQL queries to answer the questions from the assignment
for week 12, day 1.
'''


import sqlite3
import numpy as np

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?

query = """SELECT COUNT(character_id)
FROM charactercreator_character AS cc"""

results = curs.execute(query)
print("Total # of characters:", results.fetchall()[0][0])
# How many of each specific subclass?

query = """SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric as cc_cleric"""
results = curs.execute(query)
print("# of clerics:", results.fetchall()[0][0])

query = """SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter"""
results = curs.execute(query)
print("# of fighters:", results.fetchall()[0][0])

query = """SELECT COUNT(character_ptr_id)
FROM charactercreator_mage"""
results = curs.execute(query)
print("# of mages:", results.fetchall()[0][0])

query = """SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer"""
results = curs.execute(query)
print("# of necromancers:", results.fetchall()[0][0])

query = """SELECT COUNT(character_ptr_id)
FROM charactercreator_thief"""
results = curs.execute(query)
print("# of thieves:", results.fetchall()[0][0])

# How many total Items?
query = """SELECT COUNT(item_id)
FROM armory_item"""
results = curs.execute(query)
print("# items:", results.fetchall()[0][0])


# How many of the Items are weapons? How many are not?
query = """SELECT COUNT(ai.item_id)
FROM armory_item as ai, armory_weapon as aw
WHERE ai.item_id = aw.item_ptr_id"""
results = curs.execute(query)
print("Weapons: ", results.fetchall()[0][0])

# Not working
query = """SELECT COUNT(item_id)
FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);"""
results = curs.execute(query)
print("Not weapons: ", results.fetchall()[0][0])

# How many Items does each character have? (Return first 20 rows)
query = """SELECT character_id, item_id, COUNT(*)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;"""
results = curs.execute(query)
matrix = results.fetchall()
item_list = []
for row in matrix:
    item_list.append(row[2])

print("# of items for first 20 characters: ", item_list)

# How many Weapons does each character have? (Return first 20 rows)
query = """SELECT character_id, item_id, COUNT(*)
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id
LIMIT 20;
"""
results = curs.execute(query)
matrix = results.fetchall()
weapon_list = []
for row in matrix:
    weapon_list.append(row[2])

print("# of weapons for first 20 characters: ", weapon_list)
print(sum(weapon_list)/len(weapon_list))
# On average, how many Items does each Character have?

query = """SELECT AVG(counted) FROM (
SELECT character_id, item_id, COUNT(*) AS counted
FROM charactercreator_character_inventory
GROUP BY character_id);
"""
results = curs.execute(query)
print("Avg. Items per Character: ", results.fetchall()[0][0])

# On average, how many Weapons does each character have?

query = """SELECT AVG(counted) FROM (
SELECT character_id, item_id, COUNT(*) AS counted
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id);
"""
results = curs.execute(query)
print("Avg. Weapons per Character: ", results.fetchall()[0][0])
