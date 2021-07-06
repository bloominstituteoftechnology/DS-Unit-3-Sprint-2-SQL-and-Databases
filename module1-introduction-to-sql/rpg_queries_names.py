import sqlite3

conn = sqlite3.connect('./rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?
mult_name_query = """
SELECT name FROM charactercreator_character
GROUP BY name
HAVING COUNT(name) > 1;
"""
mult_name = curs.execute(mult_name_query).fetchall()
print(f'\nThe character names with more than one character: {mult_name}.\n')


# names_query = """
# SELECT name FROM charactercreator_character
# ORDER BY name;
# """
# names = curs.execute(names_query).fetchall()

# for name in names:
#     print(name[0])


curs.close()
conn.close()
