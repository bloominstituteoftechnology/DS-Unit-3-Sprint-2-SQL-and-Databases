import os
import sqlite3

DB_FILEPATE = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATE)

cursor = connection.cursor()

# How many total Characters
query = 'SELECT count(DISTINCT character_id) FROM charactercreator_character'
result = cursor.execute(query).fetchall()
print('Number of total characters:', result[0][0], '\n')

# How many of each specific subclass?
clerics = 'SELECT count(DISTINCT character_ptr_id) as Number_of_Clerics FROM charactercreator_cleric'
fighters = 'SELECT count(DISTINCT character_ptr_id) as Number_of_Fighters FROM charactercreator_fighter'
mages = 'SELECT count(DISTINCT character_ptr_id) as Number_of_Mages FROM charactercreator_mage'
necromancers = 'SELECT count(DISTINCT mage_ptr_id) as Number_of_Necromancers FROM charactercreator_necromancer'
thieves = 'SELECT count(DISTINCT character_ptr_id) as Number_of_Theives FROM charactercreator_thief'
subclass = [clerics, fighters, mages, necromancers, thieves]
for x in subclass:
    result = cursor.execute(x).fetchall()
    print('Number of clerics, fighter, mages, necromancers, and thieves, respectively:', result[0][0])
print('\n')

# how many total items?
query = 'SELECT count(DISTINCT item_id) FROM armory_item'
item_result = cursor.execute(query).fetchall()
print(f'Total number of items: {item_result[0][0]}', '\n')

# How many of the items are wepons? How many are not?
query = 'SELECT count(DISTINCT item_ptr_id) FROM armory_weapon'
weapon_result = cursor.execute(query).fetchall()
num = weapon_result[0][0]
print(f'Number of weapons: {num}, Number of not weapons: {item_result[0][0] - num}', '\n')

# How many items does each character have? (first 20)
query = 'SELECT charactercreator_character.name, COUNT(charactercreator_character_inventory.item_id) as item_count FROM charactercreator_character_inventory JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id GROUP BY name ORDER BY item_count DESC LIMIT 20'
result = cursor.execute(query).fetchall()
print('Top 20 characters with the most items:')
for i in range(0, len(result)):
    print(f'{i+1}: {result[i][0]} has {result[i][1]} items')
print('\n')

# How many weapons does each character have? (first 20)
query = 'SELECT charactercreator_character.name, COUNT(charactercreator_character_inventory.item_id) as item_count FROM charactercreator_character_inventory JOIN charactercreator_character on charactercreator_character_inventory.character_id = charactercreator_character.character_id JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY name ORDER BY item_count DESC LIMIT 20'
result = cursor.execute(query).fetchall()
print('Top 20 characters with the most weapons:')
for i in range(0, len(result)):
    print(f'{i+1}: {result[i][0]} has {result[i][1]} weapons')
print('\n')

# On average, how many items does each Character have?
query = 'SELECT avg(item_count) FROM ( SELECT charactercreator_character.name, COUNT(charactercreator_character_inventory.item_id) as item_count FROM charactercreator_character_inventory LEFT JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id GROUP BY name ORDER BY item_count DESC )subq'
result = cursor.execute(query).fetchall()
print(f'Average number of items per character is {result[0][0]:.3f}')

# On average, how many Weapons does each character have?
query = 'SELECT avg(item_count) FROM (SELECT charactercreator_character.name, COUNT(charactercreator_character_inventory.item_id) as item_count FROM charactercreator_character_inventory LEFT JOIN charactercreator_character on charactercreator_character_inventory.character_id = charactercreator_character.character_id JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY name)subq'
result = cursor.execute(query).fetchall()
print(f'Average number of weapons per character is {result[0][0]:.3f}')
