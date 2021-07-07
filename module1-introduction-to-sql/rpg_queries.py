import sqlite3


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?
query = '''SELECT count(character_id) FROM charactercreator_character;'''
curs.execute(query)
print('How many total Characters are there?')
print(curs.fetchall()[0][0], 'total characters\n')

# How many of each specific subclass?
print('How many of each specific subclass?')
subclasses = ['cleric', 'fighter', 'thief', 'mage']
for subclass in subclasses:
    query = '''SELECT count(character_ptr_id) FROM charactercreator_''' + subclass
    print(curs.execute(query).fetchall()[0][0], subclass)
query = '''SELECT count(mage_ptr_id) FROM charactercreator_necromancer;'''
print(curs.execute(query).fetchall()[0][0], 'necromancer\n')

# How many total Items?
print('How many total Items?')
query_total_items = '''SELECT count(id) FROM charactercreator_character_inventory;'''
print(curs.execute(query_total_items).fetchall()[0][0], 'total items\n')

# How many of the Items are weapons? How many are not?
print('How many of the items are weapons?')
query_total_weapons = '''SELECT count(item_ptr_id)
FROM armory_weapon, charactercreator_character_inventory
WHERE item_ptr_id = item_id;'''
print(curs.execute(query_total_weapons).fetchall()[0][0], 'items that are weapons')
print('How many are not?')
print((curs.execute(query_total_items).fetchall()[0][0]-
curs.execute(query_total_weapons).fetchall()[0][0]), 'items that are not weapons\n')

# How many Items does each character have? (Return first 20 rows)
print('How many Items does each character have?')
query = '''SELECT character_id, count(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20'''
curs.execute(query)
print(curs.fetchall())

# How many Weapons does each character have? (Return first 20 rows)
print('\nHow many Weapons does each character have?')
query = '''SELECT character_id, count(item_id)
FROM charactercreator_character_inventory, armory_weapon
WHERE item_id = item_ptr_id
GROUP BY character_id
LIMIT 20'''
curs.execute(query)
print(curs.fetchall())

# On average, how many Items does each Character have?
print('\nOn average, how many Items does each Character have?')
query = '''SELECT avg(item_count)
FROM
(
SELECT count(item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id
)'''
curs.execute(query)
print('Each character have on average %.4s items' % (curs.fetchall()[0][0]))

# On average, how many Weapons does each character have?
print('\nOn average, how many Weapons does each character have?')
query = '''SELECT avg(weapon_count)
FROM
(
SELECT count(item_id) as weapon_count
FROM charactercreator_character_inventory, armory_weapon
WHERE item_id = item_ptr_id
GROUP BY character_id
)'''
curs.execute(query)
print('Each character have on average %.4s weapons' % (curs.fetchall()[0][0]))
