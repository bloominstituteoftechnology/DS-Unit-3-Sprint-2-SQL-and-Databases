import sqlite3

conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')
cur = conn.cursor()

query1 = """
SELECT COUNT(*)
FROM charactercreator_character
"""

cur.execute(query1)
print(cur.fetchall())

query2 = """
SELECT COUNT(*)
FROM charactercreator_cleric
"""

cur.execute(query2)
print(cur.fetchall())

query3 = """
SELECT COUNT(*)
FROM charactercreator_fighter
"""

cur.execute(query3)
print(cur.fetchall())

query4 = """
SELECT COUNT(*)
FROM charactercreator_mage
"""

cur.execute(query4)
print(cur.fetchall())

query5 = """
SELECT COUNT(*)
FROM charactercreator_necromancer
"""

cur.execute(query5)
print(cur.fetchall())

query6 = """
SELECT COUNT(*)
FROM charactercreator_thief
"""

cur.execute(query6)
print(cur.fetchall())

query7 = """
SELECT COUNT(*)
FROM armory_item
"""

cur.execute(query7)
print(cur.fetchall())

query8 = """
SELECT COUNT(*)
FROM armory_weapon
"""

cur.execute(query8)
print(cur.fetchall())

query9 = """
SELECT COUNT(*)
FROM charactercreator_character ccc
LEFT JOIN charactercreator_character_inventory cci
ON cci.character_id = ccc.character_id
GROUP BY ccc.character_id
LIMIT 20
"""

cur.execute(query9)
print(cur.fetchall())

query10 = """
SELECT COUNT(*)
FROM charactercreator_character_inventory ccci
INNER JOIN armory_item ai
INNER JOIN armory_weapon aw
ON aw.item_ptr_id = ai.item_id AND ccci.item_id = ai.item_id
GROUP BY ccci.character_id
LIMIT 20
"""

cur.execute(query10)
print(cur.fetchall())

query11 = """
SELECT AVG(CountOfItems)
FROM (
    SELECT COUNT(*) AS CountOfItems
    FROM charactercreator_character ccc
    LEFT JOIN charactercreator_character_inventory cci
    ON cci.character_id = ccc.character_id
    GROUP BY ccc.character_id
)
"""

cur.execute(query11)
print(cur.fetchall())

query12 = """
SELECT AVG(CountOfWeapons)
FROM (
    SELECT COUNT(*) AS CountOfWeapons
    FROM charactercreator_character_inventory ccci
    INNER JOIN armory_item ai
    INNER JOIN armory_weapon aw
    ON aw.item_ptr_id = ai.item_id AND ccci.item_id = ai.item_id
    GROUP BY ccci.character_id
)
"""

cur.execute(query12)
print(cur.fetchall())
