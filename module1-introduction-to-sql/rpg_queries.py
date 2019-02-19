import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
char_query = '''SELECT count(*) FROM charactercreator_character'''
curs.execute(char_query)
print('Number of characters:', curs.fetchall()[0][0])
curs = conn.cursor()
cleric_query = '''SELECT count(*) FROM charactercreator_cleric'''
curs.execute(cleric_query)
print('Number of clerics:', curs.fetchall()[0][0])
curs = conn.cursor()
fighter_query = '''SELECT count(*) FROM charactercreator_fighter'''
curs.execute(fighter_query)
print('Number of fighters:', curs.fetchall()[0][0])
mage_query = '''SELECT count(*) FROM charactercreator_mage'''
curs = conn.cursor()
curs.execute(mage_query)
print('Number of mages:', curs.fetchall()[0][0])
necromancer_query = '''SELECT count(*) FROM charactercreator_necromancer'''
curs = conn.cursor()
curs.execute(necromancer_query)
print('Number of necromancers:', curs.fetchall()[0][0])
thief_query = '''SELECT count(*) FROM charactercreator_thief'''
curs = conn.cursor()
curs.execute(thief_query)
print('Number of thieves:', curs.fetchall()[0][0])
item_query = '''SELECT count(*) FROM armory_item'''
curs = conn.cursor()
curs.execute(item_query)
print('Number of items:', curs.fetchall()[0][0])
weapon_query = '''SELECT count(*) FROM armory_weapon'''
curs = conn.cursor()
curs.execute(weapon_query)
print('Number of weapons:', curs.fetchall()[0][0])
non_weapon_query = '''SELECT count(*) FROM armory_item
LEFT JOIN armory_weapon
ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id IS NULL'''
curs = conn.cursor()
curs.execute(non_weapon_query)
print('Number of items that are not weapons:', curs.fetchall()[0][0])
