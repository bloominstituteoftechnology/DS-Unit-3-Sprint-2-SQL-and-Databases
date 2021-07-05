"""
This programs is designed to be a one-shot program with multiple
sqlite queries. It is requires the .sqlite file to be in the same directory 
and will print out the results to these requested queries:

##### ASSIGNMENT #####

- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have? 


##### TO DO ######

- This program will be continually refactored. I will start by
defining a few things globally. Time-permitting I would like to
refactor to something Object-Oriented.

"""

import sqlite3
import pandas as pd

# Setting global variables for connecting to the database.
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# My queries:

def total_count():

    total_count_query = "SELECT COUNT (*) FROM charactercreator_character;"

    result = curs.execute(total_count_query).fetchall()

    return result[0][0]

def class_counts():

    class_count_query = ("SELECT (\n"
                         "SELECT COUNT(*)\n"
                         "        FROM charactercreator_cleric\n"
                         "        ) AS clerics,\n"
                         "        (\n"
                         "        SELECT COUNT(*)\n"
                         "        FROM charactercreator_fighter\n"
                         "            ) AS fighter,\n"
                         "		(\n"
                         "        SELECT COUNT(*)\n"
                         "        FROM charactercreator_mage\n"
                         "        ) AS mage,\n"
                         "        (\n"
                         "        SELECT COUNT(*)\n"
                         "        FROM charactercreator_necromancer\n"
                         "        ) AS necromancer,\n"
                         "		(\n"
                         "		SELECT COUNT(*)\n"
                         "		FROM charactercreator_thief\n"
                         "		) AS thief;")

    result = curs.execute(class_count_query).fetchall()

    return result[0]

def item_count():

    item_count_query = 'SELECT COUNT(*) FROM armory_item'

    result = curs.execute(item_count_query).fetchall()

    return result[0][0]

def weapon_count():

    weapon_count_query = 'SELECT COUNT(*) FROM armory_weapon'

    result = curs.execute(weapon_count_query).fetchall()

    return result[0][0]

def other_count():

    result = item_count() - weapon_count()

    return result

def item_per_character():

    ipc_count_query = ("SELECT cc.name AS character_name, COUNT (*)\n"
                       "FROM\n"
                       "charactercreator_character AS cc,\n"
                       "armory_item AS ai,\n"
                       "charactercreator_character_inventory AS cci\n"
                       "WHERE\n"
                       "cc.character_id = cci.character_id AND\n"
                       "ai.item_id = cci.item_id\n"
                       "GROUP BY\n"
                       "cc.name\n"
                       "LIMIT 20")


    result = curs.execute(ipc_count_query).fetchall()

    return pd.DataFrame(result)

def weapon_per_character():

    wpc_count_query = ("SELECT cc.name, COUNT(*)\n"
                       "FROM  \n"
                       "charactercreator_character AS cc,\n"
                       "charactercreator_character_inventory AS cci,\n"
                       "armory_item AS  ai,\n"
                       "armory_weapon AS aw\n"
                       "WHERE\n"
                       "cc.character_id = cci.character_id AND\n"
                       "cci.item_id = ai.item_id AND\n"
                       "ai.item_id = aw.item_ptr_id\n"
                       "GROUP BY \n"
                       "cc.name\n"
                       "LIMIT\n"
                       "20;")

    result = curs.execute(wpc_count_query).fetchall()

    return pd.DataFrame(result)

def item_average():

    item_average_qeuery = ('SELECT avg(item_count) FROM(\n'
                           '    SELECT cc.name as character_name, COUNT(*) as item_count\n'
                           '    FROM\n'
                           '    charactercreator_character AS cc,\n'
                           '    charactercreator_character_inventory AS cci,\n'
                           '    armory_item AS ai\n'
                           '    WHERE\n'
                           '    cc.character_id = cci.character_id AND\n'
                           '    cci.item_id = ai.item_id\n'
                           '    GROUP BY\n'
                           '    cc.name);')

    result = curs.execute(item_average_qeuery).fetchall()

    return result[0][0]

def weapon_average():

    weapon_average_qeuery = ("SELECT avg(weapon_count) FROM(\n"
                             "	SELECT cc.name as character_name, COUNT(*) as weapon_count\n"
                             "	FROM\n"
                             "	charactercreator_character AS cc,\n"
                             "	charactercreator_character_inventory AS cci,\n"
                             "	armory_item AS ai,\n"
                             "	armory_weapon AS aw\n"
                             "	WHERE \n"
                             "	cc.character_id = cci.character_id AND\n"
                             "	cci.item_id = ai.item_id AND\n"
                             "	ai.item_id = aw.item_ptr_id\n"
                             "	GROUP BY \n"
                             "	cc.name);")

    result = curs.execute(weapon_average_qeuery).fetchall()

    return result[0][0]

print('###### RPG DATABASE ANALYSIS ######################','\n\n'
      'There were', total_count(), 'characters in the database','where',
      '\n', class_counts()[0], 'were clerics,', class_counts()[1],
      'were fighters,', class_counts()[4],'were thieves,','\n', 'and',
      class_counts()[2], 'were mages,', class_counts()[3],
      'of which were necrocmancers.','\n\n', 'There were',
      item_count(), 'items,', weapon_count(), 'of which were weapons.',
      '\n', other_count(), 'were misc items.','\n\n',
      'Each Character had an average of', weapon_count(), 'weapons, and',
       item_count(), 'items.','\n\n\n\n')

print('###### Weapon Inventory ######','\n\n', weapon_per_character(),'\n\n\n',
      '###### Item Inventory ######', '\n\n', item_per_character())