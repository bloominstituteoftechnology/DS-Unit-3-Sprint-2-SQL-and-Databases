import sqlite3

# initialize connection
connection = sqlite3.connect('rpg_db.sqlite3')

# How many total Characters are there?
query1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'
print ('Total Character Count:',connection.cursor().execute(query1).fetchone()[0], '\n')
#302

# # How many of each specific subclass?
query2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
print ('Mage Count:',connection.cursor().execute(query2).fetchone()[0], '\n')
# mage 108, 
query3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
print ('Cleric Count:',connection.cursor().execute(query3).fetchone()[0], '\n')
# cleric 75,
query4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
print ('Fighter Count:',connection.cursor().execute(query4).fetchone()[0], '\n')
# fighter 68
query5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
print ('Necromancer Count:',connection.cursor().execute(query5).fetchone()[0], '\n')
# necromancer 11,
query6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
print ('Thief Count:',connection.cursor().execute(query6).fetchone()[0], '\n') 
#  thief 51

# # no missing values
# SELECT * 
# FROM charactercreator_character
# WHERE charactercreator_character.character_id not in
# (SELECT character_ptr_id FROM charactercreator_cleric)AND
# charactercreator_character.character_id not in
# (SELECT character_ptr_id FROM charactercreator_fighter)AND
# charactercreator_character.character_id not in
# (SELECT character_ptr_id FROM charactercreator_mage)AND
# charactercreator_character.character_id not in
# (SELECT mage_ptr_id FROM charactercreator_necromancer)AND
# charactercreator_character.character_id not in
# (SELECT character_ptr_id FROM charactercreator_thief);


# # How many total Items?
query7 = 'SELECT COUNT(item_id) FROM armory_item;'
print ('Total Items:',connection.cursor().execute(query7).fetchone()[0], '\n')

# 174 Items
# 
# # How many of the Items are weapons? How many are not?
query8 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
print ('Total Weapons:',connection.cursor().execute(query8).fetchone()[0], '\n')

query9 = 'SELECT COUNT(item_id) FROM armory_item WHERE armory_item.item_id not in (SELECT item_ptr_id FROM armory_weapon);'

print ('Total Non Weapons:',connection.cursor().execute(query9).fetchone()[0], '\n')
# # 37 weapon, 137 not
# );

# # How many Items does each character have? (Return first 20 rows)
query10 = 'SELECT name, count(name) FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id GROUP BY characters.character_id LIMIT 20;'
item_counts = connection.cursor().execute(query10).fetchmany(20)
print ('Sample of Item Count by Character Name:')
for char in item_counts:
    print (char[0], char[1])

# # How many Weapons does each character have? (Return first 20 rows)
query11 = 'SELECT name, count(name) AS weapon_count FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id LIMIT 20;'
weapon_counts = connection.cursor().execute(query11).fetchmany(20)
print ('\nSample of Weapon Count by Character Name:')
for char in weapon_counts:
    print (char[0], char[1])

# # On average, how many Items does each Character have?
query12 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id GROUP BY characters.character_id);'
print ('Average Items:',connection.cursor().execute(query12).fetchone()[0], '\n')
# # 2.97 items

# # On average, how many Weapons does each character have?
query13 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id);'
print ('Average Weapons:',connection.cursor().execute(query13).fetchone()[0], '\n')

# # 1.31 weapons