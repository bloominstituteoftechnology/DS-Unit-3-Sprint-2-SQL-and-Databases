import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?
query = '''SELECT COUNT(*)
FROM charactercreator_character;
'''
curs.execute(query)
total_characters = curs.fetchall()[0][0]
print('Total Characters:', total_characters)

# How many of each specific subclass?
cleric_query = '''SELECT COUNT(*)
FROM charactercreator_cleric;
'''
curs.execute(cleric_query)
cleric_number = curs.fetchall()[0][0]
print('Clerics:', cleric_number)

fighter_query = '''SELECT COUNT(*)
FROM charactercreator_fighter;
'''
curs.execute(fighter_query)
fighter_number = curs.fetchall()[0][0]
print('Fighters:', fighter_number)

mage_query = '''SELECT COUNT(*)
FROM charactercreator_mage;
'''
curs.execute(mage_query)
mage_number = curs.fetchall()[0][0]
print('Mages:', mage_number)

necromancer_query = '''SELECT COUNT(*)
FROM charactercreator_necromancer;
'''
curs.execute(necromancer_query)
necromancer_number = curs.fetchall()[0][0]
print('Necromancers:', necromancer_number)

thief_query = '''SELECT COUNT(*)
FROM charactercreator_thief;
'''
curs.execute(thief_query)
thief_number = curs.fetchall()[0][0]
print('Thieves:', thief_number)

# How many total Items?
query = '''SELECT COUNT(*)
FROM armory_item;
'''
curs.execute(query)
total_items = curs.fetchall()[0][0]
print('Total Items:', total_items)

# How many of the Items are weapons? How many are not?
query = '''SELECT COUNT(*)
FROM armory_weapon;
'''
curs.execute(query)
weapons = curs.fetchall()[0][0]
non_weapons = total_items - weapons
print('Total Weapons:', weapons)
print('Total Non-Weapon Items:', non_weapons)

# How many Items does each character have? (Return first 20 rows)
query = '''SELECT cc.character_id, cc.name AS character_name,
COUNT(ai.item_id) AS num_items
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY cc.character_id
ORDER BY cc.name
LIMIT 20;
'''
curs.execute(query)
characters_items = pd.DataFrame(curs.fetchall())
print("Number of Items by Characters:\n", characters_items)

# How many Weapons does each character have? (Return first 20 rows)
query = '''SELECT cc.character_id, cc.name AS character_name,
COUNT(aw.item_ptr_id) AS num_weapons
FROM charactercreator_character AS cc,
armory_weapon AS aw,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND aw.item_ptr_id = cci.item_id
GROUP BY cc.character_id
ORDER BY cc.name
LIMIT 20;
'''
curs.execute(query)
characters_weapons = pd.DataFrame(curs.fetchall())
print('Number of Weapons by Character:\n', characters_weapons)

# On average, how many Items does each Character have?
query = '''SELECT AVG(num_items)
    FROM
        (
        SELECT cc.character_id, cc.name AS character_name,
        COUNT(ai.item_id) AS num_items
        FROM charactercreator_character AS cc,
        armory_item AS ai,
        charactercreator_character_inventory AS cci
        WHERE cc.character_id = cci.character_id
        AND ai.item_id = cci.item_id
        GROUP BY cc.character_id
        );
'''
curs.execute(query)
avg_items = curs.fetchall()[0][0]
print('Average Items per Character:', avg_items)

# On average, how many Weapons does each character have?
query = '''SELECT AVG(num_weapons)
    FROM
        (
        SELECT cc.character_id, cc.name AS character_name,
        COUNT(aw.item_ptr_id) AS num_weapons
        FROM charactercreator_character AS cc,
        armory_weapon AS aw,
        charactercreator_character_inventory AS cci
        WHERE cc.character_id = cci.character_id
        AND aw.item_ptr_id = cci.item_id
        GROUP BY cc.character_id
        );
'''
curs.execute(query)
avg_weapons = curs.fetchall()[0][0]
print('Average Weapons per Character:', avg_weapons)
