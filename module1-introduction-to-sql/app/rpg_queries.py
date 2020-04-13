import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")


connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()


#query = "total number of characters;"
query = """
--dont run this
SELECT
	count(distinct character_id) as Total_characters
FROM charactercreator_character
"""

result = cursor.execute(query).fetchall()
for row in result:
    print(row["Total_characters"])


print("_________________")
#query = "total number from each subclass;"
query = """
--How many from each subclass

SELECT
--	*
	count(distinct t1.character_id) as character_id
--	,t1.name as name
	,count(distinct t2.character_ptr_id) as mage_character_id
	,count(distinct t3.character_ptr_id) as thief_character_id
	,count(distinct t4.character_ptr_id) as cleric_character_id
	,count(distinct t5.character_ptr_id) as fighter_character_id
--	,
FROM charactercreator_character t1
LEFT JOIN charactercreator_mage t2 ON t2.character_ptr_id = t1.character_id
LEFT JOIN charactercreator_thief t3 ON t3.character_ptr_id = t1.character_id
LEFT JOIN charactercreator_cleric t4 ON t4.character_ptr_id = t1.character_id
LEFT JOIN charactercreator_fighter t5 ON t5.character_ptr_id = t1.character_id
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("character",row["character_id"])
    print("mage", row["mage_character_id"])
    print("thief", row["thief_character_id"])
    print("cleric", row["cleric_character_id"])
    print("fighter", row["fighter_character_id"])

print("_________________")