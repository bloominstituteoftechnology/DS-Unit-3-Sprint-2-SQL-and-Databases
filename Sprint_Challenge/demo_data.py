import sqlite3 

conn = sqlite3.connect('demo_data.sqlite3')

cur = conn.cursor()

drop_query = 'DROP TABLE IF EXISTS demo;'

table_query = '''CREATE TABLE demo( 
                s CHAR(1) PRIMARY KEY,
                x INT NOT NULL,
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

dbfile = 'demo_data.sqlite3'

def count(dbfile,query):
    c = sqlite3.connect(dbfile)
    curs = c.cursor()
    return curs.execute(query).fetchall()[0][0]

x = count(dbfile,'SELECT COUNT(*) FROM demo;')
print (f'Total number of rows in demo table is {x}\n')

y = count(dbfile,'SELECT COUNT(*) FROM demo WHERE x>=5 AND y>=5;')
print (f'number of rows in demo table where x and y are atleast 5 is {y}\n')

z = count(dbfile,'SELECT COUNT(DISTINCT y) FROM demo ')
print (f'Number of unique values in y is {z}\n')





