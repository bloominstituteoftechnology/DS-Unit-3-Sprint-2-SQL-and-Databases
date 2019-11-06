#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Question 1
query1 = """
SELECT COUNT(*)
FROM charactercreator_character AS character
"""

curs.execute(query1)
print('The total number of characters is {}.'.format(curs.fetchone()[0]))

#Question 2

# 5 subclasses, implied Inner Join w/ WHERE

query2_cleric = """
SELECT COUNT(character.character_id)
FROM charactercreator_character AS character, charactercreator_cleric AS cleric
WHERE character.character_id = cleric.character_ptr_id

"""

query2_fighter = """
SELECT COUNT(character.character_id)
FROM charactercreator_character AS character, charactercreator_fighter AS fighter
WHERE character.character_id = fighter.character_ptr_id

"""

query2_mage = """
SELECT COUNT(character.character_id)
FROM charactercreator_character AS character, charactercreator_mage AS mage
WHERE character.character_id = mage.character_ptr_id

"""

query2_necromancer = """
SELECT COUNT(character.character_id)
FROM charactercreator_character AS character, charactercreator_necromancer AS nm
WHERE character.character_id = nm.mage_ptr_id

"""

query2_thief = """
SELECT COUNT(character.character_id)
FROM charactercreator_character AS character, charactercreator_thief AS thief
WHERE character.character_id = thief.character_ptr_id

"""

curs.execute(query2_cleric)
print('The number of clerics is {}.'.format(curs.fetchone()[0]))
curs.execute(query2_fighter)
print('The number of fighters is {}.'.format(curs.fetchone()[0]))
curs.execute(query2_mage)
print('The number of mages (magi?) is {}.'.format(curs.fetchone()[0]))
curs.execute(query2_necromancer)
print('The number of necromancers is {}.'.format(curs.fetchone()[0]))
curs.execute(query2_thief)
print('The number of thieves is {}.'.format(curs.fetchone()[0]))

# Question 3

query3 = """
SELECT COUNT(armory.item_id)
FROM armory_item AS armory

"""

curs.execute(query3)
print('The total number of items is {}.'.format(curs.fetchone()[0]))

# Question 4

query4_weapon = """
SELECT COUNT(armory.item_id)
FROM armory_item AS armory, armory_weapon AS weapon
WHERE armory.item_id = weapon.item_ptr_id

"""

query4_not = """SELECT COUNT(*)
FROM armory_item
WHERE item_id NOT IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon)"""


curs.execute(query4_weapon)
print('The number of items that are weapons is {}.'.format(curs.fetchone()[0]))

curs.execute(query4_not)
print('The number of items that are not weapons is {}.'.format(curs.fetchone()[0]))

# Question 5

query5 = """
SELECT COUNT(inventory.item_id) *1.0 / COUNT(DISTINCT inventory.character_id)
FROM charactercreator_character_inventory AS inventory

"""

curs.execute(query5)
print('On average, the number of items that each character has is {}.'.format(curs.fetchone()[0]))

# Question 6

query6 = """
SELECT COUNT(inventory.item_id) *1.0 / COUNT(DISTINCT inventory.character_id)
FROM charactercreator_character_inventory AS inventory, armory_weapon AS weapon
WHERE inventory.item_id = weapon.item_ptr_id

"""

curs.execute(query6)
print('On average, the number of weapons each character has is {}.'.format(curs.fetchone()[0]))