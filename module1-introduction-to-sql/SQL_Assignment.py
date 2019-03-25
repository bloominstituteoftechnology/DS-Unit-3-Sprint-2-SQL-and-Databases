import sqlite3


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query1 = 'SELECT count() from charactercreator_character'
print(curs.execute(query1).fetchall())

query2_cleric = 'SELECT count() from charactercreator_cleric'

query2_figher = 'SELECT count() from charactercreator_fighter'

query2_mage = 'SELECT count() from charactercreator_mage'

query2_necromancer = 'SELECT count() from charactercreator_necromancer'

query2_thief = 'SELECT count() from charactercreator_thief'

print('Number of cleric', curs.execute(query2_cleric).fetchall())
print('Number of figher',curs.execute(query2_figher).fetchall())
print('Number of mage', curs.execute(query2_mage).fetchall())
print('Number of necromancer', curs.execute(query2_necromancer).fetchall())
print('Number of thief', curs.execute(query2_thief).fetchall())

query3 = 'SELECT count() from armory_item'

print('Number of total item',curs.execute(query3).fetchall())

query4 = 'SELECT count() from armory_weapon'

print('Number of weapon', curs.execute(query4).fetchall())

query5 = 'SELECT character_id, count() from charactercreator_character_inventory group by character_id LIMIT 20'

print(curs.execute(query5).fetchall())

query6 = 'SELECT character_id, count() from charactercreator_character_inventory, armory_weapon WHERE charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id group by character_id LIMIT 20;'

print (curs.execute(query6).fetchall())

query7 = 'SELECT avg(number) from (SELECT count() as number FROM charactercreator_character_inventory GROUP by character_id)'

print (curs.execute(query7).fetchall())