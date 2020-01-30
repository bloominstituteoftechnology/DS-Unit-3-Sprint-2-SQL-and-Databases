import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Get total number of characters
query = 'SELECT COUNT(*) FROM charactercreator_character;'
num_characters = curs.execute(query).fetchall()
print("Total number of characters:", num_characters[0][0])

# Get number of characters of each class
query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
num_clerics = curs.execute(query).fetchall()
print("Total number of clerics:", num_clerics[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
num_fighters = curs.execute(query).fetchall()
print("Total number of fighters:", num_fighters[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_mage;'
num_mages = curs.execute(query).fetchall()
print("Total number of mages:", num_mages[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
num_necro = curs.execute(query).fetchall()
print("Total number of necromancers:", num_necro[0][0])

query = 'SELECT COUNT(*) FROM charactercreator_thief;'
num_thieves = curs.execute(query).fetchall()
print("Total number of thieves:", num_thieves[0][0])

# Get total number of items
query = 'SELECT COUNT(*) FROM armory_item;'
num_items = curs.execute(query).fetchall()
print("Total number of items:", num_items[0][0])

# Get total number of weapons
query = 'SELECT COUNT(*) FROM armory_weapon;'
num_weapons = curs.execute(query).fetchall()
print('Total number of weapons:', num_weapons[0][0])

print('Total number of non-weapons:', num_items[0][0] - num_weapons[0][0])

# Get number of character items for first 20 characters

