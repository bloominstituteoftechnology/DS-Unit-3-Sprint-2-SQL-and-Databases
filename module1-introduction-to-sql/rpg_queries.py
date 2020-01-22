import sqlite3
import sys

#setup the database, setup first query to create table
conn = sqlite3.connect('rpg_db.sqlite3')
#Return total Characters
curs = conn.cursor()
query = 'SELECT character_id, COUNT(*) FROM charactercreator_character;'
totalchar = curs.execute(query).fetchall()[0][0]
print("Total characters:", curs.execute(query).fetchall()[0][0])

#How many of each specific subclass?
query2a = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
print(f"Total fighters:", curs.execute(query2a).fetchall()[0][0])

query2b = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
print(f"Total cleric:", curs.execute(query2b).fetchall()[0][0])

query2c ='SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
print(f"Total mage:", curs.execute(query2c).fetchall()[0][0])

query2d = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
print(f"Total thief:", curs.execute(query2c).fetchall()[0][0])

 
# How many total items?
query3 = 'SELECT COUNT(name) FROM armory_item'
print(f"Total item:", curs.execute(query3).fetchall()[0][0])

# How many of the items are weapons?
query4 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon'

weapon = curs.execute(query4).fetchall()[0][0]

print(f"Total weapons:", weapon)

# How many are not weapons?
nonweapon = 174 - weapon
print(f"Total non-weapon item:", nonweapon)

# How many Items does each character have? (Return first 20 rows)
query5 = """select character_id, count(item_id) from charactercreator_character_inventory 
            Group by character_id
            LIMIT 20;"""
print(f"Showing first 20 characters items:", curs.execute(query5).fetchall())

# How many Weapons does each character have? (Return first 20 rows)
query6 = """SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_id) AS num_items
            FROM charactercreator_character AS cc,
            armory_item AS ai,
            charactercreator_character_inventory AS cci
            WHERE cc.character_id = cci.character_id
            AND ai.item_id = cci.item_id
            GROUP BY cc.character_id
            ORDER BY num_items DESC
            LIMIT 20;"""
print(f"Showing first 20 characters weapons:", curs.execute(query6).fetchall())
# On average, how many Items does each Character have?
query8 = 'select count(item_id) from charactercreator_character_inventory'
totalitems = curs.execute(query8).fetchall()[0][0]

averageitems = totalitems / totalchar 
print(f"On average each character has", averageitems,  "items")
# On average, how many Weapons does each character have?
query9 = 'SELECT count(character_id) from armory_weapon as aw,armory_item as ai,charactercreator_character_inventory as cci where aw.item_ptr_id = cci.item_id and ai.item_id = cci.item_id'
totalweapons = curs.execute(query9).fetchall()[0][0]
averageweapon = 302 / totalweapons
print(f"On average each characer has", averageweapon, "weapons")

curs.close()
conn.commit()
