#!/usr/bin/env python

import sqlite3 as sql
import pandas as pd
print(pd.__version__)
conc = sql.connect('rpg_db.sqlite3')
cursor = conc.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

q = 'SELECT COUNT(*) from charactercreator_character'
c = conc.execute(q).fetchone()
print(f"How many total Characters are there? {c[0]}")

q = 'SELECT COUNT(*) FROM django_content_type AS d WHERE d.app_label=="charactercreator" and d.model != "character"';
c = conc.execute(q).fetchone()
print(f"How many subclasses are there? {c[0]}")
q = """
   SELECT d.model AS model FROM django_content_type AS d WHERE d.app_label=="charactercreator" and d.model != "character"
"""
print(f"How many of each specific subclass?")
c = conc.execute(q).fetchall()
for m in c:
   if m[0] == 'necromancer':
       print('\t', 'mage-necromancer', end='')
   else:
       print('\t', m[0], end='')
   q = f"select count(*) from charactercreator_{m[0]}"
   c = conc.execute(q).fetchone()[0]
   if m[0] == 'mage':
       nq = f"select count(*) from charactercreator_necromancer"
       nc = conc.execute(nq).fetchone()[0]
       c -= nc
   print(f': {c}') 

q = "SELECT COUNT(*) FROM armory_item"
c = conc.execute(q).fetchone()
print(f"How many total Items? {c[0]})")

q = "SELECT COUNT(*) FROM armory_weapon"
c = conc.execute(q).fetchone()
q = "SELECT COUNT(*) FROM armory_item"
cn = conc.execute(q).fetchone()
print(f"How many of the Items are weapons?  {c[0]} How many are not? {cn[0] - c[0]})")

q = """
SELECT i.character_id, c.name, count(*) 
FROM charactercreator_character_inventory AS i JOIN 
charactercreator_character as c ON i.character_id = c.character_id
GROUP BY i.character_id
ORDER BY count(*) DESC
LIMIT 20
"""
c = conc.execute(q).fetchall()
d = {}
for o in c:
  d[o[0]] = o[1:]
df = pd.DataFrame.from_dict(d, orient='index', columns=['character name','# of items'])
df.index.name = 'character id'
print("How many Items does each character have? (Return first 20 rows)")
print(df.head(20),'\n\n')


q = """
SELECT i.character_id, c.name, count(*) 
FROM armory_weapon AS w JOIN charactercreator_character_inventory AS i 
ON w.item_ptr_id = i.character_id JOIN
charactercreator_character as c ON i.character_id = c.character_id
GROUP BY i.character_id
ORDER BY count(*) DESC
LIMIT 20
"""
c = conc.execute(q).fetchall()
d = {}
for o in c:
  d[o[0]] = o[1:]
df = pd.DataFrame.from_dict(d, orient='index', columns=['character name','# of weapons'])
df.index.name = 'character id'
print(f"How many Weapons does each character have? (Return first 20 rows")
print(df.head(20),'\n\n')

q = "SELECT COUNT(*) from charactercreator_character"
t = conc.execute(q).fetchone()[0]
q = f"SELECT COUNT(*)/{t}. FROM charactercreator_character_inventory"
print(f" On average, how many Items does each Character have?  {conc.execute(q).fetchone()[0]}")

q = """
SELECT AVG(items)
FROM (
     SELECT character_id, count(item_id) as items
     FROM charactercreator_character_inventory
     GROUP BY character_id);"""
print(f" On average, how many Items does each Character have?  {conc.execute(q).fetchone()[0]}")


q = """
SELECT (total * 1.0)/n  FROM (
(SELECT SUM(items) as total
FROM (
     SELECT i.character_id as id, count(*) as items
     FROM armory_weapon AS w JOIN charactercreator_character_inventory AS i 
     ON w.item_ptr_id = i.character_id
     GROUP BY i.character_id))
,
(SELECT n FROM (select count(*) as n FROM charactercreator_character))) 
 """
fo = conc.execute(q).fetchone()
print(f" On average, how many Weapons does each Character have?  {fo[0]}")