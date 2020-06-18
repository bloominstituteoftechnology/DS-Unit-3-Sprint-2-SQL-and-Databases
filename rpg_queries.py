import sqlite3
import os


def connecting(connection):
    conn = sqlite3.connect(connection)
    curs = conn.cursor()
    return curs


def totalCharacters(connection):
    curs = connecting(connection)
    query = 'SELECT count(character_id) FROM charactercreator_character;'
    curs.execute(query)
    rows = curs.fetchall()
    print(f'The number of characters is {rows[0][0]}')


def numSubclass(connection):
    print()
    curs = connecting(connection)
    query1 = 'SELECT count(*) FROM charactercreator_cleric;'
    query2 = 'SELECT count(*) FROM charactercreator_fighter;'
    query3 = 'SELECT count(*) FROM charactercreator_mage;'
    query4 = 'SELECT count(*) FROM charactercreator_necromancer;'
    query5 = 'SELECT count(*) FROM charactercreator_thief;'

    curs.execute(query1)
    numCleric = curs.fetchall()
    print(f'Number of clerics {numCleric[0][0]}')
    curs.execute(query2)
    numFighter = curs.fetchall()
    print(f'Number of fighters {numFighter[0][0]}')
    curs.execute(query3)
    numMage = curs.fetchall()
    print(f'Number of mages {numMage[0][0]}')
    curs.execute(query4)
    numNecro = curs.fetchall()
    print(f'Number of necromancers {numNecro[0][0]}')
    curs.execute(query5)
    numThief = curs.fetchall()
    print(f'Number of thieves {numThief[0][0]}')


def totalItems(connection):
    print()
    curs = connecting(connection)
    query = 'SELECT count(name) FROM armory_item;'
    curs.execute(query)
    numItems = curs.fetchall()
    print(f'The total number of items is {numItems[0][0]}')


def weaponOrNot(connection):
    print()
    curs = connecting(connection)
    query1 = 'SELECT count(item_ptr_id) FROM armory_weapon;'
    curs.execute(query1)
    numWeapons = curs.fetchall()

    query2 = 'SELECT count(name) FROM armory_item;'
    curs.execute(query2)
    numTotal = curs.fetchall()

    numNotWeapons = numTotal[0][0] - numWeapons[0][0]
    print(f'There are {numWeapons[0][0]} weapons in the game.')
    print(f'And {numNotWeapons} items that are not weapons.')


def itemsPerCharacter(connection):
    print()
    curs = connecting(connection)
    query = '''SELECT count(item_id),
                character_id
            FROM charactercreator_character_inventory
            GROUP BY character_id LIMIT 20;'''
    curs.execute(query)
    cout = curs.fetchall()
    print('Top 20 items per character:(count on left side)', cout)


def weaponsPerCharacter(connection):
    print()
    curs = connecting(connection)
    query = '''SELECT cci.character_id as `Character Id`,
                COUNT(aw.item_ptr_id) as `Weapon Count`
               FROM charactercreator_character_inventory as cci
               INNER JOIN armory_item as ai ON cci.item_id = ai.item_id
               INNER JOIN armory_weapon as aw ON ai.item_id = aw.item_ptr_id
               GROUP BY cci.character_id LIMIT 20;'''
    curs.execute(query)
    cout = curs.fetchall()
    print('Top 20 weapons per character:(count on right side)', cout)


def avgItems(connection):
    print()
    curs = connecting(connection)
    query = '''SELECT AVG(c)
            FROM(SELECT character_id, COUNT(item_id) as c
                 FROM charactercreator_character_inventory
                 GROUP BY character_id);'''
    curs.execute(query)
    avg = curs.fetchall()
    print(f'The average number of items a player has is {avg[0][0]:.0f}')


def avgWeapons(connection):
    print()
    curs = connecting(connection)
    query = '''SELECT AVG(c)
                FROM(SELECT cci.character_id as `Character Id`,
                     COUNT(aw.item_ptr_id) as c
                           FROM charactercreator_character_inventory as cci
                           INNER JOIN armory_item as ai ON
                           cci.item_id = ai.item_id INNER JOIN
                           armory_weapon as aw ON ai.item_id = aw.item_ptr_id
                           GROUP BY cci.character_id);'''
    curs.execute(query)
    avg = curs.fetchall()
    print(f'The average number of weapons a player has is {avg[0][0]:.0f}')


# Testing the method
totalCharacters('rpg_db.sqlite3')
numSubclass('rpg_db.sqlite3')
totalItems('rpg_db.sqlite3')
weaponOrNot('rpg_db.sqlite3')
itemsPerCharacter('rpg_db.sqlite3')
weaponsPerCharacter('rpg_db.sqlite3')
avgItems('rpg_db.sqlite3')
avgWeapons('rpg_db.sqlite3')
