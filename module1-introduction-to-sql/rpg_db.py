"""- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
"""


import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


#How many total Characters are there?
count_characters = 'SELECT COUNT(*) FROM charactercreator_character;' 
print(curs.execute(count_characters).fetchall())

# How many of each specific subclass?
count_cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
count_fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
count_mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
count_necromancer = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
count_thief = 'SELECT COUNT(*) FROM charactercreator_thief;'

print('Cleric number:', curs.execute(count_cleric).fetchall())
print('Fighter number:', curs.execute(count_fighter).fetchall())
print('Mage number:', curs.execute(count_mage).fetchall())
print('Necromancer number:', curs.execute(count_necromancer).fetchall())
print('Thief number:', curs.execute(count_thief).fetchall())

#How many total Items?
count_armory = 'SELECT COUNT(*) FROM armory_item;'
print('Item count:', curs.execute(count_armory).fetchall())

#How many of the Items are weapons? How many are not?
count_weapons = 'SELECT COUNT(DISTINCT armory_item.item_id) FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id;'
print('Total weapon count in items:', curs.execute(count_weapons).fetchall())

count_not_weapons = 'SELECT COUNT(*) FROM armory_item, armory_weapon WHERE armory_item.item_id <> armory_weapon.item_ptr_id;'
print('Total item count in items that are not weapons', curs.execute(count_not_weapons).fetchall()[0][0])

#How many Items does each character have? (Return first 20 rows)
# item_cleric = 'SELECT COUNT(*) FROM charactercreator_character_inventory, charactercreator_cleric WHERE charactercreator_cleric.character_ptr_id = charactercreator_character_inventory.character_id LIMIT 20;'
# print('Cleric item count:', curs.execute(item_cleric).fetchall()[0][0]) 

# item_fighter = 'SELECT COUNT(*) FROM charactercreator_character_inventory, charactercreator_fighter WHERE charactercreator_fighter.character_ptr_id = charactercreator_character_inventory.character_id;'
# print('Fighter item count:', curs.execute(item_fighter).fetchall()[0][0]) 

# item_mage = 'SELECT COUNT(*) FROM charactercreator_character_inventory, charactercreator_mage WHERE charactercreator_mage.character_ptr_id = charactercreator_character_inventory.character_id;'
# print('Mage item count:', curs.execute(item_mage).fetchall()[0][0]) 

# item_necro = 'SELECT COUNT(*) FROM charactercreator_character_inventory, charactercreator_necromancer WHERE charactercreator_necromancer.mage_ptr_id = charactercreator_character_inventory.character_id;'
# print('Necromancer item count:', curs.execute(item_necro).fetchall()[0][0]) 

# item_thief = 'SELECT COUNT(*) FROM charactercreator_character_inventory, charactercreator_thief WHERE charactercreator_thief.character_ptr_id = charactercreator_character_inventory.character_id;'
# print('Thief item count:', curs.execute(item_thief).fetchall()[0][0]) 

query = 'SELECT character_id, COUNT(distinct item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20'
result = curs.execute(query).fetchall()
print('\n Each character has the following number of items:')
for each in result:
    print(f'Character {each[0]} has {each[1]} item(s).')

# How many Weapons does each character have? (Return first 20 rows)
query = '''
    SELECT
        charactercreator_character_inventory.character_id,
        count(distinct item_ptr_id)
    FROM
        charactercreator_character_inventory
        LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
    GROUP BY
        character_id
    LIMIT
        20
'''
result = curs.execute(query).fetchall()
print('\nEach character has the following number of weapons:')
for each in result:
    print(f'Character {each[0]} has {each[1]} weapon(s).')

# - On average, how many Items does each Character have?
query = '''
    SELECT 
        COUNT(item_id)  as a, COUNT(distinct character_id) as b 
    FROM 
        charactercreator_character_inventory
        '''
result = curs.execute(query).fetchall()
print(f'\nOn average, each character has {result [0][0] / result [0][1]} items.')

# On average, how many Weapons does each character have?

query = '''
    SELECT
        COUNT(item_ptr_id) as a, count(distinct character_id) as b
    FROM
        charactercreator_character_inventory
        LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
'''
result = curs.execute(query).fetchall()
print(f'\nOne average, each character has {result[0][0] / result[0][1]} weapons\n')


