import sqlite3
from enum import Enum

class Fetch(Enum):
    FETCH_ONE  = 1
    FETCH_ALL  = 2
    DONT_FETCH = 3

def init_sqlite_conn(db_filename):
  conn = sqlite3.connect(db_filename)
  c = conn.cursor()
  return conn, c

def deinit_sqlite_conn(conn):
  conn.close()

def handle_fetch_options(curs, fetchall):

    def fetch_one(curs):
        return curs.fetchone()

    def fetch_all(curs):
        return curs.fetchall()

    def dont_fetch(curs):
        return

    fetchall_options = {
        Fetch.FETCH_ONE: fetch_one,
        Fetch.FETCH_ALL: fetch_all,
        Fetch.DONT_FETCH: dont_fetch
    }

    return fetchall_options[fetchall](curs)

def run(curs, sql, fetchall = Fetch.DONT_FETCH):
  curs.execute(sql)
  return handle_fetch_options(curs, fetchall)

def get_num_rows(curs, table):
    return run(curs,
               'SELECT COUNT(*) FROM ' + table,
               Fetch.FETCH_ONE)[0]

def get_num_characters(curs):
    return get_num_rows(curs, 'charactercreator_character')

def get_num_characters_per_type(curs):
    table = {'cleric': None, 'mage': None,
              'fighter': None, 'thief': None}
    for key in table.keys():
        table_name = 'charactercreator_' + key
        table[key] = run(curs,
                         'SELECT COUNT(*) FROM ' + table_name,
                         Fetch.FETCH_ONE)[0]
    return table

def get_num_items(curs):
    return get_num_rows(curs, 'armory_item')

def get_num_weapons(curs):
    return get_num_rows(curs, 'armory_weapon')

def get_num_weapons_and_not_weapons(curs):
    num_weapons = get_num_weapons(curs)
    total_items = get_num_items(curs)
    return num_weapons, total_items - num_weapons

def items_per_character(curs):
    sql_grouped_items_for_each_character = '''
      SELECT character_id, COUNT(item_id)
      FROM charactercreator_character_inventory
      GROUP BY character_id
      LIMIT 20
    '''
    grouped_items_per_character = run(curs,
                                      sql_grouped_items_for_each_character,
                                      Fetch.FETCH_ALL)

    return grouped_items_per_character

# def weapons_per_character(curs):
#     sql_grouped_weapons_per_character = '''
#       SELECT character_id, 
#     '''
