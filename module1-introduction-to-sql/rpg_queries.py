# introtoSQLassignment.py


import os
import sqlite3
from numpy import mean


# construct a path to wherever your database exists
# DB_FILEPATH = "data/rpg_db.sqlite3"

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dicts
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# QUESTION 1 - How many total Characters are there?

query1 = "SELECT COUNT(*) FROM charactercreator_character;"

result1 = cursor.execute(query1).fetchone()[0]

print("ANSWER 1:", result1, "total Characters")

# ANSWER 1: 302 Characters


# QUESTION 2: How many of each specific subclass?

query2a = "SELECT COUNT(*) FROM charactercreator_cleric;"

result2a = cursor.execute(query2a).fetchone()[0]

print("ANSWER 2:", result2a, "Clerics")

# ANSWER 2: 75 Clerics


query2b = "SELECT COUNT(*) FROM charactercreator_fighter;"

result2b = cursor.execute(query2b).fetchone()[0]

print("ANSWER 2:", result2b, "Fighters")

# ANSWER 2: 68 Fighters


query2c = "SELECT COUNT(*) FROM charactercreator_mage;"

result2c = cursor.execute(query2c).fetchone()[0]

print("ANSWER 2:", result2c, "Mages")

# ANSWER 2: 108 Mages


query2d = "SELECT COUNT(*) FROM charactercreator_thief;"

result2d = cursor.execute(query2d).fetchone()[0]

print("ANSWER 2:", result2d, "Thieves")

# ANSWER 2: 51 Thieves


query2e = "SELECT COUNT(*) FROM charactercreator_necromancer;"

result2e = cursor.execute(query2e).fetchone()[0]

print("ANSWER 2:", result2e, "Necromancers")

# ANSWER 2: 11 Necromancers


# QUESTION 3: How many total Items?

query3 = "SELECT COUNT(*) FROM armory_item;"

result3 = cursor.execute(query3).fetchone()[0]

print("ANSWER 3:", result3, "total Items")

# ANSWER 3: 174 total Items


# QUESTION 4: How many of the Items are weapons? How many are not?

query4 = "SELECT COUNT(*) FROM armory_weapon;"

result4 = cursor.execute(query4).fetchone()[0]

print("ANSWER 4:", result4, "of the Items are Weapons.", result3-result4, "Items are not Weapons.")

# ANSWER 4: 37 Items are Weapons. 137 items are not Weapons.


# QUESTION 5: How many Items does each character have? (Return first 20 rows)

query5 = """
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

result5 = cursor.execute(query5).fetchall()

result5_fin = []
items = []
for i in result5:
    items = i[1]
    result5_fin.append(items)

print("ANSWER 5: Each character has", str(result5_fin), "Items in the first 20 rows")

# ANSWER 5: Each character has [3, 3, 2, 4, 4, 1, 5, 3, 4, 4, 3, 3, 4, 4, 4, 1, 5, 5, 3, 1] Items in the first 20 rows


# QUESTION 6: How many Weapons does each character have? (Return first 20 rows)

query6 = """
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id IN(
SELECT item_ptr_id from armory_weapon
)
GROUP BY character_id
LIMIT 20;
"""

result6 = cursor.execute(query6).fetchall()

result6_fin = []
items = []
for i in result6:
    items = i[1]
    result6_fin.append(items)

print("ANSWER 6: Each character has", str(result6_fin), "Weapons in the first 20 rows")

# ANSWER 6: Each character has [2, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 2, 3, 2, 2, 2, 1, 1, 1] Weapons in the first 20 rows


# QUESTION 7: On average, how many Items does each Character have?

query7 = """
SELECT AVG(items) FROM (SELECT COUNT(item_id) as items
FROM charactercreator_character_inventory GROUP BY character_id);"""

result7 = cursor.execute(query7).fetchall()

print("ANSWER 7: On average, each character has", "{:.2f}".format(mean(result7)), "Items")

# ANSWER 7: 2.9735099337748343 Items


# QUESTION 8: On average, how many Weapons does each character have?

query8 = """
SELECT AVG(items) FROM (
SELECT COUNT(item_id) as items
FROM charactercreator_character_inventory as inv
JOIN armory_weapon as weapon
ON weapon.item_ptr_id = inv.item_id
GROUP BY character_id);"""

result8 = cursor.execute(query8).fetchall()

print("ANSWER 8: On average, each character has",	"{:.2f}".format(mean(result8)), "Weapons")

# ANSWER 8: 1.3096774193548386 Weapons 
