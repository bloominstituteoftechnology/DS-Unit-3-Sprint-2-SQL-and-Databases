import os
import sqlite3
import file

DB_FILEPATH = file.DB_FILEPATH

def character_count_query():
    #queries the database for the total character count

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()


    character_count_query = """
    select
        count(distinct character_id) as character_count
    from charactercreator_character;
    """
    results = curs.execute(character_count_query).fetchall()
    conn.close()

    return results

def character_subclass_count_query():
    #queries the database for the character count by character type

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    character_subclass_count_query = """
    select
        count(distinct charactercreator_mage.character_ptr_id) as mage_count,
        count(distinct charactercreator_thief.character_ptr_id) as thief_count,
        count(
            distinct charactercreator_cleric.character_ptr_id
        ) as cleric_count,
        count(
            distinct charactercreator_fighter.character_ptr_id
        ) as fighter_count,
        count(
            distinct charactercreator_necromancer.mage_ptr_id
        ) as necromancer_count
    from
        charactercreator_character
        left join charactercreator_mage on charactercreator_mage.character_ptr_id = charactercreator_character.character_id
        left join charactercreator_thief on charactercreator_thief.character_ptr_id = charactercreator_character.character_id
        left join charactercreator_cleric on charactercreator_cleric.character_ptr_id = charactercreator_character.character_id
        left join charactercreator_fighter on charactercreator_fighter.character_ptr_id = charactercreator_character.character_id
        left join charactercreator_necromancer on charactercreator_necromancer.mage_ptr_id = charactercreator_character.character_id;
    """
    results = curs.execute(character_subclass_count_query).fetchall()
    conn.close()
    return results

def item_count():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    item_count_query = """
    select
        count(distinct item_id) as item
    from armory_item
    """

    results = curs.execute(armory_count_query).fetchall()
    conn.close()
    return results

def weapons_or_nah():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    weapons_count_query = """
    select
        count(distinct armory_item.item_id) - count(distinct armory_weapon.item_ptr_id) as not_weapons_count,
        count(distinct armory_weapon.item_ptr_id) as weapons_count
    from armory_item
    left join armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
    """

    results = curs.execute(weapons_count_query).fetchall()
    conn.close()
    return results

def character_inventory_count():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    inventory_count_query = """
    select
	   character_id,
       count(item_id) as char_inventory_item
    from charactercreator_character_inventory
    group by character_id
    limit 20
    """

    results = curs.execute(weapons_count_query).fetchall()
    conn.close()
    return results

def character_weapons_count():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    character_weapons_count_query = """
    select
	   character_id,
	   count(charactercreator_character_inventory.item_id) as char_inv_weapons
    from charactercreator_character_inventory
    inner join armory_weapon on armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
    group by character_id
    limit 20
    """

    results = curs.execute(character_weapons_count_query).fetchall()
    conn.close()
    return results

def avg_items_per_character():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    average_items_per_character = """
    select
        cast(count(item_id) as float) / count(distinct character_id) as avg_inventory_item
    from charactercreator_character_inventory
    """

    results = curs.execute(average_items_per_character).fetchall()
    conn.close()
    return results

def avg_weapons_per_character():

    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    average_items_per_character = """
    select
        cast(count(armory_weapon.item_ptr_id) as float) / count(distinct character_id) as avg_weapon_inv
    from charactercreator_character_inventory
    left join armory_weapon on armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
    """

    results = curs.execute(average_items_per_character).fetchall()
    conn.close()
    return results
