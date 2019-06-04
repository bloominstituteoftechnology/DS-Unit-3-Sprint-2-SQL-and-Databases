import sqlite3

# Part 1, Querying a Database

# Connect to database
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print('Question 1: How many total Characters are there?')
query1 = 'SELECT COUNT(*) FROM charactercreator_character;'
result1 = curs.execute(query1)
print(result1.fetchall())

print('\nQuestion 2: How many of each specific subclass?')
query2 = '''SELECT (SELECT COUNT(*) FROM charactercreator_mage) AS mage_count, 
                  (SELECT COUNT(*) FROM charactercreator_thief) AS thief_count, 
                  (SELECT COUNT(*) FROM charactercreator_cleric) AS cleric_count, 
                  (SELECT COUNT(*) FROM charactercreator_fighter) AS fighter_count, 
                  (SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancer_count;'''
result2 = curs.execute(query2)
print('Order: Mage, Thief, Cleric, Fighter, Necromancer')
print(result2.fetchone())

print('\nQuestion 3: How many total Items?')
query3 = 'SELECT COUNT(*) FROM armory_item;'
result3 = curs.execute(query3)
print(result3.fetchall())

print('\nQuestion 4: How many of the Items are weapons? How many are not?')
query4 = '''SELECT (SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id = item_ptr_id),
                    (SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id <> item_ptr_id);'''
result4 = curs.execute(query4)
print(result4.fetchall())

print('\nQuestion 5: How many Items does each character have? (Return first 20 rows)')
query5 = ('''SELECT cc.name, COUNT()
         FROM charactercreator_character AS cc, charactercreator_character_inventory AS cci
         WHERE cc.character_id = cci.character_id
         GROUP BY cc.name 
         LIMIT 20;''')
result5 = curs.execute(query5)
print(result5.fetchall())

print('\nQuestion 6: How many Weapons does each character have? (Return first 20 rows)')
query6 = ('''SELECT character_id, COUNT(item_id)
            FROM charactercreator_character_inventory as ci, armory_weapon as aw
            WHERE ci.item_id = aw.item_ptr_id
            GROUP BY character_id
            LIMIT 20;''')
result6 = curs.execute(query6)
print(result6.fetchall())

print('\nQuestion 7: On average, how many Items does each Character have?')
query7 = ('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) AS items
            FROM charactercreator_character_inventory
            GROUP BY character_id);''')
result7 = curs.execute(query7)
print(result7.fetchall())

print('\nQuestion 8: On average, how many Weapons does each character have?')
query8 = ('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) AS items
            FROM charactercreator_character_inventory as ci, armory_weapon as aw
            WHERE ci.item_id = aw.item_ptr_id
            GROUP BY character_id);''')
result8 = curs.execute(query8)
print(result8.fetchall())
