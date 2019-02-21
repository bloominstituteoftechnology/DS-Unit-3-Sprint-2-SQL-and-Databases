


import sqlite3
import pandas as pd

connection = sqlite3.connect("rpg_db.sqlite3")
cursor = connection.cursor()

def query_w_names(_query, names):
    con = sqlite3.connect("rpg_db.sqlite3")
    c = con.cursor()
    print(pd.DataFrame(c.execute(_query), columns=names))
    c.close
    con.close

def query_w_named_columns(_query):
    conn = sqlite3.connect("rpg_db.sqlite3")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(_query)
    r = c.fetchone()
    print(pd.DataFrame(c.fetchall(), columns=r.keys()))
    c.close 
    conn.close

#How many total Characters are there?

total_character_query = """SELECT COUNT (DISTINCT name) FROM charactercreator_character"""

query_w_names(total_character_query, ["Character_Count"])

#How many of each specific subclass?
subclass_query = """ SELECT
    (SELECT COUNT(*) FROM charactercreator_cleric) AS clerics,
    (SELECT COUNT(*) FROM charactercreator_fighter) AS fighters,
    (SELECT COUNT(*) FROM charactercreator_mage) AS mages,
    (SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancers,
    (SELECT COUNT(*) FROM charactercreator_thief) AS theives
"""

query_w_names(subclass_query,["clerics","fighters","mages","necromancers","theives"])

#How many total items?
total_items = """
    SELECT COUNT(*) FROM armory_item
"""
query_w_names(total_items,["Total Items"])

#How many items are weapons? 
total_weapons = """
    SELECT COUNT(*) FROM armory_weapon
"""
query_w_names(total_weapons,["Total Weapons"])

#How many items are not weapons?
non_weapon = """
    SELECT COUNT(*) 
      FROM armory_item 
     WHERE item_id NOT IN 
           (SELECT item_ptr_id 
              FROM armory_weapon)
"""
query_w_names(non_weapon,["# Non-Weapons"])

#How many items does each character have (first 20 rows)?
character_inventory_item_count = """
SELECT *
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Item_Count
          FROM charactercreator_character_inventory
         GROUP BY Character_ID)
 LIMIT 20
"""
query_w_named_columns(character_inventory_item_count)

#How many weapons does each character have (first 20 rows)?
characters_weapons = """
SELECT *
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Weapon_Count
          FROM charactercreator_character_inventory
         WHERE item_id IN
               (SELECT item_ptr_id
                  FROM armory_weapon)
         GROUP BY Character_ID)
 LIMIT 20
"""
query_w_named_columns(characters_weapons)

#On average, how many items does each Character have?

#On average, how many weapons does each Character have?

