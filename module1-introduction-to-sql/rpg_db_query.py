
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

# " - How many of the Items are weapons? How many are not? "

query8 = "SELECT COUNT(*) from armory_weapon"

results8 = curs.execute(query8).fetchone()

print ("total weapons: ", results8) 

print ("non-weapon items: ",results7[0] - results8[0])

# "How many Items does each character have? (Return first 20 rows)"

query9 = """
SELECT character_id, 
    COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

results9 = curs.execute(query9).fetchall()
print ("--------------------------------------------------------------")
print("How many items does each character have? (Return first 20 rows)")
print ("--------------------------------------------------------------")
for i in results9:
    print("Character ID:",i[0], "# of Items:", i[1])
# print ("total items per character: ", results9)


print ("----------------------------------------------------------------")

# How many Weapons does each character have? (Return first 20 rows)

query10 = """
SELECT character_id, 
    COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 137 and item_id < 175
GROUP BY character_id
LIMIT 20
"""

results10 = curs.execute(query10).fetchall()

print("How many Weapons does each character have? (Return first 20 rows)")
print ("----------------------------------------------------------------")
for i in results10:
    print("Character ID:",i[0], "# of Weapons:", i[1])


# On average, how many Items does each Character have?
# Need to take # of weapons column and add every value
# then divide by the total number of values.

query11 = """
SELECT character_id, 
    COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 137 and item_id < 175
GROUP BY character_id
"""


print ("-------------------------------------------------------")
results11 = curs.execute(query11).fetchall()

total = 0
for i in results11:
    total += i[1]

print ("Average weapons of each character: ", total/len(results11))
print ("-------------------------------------------------------")


# On average, how many Items does each Character have?



query12 = """
SELECT character_id, 
    COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
"""

results12 = curs.execute(query12).fetchall()

total2 = 0
for i in results12:
    total2 += i[1]

print ("Average items of each character: ", total2/len(results12))

print ("-------------------------------------------------------")
