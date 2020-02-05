import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")
# h/t: https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name
conn.row_factory = sqlite3.Row
curs = conn.cursor()
query = """
-- How many total character are there?
 -- SELECT character_id, count(*) FROM charactercreator_character
-- 302


-- How many of each specific subclass?
-- SELECT count(distinct item_id) as sublaclass_count FROM charactercreator_character_inventory
-- 174


-- How many total Items?
-- SELECT COUNT(DISTINCT item_id) as items_count FROM armory_item
-- 174


-- How many of the Items are weapons? 138
-- How many are not? 174
--SELECT item_ptr_id, count(*) FROM armory_weapon


--How many Items does each character have? (Return first 20 rows)
-- SELECT character_id, count(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20


-- How many Weapons does each character have? (Return first 20 rows)
-- SELECT character_id, count(a.item_id) FROM charactercreator_character_inventory as a, armory_item as b, armory_weapon as c WHERE a.item_id = b.item_id AND b.item_id = c.item_ptr_id GROUP BY a.character_id LIMIT 20


-- On average, how many Items does each Character have?
-- SELECT avg(item_id) avg_item FROM charactercreator_character_inventory
-- 89


-- On average, how many Weapons does each character have?
-- SELECT avg(c.item_ptr_id) FROM charactercreator_character_inventory as a, armory_item as b, armory_weapon as c WHERE a.item_id = b.item_id AND b.item_id = c.item_ptr_id
"""
results = curs.execute(query).fetchall()
query = "SELECT * FROM charactercreator_character"
length = len(curs.execute(query).fetchall())
weapons = 0
for i in range(len(results)):
    weapons += results[i][0]
average_weapons = weapons / length
print('Average weapons per character:', average_weapons)