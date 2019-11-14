import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

# Total characters
print('How many total Characters are there?')
cur.execute('SELECT * FROM charactercreator_character')
print('SELECT * FROM charactercreator_character')
cur.fetchall()

# # Total of each subclass
# print('How many of each specific subclass?')
# cur.execute('')
# print('')
# cur.fetchall()



