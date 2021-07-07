import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
create_demo_table = '''
CREATE TABLE demo (
    s char(1),
    x int,
    y int
)'''
curs.execute(create_demo_table)
results = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
for result in results:
    insert_result = """INSERT INTO demo
    (s, x, y)
    VALUES""" + str(result[:])
    curs.execute(insert_result)
conn.commit()

curs = conn.cursor()
count_query = '''SELECT count(*) FROM demo'''
curs.execute(count_query)
print('Number of rows:', curs.fetchall()[0][0])

query = '''SELECT count(*) FROM demo
WHERE x >= 5 and y >= 5'''
curs.execute(query)
print('Number of rows where both `x` and `y` are at least 5:', curs.fetchall()[0][0])

query = '''SELECT count(DISTINCT y) FROM demo'''
curs.execute(query)
print('Number of unique values of `y`:', curs.fetchall()[0][0])
