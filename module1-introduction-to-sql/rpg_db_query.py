
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)

curs = conn.cursor()

query = "SELECT COUNT(*) from charactercreator_character"

results = curs.execute(query).fetchone()

print ("total characters: ", results)

query2 = "SELECT COUNT(*) from charactercreator_cleric"

results2 = curs.execute(query2).fetchone()

print ("total clerics: ", results2)

query3 = "SELECT COUNT(*) from charactercreator_fighter"

results3 = curs.execute(query3).fetchone()

print ("total fighters: ", results3)

query4 = "SELECT COUNT(*) from charactercreator_mage"

results4 = curs.execute(query4).fetchone()

print ("total mages: ", results4)

query5 = "SELECT COUNT(*) from charactercreator_necromancer"

results5 = curs.execute(query5).fetchone()

print ("total necromancers: ", results5)

query6 = "SELECT COUNT(*) from charactercreator_thief"

results6 = curs.execute(query6).fetchone()

print ("total thieves: ", results6)

query7 = "SELECT COUNT(*) from armory_item"

results7 = curs.execute(query7).fetchone()

print ("total items: ", results7)

query8 = "SELECT COUNT(*) from armory_weapon - COUNT(*) from armory_item"

results8 = curs.execute(query8).fetchone()

print ("total weapons: ", results8) 