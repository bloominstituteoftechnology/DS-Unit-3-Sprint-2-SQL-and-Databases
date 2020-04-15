import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


# Set up filepath, connection, and cursor
envpath = os.path.join(os.getcwd(),'..', '.env')
load_dotenv(envpath)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

sql_url = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
print(sql_url)

engine = create_engine(sql_url)
print('ENGINE:',engine)

def q(query, conn):
    return pd.read_sql(query, engine)

print()

print('1. How many total Characters are there?')

query = '''
SELECT
    count(character_id) as NumCharacters
FROM charactercreator_character
'''

print(q(query, engine),'\n')

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

print(q(query, engine),'\n')

# --------------------------------------------
print('3. How many total items?')

query = '''
SELECT
    count(item_id) as ItemCount
FROM armory_item
'''

print(q(query, engine), '\n')

# --------------------------------------------
print('4. How many of the items are weapons? How many are not?')

query = '''
SELECT
    count(armory_weapon.item_ptr_id) as WeaponCount
    ,count(armory_item.item_id) - count(armory_weapon.item_ptr_id) as NonWeaponCount
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
'''

print(q(query, engine), '\n')

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

print(q(query, engine), '\n')

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

print(q(query, engine), '\n')

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
) AS derivedTable
'''

print(q(query, engine), '\n')

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
) AS derivedTable
'''

print(q(query, engine))