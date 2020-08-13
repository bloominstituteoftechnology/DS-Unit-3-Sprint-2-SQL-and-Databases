import os
import sqlite3
"""construct a path to wherever your database exists
# DB_FILEPATH = "module1-introduction-to-sql/rpg_db.sqlite3.db"
# DB_FILEPATH = os.path.join("module1-introduction-to-sql", "example.db")
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), ",,", "module2-0...", ""example.db")
"""
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
"""
connecting to the database
"""
conn = sqlite3.connect(DB_FILEPATH)
"""cursor"""
cursor = conn.cursor()
"""How many total Characters are there?
"""
query = "SELECT COUNT(distinct character_id) FROM charactercreator_character"
print(cursor.execute(query).fetchall()[0][0])
"""
How many of each specific subclass?
"""
query1 = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_mage"
print(cursor.execute(query1).fetchall()[0][0])

query2 = "SELECT COUNT(distinct mage_ptr_id) FROM charactercreator_necromancer"
print(cursor.execute(query2).fetchall()[0][0])

query3 = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_fighter"
print(cursor.execute(query3).fetchall()[0][0])

query4 = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_cleric"
print(cursor.execute(query4).fetchall()[0][0])

query5 = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_thief"
print(cursor.execute(query5).fetchall()[0][0])
"""
How many total Items?
"""
query6 = "SELECT COUNT(distinct item_id) FROM armory_item"
print(cursor.execute(query6).fetchall()[0][0])
"""
How many of the Items are weapons? How many are not?
"""
query7 = "SELECT COUNT(item_ptr_id) as weapons_count FROM armory_weapon"
print(cursor.execute(query7).fetchall()[0][0])
"""
How many Items does each character have? (Return first 20 rows)
"""
query8 = "SELECT character_id,item_id FROM charactercreator_character_inventory LIMIT 20"
print(cursor.execute(query8).fetchall()[0][0])
"""
How many Weapons does each character have? (Return first 20 rows)
"""
query9 = "SELECT character_id ,count(distinct item_id) as weapons_count FROM charactercreator_" \
         "character_inventory WHERE item_id IN (SELECT distinct item_ptr_id FROM armory_weapon) " \
         "GROUP BY character_id LIMIT 20"
print(cursor.execute(query9).fetchall()[0][0])
"""
On average, how many Items does each Character have?
"""
query_10 = "SELECT ccc.character_id ,AVG(cinv.item_id) as items FROM charactercreator_character ccc LEFT JOIN " \
           "charactercreator_character_inventory cinv ON ccc.character_id = cinv.character_id "
print(cursor.execute(query_10).fetchall()[0][0])
"""On average, how many Weapons does each character have?
"""
query_11 = "SELECT character_id ,count(item_id) as items FROM charactercreator_character_inventory " \
           "WHERE item_id IN (" \
           "SELECT distinct item_ptr_id from armory_weapon) GROUP BY character_id "
print(cursor.execute(query_11).fetchall()[0][0])
"""
result = cursor.execute(query)
print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)
result3 = cursor.execute(query).fetchone()
print("RESULT 3", type(result3), result3)
for row in result3:
print(type(row), row)
"""
