import sqlite3
import numpy as np
import pandas as pd


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM charactercreator_character;'
result = curs.execute(query)
print('Total Character count',result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_mage;'
result = curs.execute(query)
print('Number of Mage characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_thief;'
result = curs.execute(query)
print('Number of Thief characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
result = curs.execute(query)
print('Number of Cleric characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
result = curs.execute(query)
print('Number of Fighter characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
result = curs.execute(query)
print('Number of Necromancer characters', result.fetchall())

query = 'SELECT COUNT(*) FROM armory_item;'
result = curs.execute(query)
print('Number of Items', result.fetchall())

query = 'SELECT COUNT(*) FROM armory_weapon;'
result = curs.execute(query)
print('Number of Weapons', result.fetchall())

query ="""SELECT COUNT(*)
          FROM armory_item AS ai
          WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);"""
result = curs.execute(query)
print('Number of non-Weapons', result.fetchall())

query = """SELECT cc.character_id, COUNT(DISTINCT ai.item_id)
           FROM charactercreator_character AS cc,
           charactercreator_character_inventory as cci,
           armory_item as ai
           WHERE cc.character_id = cci.character_id
           AND ai.item_id = cci.item_id
           GROUP BY 1
           LIMIT 20;"""
result = curs.execute(query)
print('Number items per character, kinda\n', result.fetchall())

query = """
        SELECT cc.character_id, COUNT(DISTINCT aw.item_ptr_id)
        FROM charactercreator_character AS cc,
        charactercreator_character_inventory as cci,
        armory_weapon as aw
        WHERE cc.character_id = cci.character_id
        AND aw.item_ptr_id = cci.item_id
        GROUP BY 1
        LIMIT 20; 
        """
result = curs.execute(query)
print('items that are weapons for each character\n', result.fetchall())

query = """
        SELECT AVG(num_items) FROM
        (SELECT cc.character_id, COUNT(DISTINCT ai.item_id) AS num_items
        FROM charactercreator_character AS cc,
        charactercreator_character_inventory as cci,
        armory_item as ai
        WHERE cc.character_id = cci.character_id
        AND ai.item_id = cci.item_id
        GROUP BY 1); 
        """
result = curs.execute(query)
print('Average items per character', result.fetchall())

query = """
        SELECT AVG(num_weapons) FROM
        (SELECT cc.character_id, COUNT(DISTINCT aw.item_ptr_id) AS num_weapons
        FROM charactercreator_character AS cc,
        charactercreator_character_inventory as cci,
        armory_weapon as aw
        WHERE cc.character_id = cci.character_id
        AND aw.item_ptr_id = cci.item_id
        GROUP BY 1); 
        """
result = curs.execute(query)
print('Average weapons per character', result.fetchall())


df = pd.read_csv('buddymove_holidayiq.csv')
print('df shape', df.shape, 'Column names', df.columns)

bh_conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = bh_conn.cursor()

df.to_sql(review, con=bh_conn)

query = """
        SELECT COUNT(*)
        FROM review
        """
result = curs.execute(query)
print(result)