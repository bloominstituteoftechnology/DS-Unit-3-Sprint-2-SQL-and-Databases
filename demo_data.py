import sqlite3

sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_cur = sl_conn.cursor()

# Creating table demo
table = """
    CREATE TABLE demo(
        s VARCHAR (10),
        x INT,
        y INT
    );
"""
sl_cur.execute(table)

# Checking for table creation accuracy
sl_cur.execute('PRAGMA table_info(demo);').fetchall()

demo_insert = """
    INSERT INTO demo (s, x, y) 
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
sl_cur.execute(demo_insert)
sl_cur.execute('SELECT * FROM demo').fetchall()
sl_cur.close()
sl_conn.commit()

# Testing demo file
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_cur = sl_conn.cursor()

sl_cur.execute('SELECT COUNT(*) FROM demo').fetchall()
sl_cur.execute("""
    SELECT * 
    FROM demo
    WHERE x >= 5 
    AND y >= 5;
"""
).fetchall() 

sl_cur.execute("""
    SELECT COUNT(DISTINCT y) 
    FROM demo
"""
).fetchall()
sl_cur.close()