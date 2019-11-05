import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
r = conn.cursor()

# How many total characters are there?
q1 = r.execute('''SELECT COUNT(distinct character_id)
                FROM charactercreator_character''').fetchone()[0]

#How many of each specific subclass?
thief_count = r.execute('SELECT COUNT(character_ptr_id) \
                FROM charactercreator_thief').fetchone()[0]

mage_count = r.execute('SELECT COUNT(character_ptr_id) \
                FROM charactercreator_mage').fetchone()[0]

cleric_count = r.execute('SELECT COUNT(character_ptr_id) \
                FROM charactercreator_cleric').fetchone()[0]

fighter_count = r.execute('SELECT COUNT(character_ptr_id) \
                FROM charactercreator_fighter').fetchone()[0]

necro_count = r.execute('SELECT COUNT(mage_ptr_id) \
                FROM charactercreator_necromancer').fetchone()[0]

q2 = {'Thief':thief_count, 'Mage':mage_count, 'Cleric':cleric_count,
      'Fighter':fighter_count, 'Necromancer':necro_count}

q3 = r.execute('''SELECT COUNT(item_id) FROM armory_item ''').fetchone()[0]

q4a = r.execute('''SELECT COUNT(item_ptr_id) from armory_weapon''').fetchone()[0]

q4b = q3 - q4a

q4 = (q4a, q4b)
