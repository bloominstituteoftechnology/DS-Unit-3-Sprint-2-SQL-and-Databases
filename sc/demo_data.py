import sqlite3
import pandas as pd

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_table_demo = """
    CREATE TABLE demo(
        s VARCHAR(24),
        x INT,
        y INT
    );
"""
cur.execute(create_table_demo)
conn.commit()

insert_into_demo = """
    INSERT INTO demo (s,x,y) VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
"""

cur.execute(insert_into_demo)
conn.commit()

def check_rows():
    print(pd.read_sql_query("""SELECT COUNT(*) as rows
                                FROM demo;""",conn))


def check_more_than_five():
print(pd.read_sql_query("""SELECT COUNT(*) as rows FROM demo
    WHERE x >= 5 AND y >= 5;""", conn))


def y_unique():
    print(pd.read_sql_query("""SELECT COUNT(DISTINCT y)unique_y_values
    FROM demo;""", conn))



















