import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

statement1 = """
CREATE TABLE demo (
    s VARCHAR(1),
    x INT,
    y INT
)
"""

cur.execute(statement1)
conn.commit()

statement2 = """
    INSERT INTO demo VALUES (
    'g', 3, 9
)
"""

cur.execute(statement2)
conn.commit()

statement3 = """
    INSERT INTO demo VALUES (
    'v', 5, 7
)
"""

cur.execute(statement3)
conn.commit()

statement4 = """
    INSERT INTO demo VALUES (
    'f', 8, 7
)
"""

cur.execute(statement4)
conn.commit()

query1 = """
SELECT COUNT(*)
FROM demo
"""

res1 = cur.execute(query1)
print(res1.fetchall())

query2 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5
AND y >= 5
"""

res2 = cur.execute(query2)
print(res2.fetchall())

query3 = """
SELECT COUNT(DISTINCT y)
FROM demo
"""

res3 = cur.execute(query3)
print(res3.fetchall())
