import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?
size_query = 'SELECT COUNT(*) FROM charactercreator_character;'
size = curs.execute(size_query).fetchone()[0]
print(f'\nThe total number of characters is {size}.\n')

# How many of each specific subclass?
for role in ['mage', 'thief', 'cleric', 'fighter']:
    query = f'SELECT COUNT(*) FROM charactercreator_{role};'
    number = curs.execute(query).fetchone()[0]
    role = role if role != "thief" else "thieve"
    print(f'The total nunber of {role}s is {number}.')

necromance_query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
num_necros = curs.execute(necromance_query).fetchone()
print(f'\nOf all the mages, {num_necros[0]} are necromancers.\n')

# How many total Items?
num_items_query = 'SELECT COUNT(*) FROM armory_item;'
num_items = curs.execute(num_items_query).fetchone()[0]
print(f'There are {num_items} distinct items in the game.')

# How many of the Items are weapons? How many are not?
num_weapons_query = 'SELECT COUNT(*) FROM armory_weapon;'
num_weapons = curs.execute(num_weapons_query).fetchone()[0]
print(f'Of those {num_items} items, {num_weapons} are weapons '
      f'and {num_items - num_weapons} are not weapons.\n')

# How many Items does each character have? (Return first 20 rows)
items_per_char_query = ("""
    SELECT cc.character_id, cc.name, COUNT(cci.item_id) AS item_count
      FROM charactercreator_character AS cc
           INNER JOIN charactercreator_character_inventory AS cci
           ON cc.character_id = cci.character_id
     GROUP BY cc.character_id
     LIMIT 20
     ;""")

items_per_char = curs.execute(items_per_char_query).fetchall()
print('**********Number of Items per Character***********')
print(tabulate(items_per_char,
      headers=['ID', 'Character Name', 'Item Count']))


# How many Weapons does each character have? (Return first 20 rows)
weapons_per_char_query = ("""
    SELECT cc.character_id, cc.name, COUNT() AS weapon_count
      FROM charactercreator_character AS cc
           INNER JOIN charactercreator_character_inventory AS cci
           ON cc.character_id = cci.character_id
           INNER JOIN armory_item as ai
           ON cci.item_id = ai.item_id
           INNER JOIN armory_weapon as aw
           ON ai.item_id = aw.item_ptr_id
     GROUP BY cc.character_id
     LIMIT 20
     ;""")

weapons_per_char = curs.execute(weapons_per_char_query).fetchall()
print('\n**********Number of Weapons per Character***********')
print(tabulate(weapons_per_char, headers=['ID', 'Name', 'Weapon Count']))

# On average, how many Items does each Character have?
avg_items_query = ("""
    SELECT AVG(item_count) FROM
    (
        SELECT cc.character_id, COUNT(cci.item_id) AS item_count
          FROM charactercreator_character AS cc
               LEFT JOIN charactercreator_character_inventory AS cci
               ON cc.character_id = cci.character_id
         GROUP BY cc.character_id
    )
    ;""")

avg_items = curs.execute(avg_items_query).fetchone()[0]
print(f'\nThere are {avg_items:.2f} items per player on average.')

# On average, how many Weapons does each character have?

# First, the average for those characters who have at least one weapon
avg_weapons_min_one_query = ("""
    SELECT AVG(weapon_count) FROM
    (
        SELECT cc.character_id, COUNT(aw.item_ptr_id) AS weapon_count
          FROM charactercreator_character AS cc
               INNER JOIN charactercreator_character_inventory as cci
               ON cc.character_id = cci.character_id
               INNER JOIN armory_item as ai
               ON cci.item_id = ai.item_id
               INNER JOIN armory_weapon as aw
               ON ai.item_id = aw.item_ptr_id
         GROUP BY cc.character_id
    )
    ;""")

avg_weapons_min_one = curs.execute(avg_weapons_min_one_query).fetchone()[0]
print(f'\nThere are {avg_weapons_min_one:.2f} average weapons among players '
      'who have at least one weapon.')

# Second, the average for over all characters
avg_weapons_query = ("""
    SELECT AVG(weapon_count) FROM
    (
        SELECT cc.character_id, COUNT(aw.item_ptr_id) AS weapon_count
          FROM charactercreator_character AS cc
               INNER JOIN charactercreator_character_inventory as cci
               ON cc.character_id = cci.character_id
               INNER JOIN armory_item as ai
               ON cci.item_id = ai.item_id
               LEFT JOIN armory_weapon as aw
               ON ai.item_id = aw.item_ptr_id
         GROUP BY cc.character_id
    )
    ;""")

avg_weapons = curs.execute(avg_weapons_query).fetchone()[0]
print(f'\nThere are {avg_weapons:.2f} average weapons among all players.\n')

curs.close()
conn.close()
