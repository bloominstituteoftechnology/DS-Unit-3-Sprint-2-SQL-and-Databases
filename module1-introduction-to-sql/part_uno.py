import sqlite3
import os

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total characters are there
total_char = curs.execute('''
SELECT Count(*) FROM charactercreator_character;
''')
print(f'''
Total Number of Registered Characters: {total_char.fetchall()[0][0]}\n
''')

# How many of characters are there for each subclass
# cleric / fighter / mage / necromancer / thief
classes = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for i in range(0, len(classes)):
    sub_char = curs.execute(f'''
    SELECT Count(*)
    FROM charactercreator_{classes[i]};
    ''')
    print(f'Total number of {classes[i]}s: \t{sub_char.fetchall()[0][0]}')
    # Not sure if there is an SQL easy way to do this.

# How many total items?
# Get unique ids in charactercreator_character_inventory -> item_id
unique_items = curs.execute(f'''
SELECT COUNT(DISTINCT item_id) FROM charactercreator_character_inventory;
''')
# Could have gotten it from armory_item but meh, same same
unique_item_count = unique_items.fetchall()[0][0]
print(f'\nNumber of unique items in game: {unique_item_count}')

# How many weapon items, how many aren't
weapon_items = curs.execute(f'''
SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon;
''')
# Idk if it's good practice to make sure the items are distinct
weapon_count = weapon_items.fetchall()[0][0]
print(f'''
Unique Weapon Count: {weapon_count}\t
Non-weapon Unique items: {unique_item_count - weapon_count}
''')

# How many items does each toon have: first 20 rows
character_items = curs.execute(f'''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
''')
for i in character_items:
    print(f'Character ID: {i[0]} \tHas {i[1]} items')

# How many weapons does each toon have: first 20 rows
# Use armory_weapon ids and associate
character_weapons = curs.execute(f'''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory c
INNER JOIN armory_weapon a
ON a.item_ptr_id = c.item_id
GROUP BY character_id
LIMIT 20;
''')
print('\n')
for i in character_weapons:
    print(f'Character ID: {i[0]} \tHas {i[1]} weapons')

# Average of items for all characters
average_items = curs.execute(f'''
SELECT AVG(itemCount)
FROM (
    SELECT character_id, COUNT(item_id) itemCount
    FROM charactercreator_character_inventory
    GROUP BY character_id
)
''')
print(f'''
Average # of items for all characters: {average_items.fetchall()[0][0]:.2f}
''')

# Average of weapons for all characters
average_weapons = curs.execute(f'''
SELECT AVG(weaponCount)
FROM (
    SELECT character_id, COUNT(item_id) weaponCount
    FROM charactercreator_character_inventory c
    INNER JOIN armory_weapon a
    ON a.item_ptr_id = c.item_id
    GROUP BY character_id
)
''')
print(f'''
Average # of weapons for all characters: {average_weapons.fetchall()[0][0]:.2f}
''')
