import sqlite3

rpg_db = 'C:/Users/David/Downloads/rpg_db.sqlite3'  # This obviously won't work if not run locally

sl_conn = sqlite3.connect(rpg_db)
sl_curs = sl_conn.cursor()

report = {"RPG DATABASE QUERY REPORT": "Enumerating.."}

# How many total characters are there?
query = "SELECT COUNT(*) FROM charactercreator_character"
query_return = sl_curs.execute(query).fetchall()
query_return_value = query_return[0][0]
report['How many total characters are there?'] = query_return_value

# How many of each specific subclass?
class_list = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for char_class in class_list:
    query = f"SELECT COUNT(*) FROM charactercreator_{char_class}"
    query_return = sl_curs.execute(query).fetchall()
    query_return_value = query_return[0][0]
    report[char_class] = query_return_value

# How many total items?
query = "SELECT COUNT(*) FROM charactercreator_character_inventory"
query_return = sl_curs.execute(query).fetchall()
query_return_value = query_return[0][0]
report['How many total items?'] = query_return_value

# How man of the Items are weapons? How many are not?
report = {}
query = "SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon;"
query_return = sl_curs.execute(query).fetchall()
query_return_value = query_return[0][0]
report['How man of the Items are weapons?'] = query_return_value
query = "SELECT COUNT(DISTINCT item_id) - COUNT(DISTINCT item_ptr_id) FROM armory_item, armory_weapon;"
query_return = sl_curs.execute(query).fetchall()
query_return_value = query_return[0][0]
report['How many are not?'] = query_return_value

# How many Items does each character have? (Return first 20 rows)
query = """
SELECT character_id, count(item_id) 
FROM charactercreator_character_inventory
GROUP by character_id
LIMIT 20
"""
query_return = sl_curs.execute(query).fetchall()
my_list = [f'Character with ID#{character[0]} has {character[1]} items' for character in query_return]
report['How many Items does each character have?'] = my_list

# How many Weapons does each character have? (Return first 20 rows)
query = """
select character_id, count(item_id)
from charactercreator_character_inventory
inner join armory_weapon
on item_id = item_ptr_id
GROUP by character_id
LIMIT 20
"""
query_return = sl_curs.execute(query).fetchall()
my_list = [f'Character with ID#{character[0]} has {character[1]} weapons' for character in query_return]
report['How many Weapons does each character have?'] = my_list

# On average, how many Items does each Character have?
query = """
SELECT character_id, count(item_id) 
FROM charactercreator_character_inventory
GROUP by character_id"""
query_return = sl_curs.execute(query).fetchall()
item_numbers = [item[1] for item in query_return]
avg = sum(item_numbers)/len(item_numbers)
report['On average, how many Items does each Character have?'] = f'On average a character has ~{round(avg, 2)} items.'

# On average, how many Weapons does each Character have?
query = """
select character_id, count(item_id)
from charactercreator_character_inventory
inner join armory_weapon
on item_id = item_ptr_id
GROUP by character_id
"""
query_return = sl_curs.execute(query).fetchall()
weapon_numbers = [item[1] for item in query_return]
avg = sum(weapon_numbers)/len(weapon_numbers)
report['On average, how many Weapons does each Character have?'] = f'The average character has {round(avg, 2)} weapons.'

for key in report.keys():
    if type(report[key]) != list:
        print(key, '\n', report[key])
    else:
        print(key)
        for item in report[key]:
            print(item)
    print('\n')