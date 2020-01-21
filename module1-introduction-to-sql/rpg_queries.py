#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print("\nHow many total Characters are there?")
query = "SELECT character_id, COUNT(*) FROM charactercreator_character;"
print(curs.execute(query).fetchall()[0][1])

print("\nHow many of each specific subclass?")
subclass_list = ['thief', 'cleric', 'fighter', 'mage']
for sub in subclass_list:
    query = f"SELECT character_ptr_id, COUNT(*) FROM charactercreator_{sub};"
    print(f"{sub}:", curs.execute(query).fetchall()[0][1])

query = "SELECT mage_ptr_id, COUNT(*) FROM charactercreator_necromancer;"
print(f"necromancer:", curs.execute(query).fetchall()[0][1])

print("\nHow many total Items?")
query = "SELECT item_id, COUNT(*) FROM armory_item;"
print(curs.execute(query).fetchall()[0][1])

print("\nHow many of the Items are weapons?")
query = """
SELECT item_id, COUNT(*)
FROM armory_item
WHERE item_id IN
(
SELECT item_ptr_id FROM armory_weapon
);
"""
print(curs.execute(query).fetchall()[0][1])

print("\nHow many of the Items are NOT weapons")
query = """
SELECT item_id, COUNT(*)
FROM armory_item
WHERE item_id NOT IN
(
SELECT item_ptr_id FROM armory_weapon
);
"""
print(curs.execute(query).fetchall()[0][1])

print("\nHow many Items does each character have? (Return first 20 rows)")
query = """
SELECT character_id, COUNT(*)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""
response = curs.execute(query).fetchall()
for char, count in response:
    print(f"char id: {char}\titem count: {count}")

print("\nHow many Weapons does each character have? (Return first 20 rows)")
query = """
SELECT character_id, COUNT(*)
FROM charactercreator_character_inventory
WHERE item_id IN
(
SELECT item_ptr_id FROM armory_weapon
)
GROUP BY character_id
LIMIT 20;
"""
response = curs.execute(query).fetchall()
for char, count in response:
    print(f"char id: {char}\tweapon count: {count}")

print("\nOn average, how many Items does each Character have?")
query = """
SELECT AVG(x.cnt)
FROM
(
SELECT COUNT(item_id) as cnt
FROM charactercreator_character_inventory
GROUP BY character_id
)x;
"""
print(curs.execute(query).fetchall()[0][0])

print("\nOn average, how many Weapons does each character have?")
query = """
SELECT AVG(x.cnt)
FROM
(
SELECT COUNT(item_id) as cnt
FROM charactercreator_character_inventory
WHERE item_id IN
(
SELECT item_ptr_id FROM armory_weapon
)
GROUP BY character_id
)x;
"""
print(curs.execute(query).fetchall()[0][0])

curs.close()
conn.commit()