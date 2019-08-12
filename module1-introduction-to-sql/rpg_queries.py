import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')


# Create a query for the total characters
curs = conn.cursor()
char_count = 'SELECT * FROM charactercreator_character'
curs.execute(char_count)
total_characters_count = len(curs.fetchall())
print(f'\nTotal Characters: {total_characters_count}\n')


# Create a query for the number of characters in each class
classes = {'charactercreator_cleric': 0,
           'charactercreator_fighter': 0,
           'charactercreator_mage': 0, 
           'charactercreator_necromancer': 0,
           'charactercreator_thief': 0}

for c in classes.keys():
    curs = conn.cursor()
    char_count = 'SELECT * FROM ' + c
    curs.execute(char_count)
    class_count = len(curs.fetchall())
    classes[c] = class_count
    print(f"There are {class_count} {(c.split('_', 1)[-1] + 's').title()}")

print('NOTE: Mages can also be Necromancers as well')


# Create a query to get the total number of items
# (sum of all items for each character)
curs = conn.cursor()
item_count = 'SELECT * FROM charactercreator_character_inventory'
curs.execute(item_count)
total_items_count = len(curs.fetchall())
print(f'\nTotal Items: {total_items_count}')

# Create a query to check how many of the total items are actually weapons
curs = conn.cursor()
weapon_count = '''
SELECT * FROM charactercreator_character_inventory
INNER JOIN armory_weapon
on item_id = item_ptr_id;
'''
curs.execute(weapon_count)
total_weapon_count = len(curs.fetchall())
print(f'Number of items that are weapons: {total_weapon_count}')

# Use subtraction to find out what items are not weapons
non_weapon_count = total_items_count - total_weapon_count
print(f'Number of items that are not weapons: {non_weapon_count}\n')


# Create a query to check how many items each character has
curs = conn.cursor()
items_per_char = '''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
'''
curs.execute(items_per_char)
print(f'Items per character (Character ID, number of Items)\n{curs.fetchall()}\n')


# Create a query that check has the number of weapons
# each character has (Only if they have more than 1)
curs = conn.cursor()
weapons_per_char = '''
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon AS aw
ON item_id = aw.item_ptr_id
GROUP BY character_id
LIMIT 20;
'''
curs.execute(weapons_per_char)
print(f'Weapons per character (Character ID, number of weapons)\n{curs.fetchall()}\n')

# Create a query of the item average of the item count
curs = conn.cursor()
item_average = '''
SELECT AVG(item_count)
FROM 
(SELECT character_id, COUNT(item_id) AS item_count 
FROM charactercreator_character_inventory 
GROUP BY character_id)
'''
curs.execute(item_average)
print(f'Average items: {curs.fetchone()[0]}')

# Get the weapon average
curs = conn.cursor()
weapon_average = '''
SELECT AVG(item_count)
FROM 
(SELECT character_id, COUNT(item_id) AS item_count 
FROM charactercreator_character_inventory 
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id)
'''
curs.execute(weapon_average)
weapon_average = curs.fetchone()[0]
print(f'Average weapons: {weapon_average}')