import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()
"""
Q: How many total Characters are there?
A: 302
"""
q_1 = 'SELECT COUNT(*) FROM charactercreator_character AS cc;'
results = curs.execute(q_1)
results.fetchall()

"""
Q: How many of each specific subclass?
A: Mage = 108
Thief = 51
Cleric = 75
Fighter = 68
"""

q_2 = 'SELECT COUNT(*) FROM charactercreator_mage AS cm, charactercreator_character AS cc WHERE cc.character_id = cm.character_ptr_id;'
results = curs.execute(q_2)
results.fetchall()

q_3 = 'SELECT COUNT(*) FROM charactercreator_thief AS ct, charactercreator_character AS cc WHERE cc.character_id = ct.character_ptr_id;'
results = curs.execute(q_3)
results.fetchall()

q_4 = 'SELECT COUNT(*) FROM charactercreator_cleric AS ccl, charactercreator_character AS cc WHERE cc.character_id = ccl.character_ptr_id;'
results = curs.execute(q_4)
results.fetchall()

q_5 = 'SELECT COUNT(*) FROM charactercreator_fighter AS cf, charactercreator_character AS cc WHERE cc.character_id = cf.character_ptr_id;'
results = curs.execute(q_5)
results.fetchall()

"""
Q: How many total Items?
A: 174
"""
q_6 = 'SELECT COUNT(*) FROM armory_item;'
results = curs.execute(q_6)
results.fetchall()

"""
Q: How many of the Items are weapons? How many are not?
A: Weapons = 37
Not weapons = 174 - 37 = 137
"""
q_7 = 'SELECT COUNT(*) FROM armory_weapon AS aw, armory_item AS ai WHERE ai.item_id = aw.item_ptr_id;'
results = curs.execute(q_7)
results.fetchall()

"""
Q: How many Items does each character have? (Return first 20 rows)
A:
"""
