# hi

import sqlite3

# Create db

conn = sqlite3.connect("demo_data.sqlite3")
print('CONNECTION:', conn)
curs = conn.cursor()
print('CURSOR:', curs)

demo_table_creation_query = """
            CREATE TABLE IF NOT EXISTS demo(
            s TEXT,
            x INT,
            y INT
            );
"""
curs.execute(demo_table_creation_query)

# Test if table creation worked
curs.execute('SELECT * from demo;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result2 = curs.fetchall()
print('DEMO TABLE EXISTS? (test): ', len(result2))

#breakpoint()   <-- WORKS TO HERE

# Add table to db
if len(result2) ==0:
    data_insertion = """
            INSERT INTO demo(s, x, y)
            VALUES ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7);
    """
    curs.execute(data_insertion)

    curs.execute('SELECT * FROM demo;')
    result2 = curs.fetchall()
    print('DEMO TABLE EXISTS? (test): ', len(result2))

conn.commit()
# breakpoint() <-- still good


curs.execute("""
            SELECT 
            *
            FROM demo
            WHERE x >= 5
            AND y >= 5;""")
result2 = curs.fetchall()
print('Number of rows where x, y both at least 5: ', len(result2))

curs.execute("""
            SELECT 
            COUNT(DISTINCT y)
            FROM demo
            ;""")
result2 = curs.fetchall()
print('Number of unique y values: ', result2[0])


# curs.execute("""SELECT * from demo""")
# result2 = curs.fetchall()
# print('Number of rows in demo: ', len(result2))


###### Evidence's block #######
#
# data2 = """
#         INSERT INTO test(name, age)
#         VALUES ("Evidence", 22),
#         ("Destiny", 30)
# """
# curs.execute(data2).fetchall()
# curs.close()
# conn.commit()

# curs.execute("""
#             SELECT 
#             AVG(age)
#             FROM test
#             where grade >= 4.0""").fetchall()
