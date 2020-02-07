import os
import sqlite3

# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
# print(DB_FILEPATH)
conn = sqlite3.connect('rpg_db.sqlite3')
# conn.row_factory = sqlite3.Row

curs = conn.cursor()

query1 = """
select
	character_id
	,count(distinct character_id) as character_count
from charactercreator_character;
"""

# Given to class in Office Hours
query2 = """
select

	CASE 
    WHEN cl.character_ptr_id is not null THEN "cleric"
    WHEN f.character_ptr_id is not null THEN "fighter"
    WHEN n.mage_ptr_id is not null THEN "mage-necro"
    WHEN m.character_ptr_id is not null THEN "mage"
    WHEN th.character_ptr_id is not null THEN "thief"
    ELSE "todo"
    END as char_type
    ,count(distinct ch.character_id) as char_count

from charactercreator_character as ch
left join charactercreator_cleric as cl on ch.character_id = cl.character_ptr_id
left join charactercreator_fighter as f on ch.character_id = f.character_ptr_id
left join charactercreator_mage as m on ch.character_id = m.character_ptr_id
left join charactercreator_thief as th on ch.character_id = th.character_ptr_id
left join charactercreator_necromancer as n on m.character_ptr_id = n.mage_ptr_id
group by char_type;
"""

query3 = """
SELECT COUNT(item_id) as item_count
FROM armory_item;
"""

query4 = """
SELECT 
	CASE
	WHEN item_ptr_id is not null THEN "weapon"
	WHEN item_id is not null THEN "item"
	END as item_type
	,count(DISTINCT armory_item.item_id) as item_count
	   
FROM armory_item
LEFT JOIN armory_weapon as w ON item_id = w.item_ptr_id
GROUP BY item_type;
"""

# Adapted from query 6
query5 = """
SELECT character_id, count(a.item_id) as item_count
FROM charactercreator_character_inventory as a, armory_item as b
WHERE a.item_id = b.item_id
GROUP BY a.character_id
LIMIT 20;
"""

# Posted by Pedro Escobedo from my DSPT3 team with renamed variables
query6 = """
SELECT character_id, count(a.item_id) as weapon_count
FROM charactercreator_character_inventory as a, armory_item as b, armory_weapon as c
WHERE a.item_id = b.item_id AND b.item_id = c.item_ptr_id
GROUP BY a.character_id
LIMIT 20;
"""

query7 = """
SELECT COUNT(a.item_id) / COUNT(DISTINCT a.character_id) as avg_items
FROM charactercreator_character_inventory as a;
"""
#----------ADDITIONAL COMMENTS - QUERY 7--------------------------

# Checking my answer for Query 7 (avg items per character) I made 2 separate queries
# counting the number of instances of item_id in charactercreator_character_inventory (898)
# as well as the number of distinct character_id within the same table (302) so the actual
# average would be 2.97 (898/302=2.97...) so I am not sure why dividing them both within
# an SQL query would apply a FLOOR() method.


# For Query 8 I had to reference a column alias with which I would take the average
# So, after some Google-ing, I found something along the lines of this where I make
# A sort of subquery and alias that as innerTable (the name probably doesn't matter).
query8 = """
SELECT AVG(weapon_count) as avg_weapons
FROM(SELECT character_id, count(a.item_id) as weapon_count
FROM charactercreator_character_inventory as a, armory_item as b, armory_weapon as c
WHERE a.item_id = b.item_id AND b.item_id = c.item_ptr_id
GROUP BY a.character_id) as innerTable;
"""

# results = curs.execute(query2).fetchall()

for query in query1, query2, query3, query4, query5, query6, query7, query8:
	results = curs.execute(query).fetchall()

breakpoint()