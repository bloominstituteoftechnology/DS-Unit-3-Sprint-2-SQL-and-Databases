import sqlite3

# Establish connection
connection = sqlite3.connect('rpg_db.sqlite3')

# How many total characters were there?
query_1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'
print ('Total Character Count:',connection.cursor().execute(query_1).fetchone()[0], '\n')

# How many of each specific subclass?
# Mage Count
query_2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
print ('Mage Count:',connection.cursor().execute(query_2).fetchone()[0], '\n')
 
# Cleric Count 
query_3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
print ('Cleric Count:',connection.cursor().execute(query_3).fetchone()[0], '\n')

# Fighter Count
query_4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
print ('Fighter Count:',connection.cursor().execute(query_4).fetchone()[0], '\n')

# Necromancer Count
query_5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
print ('Necromancer Count:',connection.cursor().execute(query_5).fetchone()[0], '\n')

# Thief Count
query_6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
print ('Thief Count:',connection.cursor().execute(query_6).fetchone()[0], '\n') 

# How Many Total Items?
query_7 = 'SELECT COUNT(item_id) FROM armory_weapon;'
print ('Total Items:',connection.cursor().execute(query_7).fetchone()[0], '\n')

# How many of the items are weapons? How many are not?
query_8 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
print ('Total Weapons:',connection.cursor().execute(query_8).fetchone()[0], '\n')

query_9 = 'SELECT COUNT(item_id) FROM armory_item WHERE armory_item.item_id not in (SELECT item_ptr_id FROM armory_weapon);'
print ('Total Non Weapons:',connection.cursor().execute(query_9).fetchone()[0], '\n')

# How many items does each character have? (Return first 20 rows)
query_10 = 'SELECT name, count(name) FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id GROUP BY characters.character_id LIMIT 20;'
item_counts = connection.cursor().execute(query_10).fetchmany(20)
print ('Sample of Item Count by Character Name:')
for char in item_counts:
    print (char[0], char[1])

# How many weapons does each character have? (Return first 20 rows)
query_11 = 'SELECT name, count(name) AS weapon_count FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id LIMIT 20;'
weapon_counts = connection.cursor().execute(query_11).fetchmany(20)
print ('\nSample of Weapon Count by Character Name:')
for char in weapon_counts:
    print (char[0], char[1])

# On average, how many items does each character have?
query_12 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id GROUP BY characters.character_id);'
print ('Average Items:',connection.cursor().execute(query_12).fetchone()[0], '\n')

# On average, how many weapons does each character have?
query_13 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id);'
print ('Average Weapons:',connection.cursor().execute(query_13).fetchone()[0], '\n')
