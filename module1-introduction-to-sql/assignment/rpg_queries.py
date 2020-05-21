import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)
print('CONNECTION:', connection)

cursor = connection.cursor()

# How many total Characters are there?
query = 'SELECT count(distinct character_id) FROM charactercreator_character'
result = cursor.execute(query).fetchall()
print(f'\nThere are {result[0][0]} total characters.')

# How many of each specific subclass?
query = 'SELECT count(distinct character_ptr_id) FROM charactercreator_cleric'
result = cursor.execute(query).fetchall()
print(f'\nThere are {result[0][0]} clerics.')

query = 'SELECT count(distinct character_ptr_id) FROM charactercreator_fighter'
result = cursor.execute(query).fetchall()
print(f'There are {result[0][0]} fighters.')

query = 'SELECT count(distinct character_ptr_id) FROM charactercreator_mage'
result = cursor.execute(query).fetchall()
print(f'There are {result[0][0]} mages.')

query = 'SELECT count(distinct mage_ptr_id) FROM charactercreator_necromancer'
result = cursor.execute(query).fetchall()
print(f'There are {result[0][0]} necromancers (a subset of mages).')

query = 'SELECT count(distinct character_ptr_id) FROM charactercreator_thief'
result = cursor.execute(query).fetchall()
print(f'There are {result[0][0]} thieves.')

# How many total Items?
query = 'SELECT count(distinct item_id) FROM armory_item'
result = cursor.execute(query).fetchall()
print(f'\nThere are {result[0][0]} total items.')

# How many of the Items are weapons? How many are not?
query = 'SELECT count(distinct item_ptr_id) FROM armory_weapon'
result1 = cursor.execute(query).fetchall()
print(f'\n{result1[0][0]} of the items are weapons.')

query = 'SELECT count(distinct item_id) FROM armory_item'
result2 = cursor.execute(query).fetchall()
print(f'{result2[0][0] - result1[0][0]} of the items are not weapons')

# How many Items does each character have? (Return first 20 rows)
query = 'SELECT character_id, count(distinct item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20'
result = cursor.execute(query).fetchall()
print('\nEach character has the following number of items:')
for each in result:
    print(f'Character {each[0]} has {each[1]} item(s).')
'''
# How many Weapons does each character have? (Return first 20 rows)
query = ''
result = cursor.execute(query).fetchall()
print('Each character has the following number of weapons:')
print(result)

# On average, how many Items does each Character have?
query = ''
result = cursor.execute(query).fetchall()
print(f'On average, each character has {result} items.')

# On average, how many Weapons does each character have?
query = ''
result = cursor.execute(query).fetchall()
print(f'One average, each character has {result} items')
'''