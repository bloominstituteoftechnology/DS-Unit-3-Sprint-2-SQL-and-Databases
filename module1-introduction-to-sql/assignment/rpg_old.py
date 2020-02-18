"""Module 1 Assignment

Queries ../rpg_db.sqlite3 and reports information.
"""

import os
import sqlite3

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
curs = conn.cursor()

# How many total Characters are there?
query = """
SELECT
    COUNT(DISTINCT character_id) AS character_count
FROM charactercreator_character;
"""
result = curs.execute(query).fetchall()
answer = result[0]['character_count']
print('How many total Characters are there?')
print(answer)

# How many of each specific subclass?
answer = {}
query = """
SELECT
    COUNT(DISTINCT character_ptr_id) as cleric_count
FROM charactercreator_cleric;
"""
result = curs.execute(query).fetchall()
answer['cleric'] = result[0]['cleric_count']

query = """
SELECT
    COUNT(DISTINCT character_ptr_id) as fighter_count
FROM charactercreator_fighter;
"""
result = curs.execute(query).fetchall()
answer['fighter'] = result[0]['fighter_count']

query = """
SELECT
    COUNT(DISTINCT character_ptr_id) as mage_count
FROM charactercreator_mage;
"""
result = curs.execute(query).fetchall()
answer['mage'] = result[0]['mage_count']

query = """
SELECT
    COUNT(DISTINCT mage_ptr_id) as necromancer_count
FROM charactercreator_necromancer;
"""
result = curs.execute(query).fetchall()
answer['necromancer'] = result[0]['necromancer_count']

query = """
SELECT
    COUNT(DISTINCT character_ptr_id) as thief_count
FROM charactercreator_thief;
"""
result = curs.execute(query).fetchall()
answer['thief'] = result[0]['thief_count']

print('How many of each specific subclass?')
print(answer)

# How many total Items?
query = """
SELECT
    COUNT(DISTINCT item_id) as item_count
FROM armory_item;
"""
result = conn.execute(query).fetchall()
answer = result[0]['item_count']
print('How many total Items?')
print(answer)

# How many of the Items are weapons? How many are not?
answer = {'total_items': answer}
query = """
SELECT
    COUNT(DISTINCT item_ptr_id) as weapon_count
FROM armory_weapon;
"""
result = curs.execute(query).fetchall()
answer['weapons'] = result[0]['weapon_count']
answer['not_weapons'] = answer['total_items'] - answer['weapons']
del answer['total_items']

print('How many of the Items are weapons? How many are not?')
print(answer)

# How many Items does each character have? (Return first 20 rows)
query = """
SELECT
    character.character_id
    ,COUNT(inventory.item_id) as item_count
FROM charactercreator_character character
LEFT JOIN charactercreator_character_inventory inventory ON
    inventory.character_id = character.character_id
GROUP BY character.character_id
LIMIT 20;
"""
result = curs.execute(query).fetchall()

print('How many Items does each character have? (Return first 20 rows)')
for row in result:
    output = {}
    for key in row.keys():
        output[key] = row[key]
    print(output)

# How many Weapons does each character have? (Return first 20 rows)
query = """
SELECT
    character.character_id
    ,COUNT(weapon.item_ptr_id) as weapon_count
FROM charactercreator_character character
LEFT JOIN charactercreator_character_inventory inventory ON
    inventory.character_id = character.character_id
LEFT JOIN armory_weapon weapon ON
    weapon.item_ptr_id == inventory.item_id
GROUP BY character.character_id
LIMIT 20
"""
result = curs.execute(query).fetchall()

print('How many Weapons does each character have? (Return first 20 rows)')
for row in result:
    output = {}
    for key in row.keys():
        output[key] = row[key]
    print(output)

# On average, how many Items does each Character have?
query = """
SELECT 
    AVG(item_count) AS avg_items
    ,AVG(weapon_count) AS avg_weapons
FROM (
    SELECT
        character.character_id
        ,COUNT(inventory.item_id) AS item_count
        ,COUNT(weapon.item_ptr_id) AS weapon_count
    FROM charactercreator_character character
    LEFT JOIN charactercreator_character_inventory inventory ON
        inventory.character_id = character.character_id
    LEFT JOIN armory_weapon weapon ON
        weapon.item_ptr_id == inventory.item_id
    GROUP BY character.character_id
)
"""
result = curs.execute(query).fetchall()

print('On average, how many Items does each Character have?')
print(result[0]['avg_items'])

# On average, how many Weapons does each character have?
print('On average, how many Weapons does each character have?')
print(result[0]['avg_weapons'])
