import sqlite3

sl_conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')
sl_cur = sl_conn.cursor()

# Number of characters -- 302
print('Total number of characters:')
query = "SELECT COUNT(character_id) FROM charactercreator_character"
sl_characters_table = sl_cur.execute(query).fetchall()
print(sl_characters_table[0][0])

# Number of clerics
print('\nNumber of clerics:')
query = "SELECT COUNT(charactercreator_cleric.character_ptr_id) FROM charactercreator_cleric"
sl_clerics_table = sl_cur.execute(query).fetchall()
print(sl_clerics_table[0][0])

# Number of fighters
print('\nNumber of fighters:')
query = "SELECT COUNT(charactercreator_fighter.character_ptr_id) FROM charactercreator_fighter"
sl_fighters_table = sl_cur.execute(query).fetchall()
print(sl_fighters_table[0][0])

# Number of mages
print('\nNumber of mages:')
query = "SELECT COUNT(charactercreator_mage.character_ptr_id) FROM charactercreator_mage"
sl_mages_table = sl_cur.execute(query).fetchall()
print(sl_mages_table[0][0])

# Number of thieves
print('\nNumber of thieves:')
query = "SELECT COUNT(charactercreator_thief.character_ptr_id) FROM charactercreator_thief"
sl_thieves_table = sl_cur.execute(query).fetchall()
print(sl_thieves_table[0][0])

# Number of necromancers
print('\nNumber of necromancers:')
query = "SELECT COUNT(charactercreator_necromancer.mage_ptr_id) FROM charactercreator_necromancer"
sl_necromancers_table = sl_cur.execute(query).fetchall()
print(sl_necromancers_table[0][0])

# Total number of items
print('\nTotal number of items:')
query = "SELECT COUNT(item_id) FROM armory_item"
sl_items_table = sl_cur.execute(query).fetchall()
print(sl_items_table[0][0])

# Number of weapons
print('\nNumber of weapons:')
query = "SELECT COUNT(item_ptr_id) FROM armory_weapon"
sl_weapons_table = sl_cur.execute(query).fetchall()
print(sl_weapons_table[0][0])

# Number of items that aren't weapons
# print("\nNumber of items that aren't weapons:")
# query = ""
# sl_nonweapons_table = sl_cur.execute(query).fetchall()
# print(sl_nonweapons_table[0][0])
