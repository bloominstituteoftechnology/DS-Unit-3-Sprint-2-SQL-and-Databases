import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

curs.execute('SELECT COUNT(character_id) FROM charactercreator_character')
print("1. ", curs.fetchall())

curs.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_thief')
print("2.\nThief: ", curs.fetchall())

curs.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_cleric')
print("Cleric: ", curs.fetchall())

curs.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_mage')
print("Mage: ", curs.fetchall())

curs.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_fighter')
print("Fighter: ", curs.fetchall())

curs.execute('SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer')
print("Necromancer: ", curs.fetchall())

curs.execute('SELECT COUNT(item_id) FROM armory_item')
num_item = curs.fetchall()
print('3. ', num_item)

curs.execute('SELECT COUNT(item_ptr_id) FROM armory_weapon')
num_weapon = curs.fetchall()
print('4. Weapons: ', num_weapon, ' Items: ', num_item[0][0]-num_weapon[0][0])

