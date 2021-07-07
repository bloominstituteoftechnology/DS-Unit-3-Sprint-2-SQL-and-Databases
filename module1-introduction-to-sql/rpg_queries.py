import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
r = conn.cursor()

q1 = r.execute('SELECT COUNT(distinct character_id) \
                FROM charactercreator_character').fetchone()[0]
thief_count = r.execute('SELECT COUNT(character_ptr_id) \
                from charactercreator_thief').fetchone()[0]
cleric_count = r.execute('SELECT COUNT(character_ptr_id) \
                from charactercreator_cleric').fetchone()[0]
mage_count = r.execute('SELECT COUNT(character_ptr_id) \
                from charactercreator_mage').fetchone()[0]
fighter_count = r.execute('SELECT COUNT(character_ptr_id) \
                from charactercreator_fighter').fetchone()[0]
necro_count = r.execute('SELECT COUNT(distinct mage_ptr_id) \
                from charactercreator_necromancer').fetchone()[0]

q2 = {'thief':thief_count, 'cleric':cleric_count, 'fighter':fighter_count,
        'mage':mage_count, 'necromancer': necro_count}
q3 = r.execute('SELECT COUNT(distinct item_id) from armory_item').fetchone()[0]
q4a = r.execute('SELECT COUNT(distinct item_ptr_id) \
                from armory_weapon').fetchone()[0]
q4b = q3 - q4a
q4 = (q4a, q4b)
first20_inv = r.execute('SELECT COUNT(id) \
                        FROM charactercreator_character_inventory \
                        GROUP BY character_id LIMIT 20').fetchall()
q5 = list(i[0] for i in first20_inv)
weapon_counts = r.execute('SELECT * FROM (SELECT count (item_id) \
                            FROM charactercreator_character_inventory \
                            INNER JOIN armory_weapon \
                            WHERE item_id = item_ptr_id \
                            GROUP BY character_id) \
                            LIMIT 20').fetchall()
q6 = list(i[0] for i in weapon_counts)

items, characters = r.execute('SELECT \
                               CAST(COUNT(charactercreator_character_inventory.item_id) AS FLOAT), \
                               CAST(COUNT(DISTINCT character_id) AS FLOAT) \
                               FROM \
                                charactercreator_character_inventory \
                                INNER JOIN \
                                armory_item \
                                ON armory_item.item_id = \
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
