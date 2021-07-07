import sqlite3
import pandas as pd


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def question1():
    query = 'SELECT COUNT(*) FROM charactercreator_character;'
    result = curs.execute(query).fetchone()
    print('How many total characters are there?', result[0])


def question2():
    query = 'SELECT(SELECT COUNT(*) \
             FROM charactercreator_cleric) AS cleric_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_mage) AS mage_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_necromancer) AS necro_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_fighter) AS fighter_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_thief) AS thief_count;'
    print('\nHow many of each specific subclass?')
    print(pd.read_sql(query, conn).T.rename(columns={0: 'Count'}))


def question3():
    query = 'SELECT COUNT(*) FROM armory_item;'
    result = curs.execute(query).fetchone()
    print('\nHow many total items?', result[0])


def question4():
    query = 'SELECT COUNT(*) FROM armory_weapon;'
    weapon_count = curs.execute(query).fetchone()
    print('\nHow many of the items are weapons?', weapon_count[0])
    query = 'SELECT COUNT(*) FROM armory_item;'
    item_count = curs.execute(query).fetchone()
    print('How many of the items are not weapons?',
          item_count[0]-weapon_count[0])


def question5():
    query = 'SELECT COUNT(*), character_id \
             FROM charactercreator_character_inventory \
             GROUP BY character_id LIMIT 20;'
    print('\nHow many items does each character have? (first 20 rows)')
    result = pd.read_sql(query, conn)
    result = result.set_index('character_id')
    print(result.T)


def question6():
    query = 'SELECT COUNT(*), character_id \
             FROM charactercreator_character_inventory AS cci, \
                  armory_weapon AS aw \
             WHERE cci.item_id = aw.item_ptr_id \
             GROUP BY character_id LIMIT 20;'
    result = pd.read_sql(query, conn)
    result = result.set_index('character_id')
    print('\nHow many weapons does each character have? (first 20 rows)')
    print(result.T)


def question7():
    query = 'SELECT AVG(items.count) FROM ( \
                SELECT COUNT(*) as count, character_id \
                FROM charactercreator_character_inventory \
                GROUP BY character_id) AS items;'
    result = curs.execute(query).fetchone()
    print('\nOn average, how many items does each character have?', result[0])


def question8():
    query = 'SELECT AVG(weapons.count) FROM ( \
                SELECT COUNT(*) as count \
                FROM charactercreator_character_inventory AS cci, \
                     armory_weapon AS aw \
                WHERE cci.item_id = aw.item_ptr_id \
                GROUP BY character_id) as weapons'
    result = curs.execute(query).fetchone()
    print('\nOn average, how many weapons does each character have?',
          result[0])


question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
