import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

"""Total number of characters"""
query1 = 'SELECT COUNT(*) FROM charactercreator_character'
print('The total number of characters are:', curs.execute(query1).fetchone())

"""How many of each specific sublcass"""
query2 = 'SELECT COUNT(*) FROM charactercreator_fighter'
print('The total number of fighters are:', curs.execute(query2).fetchone())

query3 = 'SELECT COUNT(*) FROM charactercreator_cleric'
print('The Total number of clerics are:', curs.execute(query3).fetchone())

query4 = 'SELECT COUNT(*) FROM charactercreator_mage'
print('The total number of mages are:', curs.execute(query4).fetchone())

query5 = 'SELECT COUNT(*) FROM charactercreator_thief'
print('The total number of thieves are:', curs.execute(query5).fetchone())

"""Total # of items:"""
query6 = 'SELECT COUNT(*) FROM armory_item'
print('The total number of items are:', curs.execute(query6).fetchone())

"""Total # of weapons"""
query7 = 'SELECT COUNT(*) FROM armory_weapon'
print('Total number of weapons:', curs.execute(query7).fetchone())

"""Total # of items that are not weapons:"""
print('The total number of Items that are not weapons are:', 174-37)

"""How many Items does each character have (first 20 rows)"""
query9 = """
SELECT COUNT(CCI.item_id)
FROM charactercreator_character as CC,
charactercreator_character_inventory as CCI
WHERE CCI.character_id = CC.character_id
GROUP BY CC.character_id;
"""
print('Number of items per character:', curs.execute(query9).fetchmany(20))

"""How many weapons does each character have (first 20 rows)?"""
query10 = """
SELECT COUNT(AW.item_ptr_id)
FROM charactercreator_character_inventory as CCI,
charactercreator_character as CC,
armory_item as AI,
armory_weapon as AW
WHERE CCI.character_id = CC.character_id
AND CCI.item_id = AI.item_id
AND AI.item_id = AW.item_ptr_id
GROUP BY CC.character_id;
"""
print('Number of weapons per character:', curs.execute(query10).fetchmany(20))

"""On average, how many Items does each character have?"""
query11 = """
SELECT AVG(avg_items)
FROM(SELECT COUNT(CCI.item_id) as avg_items
FROM charactercreator_character as CC,
charactercreator_character_inventory as CCI
WHERE CCI.character_id = CC.character_id
GROUP BY CC.character_id) AS T;
"""
print('Average num of items per character:', curs.execute(query11).fetchone())

"""On average, how many Weapons does each character have?"""
query12 = """
SELECT AVG(avg_weaps)
FROM (SELECT COUNT(AW.item_ptr_id) as avg_weaps
FROM charactercreator_character_inventory as CCI,
charactercreator_character as CC,
armory_item as AI,
armory_weapon as AW
WHERE CCI.character_id = CC.character_id
AND CCI.item_id = AI.item_id
AND AI.item_id = AW.item_ptr_id
GROUP BY CC.character_id) AS Z;
"""
print('Average num of weapons per character:', curs.execute(query12).fetchone())

curs.close()
conn.commit()