
# rgp_queries.py
import psycopg2
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

DB_FILEPATH = 'rpg_db.sqlite3'
connection = sqlite3.connect('rpg_db.sqlite3')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query_total = """
SELECT
	count()
FROM 
	charactercreator_character -->302 unique IDs
"""

query_class = """
SELECT
	count(distinct charactercreator_cleric.character_ptr_id) as Cleric
	,count(distinct charactercreator_fighter.character_ptr_id) as Fighter
	,count(distinct charactercreator_mage.character_ptr_id) 
    - count(distinct charactercreator_necromancer.mage_ptr_id) as Mage
	,count(distinct charactercreator_necromancer.mage_ptr_id) as Necromancer
	,count(distinct charactercreator_thief.character_ptr_id) as Thief
FROM
	charactercreator_cleric
	,charactercreator_fighter
	,charactercreator_mage
	,charactercreator_necromancer
	,charactercreator_thief
"""

query_item = """
SELECT
    count()
FROM
    armory_item
"""

query_weapon_nonweapon = """
SELECT
	 count(distinct armory_weapon.item_ptr_id)
	,count(distinct armory_item.item_id) as Weapon - count(distinct armory_weapon.item_ptr_id) as Nonweapon
FROM
	armory_weapon
	,armory_item
"""

query_char_items = """
SELECT
    character_id, count(distinct item_id) as Number_of_items
FROM
    charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

query_char_weapons = """
SELECT
    character_id, count(distinct item_id) as Number_of_Weapons
FROM
    charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20
"""

query_numb_char_items = """
SELECT AVG (NoI)
FROM
(SELECT
    character_id, (count(distinct item_id)) as NoI
FROM
    charactercreator_character_inventory
GROUP BY character_id)
"""

query_numb_char_weapons = """
SELECT AVG (NoW)
FROM
(SELECT
    character_id, count(distinct item_id) as NoW
FROM
    charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20)
"""

result1 = cursor.execute(query_total).fetchall()
print("RESULT 1", result1)

result2 = cursor.execute(query_class).fetchall()
print("RESULT 2", result2)

result3 = cursor.execute(query_item).fetchall()
print("RESULT 3", result3)

result4 = cursor.execute(query_weapon_nonweapon).fetchall()
print("RESULT 4", result4)

result5 = cursor.execute(query_char_items).fetchall()
print("RESULT 5", result5)

result6 = cursor.execute(query_char_weapons).fetchall()
print("RESULT 6", result6)

result7 = cursor.execute(query_numb_char_items).fetchall()
print("RESULT 7", result7)

result8 = cursor.execute(query_numb_char_weapons).fetchall()
print("RESULT 8", result8)