import pandas as pd
import sqlite3


dbfile = 'rpg_db.sqlite3'
'''
query = 'SELECT COUNT(*) FROM charactercreator_character;'
print (f'Total character count is {curs.execute(query).fetchall()[0][0]}')
'''
def count(dbfile,query):
    c = sqlite3.connect(dbfile)
    curs = c.cursor()
    return curs.execute(query).fetchall()[0][0]

x = count(dbfile,'SELECT COUNT(*) FROM charactercreator_character;')
print (f'Total character count is {x}\n')
#print (f'Total character count is {count(dbfile,'SELECT COUNT(*) FROM charactercreator_character')}')

y = count(dbfile,'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;')
print (f'Total Cleric character count is {y}\n')

z = count(dbfile,'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;')
print (f'Total fighter character count is {z}\n')

a = count(dbfile,'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;')
b = count(dbfile,'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;')
print (f'Total mage character count is {a+b}\n')

d = count(dbfile,'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;')
print (f'Total thief character count is {d} \n')

i = count(dbfile,'SELECT COUNT(item_id) FROM armory_item;')
print (f'Total item count is {i} \n')

w = count(dbfile,'SELECT COUNT(item_ptr_id) FROM armory_weapon;')
print (f'Total weapon count is {w}')

print (f'Total non-weapon item count is {i-w} \n')

query = '''SELECT character_id , COUNT(item_id) as 'Item Count'
FROM charactercreator_character_inventory 
GROUP BY character_id 
LIMIT 20'''

conn = sqlite3.connect(dbfile)
df = pd.read_sql(query, conn)
print(f'Below is table of first 20 character item count \n {df}')

query2 = ('''SELECT character_id, COUNT(item_id) as 'weapon count'
FROM charactercreator_character_inventory
WHERE item_id in 
    (SELECT DISTINCT item_ptr_id FROM armory_weapon)
GROUP BY character_id
LIMIT 20;''')

df2 = pd.read_sql(query2, conn)
print(f'Below is table of first 20 character weapon count \n {df2}')

query3 = """SELECT AVG(items) 
                    FROM (
                        SELECT character_id, count(item_id) as items
                        FROM charactercreator_character_inventory
                        GROUP BY character_id);"""

print(f'On average each character has this number of items {pd.read_sql(query3, conn)}')

query4 = """SELECT AVG(items) 
                    FROM (  
                        SELECT character_id, COUNT(item_id) as items
                        FROM charactercreator_character_inventory
                        WHERE item_id IN 
                                (SELECT DISTINCT item_ptr_id FROM armory_weapon)
                        GROUP BY character_id);"""

print(f'On average each character has this number of weapons {pd.read_sql(query4, conn)}')




