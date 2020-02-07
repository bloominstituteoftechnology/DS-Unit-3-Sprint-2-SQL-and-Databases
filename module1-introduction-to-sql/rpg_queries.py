import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Get total number of characters
query = 'SELECT COUNT(*) FROM charactercreator_character;'
num_characters = curs.execute(query).fetchall()
print("Total number of characters:", num_characters[0][0])

# Get number of characters of each class
query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
num_clerics = curs.execute(query).fetchall()
print("Total number of clerics:", num_clerics[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
num_fighters = curs.execute(query).fetchall()
print("Total number of fighters:", num_fighters[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_mage;'
num_mages = curs.execute(query).fetchall()
print("Total number of mages:", num_mages[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
num_necro = curs.execute(query).fetchall()
print("Total number of necromancers:", num_necro[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_thief;'
num_thieves = curs.execute(query).fetchall()
print("Total number of thieves:", num_thieves[0][0])

# Get total number of items
query = 'SELECT COUNT(*) FROM armory_item;'
num_items = curs.execute(query).fetchall()
print("Total number of items:", num_items[0][0])

# Get total number of weapons
query = 'SELECT COUNT(*) FROM armory_weapon;'
num_weapons = curs.execute(query).fetchall()
print('Total number of weapons:', num_weapons[0][0])

print('Total number of non-weapons:', num_items[0][0] - num_weapons[0][0])

# Get number of character items for first 20 characters
query = '''SELECT
	chars.character_id
	,chars.name
	,COUNT(inv.item_id) AS item_count
FROM charactercreator_character AS chars
LEFT JOIN charactercreator_character_inventory AS inv
	ON chars.character_id = inv.character_id
GROUP BY 1
LIMIT 20'''
num_char_items = curs.execute(query).fetchall()
print('Items per character for first 20 characters:')
for char in range(len(num_char_items)):
    print(num_char_items[char][1],
            "-",
            num_char_items[char][2])

# Get number of weapons for first 20 characters
query = '''
SELECT
	chars.character_id
	,chars.name
	,COUNT(DISTINCT weap.item_ptr_id) as weapon_count
FROM charactercreator_character AS chars
LEFT JOIN charactercreator_character_inventory AS inv
	ON chars.character_id = inv.character_id
LEFT JOIN armory_weapon AS weap
	ON inv.item_id = weap.item_ptr_id
GROUP BY 1
LIMIT 20
'''
num_char_weapons = curs.execute(query).fetchall()
print('Weapons per character for first 20 characters:')
for char in range(len(num_char_weapons)):
    print(num_char_weapons[char][1],
            "-",
            num_char_weapons[char][2])

# Get average items
query = '''
SELECT
	AVG(item_count) as avg_items_per_char
FROM (
SELECT
	chars.character_id
	,chars.name
	,COUNT(inv.item_id) AS item_count
FROM charactercreator_character AS chars
LEFT JOIN charactercreator_character_inventory AS inv
	ON chars.character_id = inv.character_id
GROUP BY 1
LIMIT 20
)
'''
avg_items = curs.execute(query).fetchone()
print('Average items per character:', avg_items[0])

# Get average weapons
query = '''
SELECT
	AVG(weapon_count) as avg_weapons_per_char
FROM (
SELECT
	chars.character_id
	,chars.name
	,COUNT(DISTINCT weap.item_ptr_id) as weapon_count
FROM charactercreator_character AS chars
LEFT JOIN charactercreator_character_inventory AS inv
	ON chars.character_id = inv.character_id
LEFT JOIN armory_weapon AS weap
	ON inv.item_id = weap.item_ptr_id
GROUP BY 1
)
'''
avg_weapons = curs.execute(query).fetchone()
print('Average weapons per character:', avg_weapons[0])