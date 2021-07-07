import os
import sys
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), 
                           "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# How many total Characters are there?
question_character_count = "How many total Characters are there?"
query_character_count = """
SELECT COUNT(DISTINCT(character_id)) 
FROM charactercreator_character 
AS character_count
"""

# How many of each specific subclass?
question_cleric_count = "How many clerics are there?"
query_cleric_count = """
SELECT COUNT(DISTINCT(character_ptr_id)) 
FROM charactercreator_cleric;
"""
question_fighter_count = "How many fighters are there?"
query_fighter_count = """
SELECT COUNT(DISTINCT(character_ptr_id)) 
FROM charactercreator_fighter;
"""
question_mage_count = "How many mages are there?"
query_mage_count = """
SELECT COUNT(DISTINCT(character_ptr_id)) 
FROM charactercreator_mage;
"""
question_necromancer_count = "How many necromancers are there?"
query_necromancer_count = """
SELECT COUNT(DISTINCT(mage_ptr_id)) 
FROM charactercreator_necromancer;
"""
question_thief_count = "How many thiefs are there?"
query_thief_count = """
SELECT COUNT(DISTINCT(character_ptr_id)) 
FROM charactercreator_thief;
"""

# How many total Items?
question_item_count = "How many total Items?"
query_item_count = """
SELECT COUNT(DISTINCT(item_id)) 
FROM armory_item
"""

# How many of the Items are weapons? How many are not?
question_item_is_weapon = "How many of the Items are weapons?"
query_item_is_weapon = """
SELECT COUNT(DISTINCT(item_ptr_id)) 
FROM armory_weapon
"""
question_item_not_weapon = "How many are not [weapons]?"
query_item_not_weapon = """
SELECT COUNT(DISTINCT(item_id))
FROM armory_item
LEFT JOIN armory_weapon 
ON armory_weapon.item_ptr_id = armory_item.item_id
WHERE armory_weapon.item_ptr_id IS NULL
"""

# How many Items does each character have? (Return first 20 rows)
question_items_per_character = "How many Items does each character have? (Return first 20 rows)"
query_items_per_character = """
SELECT COUNT(character_id)
FROM charactercreator_character_inventory
GROUP By character_id
LIMIT 20
"""

# How many Weapons does each character have? (Return first 20 rows)
question_weapons_per_character = "How many Weapons does each character have? (Return first 20 rows)"
query_weapons_per_character = """
SELECT COUNT(item_ptr_id)
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon
ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY character_id
LIMIT 20
"""

# On average, how many Items does each Character have?
question_avg_items_per_character = "On average, how many Items does each Character have?"
query_avg_items_per_character = """
SELECT AVG(item_count) AS average_items_per_character
FROM (SELECT DISTINCT character_id AS character_id,
COUNT(character_id) AS item_count
FROM charactercreator_character_inventory
GROUP BY character_id)
"""

# On average, how many Weapons does each character have?
question_avg_weapons_per_character = "On average, how many Weapons does each character have?"
query_avg_weapons_per_character = """
SELECT AVG(weapon_count) AS average_weapons_per_character
FROM (SELECT DISTINCT character_id AS character_id,
      COUNT(character_id) AS weapon_count
      FROM charactercreator_character_inventory
      WHERE item_id IN
      (SELECT item_ptr_id FROM armory_weapon)
      GROUP BY character_iD)
"""

# Lists of questions and queries for programmatic execution
questions = [question_character_count, 
             question_cleric_count, 
             question_fighter_count, 
             question_mage_count, 
             question_necromancer_count, 
             question_thief_count,
             question_item_count, 
             question_item_is_weapon, 
             question_item_not_weapon,
             question_items_per_character,
             question_weapons_per_character,
             question_avg_items_per_character,
             question_avg_weapons_per_character]

queries = [query_character_count, 
           query_cleric_count, 
           query_fighter_count, 
           query_mage_count, 
           query_necromancer_count, 
           query_thief_count,
           query_item_count, 
           query_item_is_weapon, 
           query_item_not_weapon,
           query_items_per_character,
           query_weapons_per_character,
           query_avg_items_per_character,
           query_avg_weapons_per_character]

orig = sys.stdout
f = open('rpg_query_answers.txt', 'a+')
sys.stdout = f


for question, query in zip(questions, queries):
    print("\n", question, "\n", query, "\n", cursor.execute(query).fetchall(), "\n\n-------------")

sys.stdout = orig
f.close()