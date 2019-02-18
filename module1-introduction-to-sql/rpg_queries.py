"""
Provides answers to some basic questions about sample RPG data
"""

import sqlite3

# initialize connection
connection = sqlite3.connect('rpg_db.sqlite3')

# How many total Characters are there?
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
        connection.cursor().execute(total_thief_query).fetchone()[0])

# How many total Items?


# How many of the Items are weapons? How many are not?
# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?