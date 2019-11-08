import sqlite3

""" Establish connection and create a cursor. """
CONN = sqlite3.connect('demo_data.sqlite3')
cursor = CONN.cursor()

""" Delete table if exists created anticipating file being
run multiple times.
"""

delete_table = "DROP TABLE IF EXISTS demo"
cursor.execute(delete_table)

create_demo_table = """
                    CREATE TABLE demo(
                        's' TEXT,
                        'x' INT,
                        'y' INT
                    )
                    """
cursor.execute(create_demo_table)

insert_info = """
            INSERT INTO demo(s, x, y)
            VALUES
            ("g", 3, 9),
            ("v", 5, 7),
            ("f", 8, 7);
            """
cursor.execute(insert_info)

cursor.close()
CONN.commit()

cursor_2 = CONN.cursor()

"""First query: how many rows are there?"""
query_1 = 'SELECT COUNT (*) FROM demo;'
rows = cursor_2.execute(query_1).fetchone()
rows = str(rows).strip('(),')
print(f'The demo table has {rows} rows.')

"""Second query: How many rows are there
where both 'x' and 'y' are at least 5?
"""

query_2 = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;'

five = cursor_2.execute(query_2).fetchone()
five = str(five).strip('(),')
print(f"There are {five} rows where 'x' and 'y' are at least five.")

"""Third query: How many unique values of 'y' are there?"""
query_3 = 'SELECT COUNT(DISTINCT y) FROM demo;'
unique_y = cursor_2.execute(query_3).fetchall()
unique_y = str(unique_y).strip('[](),')
print(f"There are {unique_y} unique values for 'y'.")
