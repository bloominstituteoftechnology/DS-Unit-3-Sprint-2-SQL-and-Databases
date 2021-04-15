import os
import sqlite3
import pandas as pd

# Set up filepath, connection, and cursor
DB_FILEPATH = os.path.join(os.path.dirname(__file__),'rpg_db.sqlite3')
print(DB_FILEPATH)

conn = sqlite3.connect(DB_FILEPATH)
print('CONNECTION:',conn)

def q(query, conn):
    return pd.read_sql(query, conn)

print()

print('1. How many total Characters are there?')

query = '''
SELECT
    count(character_id) as NumCharacters
FROM charactercreator_character
'''

print(q(query, conn),'\n')

# --------------------------------------------
print('2. How many of each specific subclass?')

query = '''
SELECT
    count(f.character_ptr_id) as FighterCount
    ,count(c.character_ptr_id) as ClericCount
    ,count(t.character_ptr_id) as ThiefCount
    ,count(m.character_ptr_id) - count(n.mage_ptr_id) as MageCount
    ,count(n.mage_ptr_id) as NecromancerCount
FROM charactercreator_character as main
LEFT JOIN charactercreator_fighter as f on main.character_id = f.character_ptr_id
LEFT JOIN charactercreator_cleric as c on main.character_id = c.character_ptr_id
LEFT JOIN charactercreator_thief as t on main.character_id = t.character_ptr_id
LEFT JOIN charactercreator_mage as m on main.character_id = m.character_ptr_id
LEFT JOIN charactercreator_necromancer as n on m.character_ptr_id = n.mage_ptr_id
'''

print(q(query, conn),'\n')

# --------------------------------------------
print('3. How many total items?')

query = '''
SELECT
    count(item_id) as ItemCount
FROM armory_item
'''

print(q(query, conn), '\n')

# --------------------------------------------
print('4. How many of the items are weapons? How many are not?')

query = '''
SELECT
    count(armory_weapon.item_ptr_id) as WeaponCount
    ,count(armory_item.item_id) - count(armory_weapon.item_ptr_id) as NonWeaponCount
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
'''

print(q(query,conn), '\n')

# --------------------------------------------
print('5. How many items does each character have (first 20 rows)')

query = '''
SELECT
    character_id as CharacterId
    ,count(item_id) as NumItems
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
'''

print(q(query,conn), '\n')

# --------------------------------------------
print('6. How many weapons does each character have (first 20 rows)')

query = '''
SELECT
	character_id as CharacterId
	,count(aw.item_ptr_id) as NumWeapons
FROM charactercreator_character_inventory as cci
LEFT JOIN armory_weapon as aw on cci.item_id = aw.item_ptr_id
GROUP BY character_id
LIMIT 20
'''

print(q(query, conn), '\n')

# --------------------------------------------
print('7. On average, how many items does each character have?')

query = '''
SELECT
	avg(NumItems) as AverageNumItems
FROM (
	SELECT
    	character_id as CharacterId
    	,count(item_id) as NumItems
	FROM charactercreator_character_inventory
	GROUP BY character_id
)
'''

print(q(query,conn), '\n')

# --------------------------------------------
print('8. On average, how many weapons does each character have?')

query = '''
SELECT
	avg(NumWeapons) as AverageNumWeapons
FROM (
    SELECT
        character_id as CharacterId
        ,count(aw.item_ptr_id) as NumWeapons
    FROM charactercreator_character_inventory as cci
    LEFT JOIN armory_weapon as aw on cci.item_id = aw.item_ptr_id
    GROUP BY character_id
)
'''

print(q(query, conn))