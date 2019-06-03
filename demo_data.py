import sqlite3
connect = sqlite3.connect('demo_data.sqlite3')
cursor = connect.cursor()

create_table ="""
CREATE TABLE demo (
    s string,
    x int,
    y int);"""

connect.cursor().execute(create_table)

type(create_table)
insert_demo = """INSERT INTO demo VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7);"""
connect.cursor().execute(insert_demo)

connect.commit()

row_counter = "SELECT COUNT(s) FROM demo"
total_rows = cursor.execute(row_counter).fetchone()[0]

#Total Rows
print(total_rows)

greater_than_5 = """
SELECT COUNT(s) FROM demo WHERE x >= 5 AND y >= 5
;"""
row_counter_2 = cursor.execute(greater_than_5).fetchone()[0]

#Rows where both x and y are greater than or equal to 5
print(row_counter_2)

unique_y = 'SELECT COUNT (DISTINCT y) from demo'
unique_y = cursor.execute(unique_y).fetchone()[0]

#Number of unique values of y
print(unique_y)