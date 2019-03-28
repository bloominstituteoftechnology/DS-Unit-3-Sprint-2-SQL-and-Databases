import sqlite3


'''exploration of the rpg dataset in sql'''


'''import rpg_db and make print(cursor object'''
rpgdb = sqlite3.connect('rpg_db.sqlite3')
cursor = rpgdb.cursor()


'''how many characters are in the game?'''
problem1 = 'SELECT COUNT(*) FROM charactercreator_character;'
print(cursor.execute(problem1).fetchall())


'''how many characters of each class are in the game?'''
problem2_cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
print(cursor.execute(problem2_cleric).fetchall())

problem2_fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
print(cursor.execute(problem2_fighter).fetchall())

problem2_mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
print(cursor.execute(problem2_mage).fetchall())

problem2_thief = 'SELECT COUNT(*) FROM charactercreator_thief;'
print(cursor.execute(problem2_thief).fetchall())

problem2_necromancer = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
print(cursor.execute(problem2_necromancer).fetchall())


'''how many items are in the game?'''
problem3 = 'SELECT COUNT(*) FROM armory_item;'
print(cursor.execute(problem3).fetchall())


'''how many weapons are in the game?
    how many non-weapon items?'''
problem4_weapons = 'SELECT COUNT(*) FROM armory_weapon;'
print(cursor.execute(problem4_weapons).fetchall())

problem4_items = """SELECT COUNT(*)
                  FROM armory_item
                  WHERE armory_item.item_id not in (
                  SELECT item_ptr_id FROM armory_weapon);"""
print(cursor.execute(problem4_items).fetchall())

'''how many items do the first twenty characters with items have?'''
problem5 = """SELECT character_id, COUNT(character_id) AS FREQUENCY
                FROM charactercreator_character_inventory
                GROUP BY character_id
                LIMIT 20;"""
print(cursor.execute(problem5).fetchall())


'''how many weapons do the first twenty characters with weapons have?'''
problem6 = """SELECT charactercreator_character_inventory.character_id,
                COUNT(charactercreator_character_inventory.character_id) AS FREQUENCY
                FROM charactercreator_character_inventory, armory_weapon
                WHERE charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
                GROUP BY character_id
                LIMIT 20;"""
print(cursor.execute(problem6).fetchall())


'''How many items does each character have, on average?'''
problem7 = """CREATE TABLE freqtable AS   
                SELECT character_id, COUNT(character_id) AS FREQUENCY
                FROM charactercreator_character_inventory
                GROUP BY character_id;"""
print(cursor.execute(problem7))

problem7_avg = 'SELECT AVG(FREQUENCY) FROM freqtable;'
print(cursor.execute(problem7_avg).fetchall())

'''How many weapons does each character have, on average?'''
problem8 = """CREATE TABLE weapon_freq AS
               SELECT charactercreator_character_inventory.character_id,
               COUNT(charactercreator_character_inventory.character_id) AS FREQUENCY
               FROM charactercreator_character_inventory, armory_weapon
               WHERE charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
               GROUP BY character_id;"""
print(cursor.execute(problem8))

problem8_avg = 'SELECT AVG(FREQUENCY) FROM weapon_freq;'
print(cursor.execute(problem8_avg).fetchall())
