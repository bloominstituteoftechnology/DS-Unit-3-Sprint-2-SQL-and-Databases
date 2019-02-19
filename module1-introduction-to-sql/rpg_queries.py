import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
def weapons_and_nonweapons():
    q ="""
    SELECT (
    SELECT COUNT(*)
    FROM armory_weapon)
    AS weapons,
    ( SELECT COUNT(*)
    FROM armory_item)
    - (SELECT Count(*)
    FROM armory_weapon)
    AS non_weapons
    """
    curs.execute(q)
    return curs.fetchall()
def percent_of_weapons():
    q="""
    SELECT 
    100 * COUNT(item_ptr_id) /(SELECT COUNT(*) FROM charactercreator_character)
        AS percent_weapons
    FROM charactercreator_character_inventory
    LEFT JOIN armory_weapon
    ON item_id = item_ptr_id
    """
    curs.execute(q)
    return curs.fetchall()

def character_inventory():
    q="""
    SELECT COUNT(item_id)
    FROM charactercreator_character_inventory
    GROUP BY character_id
    LIMIT 20
    """
    curs.execute(q)
    return curs.fetchall()

def character_weapon_count():
    q="""
    SELECT COUNT(item_ptr_id)
    FROM charactercreator_character_inventory
    LEFT JOIN armory_weapon
    ON item_id = item_ptr_id
    GROUP BY character_id
    LIMIT 20a
    """
    curs.execute(q)
    return curs.fetchall()

def num_characters():
    q="""
    SELECT COUNT(character_id)
    FROM charactercreator_character
    """
    curs.execute(q)
    return curs.fetchall()

def num_in_class():
    q="""
    SELECT (
        SELECT COUNT(*)
        FROM charactercreator_cleric
        )
        AS cleric,
        (
        SELECT COUNT(*)
        FROM charactercreator_fighter
        ) AS fighter,
        (SELECT COUNT(*)
        FROM charactercreator_mage
        ) AS mage,
        (SELECT COUNT(*)
        FROM charactercreator_necromancer 
        ) AS necromancer,
        (SELECT COUNT(*)
        FROM charactercreator_thief
        ) AS thief
    """
    curs.execute(q)
    return curs.fetchall()


def num_items():
    q="""
    SELECT COUNT(*)
    FROM armory_item
    """
    curs.execute(q)
    return curs.fetchall()



