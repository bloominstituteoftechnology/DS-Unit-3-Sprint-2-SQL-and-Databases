import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# QUERIES
GET_TOTAL_CHARACTERS = """ 
    SELECT COUNT(*)
    FROM charactercreator_character;
"""

GET_CHARACTERS_CLERIC = """
    SELECT COUNT(*)
    FROM charactercreator_cleric;

"""

GET_CHARACTERS_FIGHTER = """
    SELECT COUNT(*)
    FROM charactercreator_fighter
"""

GET_CHARACTERS_MAGE = """
    SELECT COUNT(*)
    FROM charactercreator_fighter
"""
GET_CHARACTERS_NECROMANCER = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer
"""
GET_CHARACTERS_THIEF = """
    SELECT COUNT(*)
    FROM charactercreator_thief
"""

GET_TOTAL_ITEMS = """
    SELECT  COUNT(*)
    FROM armory_item ; 

"""
GET_WEAPONS = """

 SELECT  COUNT(*)
   FROM armory_weapon AS aw, armory_item as ai
   WHERE ai.item_id = aw.item_ptr_id;
   
"""
GET_ITEMS_PER_CHARACTER = """
    SELECT cc.name, COUNT(*)
    FROM charactercreator_character AS cc,
    armory_item AS ai, charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id AND cci.item_id = ai.item_id
    GROUP BY cc.character_id
    ORDER BY 1 DESC
    LIMIT 20;

"""

GET_WEAPONS_PER_CHARACTER = """
    SELECT cc.name, COUNT(*)
    FROM charactercreator_character AS cc,
    armory_weapon AS aw, charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id AND cci.item_id = aw.item_ptr_id
    GROUP BY cc.character_id
    ORDER BY 1 DESC
    LIMIT 20;
"""

GET_NON_WEAPONS = """
  SELECT COUNT(*) 
  FROM armory_item 
  WHERE armory_item.item_id NOT IN 
  (SELECT armory_weapon.item_ptr_id 
  FROM armory_weapon)

"""

AVG_ITEMS_PER_CHARACTER = """
SELECT AVG(num_item) 
FROM (SELECT character_id, character_name,
COUNT(DISTINCT item_id) AS num_item FROM 
(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name 
FROM charactercreator_character 
AS cc, armory_item AS ai, charactercreator_character_inventory 
AS cci WHERE cc.character_id = cci.character_id 
AND ai.item_id = cci.item_id) GROUP BY 1);
"""
AVG_WEAPONS_PER_CHARACTER = """
    SELECT AVG(num_weapons)
    FROM(SELECT character_id, character_name, COUNT(DISTINCT aw_name) AS num_weapons
    FROM (SELECT cc.character_id, cc.name AS character_name, aw.item_ptr_id AS aw_name 
    FROM charactercreator_character 
    AS cc, armory_weapon AS aw, charactercreator_character_inventory 
    AS cci WHERE cc.character_id = cci.character_id 
    AND aw.item_ptr_id = cci.item_id) 
    GROUP BY 1)
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()

    total_characters = execute_query(curs, GET_TOTAL_CHARACTERS)
    print('total characters', total_characters)

    number_cleric = execute_query(curs, GET_CHARACTERS_CLERIC)
    number_fighter = execute_query(curs, GET_CHARACTERS_FIGHTER)
    print('total cleric', number_cleric, 'total fighter', number_fighter)
    number_mage = execute_query(curs, GET_CHARACTERS_MAGE)
    number_necromancer = execute_query(curs, GET_CHARACTERS_NECROMANCER)
    print('total mage', number_mage, 'total necromancer', number_necromancer)
    number_thief = execute_query(curs, GET_CHARACTERS_THIEF)
    print('total thief', number_thief)

    total_items = execute_query(curs, GET_TOTAL_ITEMS)
    print('total items', total_items)

    total_weapons = execute_query(curs, GET_WEAPONS)
    print('total weapons', total_weapons)

    non_weapons = execute_query(curs, GET_NON_WEAPONS)
    print('non weapons', non_weapons)

    items_per_character = execute_query(curs, GET_ITEMS_PER_CHARACTER)
    print('items per character', items_per_character)

    weapons_per_character = execute_query(curs, GET_WEAPONS_PER_CHARACTER)
    print('weapons per character', weapons_per_character)

    average_items_per_character = execute_query(curs, AVG_ITEMS_PER_CHARACTER)
    print('average items per character', average_items_per_character)

    average_weapons_per_character = execute_query(curs, AVG_WEAPONS_PER_CHARACTER)
    print('average weapons_per_character', average_weapons_per_character)
