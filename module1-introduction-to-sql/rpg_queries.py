import sqlite3 
import pandas as pd
import sys


DB_PATH = "rpg_db.sqlite3"


questions = ['How many total characters are there?',
              'How many of each specific subclass?',
              'How many total items?',
              'How many are weapons?',
              'How many are not?',
              'How many items does each character have?',
              'How many weapons?',
              'On average, how many items does each character have?',
              'On average, how many weapons does each character have?']

queries = ["""SELECT COUNT (DISTINCT name) AS Number_of_total_Characters
            FROM charactercreator_character""", 
            """SELECT
              (SELECT COUNT(*) FROM charactercreator_cleric) AS clerics,
              (SELECT COUNT(*) FROM charactercreator_fighter) AS fighters,
              (SELECT COUNT(*) FROM charactercreator_mage) AS mages,
              (SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancers,
              (SELECT COUNT(*) FROM charactercreator_thief) AS theives
            """,
            """SELECT COUNT(*) AS Total_Items
              FROM armory_item""",
            """SELECT COUNT(*) AS Number_of_Weapons
            FROM armory_weapon""",
            """SELECT COUNT(*) AS Non_weapons
            FROM armory_item
            WHERE item_id NOT IN
            (SELECT item_ptr_id
            FROM armory_weapon)""",
            """SELECT *
            FROM (SELECT DISTINCT character_id AS Character_ID,
            COUNT(character_id) AS Items
            FROM charactercreator_character_inventory
            GROUP BY Character_ID)
            LIMIT 20""",
            """SELECT *
            FROM (SELECT DISTINCT character_id AS Character_ID,
            COUNT(character_id) AS Weapon_Count
            FROM charactercreator_character_inventory
            WHERE item_id IN
            (SELECT item_ptr_id
            FROM armory_weapon)
            GROUP BY Character_ID)
            LIMIT 20""",
            """SELECT AVG(Item_Count) AS Avg_Items_Per_Char
            FROM (SELECT DISTINCT character_id AS Character_ID,
            COUNT(character_id) AS Item_Count
            FROM charactercreator_character_inventory
            GROUP BY Character_ID)""",
            """SELECT AVG(Weapon_Count) AS Avg_Weapons_Per_Char
            FROM (SELECT DISTINCT character_id AS Character_ID,
            COUNT(character_id) AS Weapon_Count
            FROM charactercreator_character_inventory
            WHERE item_id IN
            (SELECT item_ptr_id FROM armory_weapon)
            GROUP BY Character_ID)
            LIMIT 20"""
            ]



def db_query(query):
  db = sqlite3.connect(DB_PATH)
  db.row_factory = sqlite3.Row
  cur = db.cursor()

  cur.execute(query)

  data = cur.fetchall()
  return pd.DataFrame(data,
                     columns=data[0].keys()).to_string(index=False)
  cur.close()
  db.close()

orig = sys.stdout
f = open('rpg_query_answers.txt', 'a+')
sys.stdout = f

for question, answer in zip(questions, queries):

  print(question)
  print("~~"*40)
  print(db_query(answer) + "\n"*2)

sys.stdout = orig
f.close()

