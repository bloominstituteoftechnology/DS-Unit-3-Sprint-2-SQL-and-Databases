#!/usr/bin/env python

import psycopg2


def count_characters_total(conn):
	curr = conn.cursor()
	query = 'SELECT COUNT(DISTINCT character_id) FROM charactercreator_character'
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'There are {result} total characters.')


def count_characters_by_class(conn):
	curr = conn.cursor()
	classcounts = {'mage': None, 'thief': None, 'cleric': None, 'fighter': None}
	for classname in classcounts:
		tablename = f'charactercreator_{classname}'
		query = f'SELECT COUNT(DISTINCT character_ptr_id) FROM {tablename}'
		curr.execute(query)
		classcounts[classname] = curr.fetchone()[0]
	curr.close()

	for classname, count in classcounts.items():
		print(f'There are {count} characters of class {classname}.')


def count_items_total(conn):
	curr = conn.cursor()
	query = 'SELECT COUNT(DISTINCT item_id) FROM armory_item'
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'There are {result} total items.')


def count_items_weapons(conn):
	curr = conn.cursor()
	query = 'SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon'
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'There are {result} weapons.')


def count_items_not_weapons(conn):
	curr = conn.cursor()
	query = '''
		SELECT COUNT(DISTINCT item_id) FROM
			armory_item LEFT JOIN armory_weapon ON
			armory_item.item_id = armory_weapon.item_ptr_id
		WHERE item_ptr_id IS NULL
		'''
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'There are {result} non-weapon items.')


def count_weapons_per_character(conn):
	curr = conn.cursor()
	query = '''
		SELECT results.character_id, COUNT(*) FROM
			((armory_weapon INNER JOIN charactercreator_character_inventory
				ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id)
				AS inventory_weapons
			INNER JOIN charactercreator_character
				ON inventory_weapons.character_id = charactercreator_character.character_id)
			AS results
		GROUP BY results.character_id
		ORDER BY results.character_id ASC
		LIMIT 20
		'''
	curr.execute(query)
	result = curr.fetchall()
	curr.close()

	for row in result:
		print(f'character_id {row[0]} has {row[1]} weapons.')


def count_items_per_character(conn):
	curr = conn.cursor()
	query = '''
		SELECT results.character_id, COUNT(*) FROM
			((armory_item INNER JOIN charactercreator_character_inventory
				ON armory_item.item_id = charactercreator_character_inventory.item_id)
				AS inventory_items
			INNER JOIN charactercreator_character
				ON inventory_items.character_id = charactercreator_character.character_id)
			AS results
		GROUP BY results.character_id
		ORDER BY results.character_id ASC
		LIMIT 20
		'''
	curr.execute(query)
	result = curr.fetchall()
	curr.close()

	for row in result:
		print(f'character_id {row[0]} has {row[1]} items.')


def count_items_avg(conn):
	curr = conn.cursor()
	query = '''
		SELECT AVG(item_count) FROM
			(SELECT COUNT(*) as item_count FROM
				((armory_item INNER JOIN charactercreator_character_inventory
					ON armory_item.item_id = charactercreator_character_inventory.item_id)
					AS inventory_items
				INNER JOIN charactercreator_character
					ON inventory_items.character_id = charactercreator_character.character_id)
				AS results
			GROUP BY results.character_id)
		'''
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'Each character has an average of {result} items.')


def count_weapons_avg(conn):
	curr = conn.cursor()
	query = '''
		SELECT AVG(weapon_count) FROM
			(SELECT COUNT(*) as weapon_count FROM
				((armory_weapon INNER JOIN charactercreator_character_inventory
					ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id)
					AS inventory_weapons
				INNER JOIN charactercreator_character
					ON inventory_weapons.character_id = charactercreator_character.character_id)
				AS results
			GROUP BY results.character_id)
		'''
	curr.execute(query)
	result = curr.fetchone()[0]
	curr.close()

	print(f'Each character has an average of {result} weapons.')


if __name__ == '__main__':
	with psycopg2.connect(database="lambda_module1") as conn:
		count_characters_total(conn)
		count_characters_by_class(conn)
		count_items_total(conn)
		count_items_weapons(conn)
		count_items_not_weapons(conn)
		count_items_per_character(conn)
		count_weapons_per_character(conn)
		count_items_avg(conn)
		count_weapons_avg(conn)

