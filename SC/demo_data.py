import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")

curs = conn.cursor()

create_demo_table = """
    CREATE TABLE demo (
        s TEXT,
        x INT,
        y INT
    );
"""
curs.execute(create_demo_table)

insert_row = """
    INSERT INTO demo (s, x, y)
    VALUES ('g', 3, 9);"""
curs.execute(insert_row)

insert_row = """
    INSERT INTO demo (s, x, y)
    VALUES ('v', 5, 7);"""
curs.execute(insert_row)

insert_row = """
    INSERT INTO demo (s, x, y)
    VALUES ('f', 8, 7);"""
curs.execute(insert_row)

conn.commit()

query = """
    SELECT COUNT(*)
    FROM demo;"""
row_count = curs.execute(query).fetchall()[0][0]

query = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >=5;"""
x_and_y_at_least_5_count = curs.execute(query).fetchall()[0][0]

query = """
    SELECT COUNT(DISTINCT y)
    FROM demo;"""
unique_y_count = curs.execute(query).fetchall()[0][0]

curs.close()

print("Number of rows:", row_count,
      "\nNumber of rows where both x and y are at least 5:",
      x_and_y_at_least_5_count,
      "\nNumber of unique y values:", unique_y_count)

# Output:
# Number of rows: 3
# Number of rows where both x and y are at least 5: 2
# Number of unique y values: 2
