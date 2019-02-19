# Assignment 1 for SQL 
"""A series of SQL queries to figure out answer to the 
rpq_db"""
import sqlite3


def query_1():
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_1 = """SELECT COUNT (*) AS CountChar
	FROM charactercreator_character"""


	c.execute(query_1)
	
	print("Total character count is", c.fetchall())

def query_2():

	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_2 = """SELECT COUNT ('mages') AS NumMages
	FROM charactercreator_mage

	UNION ALL

	SELECT COUNT ('clerics') AS NumClerics
	FROM charactercreator_cleric

	UNION ALL

	SELECT COUNT ('figher') AS NumFigher
	FROM charactercreator_fighter

	UNION ALL

	SELECT COUNT ('thieves') AS NumThieves
	FROM charactercreator_thief;
	"""

	c.execute(query_2)
	
	print("Total in each subclass are: ", c.fetchall())

def query_3():
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_3 = """SELECT COUNT(item_id) 
	FROM  charctercreator_character_inventory;"""

	c.execute(query_3)

	print("Total items:", c.fetchall())

def query_4():
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_4 = """SELECT COUNT (*) FROM armory_item
	WHERE item_id IN (SELECT DISTINCT item_ptr_id FROM armory_weapon)
	"""

	c.execute(query_4)

	print("Number of weapons:", c.fetchall())

def query_5():
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_5 = """SELECT COUNT(*) FROM armory_item
	WHERE item_id NOT IN (SELECT DISTINCT item_ptr_id FROM armory_weapon)
	"""

	c.execute(query_5)

	print("Number of items that are not weapons:", c.fetchall())

def query_6():
	"""How many items does each character have?"""
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_6 = """SELECT character_id, COUNT(character_id) AS items
	FROM charactercreator_character_inventory
	GROUP BY character_id
	LIMIT 20"""

	c.execute(query_6)

	print("Each character has:", c.fetchall())

def query_7():
	"""How many weapons does each character have?"""
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_7 = """SELECT character_id, count (character_id)
	FROM armory_weapon AS weapon, 
	charactercreator_character_inventory AS inventory
	WHERE weapon.item_ptr_id = inventory.item_id
	GROUP BY inventory.character_id
	LIMIT 20;"""

	c.execute(query_7)

	print("Count of each character's weapons:", c.fetchall())

def query_8():
	"""On avg, how many items does each character have?"""
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_8 = """SELECT AVG (items)
	FROM (SELECT character_id, COUNT (item_id) AS items 
	FROM charactercreator_character_inventory
	GROUP BY character_id);"""

	c.execute(query_8)

	print(c.fetchall())

def query_9():
	"""On average, how many weapons does each character have?"""
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_9 = """SELECT AVG (weapons) FROM (SELECT character_id, COUNT (character_id) as weapons
	FROM charactercreator_character_inventory AS inventory, 
	armory_weapon AS weapon
	WHERE weapon.item_ptr_id = inventory.item_id
	GROUP BY inventory.character_id);"""

	c.execute(query_9)

	print(c.fetchall())









