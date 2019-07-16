import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
print('Assignment_1')


# 1. How many total Characters are there?
char_query = 'SELECT COUNT(*) FROM charactercreator_character;'
char_result = curs.execute(char_query)
# Answer
print('1. There are', char_result.fetchall()[0][0], 'total characters')


# 2. How many of each specific subclass?
# Mages
mage_query = 'SELECT COUNT(*) FROM charactercreator_mage;'
mage_result = curs.execute(mage_query)
mages = mage_result.fetchall()[0][0]
# Thiefs
thief_query = 'SELECT COUNT(*) FROM charactercreator_thief;'
thief_result = curs.execute(thief_query)
thiefs= thief_result.fetchall()[0][0]
# Clerics
cleric_query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
cleric_result = curs.execute(cleric_query)
clerics = cleric_result.fetchall()[0][0]
# Fighters
fighter_query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
fighter_result = curs.execute(fighter_query)
fighters = fighter_result.fetchall()[0][0]
# Answer
print('2. There are',mages,'mages',thiefs,'thiefs',clerics,'clerics','and',
      fighters,'fighters')


# 3. How many total Items?
item_query = 'SELECT COUNT(*) FROM armory_item;'
item_result = curs.execute(item_query)
items = item_result.fetchall()[0][0]
# Answer
print('3. There are', items, 'total items')


# 4. How many of the Items are weapons? How many are not?
weapon_query = 'SELECT COUNT(*) FROM armory_weapon;'
weapon_result = curs.execute(weapon_query)
weapons = weapon_result.fetchall()[0][0]
nonweapons = items - weapons
# Answer
print('4. There are',weapons,'weapons','and',nonweapons,'nonweapns')


# 5. How many Items does each character have? (Return first 20 rows)
char_item_query = """SELECT character_id, COUNT(*) AS `num`
                     FROM charactercreator_character_inventory
                     GROUP BY character_id"""
char_item_result = curs.execute(char_item_query)
print('5. Character item counts\n',char_item_result.fetchall()[:20])


# 6. How many Weapons does each character have? (Return first 20 rows)
weapon_count_query = """SELECT character_id, item_id, COUNT(*)
                      FROM charactercreator_character_inventory
                      WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
                      GROUP BY character_id LIMIT 20;"""
weapon_count_result = curs.execute(weapon_count_query)
print('6. Character weapon counts\n',weapon_count_result.fetchall())


# 7. On average, how many Items does each Character have?
char_item_query = """SELECT character_id, COUNT(*) AS `num`
                     FROM charactercreator_character_inventory
                     GROUP BY character_id"""
char_item_result = curs.execute(char_item_query)
char_items = char_item_result.fetchall()
items = []
for _ in range(len(char_items)):
    items.append(char_items[_][1])
print('Average items per character\n',sum(items)/len(items))


# 8. On average, how many Weapons does each character have?
weapon_count_query = """SELECT character_id, item_id, COUNT(*)
                      FROM charactercreator_character_inventory
                      WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
                      GROUP BY character_id LIMIT 20;"""
weapon_count_result = curs.execute(weapon_count_query)
weapon_counts = weapon_count_result.fetchall()
weapons = []
for _ in range(len(weapon_counts)):
    weapons.append(weapon_counts[_][2])
print('8. Average weapons per character\n',sum(weapons)/len(weapons))
