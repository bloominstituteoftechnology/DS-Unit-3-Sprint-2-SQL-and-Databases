import sqlite3

conn = sqlite3.connect('/Users/oliver/Desktop/Lambda_Projects/DS-Unit-3-Sprint-2-SQL-and-Databases-master/module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

characters = 'SELECT COUNT(name) FROM charactercreator_character;'
print(curs.execute(characters).fetchone())

items = 'SELECT COUNT(item_id) FROM armory_item;'
print(curs.execute(items).fetchone())

weapons = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
print(curs.execute(weapons).fetchone())

non_weapons = 'SELECT COUNT(item_id) FROM armory_item WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)'
print(curs.execute(non_weapons).fetchone())

items_by_character = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
print(curs.execute(items_by_character).fetchall())

avg_item_count = 'SELECT AVG(item_id_counts) FROM (SELECT character_id, COUNT(item_id) AS item_id_counts FROM charactercreator_character_inventory GROUP BY character_id)'
print(curs.execute(avg_item_count).fetchone())

avg_weapon_count = 'SELECT AVG(item_id_counts) AS weapon_counts FROM (SELECT character_id, COUNT(item_id) AS item_id_counts FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_id FROM armory_item WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)) GROUP BY character_id)'
print(curs.execute(avg_weapon_count).fetchone())