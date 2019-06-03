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
  query = 'SELECT COUNT(*) FROM charactercreator_character;'
  fetch(query)

  print('How many of each specific subclass')
  class_tables = ['charactercreator_mage', 'charactercreator_thief', 'charactercreator_cleric', 'charactercreator_fighter', 'charactercreator_necromancer']
  for table in class_tables:
    fetch(f'SELECT COUNT(*) FROM {table};')

  print('How many total Items?')
  query = 'SELECT COUNT(*) FROM armory_item;'
  fetch(query)

  print('How many of the Items are weapons?')
  query = 'SELECT COUNT(*) FROM armory_weapon;'
  fetch(query)

  # How many are not?
  # WHERE NOT IN

  # How many Items does each character have? (Return first 20 rows)
  # How many Weapons does each character have? (Return first 20 rows)
  # On average, how many Items does each Character have?
  # On average, how many Weapons does each character have?
