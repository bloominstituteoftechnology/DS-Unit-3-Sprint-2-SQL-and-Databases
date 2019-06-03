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
  query = 'SELECT COUNT(*) FROM armory_item;'
  fetch(query)
  print('Exiting.')


# How many total Characters are there?
# How many of each specific subclass?
# How many total Items?
# How many of the Items are weapons? How many are not?
# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
