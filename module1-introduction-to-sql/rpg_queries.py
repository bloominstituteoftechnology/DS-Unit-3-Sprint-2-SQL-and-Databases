"""
Provides answers to some basic questions about sample RPG data
"""

import sqlite3

# initialize connection
connection = sqlite3.connect('rpg_db.sqlite3')

# How many total Characters are there?
print ('#' * 80)
print ('Character Counts and Information')
total_char_query = """SELECT COUNT(character_id)
                    FROM charactercreator_character"""
print ('Total Character Count:', 
        connection.cursor().execute(total_char_query).fetchone()[0], '\n')

# How many of each specific subclass?
print ('Character by Subclass Counts')
# subclasses: fighter, mage, cleric, necromancer, thief
# fighters
total_fighter_query = """SELECT COUNT(character_ptr_id)
                    FROM charactercreator_fighter"""
print ('Total Fighter Count:', 
        connection.cursor().execute(total_fighter_query).fetchone()[0])
# mages
total_mage_query = """SELECT COUNT(character_ptr_id)
                    FROM charactercreator_mage"""
print ('Total Mage Count:', 
        connection.cursor().execute(total_mage_query).fetchone()[0])
# necromancers
total_necromancer_query = """SELECT COUNT(mage_ptr_id)
                    FROM charactercreator_necromancer"""
print ('Total Necromancer Count (Subclass of Mage):', 
        connection.cursor().execute(total_necromancer_query).fetchone()[0])
# clerics
total_cleric_query = """SELECT COUNT(character_ptr_id)
                    FROM charactercreator_cleric"""
print ('Total Cleir Count:', 
        connection.cursor().execute(total_cleric_query).fetchone()[0])
# theifs
total_thief_query = """SELECT COUNT(character_ptr_id)
                    FROM charactercreator_thief"""
print ('Total Thief Count:', 
        connection.cursor().execute(total_thief_query).fetchone()[0], '\n')

# How many total Items?
print ('#' * 80)
print ('Item Counts and Information')
total_items_query = """SELECT COUNT(item_id)
                    FROM armory_item"""
total_items = connection.cursor().execute(total_items_query).fetchone()[0]
print ('Total Items Count:', total_items)

# How many of the Items are weapons? How many are not?
total_weapons_query = """SELECT COUNT(item_ptr_id)
                      FROM armory_weapon"""
total_weapons = connection.cursor().execute(total_weapons_query).fetchone()[0]
print ('Total Weapons:', total_weapons)
print ('Total Non Deadly Items:', total_items - total_weapons)
# How many Items does each character have? (Return first 20 rows)
print ('\nBreakdown of Item Count by Character')
item_count_query = """SELECT name, count(name)
FROM charactercreator_character_inventory AS inventory
LEFT JOIN  charactercreator_character as characters
ON inventory.character_id = characters.character_id
GROUP BY characters.character_id"""
item_counts = connection.cursor().execute(item_count_query).fetchmany(20)
print ('Sample of Item Count by Character Name:')
for char in item_counts:
    print (char[0], char[1])

# How many Weapons does each character have? (Return first 20 rows)
weapon_count_query = """SELECT name, count(name) AS weapon_count
FROM charactercreator_character_inventory AS inventory
LEFT JOIN  charactercreator_character as characters
ON inventory.character_id = characters.character_id
JOIN armory_weapon
ON inventory.item_id = armory_weapon.item_ptr_id
GROUP BY characters.character_id"""
weapon_counts = connection.cursor().execute(weapon_count_query).fetchmany(20)
print ('\nSample of Weapon Count by Character Name:')
for char in item_counts:
    print (char[0], char[1])

# On average, how many Items does each Character have?
avg_items_query = """SELECT AVG(counts)
FROM (
SELECT name, COUNT(name) as counts
FROM charactercreator_character_inventory AS inventory
LEFT JOIN  charactercreator_character as characters
ON characters.character_id = inventory.character_id 
GROUP BY characters.character_id
)"""
avg_items = connection.cursor().execute(avg_items_query).fetchone()
print ('\nAverage Items Per Character: %.3f' % avg_items[0])
# On average, how many Weapons does each character have?
avg_weapons_query = """SELECT AVG(counts)
FROM (
SELECT name, COUNT(name) as counts
FROM charactercreator_character_inventory AS inventory
LEFT JOIN  charactercreator_character as characters
ON characters.character_id = inventory.character_id 
JOIN armory_weapon
ON inventory.item_id = armory_weapon.item_ptr_id
GROUP BY characters.character_id
)"""
avg_weapons = connection.cursor().execute(avg_weapons_query).fetchone()
print ('Average Items Per Character: %.3f' % avg_weapons[0])