import sqlite3
import os
import pandas as pd
from sqlalchemy import create_engine

DB_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")



conn = sqlite3.connect(DB_filepath)


curs1 = conn.cursor()

# query for finding out the total number of characters in the 
# game
totalChars_query = """
                    SELECT 
	count(distinct(character_id))
FROM charactercreator_character_inventory;
"""
subclass_amounts = """
	SELECT --*

	count(DISTINCT f.character_ptr_id) as fighter_count
	,count(DISTINCT c.character_ptr_id) as cleric_count
	, count(DISTINCT t.character_ptr_id) as thief_count
	,count(DISTINCT m.character_ptr_id) as mage_count
	
FROM charactercreator_character cc
LEFT JOIN charactercreator_fighter f on f.character_ptr_id = cc.character_id
LEFT JOIN charactercreator_cleric c on c.character_ptr_id = cc.character_id
LEFT JOIN charactercreator_thief t on t.character_ptr_id = cc.character_id
LEFT JOIN charactercreator_mage m on m.character_ptr_id = cc.character_id
	
"""


numItems = """
    SELECT
	count(DISTINCT(armory_item.item_id))
FROM armory_item
"""

nunItems_with_weapons = """
    SELECT
	
	
	count(distinct(armory_item.item_id)) as armory_id
	,armory_weapon.power as weapon_power
FROM armory_item 
LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
group by weapon_power
"""


numItems_per_char = """
    SELECT
	
	
	charactercreator_character_inventory.character_id
	,count(DISTINCT(charactercreator_character_inventory.item_id)) as num_items
FROM 
	charactercreator_character_inventory
group by charactercreator_character_inventory.character_id
LIMIT 20
"""

numWeapons_per_character = """
    SELECT
	
	
	charactercreator_character_inventory.character_id
	,count(DISTINCT(armory_weapon.power)) as num_weapons
FROM 
	charactercreator_character_inventory
LEFT JOIN armory_item on armory_item.item_id = charactercreator_character_inventory.item_id
LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
group by charactercreator_character_inventory.character_id
LIMIT 20
"""


average_num_weapons = """
	-- On average, how many Weapons does each character have?
-- There are 302 characters 
-- subquery will need to be a separate character per row and the count of
-- weapons per character(item_ptr_id)
SELECT AVG(number_weapons)

FROM(
	SELECT --*
		cc.character_id
		,cc.name
		,count(distinct item_ptr_id) number_weapons
	
	FROM charactercreator_character cc
	LEFT JOIN charactercreator_character_inventory cci on cc.character_id = cci.character_id
	LEFT JOIN armory_item a on cci.item_id = a.item_id
	LEFT JOIN armory_weapon w on a.item_id = w.item_ptr_id
	group by 1,2
)subQuery
"""

average_items_per_char = """

	-- On average, how many Items does each Character have?
-- return a single number
SELECT avg(num_items_per_char) as average_items_per_character
from (
	SELECT --*
		cc.character_id
		,cc.name
		,count(DISTINCT cci.item_id) as num_items_per_char
	
	FROM charactercreator_character cc
	LEFT JOIN charactercreator_character_inventory cci on cc.character_id = cci.character_id
	group by 1, 2
)previous	
"""

result1 = curs1.execute(totalChars_query).fetchall()
print("First Query", result1)

result2 = curs1.execute(subclass_amounts).fetchall()
print("The amounts in each of the subclasses are:\n", result2)



result6 = curs1.execute(numItems).fetchall()
print("Number of items: ", result6)

results7 = curs1.execute(nunItems_with_weapons).fetchall()
print("Number of items that are not weapons and are weapons is:\n ",results7)

results8 = curs1.execute(numItems_per_char).fetchall()
print("Number of items per character:  ", results8)


result9 = curs1.execute(numWeapons_per_character).fetchall()
print("Number of Weapons per character:  ", result9)

result10 = curs1.execute(average_items_per_char).fetchall()
print("Average number of items per character: ", result10)

result11 = curs1.execute(average_num_weapons).fetchall()
print("Average number of weapons per character: ", result11)


# Now will be loading the pandas dataframe to a sql and then will save it
# first will load the data with pandas to a csv and then 
# will change that to a sqlite and load it into the database

# my file path
CSV_Path = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")


df = pd.read_csv(CSV_Path)

# Making a path for the buddymove_holidayiq.sqlite3
# that will be saved in the data folder
Buddy_savePath = os.path.join(os.path.dirname(__file__), "..","data", "buddymove_holidayiq.sqlite3" )
#engine = create_engine('sqlite://', echo=False)
conn =sqlite3.connect(Buddy_savePath)
# putting the data into the database
df.to_sql("reviews", con=conn, if_exists="replace" )

# Creating a row factory
#conn.row_factory = sqlite3.Row

cursor1 = conn.cursor()

theQuery = """
	Select  count(*)
		

	From reviews;
	
"""


cursor1.execute(theQuery)
#engine.execute(theQuery)



#result = cursor1.fetchone()
result = cursor1.fetchall()
print("The rows in the columns in the data are:", result)



# This is the query for the second question
query = """
	SELECT COUNT(*)



	FROM reviews r
	WHERE r.Nature >= 100 and r.Shopping >= 100
"""

cursor1.execute(query)
result = cursor1.fetchall()
print("\nThis is the answer to the second question", result)
