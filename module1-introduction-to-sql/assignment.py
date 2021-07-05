import sqlite3
import os

# Establish connection to database
conn = sqlite3.connect('rpg_db.sqlite3')

# Cursor for querying database
curs = conn.cursor()

# Question 1 - How many characters are there?
a1 = curs.execute(
        'SELECT COUNT(character_id) FROM charactercreator_character'
        ).fetchall()[0][0]
print('Answer 1')
print('---------')
print(f'There are {a1} total characters.')
print('\n')

# Question 2 - How many of each specific subclass?
print('Answer 2')
print('---------')
print('There are four subclasses:')
a2a = curs.execute(
        'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'
        ).fetchall()[0][0]
print(f'There are {a2a} Fighters.')
a2b = curs.execute(
        'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'
        ).fetchall()[0][0]
print(f'There are {a2b} Clerics.')
a2c = curs.execute(
        'SELECT COUNT(character_ptr_id) FROM charactercreator_thief'
        ).fetchall()[0][0]
print(f'There are {a2c} Thieves.')
a2d = curs.execute(
        'SELECT COUNT(character_ptr_id) FROM charactercreator_mage'
        ).fetchall()[0][0]
print(f'There are {a2d} Mages.')
a2e = curs.execute(
        'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer'
        ).fetchall()[0][0]
print(f'Within Mage, there are {a2e} Necromancers.')
print('\n')

# Question 3 - How many total items are there?
a3 = curs.execute(
    'SELECT COUNT(item_id) FROM armory_item'
    ).fetchall()[0][0]
print('Answer 3')
print('---------')
print(f'There are {a3} total items.')

# Question 4 - How many items are weapons? How many are not?
a4a = curs.execute(
        'SELECT COUNT(item_ptr_id) FROM armory_weapon'
        ).fetchall()[0][0]
print('Answer 4')
print('---------')
print(f'Of the {a3} Items, {a4a} are weapons and {a3-a4a} are not.')
print('\n')

# Question 5 - How many items does each character have?(Return first 20 rows)
a5 = curs.execute(
    '''SELECT character_id, COUNT(item_id)
        FROM charactercreator_character_inventory
        GROUP BY character_id
        LIMIT 20'''
    ).fetchall()
print('Answer 5')
print('---------')
for t in a5:
    print(f'Char {t[0]} has {t[1]} item(s).')
print('\n')

# Question 6 - How many weapons does each character have?(Return first 20 rows)
a6 = curs.execute('''SELECT cci.character_id, COUNT(aw.item_ptr_id)
                     FROM charactercreator_character_inventory as cci
                     INNER JOIN armory_item AS ai
                     ON ai.item_id = cci.item_id
                     INNER JOIN armory_weapon AS aw
                     ON aw.item_ptr_id = ai.item_id
                     GROUP BY cci.character_id
                     LIMIT 20''').fetchall()
print('Answer 6')
print('---------')
for t in a6:
    print(f'Char {t[0]} has {t[1]} weapon(s).')
print('\n')

# Question 7 - On average, how many items does each character have?
a7 = curs.execute('''SELECT AVG(c)
                     FROM (
                         SELECT character_id, COUNT(item_id) as c
                         FROM charactercreator_character_inventory
                         GROUP BY character_id
                     )''').fetchall()[0][0]
print('Answer 7')
print('---------')
print(f'The average items per character is {a7:.2f}')
print('\n')

# Question 8 - On average, how many weapons does each character have?
a8 = curs.execute('''SELECT AVG(c)
                     FROM (
                         SELECT cci.character_id, COUNT(aw.item_ptr_id) AS c
                         FROM charactercreator_character_inventory AS cci
                         INNER JOIN armory_item AS ai
                         ON ai.item_id = cci.item_id
                         INNER JOIN armory_weapon AS aw
                         ON aw.item_ptr_id = ai.item_id
                         GROUP BY cci.character_id
                     )''').fetchall()[0][0]
print('Answer 8')
print('---------')
print(f'The average weapons per character is {a8:.2f}')
