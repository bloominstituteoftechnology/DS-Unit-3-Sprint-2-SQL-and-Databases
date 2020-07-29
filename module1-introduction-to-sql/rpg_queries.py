import os.path
import sqlite3

# construct a path to wherever your database exists
# DB_FILEPATH = 'https://github.com/RAV10K1/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILEPATH = os.path.join(BASE_DIR, 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

total_char = "SELECT count(character_id) FROM charactercreator_character"
no_clerics = "SELECT COUNT() FROM charactercreator_cleric"
no_fighters = "SELECT COUNT() FROM charactercreator_fighter"
no_mages = "SELECT COUNT() FROM charactercreator_mage"
no_necro = "SELECT COUNT() FROM charactercreator_necromancer"
no_thief = "SELECT COUNT() FROM charactercreator_thief"
total_items = "SELECT (select COUNT(item_id) FROM armory_item) + (select COUNT(item_ptr_id) FROM armory_weapon) AS Total_Items"
item_count = "SELECT COUNT() FROM armory_weapon"
char_item = 'SELECT character_id, count(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20'
char_wpn = 'SELECT character_id, count(item_id) FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON item_id = item_ptr_id GROUP BY character_id LIMIT 20'
avg_char_wpn = "SELECT character_id, COUNT(item_id) as 'No_of_Items',ROUND(AVG(item_id)) FROM charactercreator_character_inventory GROUP BY character_id ORDER BY character_id LIMIT 20"
avg_char_item = "SELECT character_id, count(item_id), round(avg(item_ptr_id)) FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON item_id = item_ptr_id GROUP BY character_id LIMIT 20"

queries = [total_char, no_clerics, no_fighters, no_mages, no_necro, no_thief,
            total_items, item_count, char_item, char_wpn, avg_char_item, avg_char_wpn]

for query in queries:
    result = cursor.execute(query).fetchall()
    print('Result :', result[0])