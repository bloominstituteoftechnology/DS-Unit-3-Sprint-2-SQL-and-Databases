import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row

curs = conn.cursor()

query1 = """
select
	character_id
	,count(distinct character_id) as character_count
from charactercreator_character;
"""
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
group by char_type
"""
query3 = """
SELECT COUNT(item_id) as item_count
FROM armory_item
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
GROUP BY item_type
"""

# Not correct
query5 = """
SELECT
	character_id
	
	,CASE
	WHEN item_id is not null THEN "item"
	END as num_of_items
	
from charactercreator_character_inventory
"""
query6 = """

"""
query7 = """

"""
query8 = """

"""