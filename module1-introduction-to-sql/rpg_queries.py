import sqlite3


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print('Question 1: How many total Character are there?')
query1 = 'SELECT MAX(character_id) FROM charactercreator_character;'
output1 = curs.execute(query1).fetchone()
answer1 = output1[0]
print(f'Answer: There are {answer1} total Characters.')
print(' ')

classes = ['mage', 'thief', 'cleric', 'fighter', 'necromancer']

print('Question 2: How many of each specific subclass?')
print('Answer:')
for cl in classes:
    query2 = f'SELECT COUNT(*) FROM charactercreator_{cl};'
    output2 = curs.execute(query2).fetchone()
    answer2 = output2[0]
    print(f'There are {answer2} total {cl} Characters.')
print(' ')

print('Question 3: How many total Items?')
query3 = 'SELECT COUNT(*) FROM armory_item;'
output3 = curs.execute(query3).fetchone()
answer3 = output3[0]
print(f'Answer: There are {answer3} total Items.')
print(' ')

print('Question 4: How many of the items are weapons? How many are not?')
query4 = 'SELECT COUNT(*) FROM armory_weapon;'
output4 = curs.execute(query4).fetchone()
answer4 = output4[0]
print(f'Answer: {answer4} of the items are weapons. {answer3 - answer4} are not.')
print(' ')

print('Question 5: How many Items does each character have? (Return first 20 rows)')
query5 = 'SELECT cci.character_id, cc.name AS character_name, \
        COUNT(item_id) AS number_of_items \
        FROM charactercreator_character_inventory AS cci \
        INNER JOIN charactercreator_character AS cc \
        ON cci.character_id = cc.character_id \
        GROUP BY cci.character_id \
        LIMIT 20;'
output5 = curs.execute(query5)
column_names = [t[0] for t in output5.description]
print('Answer:')
print(tuple(column_names))
for row in output5:
    print(row)
print(' ')

print('Question 6: How many Weapons does each character have? (Return first 20 rows)')
query6 = 'SELECT cci.character_id, cc.name AS character_name, \
        COUNT(aw.item_ptr_id) AS number_of_weapons \
        FROM (((charactercreator_character_inventory AS cci \
        INNER JOIN armory_item AS ai ON cci.item_id = ai.item_id) \
        LEFT JOIN armory_weapon AS aw ON ai.item_id = aw.item_ptr_id) \
        INNER JOIN charactercreator_character AS cc ON cci.character_id = cc.character_id) \
        GROUP BY cci.character_id \
        LIMIT 20;'
output6 = curs.execute(query6)
column_names = [t[0] for t in output6.description]
print('Answer:')
print(tuple(column_names))
for row in output6:
    print(row)
print(' ')

print('Question 7: On average, how many items does each Character have?')
query5_no_limit = query5.split(' LIMIT')[0]
query7 = f'SELECT AVG(number_of_items) FROM ({query5_no_limit});'
output7 = curs.execute(query7).fetchone()
answer7 = output7[0]
print(f'Answer: On average, each Character has {answer7} items.')
print(' ')

print('Question 8: On average, how many weapons does each Character have?')
query6_no_limit = query6.split(' LIMIT')[0]
query8 = f'SELECT AVG(number_of_weapons) FROM ({query6_no_limit});'
output8 = curs.execute(query8).fetchone()
answer8 = output8[0]
print(f'Answer: On average, each Character has {answer8} weapons.')
