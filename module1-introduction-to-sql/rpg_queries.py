import sqlite3
# import os
# print(os.listdir())
conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')

crs = conn.cursor()

# How many total Characters are there?
print('\nHow many total Characters are there?\n')
crs.execute(
    """SELECT count(*)
    FROM charactercreator_character; """
) 

print(f'There are {crs.fetchone()[0]} total characters') #Total 302

# How many of each specific subclass?
print('\nHow many of each specific subclass?\n')

#mage
crs.execute(
    'SELECT count(*)'
    'FROM charactercreator_mage;'
) 
mages = crs.fetchone()[0]

#necromancer
crs.execute(
    'SELECT count(*)'
    'FROM charactercreator_necromancer;'
) 
necros = crs.fetchone()[0]

#Thief
crs.execute(
    'SELECT count(*)'
    'FROM charactercreator_thief;'
) 
thieves = crs.fetchone()[0]

#cleric
crs.execute(
    'SELECT count(*)'
    'FROM charactercreator_cleric;'
) 
clerics = crs.fetchone()[0]

#fighter
crs.execute(
    'SELECT count(*)'
    'FROM charactercreator_fighter;'
) 
fighters = crs.fetchone()[0]

print(f'There are {mages} total mages ({necros} necromancers)'
    f'\n{thieves} total thieves'
    f'\n{clerics} total clerics'
    f'\n{fighters} total fighters') 

# How many total Items?
print('\nHow many total Items?\n')

crs.execute(
    'SELECT count(*)'
    'FROM armory_item;'
)

items = crs.fetchone()[0]

print(f'There are {items} total items')
# How many of the Items are weapons? How many are not?
print('\nHow many of the Items are weapons? How many are not?\n')

crs.execute(
    'SELECT count(*)'
    'FROM armory_weapon;'
)

weapons = crs.fetchone()[0]

print(f'Of the {items}, {weapons} of them are weapons, '
       f'therefore, {items - weapons} items are non-weapons')

# How many Items does each character have? (Return first 20 rows)
print('\nHow many Items does each character have? (Return first 20 rows)\n')

crs.execute(
    'SELECT *, count(*)'
    'FROM charactercreator_character_inventory '
    'GROUP BY character_id LIMIT 20;'
)

to_print = [f'character_id {row[1]} has {row[3]} items' for row in crs.fetchall()]
print(*to_print, sep='\n')

# How many Weapons does each character have? (Return first 20 rows)
print('\nHow many Weapons does each character have?'
        '(Returns first 20 characters with weapons)\n')

crs.execute(
    'SELECT *, count(*)'
    'FROM charactercreator_character_inventory, armory_weapon '
    'WHERE item_id = item_ptr_id '
    'GROUP BY character_id LIMIT 20;'
)

to_print = [f'character_id {row[1]} has {row[5]} weapon(s)' for row in crs.fetchall()]
print(*to_print, sep='\n')

# On average, how many Items does each Character have?
print('\nOn average, how many Items does each Character have?\n')

crs.execute(
    'SELECT avg(counts) as avg_item_count '
    'FROM (SELECT count(*) as counts '
    'FROM charactercreator_character_inventory GROUP BY character_id);'
)
print(f'Characters have {(crs.fetchone())[0]} items on average')

# On average, how many Weapons does each character have?
print('\nOn average, how many Weapons does each character have?\n')

crs.execute(
    'SELECT avg(counts) as avg_item_count '
    'FROM (SELECT count(*) as counts '
    'FROM charactercreator_character_inventory, armory_weapon '
    'WHERE item_id = item_ptr_id GROUP BY character_id);'
)
print(f'Characters have {(crs.fetchone())[0]} weapons on average')

# But I feel the weapon questions are wrong or answered wrong,
#  because these would be OF THOSE THAT HAVE WEAPONS, ...