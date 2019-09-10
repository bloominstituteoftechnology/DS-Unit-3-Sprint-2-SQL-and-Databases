import pandas as pd
import sqlite3
from pandas import DataFrame 

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# doing it with a function 
def query_db(query, label_str, curs):
    results = curs.execute(query)
    print(label_str, results.fetchall()[0][0])
    
# e.g. how many total characters are there?
char_count_query = """
SELECT count(character_id)
FROM charactercreator_character AS cc"""
    
query_db(query=char_count_query, label_str='Total # of characters:', curs=curs)

# 1. How many total Characters are there? 302

# cursor to look at it, use it to execute queries
curs = conn.cursor()

# query
query1 = 'SELECT count(*) FROM charactercreator_character'

# execute, fetch
curs.execute(query1)
# print(curs.fetchall())


# 2. How many of each specific subclass?



# 3. How many total Items? 174
curs2 = conn.cursor()
query2 = 'SELECT count(*) FROM armory_item'
curs2.execute(query2)
# print(curs2.fetchall())
query_db(query=query2, label_str='Total items:', curs=curs2)

# 4. How many of the Items are weapons? 138 How many are not? 174 - 138
curs3 = conn.cursor()
query3 = 'SELECT item_ptr_id, count(*) FROM armory_weapon'
query_db(query=query3, label_str='Total weapons:', curs=curs3)

# 5. How many Items does each character have? (Return first 20 rows)
curs4 = conn.cursor()
query = '''SELECT count(item_id)
FROM charactercreator_character_inventory 
GROUP BY character_id
LIMIT 20'''
print('First 20 rows of items:', curs4.execute(query).fetchall())
# pd.read_sql(query, conn)

# 6. How many Weapons does each character have? (Return first 20 rows)
curs5 = conn.cursor()
query = '''SELECT character_id, count(a.item_id)
FROM charactercreator_character_inventory as a,
armory_item as b, 
armory_weapon as c
WHERE a.item_id = b.item_id
AND b.item_id = c.item_ptr_id
GROUP BY a.character_id
LIMIT 20'''
curs5.execute(query).fetchall()
pd.read_sql(query, conn)

# on average, how many weapons does each character have?

avg_weapons_per_char = """
SELECT avg(wc) 
FROM (SELECT cci.character_id, count(aw.item_ptr_id) AS wc
FROM charactercreator_character_inventory AS cci
    INNER JOIN armory_item AS ai on cci.item_id = ai.item_id
    LEFT JOIN armory_weapon AS aw ON ai.item_id = aw.item_ptr_id
GROUP BY cci.character_id)
"""

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# df = pd.read_sql(avg_weapons_per_char, conn)
# print(df)

# better way to print
query_db(query=avg_weapons_per_char, label_str='Avg. weapons per character:', curs=curs)









    