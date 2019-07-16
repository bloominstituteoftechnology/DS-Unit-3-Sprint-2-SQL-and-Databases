import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curr = conn.cursor()

query = """SELECT name FROM charactercreator_character;"""


# How many total characters are there?
hmm = curr.execute(query)
print(f'Total characters: {len(hmm.fetchall())}\n')

# How many of each specific subclass?
queries = ['''SELECT character_ptr_id FROM charactercreator_cleric;''',
           '''SELECT character_ptr_id FROM charactercreator_fighter;''',
           '''SELECT character_ptr_id FROM charactercreator_mage;''',
           '''SELECT mage_ptr_id FROM charactercreator_necromancer;''',
           '''SELECT character_ptr_id FROM charactercreator_thief;''']

for query in queries:
    replies = curr.execute(query)
    print(query.split('_')[-1])
    print(len(replies.fetchall()))

# How many total items:
query = '''SELECT item_id FROM armory_item'''
total = len(curr.execute(query).fetchall())
print(f'total items: {total}')

# How many are weapons? How many are not
query = '''SELECT item_ptr_id FROM armory_weapon'''
weapons = len(curr.execute(query).fetchall())
are_not = total - weapons
print(f'non-weapon items: {are_not}')

# How many items does each character have?
things = curr.execute('''SELECT name, COUNT(item_id) FROM charactercreator_character_inventory INNER JOIN 
                        charactercreator_character USING (character_id)
                        GROUP BY name 
                        ORDER BY name LIMIT 20;
                        ''')
for thing in things.fetchall():
    print(thing)
print()

another_things = curr.execute('''SELECT cc.name, COUNT(item_ptr_id) FROM charactercreator_character_inventory cci
                                LEFT JOIN  charactercreator_character cc on cc.character_id = cci.character_id
                                LEFT JOIN armory_item ai on cci.item_id = ai.item_id
                                LEFT JOIN  armory_weapon aw on ai.item_id = aw.item_ptr_id
                                GROUP BY cc.name
                                ORDER BY cc.character_id LIMIT 20''')
for thing in another_things.fetchall():
    print(thing)
