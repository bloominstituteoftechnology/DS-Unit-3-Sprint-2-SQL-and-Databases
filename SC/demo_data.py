import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS demo (
        s VARCHAR(255) PRIMARY KEY,
        x INT,
        y INT
    );
'''

insert_g = """
    INSERT INTO demo
    VALUES ('g', 3, 9);
"""
insert_v = """
    INSERT INTO demo
    VALUES ('v', 5, 7);
"""

insert_f = """
    INSERT INTO demo
    VALUES ('f', 8, 7);
"""

curs.execute(create_table)
curs.execute(insert_g)
curs.execute(insert_v)
curs.execute(insert_f)

# CHECK TO SEE IF ALL WORKED WELL
query = '''
    SELECT * FROM demo;
'''
curs.execute(query)
print(curs.fetchall())

# COUNT THE ROWS
curs = conn.cursor()
query = '''
    SELECT COUNT(*) FROM demo;
'''
curs.execute(query)
print(f'There are {curs.fetchall()[0][0]} rows')

# NUMBER OF ROWS WHERE X AND Y ARE GREATER THAN OR EQUAL TO 5
curs = conn.cursor()
query = '''
    SELECT COUNT(*) FROM demo
    WHERE x >= 5 AND y >= 5;
'''
curs.execute(query)
print(f'There are {curs.fetchall()[0][0]} rows that have x and y at least 5')

# HOW MANY UNIQUE Y'S ARE THERE?
curs = conn.cursor()
query = '''
    SELECT COUNT(DISTINCT y) FROM demo;
'''
curs.execute(query)
print(f'There are {curs.fetchall()[0][0]} unique y values')

curs.close()
conn.commit()