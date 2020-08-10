import sqlite3


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# How many total characters are there?
# 302
query = 'SELECT COUNT(*) FROM charactercreator_character'
curs.execute(query)
results = curs.fetchall()
print(results)

# How many of each specific subclass?
# Cleric = 75
# Fighter = 68
# Mage = 108
# Thief = 51
# Necromancer = 11
# The 11 Necromancers also fall under Mage
query2_c = 'SELECT COUNT(*) FROM charactercreator_cleric'
query2_f = 'SELECT COUNT(*) FROM charactercreator_fighter'
query2_m = 'SELECT COUNT(*) FROM charactercreator_mage'
query2_t = 'SELECT COUNT(*) FROM charctercreator_thief'
query2_n = 'SELECT COUNT(*) FROM charctercreator_necromancer'

# Cleric
curs.execute(query2_c)
results2_c = curs.fetchall()
print(results2_c)

# Fighter
curs.execute(query2_f)
results2_f = curs.fetchall()
print(results2_f)

# Mage
curs.execute(query2_m)
results2_m = curs.fetchall()
print(results2_m)

# Thief
curs.execute(query2_t)
results2_t = curs.fetchall()
print(results2_t)

# Necromancer
curs.execute(query2_n)
results2_n = curs.fetchall()
print(results2_n)

# How many total Items?
# 174
query3 = 'SELECT COUNT(*) FROM armory_item'
curs.execute(query3)
results3 = curs.fetchall()
print(results3)

# How many of the items are weapons?
# 37
query4 = 'SELECT COUNT(*) FROM armory_weapon'
curs.execute(query4)
results4 = curs.fetchall()
print(results4)
# How many are not
# 137
print(174-37)

# How many items does each character have (First 20 Rows)
# Still needs work
query5 = 'SELECT * FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
curs.execute(query5)
results5 = curs.fetchall()
print(results5)