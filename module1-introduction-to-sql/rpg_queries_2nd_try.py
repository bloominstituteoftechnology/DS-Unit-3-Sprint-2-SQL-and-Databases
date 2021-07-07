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

each_inv = r.execute('SELECT COUNT(id) \
                      FROM charactercreator_character_inventory \
                      GROUP BY character_id LIMIT 20').fetchall()
q5 = list(i[0] for i in each_inv)

weapon_counts = r.execute('SELECT * FROM (SELECT count (item_id) \
                            FROM charactercreator_character_inventory \
                            INNER JOIN armory_weapon \
                            WHERE item_id = item_ptr_id \
                            GROUP BY character_id) \
                            LIMIT 20').fetchall()

q6 = list(i[0] for i in weapon_counts)

items, characters = r.execute('SELECT \
                               CAST(COUNT(charactercreator_character_inventory.item_id) as FLOAT), \
                               CAST(COUNT(DISTINCT character_id) AS FLOAT) \
                               FROM \
                               charactercreator_character_inventory \
                               INNER JOIN \
                               armory_item \
                               on armory_item.item_id = \
                               charactercreator_character_inventory.item_id').fetchone()

q7 = items / characters

q8 = r.execute('SELECT \
                COUNT(charactercreator_character_inventory.item_id) \
                FROM \
                charactercreator_character_inventory INNER JOIN armory_weapon \
                ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id').fetchone()[0] / characters

answers = [q1, q2, q3, q4, q5, q6, q7, q8]

questions = ['How many total Characters are there?',
'How many of each specific subclass?',
'How many total Items?',
'How many of the Items are weapons? How many are not?',
'How many Items does each character have? (Return first 20 rows)',
'How many Weapons does each character have? (Return first 20 rows)',
'On average, how many Items does each Character have?',
'On average, how many Weapons does each character have?']

for i, j in zip(answers, questions):
    print(j, i)
