"""
- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
"""

import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


conn = connect_to_db()
curs = conn.cursor()

# Total Number of Characters
total_characters = """
    SELECT COUNT(*)
    FROM charactercreator_character;
    """
results1 = execute_query(curs, total_characters)

# How many of each specific subclass?
# cleric class
cleric_class = """
SELECT COUNT(*)
FROM charactercreator_cleric;
"""
resultscleric = execute_query(curs, cleric_class)
# answer: 75

# Fighter Class
fighter_class = """
SELECT COUNT(*)
FROM charactercreator_fighter;
"""
resultsfighter = execute_query(curs, fighter_class)
# answer: 68

# Mage Class
mage_class = """
SELECT COUNT(*)
FROM charactercreator_mage;
"""
resultsmage = execute_query(curs, mage_class)
# answer: 108

# Necromancer
necromancer_class = """
SELECT COUNT(*)
FROM charactercreator_necromancer;
"""
resultsnecromancer = execute_query(curs, necromancer_class)
# answer: 11

# Theif
thief_class = """
SELECT COUNT(*)
FROM charactercreator_thief;
"""
resultstheif = execute_query(curs, thief_class)
# Answer: 51

# Total Items
total_items = """
SELECT COUNT(*)
FROM armory_item;
"""
resultsitems = execute_query(curs, total_items)
# Answer: 174

# How Many Items are weapons (contain a power attr)?
total_weapons = """
SELECT COUNT(*)
FROM armory_weapon
"""
results_weapons = execute_query(curs, total_weapons)
# Answer: 37

# How Many Items are not weapons
not_weapons = execute_query(curs, total_items)[0][0] - execute_query(curs, total_weapons)[0][0]
# answer:

# How many Items does each character have? (Return first 20 rows)
character_items_20 = """
SELECT character_id, name, COUNT(item_id) FROM
(SELECT cc.character_id, cc.name, ai.item_id, ai.name
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id)
GROUP BY 1 ORDER BY 3 DESC
LIMIT 20;"""
resultscharitems20 = execute_query(curs, character_items_20)

# How many weapons does each character have? (Return first 20 rows)
character_weapons_20 = """
SELECT character_id, name, COUNT(item_ptr_id) FROM
(SELECT cc.character_id, cc.name, aw.item_ptr_id, aw.power
FROM charactercreator_character AS cc,
armory_weapon AS aw,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND aw.item_ptr_id = cci.item_id)
GROUP BY 1 ORDER BY 2 DESC
LIMIT 20;"""
resultscharweapons20 = execute_query(curs, character_weapons_20)

# Avg items per character
avg_items_character = """
SELECT AVG(nc) FROM
(SELECT character_id, COUNT(DISTINCT item_id) AS nc FROM
(SELECT cc.character_id, cc.name, ai.item_id, ai.name
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id)
GROUP BY 1 ORDER BY 2 DESC) """
resultsavgitems = execute_query(curs, avg_items_character)
# answer : 2.97

# Avg weapons per character
avg_weapons_character = """
SELECT AVG(nc) FROM
(SELECT character_id, COUNT(DISTINCT item_ptr_id) AS nc FROM
(SELECT cc.character_id, cc.name, aw.item_ptr_id, aw.power
FROM charactercreator_character AS cc,
armory_weapon AS aw,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND aw.item_ptr_id = cci.item_id)
GROUP BY 1 ORDER BY 2 DESC)
"""
resultsavgweapons = execute_query(curs, avg_weapons_character)
# Answer = 1.31

if __name__ == '__main__':
    print(
        f'Report of rpg_queries \n'
        f'Total Number Characters: {results1[0][0]} \n \n'
        f'Number of Clerics: {resultscleric[0][0]} \n'
        f'Number of Fighters: {resultsfighter[0][0]} \n'
        f'Number of Mages: {resultsmage[0][0]} \n'
        f'Number of Necromancers: {resultsnecromancer[0][0]} \n'
        f'Number of Theifs: {resultstheif[0][0]} \n \n'
        f'Total Items: {resultsitems[0][0]} \n'
        f'Total Weapons {results_weapons[0][0]}\n'
        f'Total Items that are not Weapons: {not_weapons}\n \n'
        f'Top 20 Characters Number of Items: {resultscharitems20}\n \n'
        f'Top 20 Characters Number of Weapons: {resultscharweapons20}\n \n'
        f'Avg items per Character: {round(resultsavgitems[0][0], 2)}\n'
        f'Avg items per Character: {round(resultsavgweapons[0][0], 2)}\n'

    )
