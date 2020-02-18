"""Module 1 Assignment

Queries ../rpg_db.sqlite3 and reports information.
"""

import os
import sqlite3

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
curs = conn.cursor()


def answer(question, query):
    """Print question and answer based on SQL query."""
    print(question)
    result = conn.execute(query).fetchall()
    answer = [
        {key: result[row][key] for key in result[row].keys()}
        for row in range(len(result))
    ]
    for a in answer:
        print(a)


# How many total Characters are there?
query = """
SELECT
    COUNT(DISTINCT character_id) AS character_count
FROM charactercreator_character;
"""
answer('How many total Characters are there?', query)

# How many of each specific subclass?
query = """
SELECT
    *
FROM
    (SELECT COUNT(DISTINCT character_ptr_id) AS Cleric FROM charactercreator_cleric)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Fighter FROM charactercreator_fighter)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Mage FROM charactercreator_mage)
    ,(SELECT COUNT(DISTINCT mage_ptr_id) AS Necromancer FROM charactercreator_necromancer)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Thief FROM charactercreator_thief);
"""
answer('How many of each specific subclass?', query)

# How many total Items?
query = """
SELECT
    COUNT(DISTINCT item_id) AS item_count
FROM armory_item;
"""
answer('How many total Items?', query)

# How many of the Items are weapons? How many are not?
query = """
SELECT
    weapon_count AS weapon
    ,(item_count - weapon_count) AS non_weapon
FROM (
    SELECT
        COUNT(DISTINCT item_id) AS item_count
        ,COUNT(DISTINCT armory_weapon.item_ptr_id) AS weapon_count
    FROM armory_item
    LEFT JOIN armory_weapon ON
        armory_weapon.item_ptr_id = armory_item.item_id
)
"""
answer('How many of the Items are weapons? How many are not?', query)

# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
query = """
SELECT
    inventory.character_id AS character_id
    ,COUNT(inventory.item_id) AS item_count
    ,COUNT(armory_weapon.item_ptr_id) AS weapon_count
FROM charactercreator_character_inventory inventory
LEFT JOIN armory_weapon ON
    armory_weapon.item_ptr_id = inventory.item_id
GROUP BY inventory.character_id
LIMIT 20;
"""
answer('How many Items and Weapons does each character have?', query)

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
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
answer('On average, how many Items and weapons does each Character have?', query)
