# SQLite3 queries for module 1 Assignment

import sqlite3

connection = sqlite3.connect('rpg_db.sqlite3')
cursor = connection.cursor()

# Total number of characters
def character_count:
    cursor.execute("""SELECT COUNT(character_id)
                      FROM charactercreator_character;
                   """)
    return cursor.fetchall()

# Number in each subclass
def subclass_count:
    # mage count
    cursor.execute("""SELECT  'mage', COUNT(character_ptr_id) 
                      FROM charactercreator_mage
                      
                      UNION

                      SELECT 'cleric', COUNT(character_ptr_id)
                      FROM charactercreator_cleric
                      
                      UNION
	
                      SELECT 'fighter' COUNT(character_ptr_id)
                      FROM charactercreator_fighter
                      
                      UNION
	
                      SELECT 'thief' COUNT(character_ptr_id)
                      FROM charactercreator_thief;
                   """)
    return cursor.fetchall()
    
# Number of total Items?
def total_items():
    cursor.execute("""SELECT COUNT(item_id)
                      FROM armory_item;
                   """)
    return cursor.fetchall()


# Number of weapons.
def weapon_items():
    cursor.execute("""SELECT COUNT(item_id)
                      FROM armory_item
                      WHERE item_id IN
                          (SELECT item_ptr_id
                          FROM armory_weapon);
                    """)
    return cursor.fetchall()

# Number that are not weapons
def nonweapon_items():
    cursor.execute("""SELECT COUNT(item_id)
                      FROM armory_item
                      WHERE item_id NOT IN
                          (SELECT item_ptr_id
                          FROM armory_weapon);
                   """)
    return cursor.fetchall()


# Number of items each character has... Return the first twenty rows
def character_items():
    cursor.execute("""SELECT character_id, count(item_id)
                      FROM charactercreator_character_inventory
                      GROUP BY character_id
                      LIMIT 20;
                   """)
    return cursor.fetchall()


# Number of weapons each character has... Return the first twenty rows
def character_weapons():
    cursor.execute("""SELECT character_id, count(item_id)
                      FROM charactercreator_character_inventory
                      WHERE item_id IN
                        (SELECT distinct item_ptr_id
                        FROM armory_weapon)
                      GROUP BY character_id
                      LIMIT 20;
                      """)
    return curs.fetchall()


# The average of how many items each character has
def avg_items():
    cursor.execute("""SELECT AVG(items)
                      FROM 
                          (SELECT character_id, count(item_id) as items
                           FROM charactercreator_character_inventory
                      GROUP BY character_id);
                    """)
    return cursor.fetchall()


# The average of how many weapons each character has
def avg_weapons():
    cursor.execute("""SELECT AVG(items)
                      FROM 
                        (SELECT character_id, count(item_id) as items
                        FROM charactercreator_character_inventory
                      WHERE item_id IN 
                        (SELECT distinct item_ptr_id
                        FROM armory_weapon)
                      GROUP BY character_id);
                    """)
    return cursor.fetchall()
    

