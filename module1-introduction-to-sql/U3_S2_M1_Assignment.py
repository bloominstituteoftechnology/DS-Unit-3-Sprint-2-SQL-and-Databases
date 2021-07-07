## ASSIGNMENT PART I

import sqlite3

rpg_conn = sqlite3.connect('rpg_db.sqlite3')
curs = rpg_conn.cursor()

# How many total Characters are there?
char_query = 'SELECT * FROM charactercreator_character'
chars = curs.execute(char_query).fetchall()
q1 = len(chars)
print('\n# How many total Characters are there?')
print(q1)

# How many of each specific subclass?
mage_query = 'SELECT * FROM charactercreator_mage'
necromancer_query = 'SELECT * FROM charactercreator_necromancer'
thief_query = 'SELECT * FROM charactercreator_thief'
cleric_query = 'SELECT * FROM charactercreator_cleric'
fighter_query = 'SELECT * FROM charactercreator_fighter'
mages = len(curs.execute(mage_query).fetchall())
necromancers = len(curs.execute(necromancer_query).fetchall())
thieves = len(curs.execute(thief_query).fetchall())
clerics = len(curs.execute(cleric_query).fetchall())
fighters = len(curs.execute(fighter_query).fetchall())
print('\n\n# How many of each specific subclass? \n')
print(f' Mages: {mages} \n    --{necromancers} of whom are necromancers')
print(f' Thieves: {thieves}')
print(f' Clerics: {clerics}')
print(f' Fighters: {fighters}')

# How many total Items?
item_query = 'SELECT * FROM armory_item'
q3 = len(curs.execute(item_query).fetchall())
print('\n\n# How many total Items? \n', q3)

# How many of the Items are weapons? How many are not?
weapon_query = 'SELECT * FROM armory_weapon'
q4 = len(curs.execute(weapon_query).fetchall())
print(f'\n\n# How many of the Items are weapons? \n {q4}')
print(f'\n\n# How many are not? \n {q3 - q4}')

# How many Items does each character have? (Return first 20 rows)
print('\n\n# How many Items does each character have? (Return first 20 rows) \n')
for i in range(0,20):
    temp_char = chars[i][0]
    char_item_count_query = f'SELECT * FROM charactercreator_character_inventory as cci WHERE cci.character_id = {temp_char}'
    q5 = curs.execute(char_item_count_query).fetchall()
    print(f'{chars[i][1]}: {len(q5)} items!')

# How many Weapons does each character have? (Return first 20 rows)
print('\n\n# How many Weapons does each character have? (Return first 20 rows) \n')
for i in range(0,20):
    temp_char = chars[i][0]
    char_weapon_count_query = (f'SELECT * FROM charactercreator_character_inventory as cci, '
                               f'armory_weapon as ai '
                               f'WHERE cci.character_id = {temp_char} '
                               f'AND cci.item_id = ai.item_ptr_id')
    q6 = curs.execute(char_weapon_count_query).fetchall()
    print(f'{chars[i][1]}: {len(q6)} weapon(s)!')

# On average, how many Items does each Character have?
q7 = q3/q1
print('\n\n# On average, how many Items does each Character have? \n', (q7))

# On average, how many Weapons does each character have?
q8 = q4/q1
print('\n\n# On average, how many Weapons does each character have? \n', (q8))


## Assignment 2
print('\n\n\nAssignment 2!')
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

from sqlalchemy import create_engine
conn = create_engine('sqlite://', echo=False)

df.to_sql('buddy', conn)

query = 'SELECT * FROM buddy'
buddy_table = conn.execute(query).fetchall()

print('\n- Count how many rows you have - it should be 249!')
print(f'Total rows: {len(buddy_table)}\n')

query2 = 'SELECT Nature, Shopping FROM buddy WHERE Nature > 100 AND Shopping > 100'
q2 = conn.execute(query2).fetchall()

print('\n\n- How many users who reviewed at least 100 `Nature` in the category also'
      ' reviewed at least 100 in the `Shopping` category?')
print(len(q2), '\n')
