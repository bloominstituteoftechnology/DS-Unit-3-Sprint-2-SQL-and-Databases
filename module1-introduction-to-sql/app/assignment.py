import sqlite3
import os

# construct the path from os module to make sure that it runs platform independant
DB_FILENAME= os.path.join(os.path.dirname(__file__),"..","data","rpg_db.sqlite3")

connection=sqlite3.connect(DB_FILENAME)
connection.row_factory = sqlite3.Row # lest reat our objects like dict nor tuples
curs=connection.cursor()

# question one
# what is the total number of characters?
query="""
SELECT
	COUNT(DISTINCT character_id) as char_count
FROM charactercreator_character
ORDER BY 1
"""
result=curs.execute(query).fetchall()
for row in result:
    print("the total number of characters is",row[0])

# question two
# what is the total number of characters in each subclass?
#query="""
#"""
#result=curs.execute(query).fetchall()
print("How many of characters are in each subclass? IDK")

# question three
# what are the total number of items?
query="""
SELECT
	count(item_id) as item_count
FROM armory_item
"""
result=curs.execute(query).fetchall()
for row in result:
    print("the total number of items is",row[0])

# question four
# out of the total number of items how man are weapons?
# how many are not weapons?
query="""
SELECT 
	count(i.item_id) as total_items,
	count(distinct w.item_ptr_id) as iswep
FROM armory_item as i
LEFT JOIN armory_weapon as w on i.item_id = w.item_ptr_id
"""
result=curs.execute(query).fetchall()
print("the total number of items that are weapons is ",
        result[0][1],
        "\nthe total number of items that are not weapons is ",
        result[0][0]-result[0][1],
        sep='')

# question five:
# how many items does each character have?
query="""
SELECT 
	x.character_name,
	x.item_name,
	count(x.character_name) as number_of_items
FROM (
	SELECT 
		chars.name as character_name,
		items.name as item_name
	FROM charactercreator_character_inventory as inv
	JOIN armory_item as items ON inv.item_id = items.item_id
	JOIN charactercreator_character as chars ON inv.character_id = chars.character_id

) x
GROUP BY x.character_name
ORDER BY number_of_items DESC
LIMIT 20
"""
result=curs.execute(query).fetchall()
avg_items=0
for i in range(len(result)):
    avg_items+=result[i][2]
    print(f"the character named {result[i][0]} has {result[i][2]} items")
print(f"on average the characters have {round(avg_items/len(result),2)}")