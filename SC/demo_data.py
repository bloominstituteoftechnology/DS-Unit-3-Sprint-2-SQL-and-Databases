'''
This module solves the first section of the sprint challenge:
I create and populate a database.
'''
import sqlite3


def answer_query(query, conn, curs):
    """
    This function prints the value of a query from a database.
    """
    results = conn.execute(query)
    results = results.fetchall()[0][0]
    print(results)


print("PART 1:")

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

conn.execute("DROP TABLE IF EXISTS demo")

create_query = """ CREATE TABLE demo(
s CHAR(1),
x INT,
y INT
);
"""
conn.execute(create_query)
conn.commit()

insert_query = """
INSERT INTO demo (s, x, y)
VALUES
('g', 3, 9),
('v', 5, 7),
('g', 8, 7);
"""
conn.execute(insert_query)
conn.commit()

test_query_1 = """
SELECT COUNT(*)
FROM demo
"""
answer_query(test_query_1, conn, curs)

test_query_2 = """
SELECT COUNT(*)
FROM demo
WHERE (x >= 5) AND (y >= 5)
"""
answer_query(test_query_2, conn, curs)

test_query_3 = """
SELECT COUNT(DISTINCT y)
FROM demo
"""
answer_query(test_query_2, conn, curs)
