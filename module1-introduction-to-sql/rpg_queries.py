# imports
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total characters?
curs.execute('''
        SELECT COUNT(DISTINCT character_id)
        FROM charactercreator_character;
        ''')
print(f'Total number of characters: {curs.fetchone()[0]}')

# How many of each specific subclass?
curs.execute('''
        SELECT COUNT(DISTINCT character_ptr_id)
        FROM charactercreator_cleric;
        ''')
print(f'Total number of clerics: {curs.fetchone()[0]}')

curs.execute('''
        SELECT COUNT(DISTINCT character_ptr_id))
        FROM charactercreator_fighter;
        ''')
print(f'Total number of fighters: {curs.fetchone()[0]}')

curs.execute('''
        SELECT COUNT(DISTINCT character_ptr_id)
        FROM charactercreator_mage;
        ''')
print(f'Total number of mages: {curs.fetchone()[0]}')

curs.execute('''
        SELECT COUNT(DISTINCT character_ptr_id)
        FROM charactercreator_thief;
        ''')
print(f'Total number of thieves: {curs.getchone()[0]}')

# How many total Items?
curs.execute('''
        SELECT COUNT(item_id)
        FROM charactercreator_character_inventory;
        ''')
print(f'Total Items: {curs.fetchone()[0]}')

# How many of the Items are weapons? How many are not?
curs.execute('''
        SELECT COUNT(item_ptr_id)
        FROM armory_weapon;
        ''')
print(f'Total weapons: {curs.fetchone()[0]}')

curs.execute('''
        SELECT COUNT(item_id)
        FROM charactercreator_character_inventory
        WHERE item_id
        NOT IN
        (SELECT DISTINCT item_ptr_id
        FROM armory_weapon);
        ''')
print(f'Items not weapons: {curs.fetchone()[0]}')

# How many Items does each character have?
# Return first 20 rows.
curs.execute('''
        SELECT character_id, COUNT(*) AS `num`
        FROM charactercreator_character_inventory
        GROUP BY character_id;
        ''')
print(f'First 20 character item totals: {curs.fetchone[:20]}')

# How many Weapons does each character have?
# Return first 20 rows.
curs.execute('''
        SELECT character_id, COUNT(*) AS `num`
        FROM charactercreator_character_inventory
        GROUP BY character_id
        WHERE item_id IN
        (SELECT DISTINCT item_ptr_id
        FROM armory_weapon);
        ''')

# On average, how many Items does each Character have?
curs.execute('''
        )
##### NOT FINISHED #####