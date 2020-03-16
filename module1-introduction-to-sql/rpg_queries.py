import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')


def execute(sql_query):
    curs = conn.cursor()
    return curs.execute(sql_query).fetchall()


# total characters
query = 'SELECT COUNT(*) FROM charactercreator_character'
print(f'Total Characters: {execute(query)}')

# subclass counts
subclass = ['mage', 'thief', 'cleric', 'fighter', 'necromancer']
for x in subclass:
    if x == 'mage':
        query = f'SELECT COUNT(*) FROM charactercreator_{x}'
        query2 = 'SELECT COUNT(*) FROM charactercreator_necromancer'
        query3 = f'SELECT ({query}) - ({query2})'
        print(f'Mage Count: {execute(query3)}')
    else:
        query = f'SELECT COUNT(*) FROM charactercreator_{x}'
        print(f'{x.capitalize()} Count: {execute(query)}')

# total items
query = 'SELECT COUNT(*) FROM armory_item'
print(f'Total Items: {execute(query)}')

# weapons vs not
query = 'SELECT COUNT(*) FROM armory_weapon'
query2 = 'SELECT COUNT(*) FROM armory_item'
query3 = f'SELECT ({query2}) - ({query})'
print(f'Weapon Count: {execute(query)}')
print(f'Non-Weapon Item Count: {execute(query3)}')

# Items per character
query = 'SELECT character_id FROM charactercreator_character_inventory LIMIT 20'
counts = {f'Character Id: {i[0]}': f'Item Count: {execute(query).count(i)}' for i in execute(query)}
print(counts)

# Weapons per character
query = 'SELECT character_id FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id WHERE item_id = armory_weapon.item_ptr_id LIMIT 20'
counts = {f'Character Id: {i[0]}': f'Item Count: {execute(query).count(i)}' for i in execute(query)}
print(counts)

# Average items per character
query = 'SELECT COUNT(*) FROM charactercreator_character_inventory'
query2 = 'SELECT COUNT(*) FROM charactercreator_character'
div = tuple(x / y for x, y in zip(execute(query)[0], execute(query2)[0]))
print(f'Average Items Per Character: {div[0]}')

# Average Weapons Per Character
query = 'SELECT COUNT(*) FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id WHERE item_id = armory_weapon.item_ptr_id'
query2 = 'SELECT COUNT(*) FROM charactercreator_character'
div = tuple(x / y for x, y in zip(execute(query)[0], execute(query2)[0]))
print(f'Average Weapons Per Character: {div[0]}')


