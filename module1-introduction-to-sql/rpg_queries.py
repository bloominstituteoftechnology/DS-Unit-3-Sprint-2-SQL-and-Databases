import sqlite3
import os

# Connect to database
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__),
                                 "..", "module1-introduction-to-sql",
                                 "rpg_db.sqlite3")
connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row
print(type(connection))

# Instantiate Cursor
cursor = connection.cursor()
print(type(cursor))

# Total characters
query = """
SELECT count(distinct character_id)
FROM charactercreator_character """
result = cursor.execute(query).fetchall()[0]
print("Total number of characters:", result[0])


# Number of Clerics
query = """
SELECT count(distinct character_ptr_id)
FROM charactercreator_cleric"""
result = cursor.execute(query).fetchall()[0]
print("Total number of Clerics:", result[0])

# Number of Fighters
query = """
SELECT count(distinct character_ptr_id)
FROM charactercreator_fighter"""
result = cursor.execute(query).fetchall()[0]
print("Total number of Fighters:", result[0])

# Number of Mages
query = """
SELECT count(distinct character_ptr_id)
FROM charactercreator_mage"""
result = cursor.execute(query).fetchall()[0]
print("Total number of Mages:", result[0])

# Number of Necromancers
query = """
SELECT count(distinct mage_ptr_id)
FROM charactercreator_necromancer"""
result = cursor.execute(query).fetchall()[0]
print("Total number of Necromancers:", result[0])

# Number of Thieves
query = """
SELECT count(distinct character_ptr_id)
FROM charactercreator_thief"""
result = cursor.execute(query).fetchall()[0]
print("Total number of Thieves:", result[0])

# Total number of items
query = """
SELECT count(item_id)
FROM charactercreator_character_inventory"""
items = cursor.execute(query).fetchall()[0]
print("Total number of items:", items[0])

# Number of weapons
query = """
SELECT count(power) as weapon_count
FROM charactercreator_character_inventory cci
JOIN armory_weapon on armory_weapon.item_ptr_id = cci.item_id"""
weapons = cursor.execute(query).fetchall()[0]
print("Total number of Weapons:", weapons[0])


# How many are not?
# Total number of items - number of weapons
print("Non-weapon items:", (items[0] - weapons[0]))


# Number of items each character has
items_query = """
SELECT
    COUNT(item_id) as item_counts
    ,charactercreator_character_inventory.character_id
FROM
    charactercreator_character_inventory
GROUP BY
    charactercreator_character_inventory.character_id
ORDER BY
    item_counts DESC
LIMIT
    20 """
items = cursor.execute(items_query).fetchall()
for row in items:
    print("-----")
    # using row factories:
    print("Character id, item count")
    print(row["character_id"], row["item_counts"])

# How many weapons does each character have
weapons_query = """
SELECT
    COUNT(power) as weapon_count
    ,cci.character_id
FROM
    charactercreator_character_inventory cci
LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = cci.item_id
GROUP BY
    cci.character_id
ORDER BY
    weapon_count DESC
LIMIT 20"""
weapons = cursor.execute(weapons_query).fetchall()
for row in weapons:
    print("-----")
    # using row factories:
    print("Character id, weapon count")
    print(row["character_id"], row["weapon_count"])

# How many items on average per character
query = """
SELECT
    AVG(item_count)
FROM (
    SELECT
        COUNT(item_id) as item_count
        ,cci.character_id
    FROM
        charactercreator_character_inventory cci
    LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = cci.item_id
    GROUP BY
        cci.character_id
) subq """
result = cursor.execute(query).fetchall()[0]
print("Number of items each character has on average:", result[0])

# How many weapons on average per character
query = """
SELECT
    AVG(weapon_count)
FROM (
    SELECT
        COUNT(power) as weapon_count
        ,cci.character_id
    FROM
        charactercreator_character_inventory cci
    LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = cci.item_id
    GROUP BY
        cci.character_id
) subq """
result = cursor.execute(query).fetchall()[0]
print("Number of weapons each character has on average:", result[0])
