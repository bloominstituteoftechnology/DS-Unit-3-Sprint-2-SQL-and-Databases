import sqlite3
import os

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

#How many total Characters are there?
q1 = 'SELECT COUNT(character_id) FROM charactercreator_character'

#How many of each specific subclass?
q2a = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'
q2b = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'
q2c = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage'
q2d = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer'
q2e = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief'

#How many total items?
q3 = 'SELECT COUNT(item_id) FROM armory_item'

#How many of the items are weapons? How many are not?
q4a = 'SELECT COUNT(name) FROM armory_item INNER JOIN armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id'
q4b = 'SELECT COUNT(name) FROM armory_item WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)'

#How many Items does each character have? (Return first 20 rows)
q5 = 'SELECT c.character_id, c.name, i.item_id \
FROM charactercreator_character AS c \
INNER JOIN charactercreator_character_inventory AS i \
ON c.character_id = i.character_id \
LIMIT 20'

#How many Weapons does each character have? (Return first 20 rows)
q6 = 'SELECT c.character_id, c.name, i.item_id \
FROM charactercreator_character AS c \
INNER JOIN charactercreator_character_inventory AS i \
ON c.character_id = i.character_id \
WHERE i.item_id IN (SELECT item_ptr_id FROM armory_weapon) \
LIMIT 20'

#On average, how many items does each Character have?
q7 = 'SELECT AVG(c) FROM (SELECT character_id, COUNT(item_id) as c \
FROM charactercreator_character_inventory GROUP BY character_id)'

#On average, how many Weapons does each character have?
q8 = 'SELECT AVG(c) FROM (SELECT character_id, COUNT(item_id) as C \
FROM charactercreator_character_inventory cci JOIN armory_weapon \
WHERE item_id = item_ptr_id GROUP BY character_id)'

# Execute
curs1 = conn.cursor()
print ('total number of characters:', curs1.execute(q1).fetchall())

curs2a = conn.cursor()
print('total number of clerics:', curs2a.execute(q2a).fetchall())

curs2b = conn.cursor()
print ('total number of fighters:', curs2b.execute(q2b).fetchall())

curs2c = conn.cursor()
print('total number of mages:', curs2c.execute(q2c).fetchall())

curs2d = conn.cursor()
print('total number of necromancers:', curs2d.execute(q2d).fetchall())

curs2e = conn.cursor()
print('total number of theives:', curs2e.execute(q2e).fetchall())

curs3 = conn.cursor()
print('total number of items:', curs3.execute(q3).fetchall())

curs4a = conn.cursor()
print('total number of weapons:', curs4a.execute(q4a).fetchall())

curs4b = conn.cursor()
print('total number of items that are not weapons:', curs4b.execute(q4b).fetchall())

curs5 = conn.cursor()
print('items for first 20 characters:', curs5.execute(q5).fetchall())

curs6 = conn.cursor()
print('weapons for first 20 characters:', curs6.execute(q6).fetchall())

curs7 = conn.cursor()
print('avg items per character:', curs7.execute(q7).fetchall())

curs8 = conn.cursor()
print('avg weapons per character:', curs8.execute(q8).fetchall())
