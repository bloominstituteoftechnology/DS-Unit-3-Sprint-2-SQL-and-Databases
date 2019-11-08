"""
A few fun queries in SQL
"""

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
print('opened database successfully')
curs = conn.cursor()


print("\nHow many of each specific class?")
class_list = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for cls in class_list:
    query = f"select count(*) from charactercreator_{cls};"
    print(f"{cls}:",curs.execute(query).fetchall()[0][0])


print("\nHow many total characters are there?")
query = "select count(*) from charactercreator_character;"
print(curs.execute(query).fetchall()[0][0])

print("\nHow many total items?")
query = 'SELECT COUNT (item_id) FROM armory_item;'
print(curs.execute(query).fetchall()[0][0])

print("\nHow many of the items are weapons?")
query = 'SELECT COUNT (item_ptr_id) FROM armory_weapon;'
print(curs.execute(query).fetchall()[0][0])

print("\nHow many items does each characater have?")
query = 'SELECT character_id, COUNT (item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
items_chars = curs.execute(query).fetchall()
for char, count in items_chars:
    print(f'character: {char}, item count: {count}')


print("\nOn average, how many items does each character have?")
query = 'SELECT AVG(item_count) FROM (SELECT character_id, COUNT (item_id) as item_count FROM charactercreator_character_inventory GROUP BY character_id);'
print(curs.execute(query).fetchall()[0][0])
