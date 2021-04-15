import os
import sqlite3
from prettytable import PrettyTable

# Connect to the sqlite3 database
DB_FILEPATH = "rpg_db.sqlite3"
conn = sqlite3.connect(DB_FILEPATH)

# Question #1: How many total Characters are there?
conn_curs = conn.cursor()
q1_query = "SELECT Count(DISTINCT NAME) FROM charactercreator_character"
q1_results = conn_curs.execute(q1_query).fetchall()
print(f'-----\nQuestion #1 How many total Characters are there? {q1_results[0][0]}\n\n')

# Question #2 How many of each specific subclass?
cols = ("cleric", "fighter", "mage", "necromancer", "thief")
q2_query = """SELECT cleric, fighter, mage, necromancer, thief 
FROM (SELECT Count(*) as cleric FROM charactercreator_cleric)
LEFT JOIN (SELECT Count(*) as fighter FROM charactercreator_fighter)
LEFT JOIN (SELECT Count(*) as mage FROM charactercreator_mage)
LEFT JOIN (SELECT Count(*) as necromancer FROM charactercreator_necromancer)
LEFT JOIN (SELECT Count(*) as thief FROM charactercreator_thief)"""
q2_results = conn_curs.execute(q2_query).fetchall()
t = PrettyTable(cols)
t.add_row(q2_results[0])
print(f'-----\nQuestion #2 How many of each specific subclass?')
print(t)

# Question #3 How many total Items?
q3_query = "SELECT Count(*) FROM armory_item" 
q3_results = conn_curs.execute(q3_query).fetchall()
print(f'\n\n-----\nQuestion #3 How many total Items? {q3_results[0][0]}')

# Question #4 How many of the Items are weapons?
q4a_query = "SELECT count(*) FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id"
q4a_results = conn_curs.execute(q4a_query).fetchall()

# Question #4 How many are not?
q4b_query = """SELECT count(armory_item.item_id)
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id IS NULL"""
q4b_results = conn_curs.execute(q4b_query).fetchall()

print(f'\n\n-----\nQuestion #4 How many of the Items are weapons? {q4a_results[0][0]}')
print(f'Question #4 How many are not? {q4b_results[0][0]}\n\n')

# Question #5 How many Items does each character have? (Return first 20 rows)
cols = ("char_name", "count")
q5_query = """SELECT charactercreator_character.name as char_name, count(*) as cnt
FROM charactercreator_character
INNER JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY char_name
ORDER BY cnt DESC LIMIT 20"""
q5_results = conn_curs.execute(q5_query).fetchall()
t = PrettyTable(cols)
for rw in q5_results:
    t.add_row(rw)
print(f'-----\nQuestion #5 How many Items does each character have? (Return first 20 rows)')
print(t)

# Question #6 How many Weapons does each character have? (Return first 20 rows)
cols = ("char_name", "count")
q6_query = """SELECT charactercreator_character.name as char_name, count(*) as cnt
FROM charactercreator_character
INNER JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY char_name
ORDER BY cnt DESC LIMIT 20"""
q6_results = conn_curs.execute(q6_query).fetchall()
t = PrettyTable(cols)
for rw in q6_results:
    t.add_row(rw)
print(f'\n\n-----\nQuestion #6 How many Weapons does each character have? (Return first 20 rows)')
print(t)

# Question #7 On average, how many Items does each Character have?
q7_query = """SELECT ROUND(AVG(cnt), 2) as average_num_items
FROM (
	SELECT charactercreator_character.name as char_name, count(*) as cnt
	FROM charactercreator_character
	INNER JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY char_name 
)"""
q7_results = conn_curs.execute(q7_query).fetchall()
print(f'\n\n-----\nQuestion #7 On average, how many Items does each Character have? {q7_results[0][0]}\n\n')

# Question #8 On average, how many Weapons does each character have?
q8_query = """SELECT ROUND(AVG(cnt), 2) as average_num_weapons
FROM (
  SELECT charactercreator_character.name as char_name, count(*) as cnt
  FROM charactercreator_character
  INNER JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
  INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
  GROUP BY char_name
)"""
q8_results = conn_curs.execute(q8_query).fetchall()
print(f'-----\nQuestion #8 On average, how many Weapons does each character have? {q8_results[0][0]}\n\n')
