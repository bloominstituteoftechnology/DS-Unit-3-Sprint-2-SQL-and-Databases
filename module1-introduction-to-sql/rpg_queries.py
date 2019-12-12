"""
python SQL queries in atom
"""

import sqlite3
conn = sqlite33.connet('rpg_dbsqlite3')
import os
os.listdir()
conn
curs = conn.cursor()

# how many total Characters are there?
curs.execute('SELECT count(character_id) FROM charactercreator_character;').fetchall()

# how many of each specific subclass?
curs.excute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall()

curs.execute('SELECT count(character_ptr_id) FROM charactercreator_thief;').fetchall()

curs.execute('SELECT count(character_ptr_id) FROM charactercreator_cleric;').fetchall()

curs.execute('SELECT count(character_ptr_id) FROM charactercreator_fighter;').fetchall()

curs.execute('SELECT count(mage_ptr_id) FROM charactercreator_necromancer;').fetchall()

# how many total items?
curs.excute('SELECT count(item_id) FROM armory_item;').fetchall()

# how many of the items are weapons? how many are not?
curs.execute('SELECT count(item_id) FROM armory_item as ai, armory_weapon as aw WHERE ai.item_id = aw.item_ptr_id;')fetchall()

curs.excute('SELECT count(item_id) FROM armory_item WHERE item_id NOT IN(SELECT item_id FROM armory_weapon);').fetchall()

# how many weapons does each character have?  (return first 20 rows)
curs.execute('SELECT count(item_ptr_id) FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE ai.item_id = cci.item_id AND ai.item_id = aw.item_ptr_id group by character_id LIMIT 20;').fetchall()

# on average, how many items does each character have?
curs.execute('SELECT avg(count) FROM (SELECT count(item_id) as count FROM charactercreator_character_inventory as cci group by character_id);').fetchall()

# on average how many weapons does each character have?
curs.execute('SELECT avg(count) FROM (SELECT count(item_ptr_id) as count FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE ai.item_id = cci.item_id AND ai.item_id = aw.item_ptr_id group by character_id)').fetchall()

curs.close()
conn.commit()
