import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM charactercreator_character;'
result = curs.execute(query)
print('Total Character count',result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_mage;'
result = curs.execute(query)
print('Number of Mage characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_thief;'
result = curs.execute(query)
print('Number of Thief characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
result = curs.execute(query)
print('Number of Cleric characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
result = curs.execute(query)
print('Number of Fighter characters', result.fetchall())

query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
result = curs.execute(query)
print('Number of Necromancer characters', result.fetchall())

query = 'SELECT COUNT(*) FROM armory_item;'
result = curs.execute(query)
print('Number of Items', result.fetchall())

query = 'SELECT COUNT(*) FROM armory_weapon;'
result = curs.execute(query)
print('Number of Weapons', result.fetchall())

query = 'SELECT COUNT(ai.item_id) FROM armory_item AS ai LEFT JOIN armory_weapon AS aw WHERE NOT ai.item_id == aw.item_ptr_id;'
result = curs.execute(query)
print('Number of non-WeaponsFIXTHIS', result.fetchall())

query = """SELECT character.name, inventory.id 
           FROM charactercreator_character_inventory AS inventory, charactercreator_character AS character 
           WHERE character.character_id = inventory.character_id
           LIMIT 20;"""
result = curs.execute(query)
print('Number items per character, kinda\n', result.fetchall())

query = """
        SELECT character.name, inventory.id 
        FROM charactercreator_character_inventory AS inventory, charactercreator_character AS character
        WHERE character.character_id = inventory.character_id
        AND inventory.item_id IN (SELECT item_ptr_id FROM armory_weapon)
        LIMIT 20; 
        """
result = curs.execute(query)
print('items that are weapons for each character\n', result.fetchall())




