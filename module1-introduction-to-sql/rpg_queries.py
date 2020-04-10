import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query_q1 = "SELECT count(character_id) from charactercreator_character;"
query_q2_cleric = "SELECT count(character_ptr_id) FROM charactercreator_cleric"
query_q2_fighter = "SELECT count(character_ptr_id) FROM charactercreator_fighter"
query_q2_mage = "SELECT count(character_ptr_id) FROM charactercreator_mage"
query_q2_necromancer = "SELECT count(mage_ptr_id) FROM charactercreator_necromancer"
query_q2_thief = "SELECT count(character_ptr_id) FROM charactercreator_thief"
query_q3 = "SELECT count(item_id) FROM armory_item"
query_q4 = 'SELECT count(item_ptr_id) FROM armory_weapon'


#########################################################################################

results_q1 = curs.execute(query_q1).fetchall()
print("RESULTS_Q1", results_q1)

results_q2_cleric = curs.execute(query_q2_cleric).fetchall()
print("RESULTS_Q2_CLERIC", results_q2_cleric)

results_q2_fighter = curs.execute(query_q2_fighter).fetchall()
print("RESULTS_Q2_FIGHTER", results_q2_fighter)

results_q2_mage = curs.execute(query_q2_mage).fetchall()
print("RESULTS_Q2_MAGE", results_q2_mage)

results_q2_necromancer = curs.execute(query_q2_necromancer).fetchall()
print("RESULTS_Q2_NECROMANCER", results_q2_necromancer)

results_q2_thief = curs.execute(query_q2_thief).fetchall()
print("RESULTS_Q2_THIEF", results_q2_thief)

results_q3 = curs.execute(query_q3).fetchall()
print("RESULTS_Q3", results_q3)

results_q4 = curs.execute(query_q4).fetchall()
print("RESULTS_Q4", results_q4)

########################################################################################