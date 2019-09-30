import sqlite3 

conn = sqlite3.connect('Sprint_Challenge/demo_data.sqlite3')

cur = conn.cursor()

drop_query = 'DROP TABLE IF EXISTS demo;'

table_query = '''CREATE TABLE demo( 
                s CHAR(1) PRIMARY KEY
                x INT NOT NULL
                y INT NOT NULL);'''

insert_query = """INSERT INTO demo VALUES(?, ?, ?);"""

values = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

print('Dropping table demo if it exists\n')
conn.execute(drop_query)
print('Creating demo table....\n')
conn.execute(table_query)
print('Populating demo table with values....\n')
conn.executemany(insert_query,values)

conn.commit()

dbfile = 'Sprint_Challenge/demo_data.sqlite3'

def count(dbfile,query):
    c = sqlite3.connect(dbfile)
    curs = c.cursor()
    return curs.execute(query).fetchall()[0][0]




