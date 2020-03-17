import pandas as pd
import sqlite3

DB_FILE_PATH = 'rpg_db.sqlite3'
connection = sqlite3.connect(DB_FILE_PATH)
curs = connection.cursor()

#-- How many total Characters are there?
query1 = '''
SELECT COUNT() FROM charactercreator_character cc;
'''
result1 = curs.execute(query1).fetchall()
print('\n****RESULT1:****\n-- How many total Characters are there?\n', result1, '\n')


#-- How many of each specific subclass?
query2 = '''
SELECT COUNT(DISTINCT charactercreator_cleric.character_ptr_id)as cleric
     , COUNT(DISTINCT charactercreator_fighter.character_ptr_id) as fighter
     , COUNT(DISTINCT charactercreator_mage.character_ptr_id) as mage
     -- , COUNT(DISTINCT charactercreator_necromancer.mage_ptr_id) as nec
     , COUNT(DISTINCT charactercreator_thief.character_ptr_id) as theif
FROM charactercreator_cleric
   , charactercreator_fighter
   , charactercreator_mage
   -- , charactercreator_necromancer
   , charactercreator_thief;
'''
result2 = curs.execute(query2).fetchall()
print('\n****RESULT2:****\n-- How many of each specific subclass?\n', result2, '\n')


#-- How many total Items?
query3 = '''
SELECT COUNT(DISTINCT armory_item.item_id) 
FROM armory_item;
'''
result3 = curs.execute(query3).fetchall()
print('\n****RESULT3:****\n-- How many total Items?\n', result3, '\n')


#-- How many of the Items are weapons? How many are not?
query4 = '''
SELECT COUNT(DISTINCT armory_item.item_id) as 'total items'
     , COUNT(DISTINCT armory_weapon.item_ptr_id) as weapons
     , (COUNT(DISTINCT armory_item.item_id)) - (COUNT(DISTINCT armory_weapon.item_ptr_id)) as 'non-weapons'
FROM armory_item
   , armory_weapon;
'''
result4 = curs.execute(query4).fetchall()
print('\n****RESULT4:****\n-- How many of the Items are weapons? How many are not?\n', result4, '\n')


#-- How many Items does each character have? (Return first 20 rows)
query5 = '''
SELECT cc.character_id
     , cc.name 
     , COUNT(cci.item_id) AS 'num of items' 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
GROUP BY cc.character_id
LIMIT 20;
'''
result5 = curs.execute(query5).fetchall()
print('\n****RESULT5:****\n-- How many Items does each character have? (Return first 20 rows)\n', result5, '\n')


#-- How many Weapons does each character have? (Return first 20 rows)
query6 = '''
SELECT cc.character_id
     , cc.name 
     , COUNT(aw.item_ptr_id ) AS 'num of weapons' 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
LEFT JOIN armory_weapon aw
ON cci.item_id = aw.item_ptr_id
-- WHERE cci.item_id = aw.item_ptr_id 
GROUP BY cc.character_id
LIMIT 20;
'''
result6 = curs.execute(query6).fetchall()
print('\n****RESULT6:****\n-- How many Weapons does each character have? (Return first 20 rows)\n', result6, '\n')



#-- On average, how many Items does each Character have?
query7 = '''
SELECT AVG(num_of_items)
FROM
(SELECT cc.character_id
     , cc.name 
     , COUNT(cci.item_id) AS num_of_items 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
GROUP BY cc.character_id);
'''
result7 = curs.execute(query7).fetchall()
print('\n****RESULT7:****\n-- On average, how many Items does each Character have?\n', result7, '\n')




#-- On average, how many Weapons does each character have?
query8 = '''
SELECT AVG(num_of_weapons)
FROM 
(SELECT cc.character_id
     , cc.name 
     , COUNT(aw.item_ptr_id ) AS num_of_weapons
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
LEFT JOIN armory_weapon aw
ON cci.item_id = aw.item_ptr_id
-- WHERE cci.item_id = aw.item_ptr_id 
GROUP BY cc.character_id);
'''
result8 = curs.execute(query8).fetchall()
print('\n****RESULT8:****\n-- On average, how many Weapons does each character have?\n', result8, '\n')