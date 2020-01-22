import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

#How many total Characters are there?
print('How many total Characters are there?')
query = 'SELECT COUNT(*) FROM charactercreator_character;'
tot_chars = curs.execute(query).fetchall()[0][0]
print(tot_chars)

# How many of each specific subclass?
print('How many of each specific subclass?')
subclasses = [
    'charactercreator_cleric', 'charactercreator_fighter',
    'charactercreator_mage', 'charactercreator_necromancer',
    'charactercreator_thief'
    ]

for subclass in subclasses:
    query = 'SELECT COUNT(*) FROM ' + subclass + ';'
    count = curs.execute(query).fetchall()[0][0]
    print(subclass + ': ' + str(count))

# How many total Items?
print('How many total Items?')
query = 'SELECT COUNT(*) FROM armory_item;'
tot_items = curs.execute(query).fetchall()[0][0]
print(tot_items)

# How many of the Items are weapons? How many are not?
print('How many of the Items are weapons? How many are not?')
query = 'SELECT COUNT(*) FROM armory_weapon;'
tot_weapons = curs.execute(query).fetchall()[0][0]
print(f'{tot_weapons} are weapons, {tot_items-tot_weapons} are not')

# How many Items does each character have? (Return first 20 rows)
print('How many Items does each character have? (Return first 20 rows)')
query = '''
    SELECT cc.character_id, COUNT(*) itemcount 
    FROM charactercreator_character as cc, armory_item as ai,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id and ai.item_id = cci.item_id
    GROUP BY cc.character_id;
    '''
char_item_count = curs.execute(query).fetchall()[:20]
print(char_item_count)

# How many Weapons does each character have? (Return first 20 rows)
# this ignores characters with no weapons
print('How many Weapons does each character have? (Return first 20 rows)')
query = '''
    SELECT cc.character_id, COUNT(*) weaponcount 
    FROM charactercreator_character as cc, armory_weapon as aw,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id 
    and aw.item_ptr_id= cci.item_id
    GROUP BY cc.character_id;
    '''
char_weapon_count = curs.execute(query).fetchall()[:20]
print(char_weapon_count)

# On average, how many Items does each Character have?
print('On average, how many Items does each Character have?')
query = '''
    SELECT AVG(itemcount)
    FROM(
	    SELECT cc.character_id, COUNT(*)  itemcount
	    FROM charactercreator_character as cc, armory_item as ai,
	    charactercreator_character_inventory as cci
	    WHERE cc.character_id = cci.character_id and ai.item_id = cci.item_id
	    GROUP BY cc.character_id);
    '''
avg_items = curs.execute(query).fetchall()[0][0]
print(avg_items)

# On average, how many Weapons does each character have?
print('On average, how many Weapons does each character have?')
query = '''
    SELECT COUNT(*) weaponcount 
    FROM charactercreator_character as cc, armory_weapon as aw,
        charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id 
        and aw.item_ptr_id= cci.item_id;
'''
# gets total number of weapons held by characters
weapons_held = curs.execute(query).fetchall()[0][0]

# calculate average weapons per character
avg_weapons = weapons_held/tot_chars
print(avg_weapons)