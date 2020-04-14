import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

#comment queries with what they're doing
query = "SELECT count(distinct character_id) FROM charactercreator_character"
result = cursor.execute(query).fetchall()
print(f"There are {result[0][0]} characters")

for database in ["mage", "thief", "cleric", "fighter"]:
    database_name = "charactercreator_" + database
    query = f"""
    SELECT
        count(distinct character_ptr_id) as character_count
    FROM {database_name}
    """
    result = cursor.execute(query).fetchall()
    print(database, result[0][0])

query = "SELECT count(distinct item_id) FROM armory_item"
result = cursor.execute(query).fetchall()
n_items = result[0][0]
print(f"There are {n_items} items")

query = "SELECT count(distinct item_ptr_id) FROM armory_weapon"
result = cursor.execute(query).fetchall()
n_weapons = result[0][0]
print(f"The percentage of weapons is {n_weapons/n_items:.2f}")

query = """
SELECT
    character_id,
    count(distinct id) as total_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(row[0], row[1])

query = """
SELECT
    charactercreator_character_inventory.character_id,
    count(distinct charactercreator_character_inventory.id)
FROM charactercreator_character_inventory
JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 5
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(row[0], row[1])

#any characters with no items? include them
query = """
SELECT
    count(item_id) as item_count,
    count(distinct character_id) as character_count
FROM charactercreator_character_inventory
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(dict(row))
print("Items per char:", result[0]["item_count"]/result[0]["character_count"])