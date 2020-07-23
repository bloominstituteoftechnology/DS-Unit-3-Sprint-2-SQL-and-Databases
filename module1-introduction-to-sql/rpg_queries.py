import sqlite3

connect = sqlite3.connect('rpg_db.sqlite3')
cursor = connect.cursor()

cursor.execute('SELECT COUNT(character_id) FROM charactercreator_character')
print("1. ", cursor.fetchall())

cursor.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_thief')
print("2.\nThief: ", cursor.fetchall())

cursor.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_cleric')
print("Cleric: ", cursor.fetchall())

cursor.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_mage')
print("Mage: ", cursor.fetchall())

cursor.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_fighter')
print("Fighter: ", cursor.fetchall())

cursor.execute('SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer')
print("Necromancer: ", cursor.fetchall())

cursor.execute('SELECT COUNT(item_id) FROM armory_item')
num_item = cursor.fetchall()
print('3. ', num_item)

cursor.execute('SELECT COUNT(item_ptr_id) FROM armory_weapon')
num_weapon = cursor.fetchall()
print(
    '4. Weapons: ',
    num_weapon,
    ' Items: ',
    num_item[0][0] -
    num_weapon[0][0])

cursor.execute('''SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20''')
print('5. ', cursor.fetchall())

cursor.execute('''SELECT COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id
LIMIT 20''')
print('6. ', cursor.fetchall())


cursor.execute('''SELECT AVG(a.rcount) FROM
(select count(*) as rcount
FROM charactercreator_character_inventory cci
GROUP BY character_id) a''')
print('7. ', cursor.fetchall())

cursor.execute('''SELECT AVG(a.rcount) FROM
(select count(*) as rcount
FROM charactercreator_character_inventory cci
WHERE item_id > 137
GROUP BY character_id) a''')
print('8. ', cursor.fetchall())
