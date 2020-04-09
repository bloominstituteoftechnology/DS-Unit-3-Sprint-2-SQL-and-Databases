# app/rpg_quiries.py

import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

# How many total Characters are there?
query1 = """
SELECT
    count(distinct character_id) as total_characters
FROM charactercreator_character
"""
r = curs.execute(query1).fetchone()
print("Total Number of Characters:")
print(r[0])

# How many total Items?
query2 = """
SELECT 
	COUNT(DISTINCT item_id)
FROM armory_item
"""
r = curs.execute(query2).fetchone()
print("\nTotal Number of Items:")
print(r[0])

# How many of the Items are weapons?
query3 = """
SELECT 
	COUNT(DISTINCT item_id)
FROM armory_item i
JOIN armory_weapon w ON w.item_ptr_id = i.item_id
"""
r = curs.execute(query3).fetchone()
print("\nNumber of Weapons:")
print(r[0])

# How many are not?
query4 = """
SELECT 
	COUNT(DISTINCT item_id)
FROM armory_item i
LEFT JOIN armory_weapon w ON w.item_ptr_id = i.item_id
WHERE w.power IS NULL
"""
r = curs.execute(query4).fetchone()
print("\nNumber of Non-Weapon Items:")
print(r[0])

# How many of each specific subclass?
query5 = """
SELECT 
	COUNT(DISTINCT cleric.character_ptr_id) as Clerics
	, COUNT(DISTINCT fighter.character_ptr_id) as Fighters
	, COUNT(DISTINCT mage.character_ptr_id) as Mages
	, COUNT(DISTINCT necromancer.mage_ptr_id) as Necromancers
	, COUNT(DISTINCT thief.character_ptr_id) as Thiefs
	
FROM charactercreator_character cc
Left JOIN charactercreator_cleric cleric ON cc.character_id = cleric.character_ptr_id
Left JOIN charactercreator_fighter fighter ON cc.character_id = fighter.character_ptr_id
Left JOIN charactercreator_mage mage ON cc.character_id = mage.character_ptr_id
Left JOIN charactercreator_necromancer necromancer ON cc.character_id = necromancer.mage_ptr_id
Left JOIN charactercreator_thief thief ON cc.character_id = thief.character_ptr_id
"""
r = curs.execute(query5).fetchall()
print("\nNumbers of Each Class:")
classes = ['Clerics', 'Fighters', 'Mages', 'Necromancers', 'Thiefs']
for i in range(5):
    print(classes[i], ":", (r[0][i]))

# How many Items does each character have? (Return first 20 rows)
query6 = """
SELECT 
	name
	, COUNT(item_id) AS number_of_items
	
FROM charactercreator_character AS cc 
LEFT JOIN charactercreator_character_inventory AS inven ON inven.character_id = cc.character_id
GROUP BY inven.character_id
LIMIT 20
"""
r = curs.execute(query6).fetchall()
print("\nItems per character:")
for i in range(len(r)):
    print(f'{r[i][0]} HAS {r[i][1]} ITEMS')
