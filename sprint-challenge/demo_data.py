import sqlite3


#opening connection
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

#Creating table
table = """
    CREATE TABLE demo(
        s VARCHAR (10),
        x INT,
        y INT
    );
"""

cur.execute('DROP TABLE demo')
cur.execute(table)

demo_insert = """
    INSERT INTO demo (s, x, y) 
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
cur.execute(demo_insert)
cur.close()
conn.commit()

#Count how many rows you have
cur.execute('SELECT COUNT(*) FROM demo')
answer = cur.fetchall()
print(f'There are {answer} rows.\n')

#How many rows are there where both 'x' and 'y' are at least 5?
cur.execute("""
    SELECT COUNT(*) 
    FROM demo
    WHERE x >= 5 
    AND y >= 5;
""")
answer = cur.fetchall()
print(f'There are {answer} rows with values of at least 5.\n')

#How many unique values of y are there?
cur.execute("""
    SELECT COUNT(DISTINCT y) 
    FROM demo
""")
answer = cur.fetchall()
print(f"There are {answer} unique values of 'y'.")

#Closing connection and committing
cur.close()
conn.commit()