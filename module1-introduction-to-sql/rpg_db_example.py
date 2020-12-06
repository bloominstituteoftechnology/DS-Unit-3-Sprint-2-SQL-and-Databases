import sqlite3

def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

GET_CHARACTERS = """
 SELECT *
 FROM charactercreator_character
"""

CHARACTER_COUNT = """
 SELECT COUNT(*)
 FROM charactercreator_character
"""
CLASS_COUNT = """
SELECT (SELECT COUNT(*) FROM charactercreator_cleric) AS cleric,
(SELECT COUNT(*) FROM charactercreator_fighter) AS fighter,
(SELECT COUNT(*) FROM charactercreator_mage) AS mage,
(SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancer,
(SELECT COUNT(*) FROM charactercreator_thief) AS theif
"""
ITEM_COUNT = """
 SELECT COUNT(*)
 FROM armory_item
"""
WEP_COUNT = """
SELECT COUNT(*) name
FROM armory_item
INNER JOIN armory_weapon
ON armory_item.item_id = armory_weapon.item_ptr_id
"""
ITEMS_NO_WEPS = """
SELECT(
SELECT COUNT(*)
FROM armory_item
) -
(SELECT COUNT(*)
FROM armory_weapon
)
"""
CHAR_ITEM_COUNT = """
SELECT character_id, COUNT(*)
FROM charactercreator_character_inventory
GROUP BY item_id LIMIT 20;
"""
CHAR_WEP_COUNT = """
SELECT charactercreator_character_inventory.character_id, COUNT(*)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id LIMIT 20
"""
AVG_WEAPONS = """
SELECT AVG(num_weapons)
FROM
(
SELECT charactercreator_character_inventory.character_id, COUNT(*) AS num_weapons
FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
)
"""
AVG_ITEMS = """
SELECT AVG(num_items)
FROM
(
SELECT charactercreator_character_inventory.character_id, COUNT(*) AS num_items
FROM charactercreator_character_inventory
INNER JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
GROUP BY charactercreator_character_inventory.character_id
)
"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    char_count = execute_query(curs, CHARACTER_COUNT)
    results = execute_query(curs, GET_CHARACTERS)
    class_count = execute_query(curs, CLASS_COUNT)
    item_count = execute_query(curs, ITEM_COUNT)
    wep_count = execute_query(curs, WEP_COUNT)
    items_no_weps = execute_query(curs, ITEMS_NO_WEPS)
    char_item_count = execute_query(curs, CHAR_ITEM_COUNT)
    char_wep_count = execute_query(curs, CHAR_WEP_COUNT)
    avg_items = execute_query(curs, AVG_ITEMS)
    avg_weapons = execute_query(curs, AVG_WEAPONS)
    print(results[0])
    print("Character Count:", char_count)
    print("Class Count (cleric, fighter, mage, necromancer, theif):", class_count)
    print("Item Count", item_count)
    print("Weapon Count:", wep_count)
    print("Items without Weapons:", items_no_weps)
    print("Items per character ID:", char_item_count)
    print("Weapons per character ID:", char_wep_count)
    print("Average Number of Items Per Character:", avg_items)
    print("Average Number of Weapons Per Character:", avg_weapons)



