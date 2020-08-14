# This directory contains a file rpg_db.sqlite3, a database for a hypothetical webapp role-playing game. This test data has dozens-to-hundreds of randomly generated characters across the base classes (Fighter, Mage, Cleric, and Thief) as well as a few Necromancers. Also generated are Items, Weapons, and connections from characters to them. Note that, while the name field was randomized, the numeric and boolean fields were left as defaults.
#
# Use sqlite3 to load and write queries to explore the data, and answer the following questions:
# How many total Characters are there?

"302 Characters"
"""
SELECT COUNT(*) AS Number of Characters
FROM charactercreator_character;
"""

# How many of each specific subclass?
"108 Mage"
""" 
SELECT COUNT(*) AS Mage_Counts 
FROM charactercreator_character AS CC
JOIN charactercreator_mage AS CCM ON CCM.character_ptr_id = CC.character_id;
"""



# How many total Items?
"174 items"
"""
SELECT COUNT(DISTINCT(item_id))
FROM armory_item;
"""


# How many of the Items are weapons? How many are not?
"37 Weapons"
"""
SELECT COUNT(*)
FROM armory_item LEFT JOIN armory_weapon
ON  armory_weapon.item_ptr_id = armory_item.item_id
WHERE armory_weapon.item_ptr_id NOT NULL
"""

"137 Non Weapons"
"""
SELECT COUNT(*)
FROM armory_item LEFT JOIN armory_weapon
ON  armory_weapon.item_ptr_id = armory_item.item_id
WHERE armory_weapon.item_ptr_id is NULL;
"""

# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have?
# On average, how many Weapons//
# does each character have?

import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
