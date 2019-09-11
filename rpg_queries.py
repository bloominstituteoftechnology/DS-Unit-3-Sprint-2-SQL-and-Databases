import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
# print(dir(curs))
query = 'SELECT character_id, COUNT(*) FROM charactercreator_character;'
print('Pulls total number of characters')
curs.execute(query)
print(curs.execute(query).fetchall())

curs = conn.cursor()
query2 = 'SELECT character_ptr_id, COUNT(*) FROM charactercreator_mage;'
print('Pulls total number of mage class')
curs.execute(query2)
print(curs.execute(query2).fetchall())

curs = conn.cursor()
query3 = 'SELECT character_ptr_id,  COUNT(*) FROM charactercreator_thief;'
print('Pulls total number of thief class')
curs.execute(query3)
print(curs.execute(query3).fetchall())

curs = conn.cursor()
query4 = 'SELECT character_ptr_id,  COUNT(*) FROM charactercreator_cleric;'
print('Pulls total number of cleric class')
curs.execute(query4)
print(curs.execute(query4).fetchall())

curs = conn.cursor()
query5 = 'SELECT character_ptr_id,  COUNT(*) FROM charactercreator_fighter;'
print('Pulls total number of fighter class')
curs.execute(query5)
print(curs.execute(query5).fetchall())

curs = conn.cursor()
query6 = 'SELECT item_ptr_id, COUNT(*) FROM armory_weapon;'
print('Pulls total number of weapons')
curs.execute(query6)
print(curs.execute(query6).fetchall())

# I BELIEVE QUERY 7'S ANSWER IS WRONG; THERE'S ONLY 174 TOTAL ARMORY ITEMS - 37 WEAPONS
curs = conn.cursor()
query7 = 'SELECT COUNT(*) FROM armory_weapon, armory_item WHERE item_id <> item_ptr_id'
print('Pulls total number of non-weapons from armory')
curs.execute(query7)
print(curs.execute(query7).fetchall())

curs = conn.cursor()
query8 = ('''SELECT cc.name, COUNT()
            FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci
            WHERE cc.character_id = cci.character_id
            GROUP BY cc.name
            LIMIT 20;''')
print('Pulls total number of items per character for the first 20 characters in the table')
curs.execute(query8)
print(curs.execute(query8).fetchall())

curs = conn.cursor()
query9 = ('''SELECT character_id, COUNT(item_id)
            FROM charactercreator_character_inventory AS cci,
            armory_weapon AS aw
            WHERE cci.item_id = aw.item_ptr_id
            GROUP BY character_id
            LIMIT 20;''')
print('Pulls total number of weapons per character for the first 20 characters in the table')
curs.execute(query9)
print(curs.execute(query9).fetchall())

curs = conn.cursor()
query10 = ('''SELECT AVG(items)
            FROM(
                SELECT character_id, COUNT(item_id) AS items
                FROM charactercreator_character_inventory
                GROUP BY character_id);''')
print('Pulls average number of items per character')
curs.execute(query10)
print(curs.execute(query10).fetchall())

curs = conn.cursor()
query11 = ('''SELECT AVG(items)
            FROM(
                SELECT character_id, COUNT(item_id) AS items
                FROM charactercreator_character_inventory AS cci,
                armory_weapon AS aw
                WHERE cci.item_id = aw.item_ptr_id
                GROUP BY character_id);''')
print('Pulls average number of weapons per character')
curs.execute(query11)
print(curs.execute(query11).fetchall())

