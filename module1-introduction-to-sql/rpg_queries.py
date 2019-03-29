import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

print('Total number of Characters:')
query1 = 'SELECT COUNT(*) FROM charactercreator_character;'
print(curs.execute(query1).fetchall())

print('Number of characters in cleric subclass:')
query21 ='SELECT count(*) from charactercreator_cleric'
print(curs.execute(query21).fetchall()) 

print('Number of characters in fighter subclass:')
query22 = 'SELECT count(*) from charactercreator_fighter'
print(curs.execute(query22).fetchall()) 

print('Number of characters in mage subclass:')
query23 = 'SELECT count(*) from charactercreator_mage'
print(curs.execute(query23).fetchall())

print('Number of characters in necromancer subclass:')
query24 = 'SELECT count(*) from charactercreator_necromancer'
print(curs.execute(query24).fetchall())

print('Number of characters in thief subclass:')
query25 = 'SELECT count(*) from charactercreator_thief;'
print(curs.execute(query25).fetchall())

print('Number of items:')
query3 = 'SELECT count(*) FROM armory_item;'
print(curs.execute(query3).fetchall())

print('Number of items that are weapons:')
query4 = 'SELECT count(*) FROM armory_item as item, armory_weapon as weapon WHERE item.item_id = weapon.item_ptr_id;'
print(curs.execute(query4).fetchall())

print('Number of items that are not weapons:')
query5 = 'SELECT COUNT(*) FROM armory_item WHERE armory_item.item_id not in (SELECT item_ptr_id FROM armory_weapon);'
print(curs.execute(query5).fetchall())

print('Number of items in characters:')
query6 = 'SELECT character_id FROM charactercreator_character a, armory_item b WHERE a.character_id = b.item_id LIMIT 20;'
print(curs.execute(query6).fetchall())

print('Number of weapons in characters:')
query7 = 'SELECT character_id from charactercreator_character a, armory_weapon b WHERE a.character_id = b.item_ptr_id LIMIT 20;'
print(curs.execute(query7).fetchall())

print('Average number of items in characters:')
query8 = 'SELECT avg(character_id) FROM charactercreator_character a, armory_item b WHERE a.character_id = b.item_id;'
print(curs.execute(query8).fetchall())

print('Average number of weapons in characters:')
query9 = 'SELECT avg(character_id) from charactercreator_character a, armory_weapon b WHERE a.character_id = b.item_ptr_id;'
print(curs.execute(query9).fetchall())