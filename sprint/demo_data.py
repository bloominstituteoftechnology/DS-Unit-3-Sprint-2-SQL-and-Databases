import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

def create_table():
    cur.execute('''CREATE TABLE demo
    (s varchar(10),
    x INT NOT NULL,
    y INT NOT NULL);
    ''')
    return

def insert_rows():
    cur.execute('''INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)''')
    cur.execute('''INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)''')
    cur.execute('''INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)''')
    conn.commit()
    return

def querydb(query):
    cur.execute(query)
    results = cur.fetchall()
    return results

# Questions
'''Count how many rows you have - it should be 3!
How many rows are there where both x and y are at least 5?
How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?'''

if __name__ == '__main__':
    q1 = '''SELECT COUNT(s) FROM demo'''
    print(f'The count of rows is {querydb(q1)[0][0]} \n')
    

    q2 = '''SELECT COUNT(s) FROM demo WHERE demo.x >= 5'''
    print(f'Rows when x and y are both at least 5 is {querydb(q2)[0][0]} \n')
    

    q3 = '''SELECT COUNT(DISTINCT(y)) FROM demo'''
    print(f'The unique values of y are {querydb(q3)[0][0]} \n')
    

    cur.close()
    conn.close()