# import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

query = "SELECT DISTINCT name FROM charactercreator_character"
chars = cursor.execute(query).fetchall()
q1 = len(chars)

print('\n # How many total characters are there?')
print(f'   Total characters: {q1}')

query1 = "SELECT * FROM charactercreator_cleric"
query2 = "SELECT * FROM charactercreator_fighter"
query3 = "SELECT * FROM charactercreator_mage"
query4 = "SELECT * FROM charactercreator_thief"
query5 = "SELECT * FROM charactercreator_necromancer"

chars = cursor.execute(query1).fetchall()
cleric = len(chars)
chars = cursor.execute(query2).fetchall()
fighter = len(chars)
chars = cursor.execute(query3).fetchall()
mage = len(chars)
chars = cursor.execute(query4).fetchall()
thief = len(chars)
chars = cursor.execute(query5).fetchall()
necromancer = len(chars)

print('\n # How many of each specific subclass?')
print(f'   Cleric: {cleric}')
print(f'   Fighter: {fighter}')
print(f'   Mage: {mage}')
print(f'   Thief: {thief}')
print(f'   Necromancer: {necromancer}')

query6 = "SELECT * FROM charactercreator_character_inventory"
chars = cursor.execute(query6).fetchall()
item = len(chars)

print('\n # How many total Items?')
print(f'   Total Items: {item}')

query7 = "SELECT * FROM armory_weapon"
chars = cursor.execute(query7).fetchall()
weapons = len(chars)

print('\n # How many of the Items are weapons? How many are not?')
print(f'   Weapon Items: {weapons}')
print(f'   Items that are not weapon: {item - weapons}')


query8 = '''
            SELECT
                cc.name,
	            count(distinct ai.item_id) as item_count
            FROM charactercreator_character as cc
            JOIN charactercreator_character_inventory as ci
            ON cc.character_id = ci.character_id
            JOIN armory_item as ai
            on ci.item_id = ai.item_id
            GROUP by cc.name
            LIMIT 20'''
chars = cursor.execute(query8).fetchall()

print('\n # How many Items does each character have? (Return first 20 rows)')
for i in chars:
    print(i)

query9 = '''
         SELECT
	        cc.name,
	        count(distinct aw.item_ptr_id) as weapon_count
         FROM charactercreator_character as cc
         JOIN charactercreator_character_inventory as ci
         ON cc.character_id = ci.character_id
         JOIN armory_weapon as aw
         on ci.item_id = aw.item_ptr_id
         GROUP by cc.name
         LIMIT 20'''

chars = cursor.execute(query9).fetchall()

print('\n # How many Weapons does each character have? (Return first 20 rows)')
for c in chars:
    print(c)
# print(f'First 20 rows of weapons each character have are: \n{chars}')

print('\n # On average, how many Items does each Character have?')
print(f'  On average, Character have {item/q1:.2f} items.')

print('\n # On average, how many Weapons does each Character have?')
print(f'  On average, Character have {weapons/q1:.2f} weapons.')
