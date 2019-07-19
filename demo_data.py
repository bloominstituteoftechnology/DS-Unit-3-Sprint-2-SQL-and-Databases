import numpy as np
import pandas as pd
def main():
    import sqlite3

    conn = sqlite3.connect('demo_data.sqlite3') # Open connection to local DB
    c = conn.cursor() # Reference to cursor
    c.execute('''DROP TABLE demo;''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS demo (
        s Varchar,
        x Int,
        y Int
    );
    ''')
    c.execute('''INSERT INTO demo VALUES('g', 3, 9);''')
    c.execute('''INSERT INTO demo VALUES('v', 5, 7);''')
    c.execute('''INSERT INTO demo VALUES('f', 8, 7);''')

    demo = pd.read_sql_query("SELECT * FROM demo", conn)
    print(demo.shape)
    print(list(c.execute('''SELECT COUNT(*) FROM demo WHERE x >=5 AND y >= 5;''')))
    print(list(c.execute('''SELECT DISTINCT COUNT(y) FROM demo;'''))) 

    conn.commit()

if __name__ == "__main__":
    main()
