import sqlite3
from collections import Counter

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total characters are there?
q = 'SELECT count(*) FROM charactercreator_character;'
print('Total characters:', curs.execute(q).fetchall())

# How many of each specific subclass?
classes = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
full = ['charactercreator_' + i for i in classes]
q = [curs.execute('SELECT count(*) FROM ' + i).fetchall() for i in full]
print('Cleric, fighter, mage, necromancer, thief counts:\n', q)

# How many total items?
q = 'SELECT count(*) FROM armory_item;'
print('Total items:', curs.execute(q).fetchall())

# How many of the items are weapons, how many are not?
# Get item and weapon ids
q1 = 'SELECT item_id FROM armory_item'
q2 = 'SELECT item_ptr_id FROM armory_weapon'
id_i = [curs.execute(q1).fetchall()]
id_i = [y for x in id_i for y in x]
id_i = list(sum(id_i, ()))
id_w = [curs.execute(q2).fetchall()]
id_w = [y for x in id_w for y in x]
id_w = list(sum(id_w, ()))
intersection = set(id_i) & set(id_w)
print('Number of items that are weapons:', len(intersection))
print('Number of items that are not weapons', len(id_i) - len(id_w))

# How many items does each character have?
q = 'SELECT character_id FROM charactercreator_character_inventory'
char_ids = curs.execute(q).fetchall()
char_ids = list(sum(char_ids, ()))
n_items = list(Counter(char_ids).values())
print('Number of items of the first 20 characters:', n_items[:20])

# How many weapons does each character have, but lets do acutal SQL this time?
# In other words: how many armory weapon ids are in the character iventory?
q = """
SELECT character.name, item.item_id
FROM charactercreator_character AS character,
armory_item AS item,
charactercreator_character_inventory AS inventory
WHERE character.character_id = inventory.character_id
AND item.item_id = inventory.item_id;"""
char_w = curs.execute(q).fetchall()
char_w = list(sum(char_w, ()))
print('First 20 characters, num items:\n', char_w[:40])

# On average, how many items does each character have?
print('Average number of items for a character to have:',
      round(sum(n_items) / len(n_items)))

# On average, how many weapons does each character have?
q = 'SELECT item_id FROM charactercreator_character_inventory;'
item_id = curs.execute(q).fetchall()
weapon_ids = [i for i in list(sum(item_id, ())) if i >= 138] # armory ids start with 138
n_weapons = list(Counter(char_ids).values())
print('Average number of weapons for a character to have:',
      round(sum(n_weapons) / len(n_weapons)))
