import sqlite3

import contextlib

import os
os.system("wget 'https://github.com/serinamarie/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true' ")
os.rename("rpg_db.sqlite3?raw=true", "rpg_db.sqlite3")

# connect to sqlite database
conn = sqlite3.connect("rpg_db.sqlite3")

# How many total Characters are there? 302
query_1 = '''
SELECT COUNT(character_id)
FROM charactercreator_character;
'''

# How many of each specific subclass? Clerics =  75, Fighters = 68
# Mages = 108, Necromancers = 11, Thieves = 51

query_2 = '''
SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric cc;
'''

query_3 = '''
SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;
'''

query_4 = '''
SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;
'''

query_5 = '''
SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer;
'''

query_6 = '''
SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;
'''

# How many total Items? 174
query_7 = '''
SELECT COUNT(item_id)
FROM armory_item;
'''

# How many of the Items are weapons? 37, 137 non-weapons
query_8 = '''
SELECT COUNT(item_ptr_id)
FROM armory_weapon;
'''

# How many Items does each character have?
query_9 = '''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
'''

# How many Weapons does each character have?
query_10 = '''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory cci
JOIN armory_weapon
WHERE item_id = item_ptr_id
GROUP BY character_id
LIMIT 20;
'''

# On average, how many Items does each Character have? 2.973
query_11 = '''
SELECT avg(c)
	FROM
	(
	SELECT character_id, COUNT(item_id) as c
	FROM charactercreator_character_inventory
	GROUP BY character_id
	);
	'''

# On average, how many Weapons does each character have? 1.309
query_12 = '''
SELECT avg(c)
	FROM
	(
	SELECT character_id, COUNT(item_id) as c
	FROM charactercreator_character_inventory cci
	JOIN armory_weapon
	WHERE item_id = item_ptr_id
	GROUP BY character_id
	);
	'''

with contextlib.closing(conn.cursor()) as cursor:
	cursor.execute(query_1)
	result_1 = cursor.fetchall()
	print("Query 1:", result_1)

	cursor.execute(query_2)
	result_2 = cursor.fetchall()
	print("Query 2:", result_2)

	cursor.execute(query_3)
	result_3 = cursor.fetchall()
	print("Query 3:", result_3)

	cursor.execute(query_4)
	result_4 = cursor.fetchall()
	print("Query 4:", result_4)

	cursor.execute(query_5)
	result_5 = cursor.fetchall()
	print("Query 5:", result_5)

	cursor.execute(query_6)
	result_6 = cursor.fetchall()
	print("Query 6:", result_6)

	cursor.execute(query_7)
	result_7 = cursor.fetchall()
	print("Query 7:", result_7)

	cursor.execute(query_8)
	result_8 = cursor.fetchall()
	print("Query 8:", result_8)

	cursor.execute(query_9)
	result_9 = cursor.fetchall()
	print("Query 9:", result_9)

	cursor.execute(query_10)
	result_10 = cursor.fetchall()
	print("Query 10:", result_10)

	cursor.execute(query_11)
	result_11 = cursor.fetchall()
	print("Query 11:", result_11)

	cursor.execute(query_12)
	result_12 = cursor.fetchall()
	print("Query 12:", result_12)

cursor.close()
conn.close()
