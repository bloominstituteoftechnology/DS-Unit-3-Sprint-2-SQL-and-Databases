import os
import sqlite3
import pandas as pd


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Question 1
curs.execute('SELECT COUNT (name) \
                      FROM charactercreator_character;')
print('Answer 1:', curs.fetchall()[0][0], '\n')

# Question 2
curs.execute('SELECT COUNT (character_ptr_id) \
                      FROM charactercreator_mage;')
print('Answer 2:', curs.fetchall()[0][0])

curs.execute('SELECT COUNT (character_ptr_id) \
                      FROM charactercreator_fighter;')
print('Answer 2:', curs.fetchall()[0][0])

curs.execute('SELECT COUNT (character_ptr_id) \
                      FROM charactercreator_thief;')
print('Answer 2:', curs.fetchall()[0][0])

curs.execute('SELECT COUNT (character_ptr_id) \
                      FROM charactercreator_cleric;')
print('Answer 2:', curs.fetchall()[0][0], '\n')

# Question 3
curs.execute('SELECT COUNT (name) \
                      FROM armory_item;')
print('Answer 3:', curs.fetchall()[0][0], '\n')

# Question 4
curs.execute('SELECT COUNT (item_ptr_id) \
                      FROM armory_weapon;')
print('Answer 4:')
print('Is weapon:', curs.fetchall()[0][0])
curs.execute('SELECT item_id FROM armory_item \
              EXCEPT \
              SELECT item_ptr_id FROM armory_weapon \
              ;')
print('Not weapon', len(curs.fetchall()))

# Question 5
query = ("SELECT character_id as 'Character Id', \
         COUNT(item_id) as 'Item Count' \
         FROM charactercreator_character_inventory \
         GROUP BY character_id \
         LIMIT 20 \
         ;")
items_per_character = pd.read_sql(query, conn)
print('Answer 5:')
print(items_per_character, '\n')

# Question 6
query = ("SELECT cci.character_id AS 'Character ID', \
         COUNT (aw.item_ptr_id) AS 'Weapon Count' \
         FROM charactercreator_character_inventory as cci \
         INNER JOIN armory_item as ai ON cci.item_id = ai.item_id \
         INNER JOIN armory_weapon as aw ON ai.item_id = aw.item_ptr_id \
         GROUP BY cci.character_id \
         LIMIT 20 \
         ;")
weapons_per_character = pd.read_sql(query, conn)
print(weapons_per_character, '\n')

# Question 7
query = ('SELECT AVG(c) \
         FROM( \
	         SELECT character_id, COUNT(item_id) as c \
	         FROM charactercreator_character_inventory \
	         GROUP BY character_id \
             ) \
         ;')
curs.execute(query)
print('Answer 7:', curs.fetchall()[0][0], '\n')

# Question 8
query = ("SELECT AVG(wc) \
         FROM( \
	         SELECT cci.character_id AS 'Character ID', \
             COUNT (aw.item_ptr_id) AS wc \
             FROM charactercreator_character_inventory as cci \
             INNER JOIN armory_item as ai ON cci.item_id = ai.item_id \
             INNER JOIN armory_weapon as aw ON ai.item_id = aw.item_ptr_id \
             GROUP BY cci.character_id \
             ) \
         ;")
curs.execute(query)
print('Answer 8:', curs.fetchall()[0][0])
