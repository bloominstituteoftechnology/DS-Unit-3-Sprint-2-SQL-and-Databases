#!/usr/bin/env python3
import sqlite3
import typing


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def fetch(query: str) -> None:
  '''
  Query ./rpg_db.sqlite3 database with the query parameter
  and print the result, returning None.

  Parameters:
  query (str): a valid `sqlite3` select statement

  Returns:
  None
  '''
  try:
    result = curs.execute(query)
  except ValueError as err:
    print('Invalid query. Exiting.', err)
  else:
    print(result.fetchall())
    return None

if __name__ == '__main__':
  print('How many total characters are there?')
  fetch('SELECT COUNT(*) FROM charactercreator_character;')

  print('How many of each specific subclass?')
  class_tables = ['charactercreator_mage', 'charactercreator_thief', 'charactercreator_cleric', 'charactercreator_fighter', 'charactercreator_necromancer']
  for table in class_tables:
    fetch(f'SELECT COUNT(*) FROM {table};')

  print('How many total Items?')
  fetch('SELECT COUNT(*) FROM armory_item;')

  print('How many of the Items are weapons?')
  fetch('SELECT COUNT(*) FROM armory_weapon;')

  print('How many are not?')
  fetch('SELECT COUNT(*) FROM armory_item WHERE NOT EXISTS (SELECT * FROM armory_weapon WHERE armory_weapon.item_ptr_id = armory_item.item_id);')

  print('How many Items does each character have? (Return first 20 rows)')
  fetch('SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;')

  print('How many Weapons does each character have? (Return first 20 rows)')
  fetch('SELECT cci.character_id, COUNT(cci.item_id) FROM charactercreator_character_inventory AS cci WHERE cci.item_id IN (SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id LIMIT 20;')

  print('On average, how many Items does each Character have?')
  fetch('SELECT AVG(inv_count) FROM (SELECT COUNT(item_id) AS inv_count FROM charactercreator_character_inventory GROUP BY character_id);')

  print('On average, how many Weapons does each character have?')
  fetch('SELECT AVG(weapon_count) FROM (SELECT COUNT(item_id) AS weapon_count FROM charactercreator_character_inventory WHERE charactercreator_character_inventory.item_id IN (SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id);')
