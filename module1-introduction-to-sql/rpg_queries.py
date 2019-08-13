import sqlite3

con = sqlite3.connect('rpg_db.sqlite3')

def sql_fetch(con):
    cursor = con.cursor()

    """ Get total number of Characters"""

    query1 = '''SELECT COUNT (DISTINCT name)
    FROM charactercreator_character;'''
    cursor.execute(query1)
    rows1 = cursor.fetchall()
    for row in rows1:
        print(f'Total number of characters: {row[0]}')

    """ Get total number of Characters"""

    query2 = '''SELECT COUNT (DISTINCT character_ptr_id)
    FROM charactercreator_mage
    UNION ALL
    SELECT COUNT (DISTINCT character_ptr_id)
    FROM charactercreator_cleric
    UNION ALL
    SELECT COUNT (DISTINCT mage_ptr_id)
    FROM charactercreator_necromancer
    UNION ALL
    SELECT COUNT (DISTINCT character_ptr_id)
    FROM charactercreator_thief
    UNION ALL
    SELECT COUNT (DISTINCT character_ptr_id)
    FROM charactercreator_fighter;'''
    
    cursor.execute(query2)
    rows2 = cursor.fetchall()
    rows_result = [x[0] for x in rows2]
    labels = ['mages','clerics','necromancers','thiefs','fighters']
    for label, row in zip(labels, rows_result):
        print(f'Total number of {label}: {row}')

    """ Get total number of items"""

    query3 = '''SELECT count(*)
    FROM armory_item;'''

    cursor.execute(query3)
    rows3 = cursor.fetchall()
    for row in rows3:
        print(f'Total number of items: {row[0]}')

    """ How many of the Items are weapons? How many are not? """

    query4 = '''SELECT count(*)
    FROM armory_item
    WHERE item_id in (select item_ptr_id from armory_weapon)
    UNION ALL
    SELECT count(*)
    FROM armory_item
    WHERE item_id not in (select item_ptr_id from armory_weapon);'''

    cursor.execute(query4)
    rows4 = cursor.fetchall()
    rows4_result = [x[0] for x in rows4]
    labels4 = ['weapons','non-weapons']
    for label, row in zip(labels4, rows4_result):
        print(f'Total number of {label}: {row}')

    """How many Items does each character have? (Return first 20 rows)"""

    query5 = '''SELECT COUNT(cci.item_id) as "Items per character", cc.name as "Character Name"
    FROM charactercreator_character_inventory as cci, charactercreator_character as cc
    WHERE cci.character_id = cc.character_id
    GROUP BY cc.name
    ORDER BY COUNT(cci.item_id) DESC
    LIMIT 20;'''

    cursor.execute(query5)
    rows5 = cursor.fetchall()
    rows5_result = [x[0] for x in rows5]
    labels5 = [x[1] for x in rows5]
    print('CHARACTER: NO. OF ITEMS')
    for label, row in zip(labels5, rows5_result):
        print(f'{label}: {row}')

    """How many Weapons does each character have? (Return first 20 rows)"""

    query6 = '''SELECT COUNT(cci.item_id) as "Weapons per character", cc.name as "Character Name"
    FROM charactercreator_character_inventory as cci, charactercreator_character as cc, armory_weapon as aw
    WHERE cci.character_id = cc.character_id AND cci.item_id = aw.item_ptr_id
    GROUP BY cc.name
    ORDER BY COUNT(cci.item_id) DESC
    LIMIT 20;'''

    cursor.execute(query6)
    rows6 = cursor.fetchall()
    rows6_result = [x[0] for x in rows6]
    labels6 = [x[1] for x in rows6]
    print('CHARACTER: NO. OF WEAPONS')
    for label, row in zip(labels6, rows6_result):
        print(f'{label}: {row}')

    """On average, how many Items does each Character have?"""

    query7 = '''SELECT AVG(a.item_count)
    FROM
    (SELECT COUNT(item_id) as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id) as a'''

    cursor.execute(query7)
    rows7 = cursor.fetchall()
    for row in rows7:
        print(f'Average number of items: {row[0]:.2f}')


    """On average, how many Weapons does each character have?"""
    
    query8 = '''SELECT AVG(a.item_count)
    FROM
    (SELECT COUNT(cci.item_id) as item_count
    FROM charactercreator_character_inventory as cci, armory_weapon as aw
    WHERE cci.item_id = aw.item_ptr_id
    GROUP BY character_id) as a'''

    cursor.execute(query8)
    rows8 = cursor.fetchall()
    for row in rows8:
        print(f'Average number of weapons: {row[0]:.2f}')
    
    cursor.close()
    con.commit()

sql_fetch(con)

