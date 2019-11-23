# Import
import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Character count
query = '''SELECT COUNT(name) FROM charactercreator_character;'''
curs.execute(query)
results = curs.fetchall()
print('\n------------RPG-QUERIES------------')
print('How many total characters are there?')
print(results[0][0])

# Cleric count
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'''
curs.execute(query)
results = curs.fetchall()
print('Clerics:', results[0][0])

# Fighters count
query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
curs.execute(query)
results = curs.fetchall()
print('Fighters:', results[0][0])

# Mage count
query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_mage
WHERE character_ptr_id NOT IN
(
SELECT mage_ptr_id FROM charactercreator_necromancer
);'''
curs.execute(query)
results = curs.fetchall()
print('\nHow many of each specific subclass?')
print('Mages:', results[0][0])

# Necromancer count
query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_mage
WHERE character_ptr_id IN
(
SELECT mage_ptr_id FROM charactercreator_necromancer
);'''
curs.execute(query)
results = curs.fetchall()
print('Necromancers:', results[0][0])

# Thief count
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'''
curs.execute(query)
results = curs.fetchall()
print('Thieves:', results[0][0])

# Total items
query = '''SELECT COUNT (*) FROM armory_item;'''
curs.execute(query)
results = curs.fetchall()
print('How many total items', results[0][0])

# weapon count
query = '''SELECT COUNT(item_ptr_id) from armory_weapon;'''
curs.execute(query)
results = curs.fetchall()
print('Weapons:', results[0][0])

# Non-weapon count
query = '''SELECT count(item_id)
FROM armory_item
WHERE item_id NOT  IN
(
SELECT item_ptr_id FROM armory_weapon
)'''
curs.execute(query)
results = curs.fetchall()
print('Non-weapons:', results[0][0])

# Items by character
query = '''SELECT COUNT(ai.name)
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY cc.character_id
LIMIT 20;'''
curs.execute(query)
results = curs.fetchall()
print('\nHow many items does each character have?(first 20)')
print(results)

# Weapons by character
query = '''SELECT COUNT(ai.name)
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci,
armory_weapon as aw
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id
LIMIT 20;'''
curs.execute(query)
results = curs.fetchall()
print('\nHow many weapons does each character have?(first 20)')
print(results)

# Average items per character

query = '''SELECT AVG(item_count)
FROM (SELECT COUNT(item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id);'''

curs.execute(query)
print('\nOn average how many items does each Character have?')
print(curs.fetchall()[0][0])

# Average weapons per character

query = '''SELECT AVG(item_count)
FROM(SELECT COUNT(item_id) AS item_count
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id);'''

curs.execute(query)
print('\nOn average how many weapons does each character have?')
print(curs.fetchall()[0][0])
curs.close






