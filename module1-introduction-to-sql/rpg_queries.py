import os
import sqlite3

# Connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')
cursor = connection.cursor()

# How many total Characters are there?
query = "SELECT COUNT(*) FROM charactercreator_character;"
result = cursor.execute(query).fetchall()
print("-----------------")
print("TOTAL CHARACTERS:", result[0][0])
print("-----------------")

# How many of each specific subclass?
for subclass in ('cleric', 'fighter', 'mage', 'necromancer', 'thief'):
    name = 'charactercreator_'+subclass
    query = "SELECT COUNT(*) FROM "+name+";"
    result = cursor.execute(query).fetchall()
    print(f'TOTAL {subclass}s: {result[0][0]}')
print("-----------------")

# How many total Items?
result = cursor.execute("SELECT COUNT(*) FROM armory_item;").fetchall()
print("TOTAL ITEMS:", result[0][0])
print("-----------------")

# How many of the Items are weapons?
query = """
    SELECT COUNT(item_id)
    FROM armory_item
    WHERE item_id IN (
        SELECT DISTINCT item_ptr_id
        FROM armory_weapon)
    """
result = cursor.execute(query).fetchall()
print("TOTAL WEAPONS:", result[0][0])
print("-----------------")

# How many are not?
query = """
    SELECT COUNT(item_id)
    FROM armory_item
    WHERE item_id NOT IN (
        SELECT DISTINCT item_ptr_id
        FROM armory_weapon)
    """
result = cursor.execute(query).fetchall()
print("TOTAL OTHER ITEMS:", result[0][0])
print("-----------------")

# How many Items does each character have? (Return first 20 rows)
query = """
    SELECT name, COUNT(item_id) as total_items
    FROM charactercreator_character_inventory cci
        JOIN charactercreator_character cc
        ON cci.character_id=cc.character_id
    GROUP BY name
    LIMIT 20
    """
result = cursor.execute(query).fetchall()
print("TOTAL NUMBER OF ITEMS PER CHARACTER:")
for row in result:
    print(f'{row[0]} has {row[1]} items')
print("-----------------")

# How many Weapons does each character have? (Return first 20 rows)
query = """
    SELECT name, COUNT(item_id) as total_items
    FROM charactercreator_character_inventory cci
        JOIN charactercreator_character cc
        ON cci.character_id=cc.character_id
    WHERE item_id IN (
        SELECT DISTINCT item_ptr_id
        FROM armory_weapon
    )
    GROUP BY name
    LIMIT 20
    """
result = cursor.execute(query).fetchall()
print("TOTAL NUMBER OF WEAPONS PER CHARACTER:")
for row in result:
    print(f'{row[0]} has {row[1]} weapons')
print("-----------------")

# On average, how many Items does each Character have?
query = """
   SELECT AVG(total_items)
   FROM (
    SELECT name, COUNT(item_id) as total_items
    FROM charactercreator_character_inventory cci
        JOIN charactercreator_character cc
        ON cci.character_id=cc.character_id
    GROUP BY name)
    """
result = cursor.execute(query).fetchall()
print(f'On average, each character has {result[0][0]:.2f} items')
print("-----------------")

# On average, how many Weapons does each character have?
query = """
   SELECT AVG(total_items)
   FROM (
    SELECT name, COUNT(item_id) as total_items
    FROM charactercreator_character_inventory cci
        JOIN charactercreator_character cc
        ON cci.character_id=cc.character_id
    WHERE item_id IN (
        SELECT DISTINCT item_ptr_id
        FROM armory_weapon
    )
    GROUP BY name)
    """
result = cursor.execute(query).fetchall()
print(f'On average, each character has {result[0][0]:.2f} weapons')
print("-----------------")
