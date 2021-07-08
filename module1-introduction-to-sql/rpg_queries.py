
import sqlite3
import pandas as pd

connection = sqlite3.connect("rpg_db.sqlite3")
cursor = connection.cursor()

def query_w_names(query, names):
    con = sqlite3.connect("rpg_db.sqlite3")
    c = con.cursor()
    print(pd.DataFrame(c.execute(query), columns=names))
    c.close
    con.close

def query_w_named_columns(query):
    conn = sqlite3.connect("rpg_db.sqlite3")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    print(pd.DataFrame(data, columns=data[0].keys()).to_string(index=False))
    cur.close 
    conn.close

#How many total Characters are there?
print("\nHow many total Characters are there?")
query_w_named_columns("""
SELECT COUNT (DISTINCT name) AS Number_of_total_Characters
  FROM charactercreator_character 
""")

# How many of each specific subclass?
print("\nHow many of each specific subclass?")
query_w_named_columns("""
SELECT
    (SELECT COUNT(*) FROM charactercreator_cleric) AS clerics,
    (SELECT COUNT(*) FROM charactercreator_fighter) AS fighters,
    (SELECT COUNT(*) FROM charactercreator_mage) AS mages,
    (SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancers,
    (SELECT COUNT(*) FROM charactercreator_thief) AS theives
""")

#How many total items?
print("\nHow many total items?")
query_w_named_columns("""
    SELECT COUNT(*) AS Total_Item_Count
      FROM armory_item 
""")

#How many items are weapons? 
print("\nHow many items are weapons?")
query_w_named_columns("""
    SELECT COUNT(*) AS Number_of_Weapons
      FROM armory_weapon 
""")

#How many items are not weapons?
print("\nHow many items are not weapons?")
query_w_named_columns("""
    SELECT COUNT(*) AS Non_Weapon_Item_Count
      FROM armory_item 
     WHERE item_id NOT IN 
           (SELECT item_ptr_id 
              FROM armory_weapon)
""")

#How many items does each character have (first 20 rows)?
print("\nHow many items does each character have?")
query_w_named_columns("""
SELECT *
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Item_Count
          FROM charactercreator_character_inventory
         GROUP BY Character_ID)
 LIMIT 20
""")

#How many weapons does each character have (first 20 rows)?
print("\nHow many weapons does each character have?")
query_w_named_columns("""
SELECT *
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Weapon_Count
          FROM charactercreator_character_inventory
         WHERE item_id IN
               (SELECT item_ptr_id
                  FROM armory_weapon)
         GROUP BY Character_ID)
 LIMIT 20
""")

#On average, how many items does each Character have?
print("\nHow many items does each character have on Average?")
query_w_named_columns("""
SELECT AVG(Item_Count) AS Average_Number_of_Items_Per_Character
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Item_Count
          FROM charactercreator_character_inventory
         GROUP BY Character_ID)
""")

#On average, how many weapons does each Character have?
print("\nHow many items does each character have on Average?")
query_w_named_columns("""
SELECT AVG(Weapon_Count) AS Average_Character_Weapon_Count
  FROM (SELECT DISTINCT character_id AS Character_ID, 
               COUNT(character_id) AS Weapon_Count
          FROM charactercreator_character_inventory
         WHERE item_id IN
               (SELECT item_ptr_id
                  FROM armory_weapon)
         GROUP BY Character_ID)
 LIMIT 20
""")