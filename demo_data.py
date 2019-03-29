import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

drop_query = 'DROP TABLE IF EXISTS demo'
initialize_query = """CREATE TABLE demo(
    s string,
    x int,
    y int
);"""

conn.cursor().execute(drop_query)
conn.cursor().execute(initialize_query)

insert_query = """INSERT INTO demo VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);"""

conn.cursor().execute(insert_query)

conn.commit()

count_query = 'SELECT COUNT(s) FROM demo'

row_count = conn.cursor().execute(count_query).fetchone()[0]
print('there are %s rows in demo data' % row_count)

greater_than_query = """SELECT COUNT(s) FROM demo
                        WHERE x >= 5 AND y >=5;"""
greater_than_ans = conn.cursor().execute(greater_than_query).fetchone()[0]
print('there are %s rows in demo data where both x and y are at least 5.' % greater_than_ans)

unique_y_query = """SELECT COUNT(DISTINCT(y)) FROM demo"""
unique_y_ans = conn.cursor().execute(unique_y_query).fetchone()[0]
print('there are %s unique y values' % unique_y_ans)