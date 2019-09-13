import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

c = conn.cursor()

c.execute('DROP TABLE demo')

query = '''
        CREATE TABLE
            demo (
                s VARCHAR,
                x int,
                y int
            )
        '''

c.execute(query)

query = '''
        INSERT INTO
            demo
                (s, x, y)
            VALUES
                ('g',3,9),
                ('v',5,7),
                ('f',8,7)
        '''

c.execute(query)

query = 'SELECT * FROM demo'
c.execute(query)
print(f'New Table Created: {c.fetchall()}')

conn.commit()

##### COUNT ROWS #####
query = 'SELECT COUNT(s) FROM demo'
c.execute(query)
print(f'Total Rows: {c.fetchone()[0]}')

##### COUNT ROWS WHERE > 5 #####
query = '''
        SELECT
            COUNT(*)
        FROM
            demo
        WHERE
            x >= 5
                and
            y >= 5
        '''
c.execute(query)
print(f'Rows > 5: {c.fetchone()[0]}')

##### UNIQUE Y VALUES #####
query = '''
        SELECT
            COUNT(DISTINCT(y))
        FROM
            demo
        '''
c.execute(query)
print(f'Unique Y Values: {c.fetchone()[0]}')

conn.close()