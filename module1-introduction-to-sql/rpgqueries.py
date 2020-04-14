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

#query = "Total Items;"
query = """
SELECT
--	*
	count(DISTINCT item_id) as item_id
FROM armory_item
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("total items",row["item_id"])
    
print("_________________")

#query = "Items that are weapons;"
query = """
SELECT
--	*
	count(DISTINCT item_ptr_id) as item_id
FROM armory_weapon
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("items that are weapons",row["item_id"])
    
print("_________________")

#query = "Items that are NOT weapons;"
query = """
SELECT 
--	*
	count(distinct t1.item_id) as total_items
	,count(distinct t2.item_ptr_id) as total_weapons
FROM armory_item t1
LEFT JOIN armory_weapon t2 on t2.item_ptr_id = t1.item_id
WHERE t2.item_ptr_id IS NULL
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("items that are NOT weapons",row["total_items"])

print("_________________")

#query = "how many items each character have;"
query = """
SELECT 
--	*
	t1.character_id as character_id
	,t1.name as name
	,count(t2.item_id) as item_id
FROM charactercreator_character t1
LEFT JOIN charactercreator_character_inventory t2 ON t2.character_id = t1.character_id
GROUP BY t1.character_id
ORDER BY t2.item_id
LIMIT 20
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("character_id",row["character_id"])
    print("character_name",row["name"])
    print("items",row["item_id"])
    print('***')

print("_________________")

#query = "how many weapons does each character have;"
query = """
SELECT
--	*
--	t1.item_id as item_id
	count(t2.item_ptr_id) as weapons
	,t3.character_id as character_id
	,t3.name as character_name
FROM charactercreator_character_inventory t1
LEFT JOIN armory_weapon t2 ON t2.item_ptr_id = t1.item_id
LEFT JOIN charactercreator_character t3 ON t3.character_id = t1.character_id
WHERE t2.item_ptr_id IS NOT NULL
GROUP BY t3.character_id
LIMIT 20
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("weapons",row["weapons"])
    print("character_name",row["character_name"])
    print("character_id",row["character_id"])
    print('***')

print("_________________")

#query = "average Items;"
query = """
SELECT
	(CAST(COUNT(t2.item_id)AS FLOAT) / CAST(COUNT(DISTINCT t1.character_id)AS FLOAT)) as avg_item_per_character
FROM charactercreator_character t1
LEFT JOIN charactercreator_character_inventory t2 ON t2.character_id = t1.character_id
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("avg_items",row["avg_item_per_character"])
    

print("_________________")

#query = "average weapons;"
query = """
SELECT
--	*
--	t1.item_id as item_id
	(cast(count(t2.item_ptr_id) AS FLOAT) / cast(count(distinct t1.character_id) AS FLOAT)) as avg_weapon_character
FROM charactercreator_character_inventory t1
LEFT JOIN armory_weapon t2 ON t2.item_ptr_id = t1.item_id
LEFT JOIN charactercreator_character t3 ON t3.character_id = t1.character_id
WHERE t2.item_ptr_id IS NOT NULL
"""
result = cursor.execute(query).fetchall()
for row in result:
    print("avg_weapons",row["avg_weapon_character"])
    

print("_________________")
