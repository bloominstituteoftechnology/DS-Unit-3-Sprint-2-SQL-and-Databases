import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_table = '''
    CREATE TABLE demo (
        s TEXT,
        x INT,
        y INT
);
'''
curs.execute(create_table)

data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

for datum in  data:
    insert_data = '''
        INSERT INTO demo (s, x, y)
        VALUES ''' + str(datum[:]) + ';'
    curs.execute(insert_data)

conn.commit()

query = '''
    SELECT s 
    FROM demo
    WHERE x >= 5 AND y >=5;
    '''
curs.execute(query)
print('Rows with x,y >=5:', curs.fetchall())

query = '''
    SELECT COUNT(DISTINCT(y))
    FROM DEMO
    '''
curs.execute(query)
print('Number of unique values in y:', curs.fetchall())

