import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
create_demo_table = "CREATE TABLE demo (s VARCHAR(30),x INT,y INT);"
curs.execute(create_demo_table)

first_row = """
    INSERT INTO demo
    (s, x, y)
    VALUES ('g', 3, 9);
    """
second_row = """
    INSERT INTO demo
    (s, x, y)
    VALUES ('v', 5, 7);
    """
third_row = """
    INSERT INTO demo
    (s, x, y)
    VALUES ('f', 8, 7);
    """

rows = [first_row, second_row, third_row]
for row in rows:
    curs.execute(row)

conn.commit()

row_count = "SELECT COUNT(*) FROM demo"
row_num = curs.execute(row_count).fetchall()[0][0]
print('demo table has {} rows'.format(row_num))

# X and Y both > 5
query = "SELECT COUNT(*) FROM demo WHERE (x >= 5 AND y >= 5);"
response = curs.execute(query).fetchall()[0][0]
print(f'{response} rows exist with x and y values both at least 5')

# How many unique values of `y` are there?
query = "SELECT COUNT(DISTINCT y) FROM demo"
response = curs.execute(query).fetchall()[0][0]
print(f'There are {response} unique y values')