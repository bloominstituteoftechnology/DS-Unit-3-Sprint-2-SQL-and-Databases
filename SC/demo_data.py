import sqlite3

# create connection
sl_conn = sqlite3.connect('/Users/Elizabeth/sql/demo_data.sqlite3')
sl_curs = sl_conn.cursor()

# create table schema
create_table = """
        CREATE TABLE demo (
        s VARCHAR(1),
        x INT,
        y INT
        );
        """
# sl_curs.execute(create_table)

# data
demo_data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]


# # # insert data
# for data in demo_data:
#     demo_insert = """
#             INSERT INTO demo (
#             s, x, y)
#             VALUES """ + str(data) + ';'
#     sl_curs.execute(demo_insert)

# # commit data
# sl_curs.close()
# sl_conn.commit()


# sl_curs = sl_conn.cursor()

# # Check how many rows
# query = """
#         SELECT COUNT(*) FROM demo;"""
# answer = sl_curs.execute(query).fetchall()[0][0]
# print('There are {} rows'.format(answer))
#
# # How many rows are there where both x and y are at least 5?
# query = """
#         SELECT COUNT(*) FROM demo
#         WHERE x>=5 AND y>=5;"""
# answer = sl_curs.execute(query).fetchall()[0][0]
# print('There are {} rows where x and y are at least 5'.format(answer))

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
query = """
        SELECT COUNT(DISTINCT y) FROM demo;
        """
answer = sl_curs.execute(query).fetchall()[0][0]
print('There are {} distinct values of y'.format(answer))



test = sl_curs.execute('SELECT * FROM demo;').fetchall()
# test = sl_curs.execute('PRAGMA table_info(demo);').fetchall()
print(test)
