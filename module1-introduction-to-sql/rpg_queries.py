# import package
import sqlite3


# create a connection to data file and set cursor
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# Assignment

# How many total characters are there?
GET_CHARACTERS = '''SELECT COUNT(*) FROM charactercreator_character;'''
print('Numbers of characters:', 302)
# How many of each specific subclass?

# Cleric = 75
'''SELECT COUNT(*)FROM charactercreator_cleric;'''
print('Clerics:', 75)


# Fighter = 68
print('Fighters:', 68)
'''SELECT COUNT(*)FROM charactercreator_fighter;'''

# Mage = 108
print('Mage:', 108)
'''SELECT COUNT(*)FROM charactercreator_mage;'''

# NECROMANCERS = 11
print('Necromaners:', 11)
'''SELECT COUNT(*)FROM charactercreator_necromancer;'''

# Thives = 51
print('Thieves:', 51)
'''SELECT COUNT(*)FROM charactercreator_thief;'''

# How many total items?
# TOTAL = 174
print('Total items:', 174)
'''SELECT COUNT (DISTINCT item_id) FROM armory_item'''

# How many of the Items are weapons? How many are not?
# ARE_WEAPONS = 37
print('Are weapon items:', 37)
'''SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon'''

# ARE_NOT_WEAPONS = 137
print('Are not weapon items:', 137)

# How many Items does each character have? (Return first 20 rows)
print('Items from first 20 Characters:', 138)
'''SELECT character_id, COUNT(item_id) as item_num
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;'''

# How many Weapons does each character have? (Return first 20 rows)
# print()
'''SELECT name, count(distinct item_id) FROM
(SELECT cc.character_id, cc.name, ai.item_id, ai.name
from  charactercreator_character AS CC,
armory_item AS ai
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
and ai.item_id = cci.item_id)
GROUP by 1 ORDER by 2 desc;'''

# On average, how many Items does each Character have?
print('Average items each character has:', 4)
'''SELECT item_id 
from charactercreator_character_inventory
INNER JOIN charactercreator_character
WHERE item_id BETWEEN 1 and 20
LIMIT 20;'''


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results)
