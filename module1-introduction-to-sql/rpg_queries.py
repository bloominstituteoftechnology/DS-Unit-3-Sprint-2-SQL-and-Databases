import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = '''SELECT count(*)
           FROM charactercreator_character;'''
total_characters = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_cleric'''
curs.execute(query).fetchall()
total_clerics = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_fighter'''
curs.execute(query).fetchall()
total_fighters = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_mage'''
curs.execute(query).fetchall()
total_mages = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_thief'''
curs.execute(query).fetchall()
total_thieves = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_necromancer'''
curs.execute(query).fetchall()
total_necromancers = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM charactercreator_necromancer'''
curs.execute(query).fetchall()
total_necromancers = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM armory_item'''
curs.execute(query).fetchall()
total_items = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM armory_weapon'''
curs.execute(query).fetchall()
total_weapons = curs.execute(query).fetchall()[0][0]

total_non_weapons = total_items - total_weapons

query = '''SELECT count(*)
           FROM charactercreator_character_inventory
           GROUP BY character_id
           LIMIT 20'''
number_of_items_per_character_raw = curs.execute(query).fetchall()
number_of_items_per_character = []
for element in number_of_items_per_character_raw:
    number_of_items_per_character.append(element[0])
number_of_items_per_character

query = '''SELECT count(*)
           FROM charactercreator_character_inventory
           WHERE item_id IN
           (
               SELECT item_ptr_id FROM armory_weapon
           )
           GROUP BY character_id
           LIMIT 20'''
number_of_weapons_per_character_raw = curs.execute(query).fetchall()
number_of_weapons_per_character = []
for element in number_of_weapons_per_character_raw:
    number_of_weapons_per_character.append(element[0])
number_of_weapons_per_character

query = '''SELECT count(*)
           FROM charactercreator_character_inventory
           GROUP BY character_id'''
number_of_items_per_character_raw = curs.execute(query).fetchall()
item_count = 0
for element in number_of_items_per_character_raw:
    item_count += element[0]
average_number_of_items_per_character = item_count / len(
    number_of_items_per_character_raw)

query = '''SELECT count(*)
           FROM charactercreator_character_inventory
           WHERE item_id IN
           (
               SELECT item_ptr_id FROM armory_weapon
           )
           GROUP BY character_id'''
number_of_weapons_per_character_raw = curs.execute(query).fetchall()
weapon_count = 0
for element in number_of_weapons_per_character_raw:
    weapon_count += element[0]
average_number_of_weapons_per_character = weapon_count / len(
    number_of_weapons_per_character_raw)

print('Total number of characters:', total_characters,
      '\nTotal number of characters who are clerics:', total_clerics,
      '\nTotal number of characters who are fighters:', total_fighters,
      '\nTotal number of characters who are mages:', total_mages,
      '\nTotal number of characters who are thieves:', total_thieves,
      '\nTotal number of mages who are necromancers:', total_necromancers,
      '\nTotal number of items:', total_items,
      '\nTotal number of items that are weapons:', total_weapons,
      '\nTotal number of items that are not weapons:', total_non_weapons,
      '\nTotal number of items per character:', number_of_items_per_character,
      '\nTotal number of weapons per character:',
      number_of_weapons_per_character,
      '\nAverage number of items per character:',
      average_number_of_items_per_character,
      '\nAverage number of weapons per character:',
      average_number_of_weapons_per_character)