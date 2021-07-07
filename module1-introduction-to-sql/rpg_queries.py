import sqlite3

## question number 1 - "how many characters are there?"

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query0 = ('SELECT COUNT(*) FROM charactercreator_character;')
request0 = curs.execute(query0)

total_characters = request0.fetchone()[0]

print('1: How many total characters are there?\n',
    'There are {} characters.'.format(total_characters))


## question number 2 - "How many of each specific subclass?"

tables = ['charactercreator_mage', 'charactercreator_thief',
          'charactercreator_cleric', 'charactercreator_fighter']

print('2: How many of each specific subclass?')
for _ in tables:
    q = ('SELECT COUNT(*) FROM {};').format(_)
    request = curs.execute(q)
    print('{}?\nThere are {}'.format(_, request.fetchone()[0]))


## question 3 - "How many total Items?"
query1 = ('SELECT COUNT(*) FROM armory_item;')
request1 = curs.execute(query1)

total_number_of_items = request1.fetchone()[0]

print('3: How many total items?\nThere are {} items'.format(total_number_of_items))

## question 4 - "How many of the Items are weapons? How many are not?"

query2 = ('SELECT COUNT(*) FROM armory_weapon;')
request2 = curs.execute(query2)
number_of_weapons = request2.fetchone()[0]

print('4a: How many number of items are weapons?\n{}'.format(number_of_weapons))
print('4b: How many are not weapons?\n{}'.format((total_number_of_items - number_of_weapons)))

## question 5 - "How many Items does each character have? (Return first 20 rows)"

query3 = ('''
    SELECT cc.name, COUNT(cci.item_id)
    FROM charactercreator_character_inventory AS cci, charactercreator_character AS cc
    WHERE cc.character_id = cci.character_id
    GROUP BY cci.character_id
    LIMIT 20;''')
request3 = curs.execute(query3)
number_items_owned = request3.fetchall()

print('5: How many items does each character have?\n{}'.format(number_items_owned))

          
## question 6 - "How many Weapons does each character have? (Return first 20 rows)"

query4 = ('''
    SELECT name, COUNT(item_id)
    FROM charactercreator_character AS cc JOIN charactercreator_character_inventory AS cci
    ON cc.character_id = cci.character_id
    JOIN armory_weapon AS aw
    ON aw.item_ptr_id = cci.item_id
    GROUP BY cci.character_id
    LIMIT 20;
    ''')
request4 = curs.execute(query4)
number_weapons_owned = request4.fetchall()

print('6: How many weapons does each character have?\n{}'.format(number_weapons_owned))

## question 7 - "On average, how many Items does each Character have?"
query5 = ('''
    SELECT AVG(items)
    FROM (SELECT COUNT(item_id) as items
        FROM charactercreator_character_inventory
        GROUP BY character_id);
    ''')
request5 = curs.execute(query5)
avg_items_owned = request5.fetchone()[0]

print('7: How many items does each character have on average?\n{}'.format(avg_items_owned))

## question 8 - "On average, how many Weapons does each character have?"

query6 = ('''
    SELECT COUNT(cci.item_id) 
    FROM charactercreator_character_inventory AS cci, armory_weapon AS aw 
    WHERE aw.item_ptr_id = cci.item_id;
    ''')
request6 = curs.execute(query6)

total_weapons_owned = request6.fetchone()[0]

avg_weapons = total_weapons_owned / total_characters

print('8: How many weapons does each character own on average?\n{}'.format(avg_weapons))