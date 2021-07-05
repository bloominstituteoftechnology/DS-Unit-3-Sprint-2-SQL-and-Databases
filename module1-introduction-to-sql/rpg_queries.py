import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Query Function
def query(query):
    result = curs.execute(query)
    return result.fetchall()

# How many total Characters are there?
print ('How many total Characters are there?')
total_char = 'SELECT COUNT(character_id) FROM charactercreator_character;'
total_char = query(total_char)[0][0]
print('There are',total_char, 'total characters')

# How many of each specific subclass?
print('\n', '\n', 'How many of each specific subclass?')
mage = 'SELECT COUNT(cm.character_ptr_id) FROM charactercreator_mage as cm;'
thief = 'SELECT COUNT(ct.character_ptr_id) FROM charactercreator_thief as ct;'
cleric = 'SELECT COUNT(ccl.character_ptr_id) FROM charactercreator_cleric as ccl;'
fighter = 'SELECT COUNT(cf.character_ptr_id) FROM charactercreator_fighter as cf;'
necro = 'SELECT COUNT(cn.mage_ptr_id) FROM charactercreator_necromancer as cn;'

total_mage = query(mage)[0][0]
total_thief = query(thief)[0][0]
total_cleric = query(cleric)[0][0]
total_fighter = query(fighter)[0][0]

# Necromancer is a subclass of mage
total_necro = query(necro)[0][0]
# Subtract necromancers from mage class
total_mage = total_mage - total_necro

# Print statements
print('There are',str(total_mage), 'mages in total')
print('There are',str(total_thief), 'thieves in total')
print('There are',str(total_cleric), 'clerics in total')
print('There are',str(total_fighter), 'fighters in total')
print('There are',str(total_necro), 'necromancers in total')

# How many total items?
print('\n', '\n', 'How many total items?')

items = 'SELECT COUNT(ai.item_id) FROM armory_item as ai;'
total_items = query(items)[0][0]
print("There are", total_items, "total items")

# How many of the Items are weapons? How many are not?
print('\n', '\n', 'How many of the Items are weapons? How many are not?')

weapons = 'SELECT COUNT(aw.item_ptr_id) FROM armory_weapon as aw;'
total_weapons = query(weapons)[0][0]
non_weapons = total_items - total_weapons
print(total_weapons, 'of the items in the armory are weapons,', non_weapons, 'are not')

# How many Items does each character have? (Return first 20 rows)
print('\n', '\n', 'How many Items does each character have? (Return first 20 rows)')

char_items = """
SELECT cc.name, COUNT(DISTINCT ai.item_id)
FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci, armory_item AS ai
WHERE cc.character_id = cci.character_id
AND ai.item_id=cci.item_id
GROUP BY 1
LIMIT 20;
"""
num_items = query(char_items)
print("The first 20 characters have the following items: ", num_items)

# How many Weapons does each character have? (Return first 20 rows)
print('\n', '\n', 'How many Weapons does each character have? (Return first 20 rows)')

char_weapons = """
SELECT cc.name, COUNT(DISTINCT aw.item_ptr_id)
FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci, armory_item AS ai, armory_weapon as aw
WHERE cc.character_id = cci.character_id
AND ai.item_id=cci.item_id
AND ai.item_id=aw.item_ptr_id
GROUP BY 1
LIMIT 20;
"""
num_weapons = query(char_weapons)
print('Of the first 20 characters carrying weapons, these are how many they have: ', num_weapons)

# On average, how many Items does each Character have?
print('\n', '\n', 'On average, how many Items does each Character have?')

avg_items = """
SELECT AVG(num_items) FROM
(SELECT cc.name, COUNT(DISTINCT ai.item_id) as num_items
FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci, armory_item AS ai
WHERE cc.character_id = cci.character_id
AND ai.item_id=cci.item_id
GROUP BY 1
LIMIT 20);
"""
avg_items = query(avg_items)[0][0]
print('The average character has', avg_items, 'items')

# On average, how many Weapons does each character have?
print('\n', '\n', 'On average, how many Weapons does each character have?')

avg_weapons = """
SELECT AVG(num_weapons) FROM
(SELECT cc.name, COUNT(DISTINCT aw.item_ptr_id) as num_weapons
FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci, armory_item AS ai, armory_weapon as aw
WHERE cc.character_id = cci.character_id
AND ai.item_id=cci.item_id
AND ai.item_id=aw.item_ptr_id
GROUP BY 1
LIMIT 20);
"""
avg_weapons = query(avg_weapons)[0][0]
print('The average character has', avg_weapons, 'weapons')



