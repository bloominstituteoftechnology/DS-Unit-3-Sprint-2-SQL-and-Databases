import sqlite3 as sql

connect = sql.connect('rpg_db.sqlite3')
curse = connect.cursor()


def total_char_count():
    '''Total all characters'''
    curse.execute('''SELECT COUNT(distinct character_id)
        FROM charactercreator_character;''')
    return curse.fetchall()


def sub_class():
    '''Grab population count of each subclass of characters'''
    curse.execute('''SELECT "mages", COUNT(*)
        From charactercreator_mage
    
        UNION
    
        SELECT "clerics", COUNT(*)
        FROM charactercreator_cleric

        UNION 

        SELECT "fighter", COUNT(*)
        FROM charactercreator_fighter

        UNION

        SELECT "thieves", COUNT(*)
        FROM charactercreator_thief;''')
    return curse.fetchall()


def item_count():
    '''Total count of all items'''
    curse.execute('''SELECT COUNT(distinct item_id)
        FROM armory_item;''')
    return curse.fetchall()


def weapons():
    '''Amount of items that are weapons'''
    curse.execute('''SELECT COUNT(*)
        FROM armory_item
        WHERE item_id IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon);''')
    return curse.fetchall()


def not_weapon():
    '''Any item that is not  weapon'''
    curse.execute('''SELECT COUNT(*)
        FROM armory_item
        WHERE item_id NOT IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon);''')
    return curse.fetchall()


def char_items():
    '''Amount of items a character has, first 20 characters'''
    curse.execute(''' SELECT character_id, COUNT( item_id)
        FROM charactercreator_character_inventory
        GROUP BY character_id
        LIMIT 20;''')
    return curse.fecthall()


def char_weapons():
    '''Weapons held by characters, first 20 characters'''
    curse.execute('''SELECT character_id,COUNT(item_id)
        From charactercreator_character_inventory
        WHERE item_id IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon)
        GROUP BY character_id
        LIMIT 20;''')
    return curse.fetchall()


def item_avg():
    '''How many items the average person carries'''
    curse.execute('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) AS items
            FROM charactercreator_character_inventory
            GROUP BY character_id);''')
    return curse.fetchall()


def weapon_avg():
    '''Average weapon count per character'''
    curse.execute('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) as items
            FROM charactercreator_character_inventory
            Where item_id IN(
                    SELECT distinct item_ptr_id
                    FROM armory_weapon)
            GROUP BY character_id);''')
    return curse.fetchall()
