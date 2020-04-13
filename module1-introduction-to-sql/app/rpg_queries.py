# app/rpg_queries.py

import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = '''
SELECT count(DISTINCT character_id)
FROM charactercreator_character
'''
total_characters = cursor.execute(query).fetchall()
print("Total Characters:", total_characters[0][0]) # > 302

query2 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_mage
'''
mage_characters = cursor.execute(query2).fetchall()
print("Total Mage:", mage_characters[0][0]) # > 108

query3 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_thief
'''
thief_characters = cursor.execute(query3).fetchall()
print("Total Thiefs:", thief_characters[0][0]) # > 51

query4 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_cleric
'''
cleric_characters = cursor.execute(query4).fetchall()
print("Total Cleric:", cleric_characters[0][0]) # > 75

query5 = '''
SELECT count(DISTINCT character_ptr_id)
FROM charactercreator_fighter
'''
fighter_characters = cursor.execute(query5).fetchall()
print("Total Fighters:", fighter_characters[0][0]) # > 68