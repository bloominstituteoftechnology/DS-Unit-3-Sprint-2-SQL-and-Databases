import sqlite3
import pandas as pd

!wget https://github.com/jonathanmendoza-tx/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true -O rpg_db.sqlite3

#create connection
conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

def question_one():
	query_characters = """
	SELECT COUNT(character_id)
	FROM charactercreator_character
	"""
	cur.execute(query_characters)
	total_characters = cur.fetchall()

	print(f'There are {total_characters[0][0]} total characters')


def question_two():
	query_cleric = """
	SELECT COUNT(character_ptr_id)
	FROM charactercreator_cleric
	"""
	cur.execute(query_cleric)
	total_clerics = cur.fetchall()

	print(f'There are {total_clerics[0][0]} total clerics')


	query_fighter = """
	SELECT COUNT(character_ptr_id)
	FROM charactercreator_fighter
	"""
	cur.execute(query_fighter)
	total_fighters = cur.fetchall()

	print(f'There are {total_fighters[0][0]} total fighters')

	query_mage = """
	SELECT COUNT(character_ptr_id)
	FROM charactercreator_mage
	"""
	cur.execute(query_mage)
	total_mages = cur.fetchall()

	print(f'There are {total_mages[0][0]} total mages')


	query_necromancer = """
	SELECT COUNT(mage_ptr_id)
	FROM charactercreator_necromancer
	"""
	cur.execute(query_necromancer)
	total_necromancers = cur.fetchall()

	print(f'There are {total_necromancers[0][0]} total necromancers')


	query_thief = """
	SELECT COUNT(character_ptr_id)
	FROM charactercreator_thief
	"""
	cur.execute(query_thief)
	total_thievs = cur.fetchall()

	print(f'There are {total_thievs[0][0]} total thievs')


def question_three():
	query_armory = """
	SELECT COUNT(item_id)
	FROM armory_item
	"""
	cur.execute(query_armory)
	total_items = cur.fetchall()

	print(f'There are {total_items[0][0]} total items')


def question_four():
	query_weapons = """
	SELECT COUNT(item_ptr_id)
	FROM armory_weapon
	"""
	cur.execute(query_weapons)
	total_weapons = cur.fetchall()

	items_not_weapons = total_items[0][0] - total_weapons[0][0]
	
	print(f'There are {total_weapons[0][0]} total weapons')
	print(f'There are {items_not_weapons} items that are not weapons')


def question_five():
	query_char_items = """
	SELECT COUNT(item_id), character_id
	FROM charactercreator_character_inventory
	GROUP BY character_id
	"""
	cur.execute(query_char_items)
	items_per_char = cur.fetchall()

	items_df = pd.DataFrame(items_per_char, columns = ['num_of_items', 'char_id'])
	items_df = items_df.set_index('char_id', verify_integrity = True)

	print(items_df.head(20))


def question_six_to_eight():
	query_char_weapons = """
	SELECT COUNT(item_id), character_id
	FROM charactercreator_character_inventory
	WHERE item_id IN 
	  (
	  SELECT item_ptr_id
	  FROM armory_weapon 
	  )
	GROUP BY character_id
	"""
	cur.execute(query_char_weapons)
	weapons_per_char = cur.fetchall()

	weapons_df = pd.DataFrame(weapons_per_char, columns = ['num_of_weapons', 'char_id'])
	weapons_df = weapons_df.set_index('char_id', verify_integrity = True)

	print(weapons_df.head(20))



	item_count = list(zip(*items_per_char))[0]
	avg_items_per_char = sum(item_count)/ total_characters[0][0]
	
	print(f'There are an average of {avg_items_per_char} items per character')



	weapon_count = list(zip(*weapons_per_char))[0]
	avg_weapons_per_char = sum(weapon_count)/total_characters[0][0]
	
	print(f'There are an average of {avg_weapons_per_char} weapons per character')

question_one()
question_two()
question_three()
question_four()
question_five()
question_six_to_eight()
