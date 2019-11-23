# imports
import sqlite3

# open connection and cursor
demo_conn = sqlite3.connect('demo_data.sqlite3')
demo_cur = demo_conn.cursor()

# table creation command
create_demo_table = """
CREATE TABLE demo(
    s VARCHAR(1) PRIMARY KEY,
    x INT,
    y INT);
"""

# table insertion command
insert_into_demo = """
INSERT INTO demo (s, x, y) VALUES 
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""

# execute table creation
demo_cur.execute(create_demo_table)
demo_conn.commit()

# execute table insertion
demo_cur.execute(insert_into_demo)
demo_conn.commit()

def row_count():
    '''count the rows in the demo table. returns 3'''
    demo_cur.execute("""SELECT COUNT(*) FROM demo;""")
    return demo_cur.fetchall()


def row_count_greater_5():
    '''count the number of rows where both entries are >=5. returns 2.'''
    demo_cur.execute("""SELECT COUNT(*) FROM demo WHERE (x >= 5) AND (y >= 5);""")
    return demo_cur.fetchall()


def count_distinct_y():
    '''count the number of rows with unique y values. returns 2.'''
    demo_cur.execute("""SELECT COUNT(DISTINCT(y)) FROM demo;""")
    return demo_cur.fetchall()

print(row_count())
print(row_count_greater_5())
print(count_distinct_y())
