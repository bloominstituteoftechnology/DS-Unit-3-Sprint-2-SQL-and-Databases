import sqlite3

sqlite_file = "demo_data.sqlite3"
table_name = "demo"

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

table_creation = """
CREATE TABLE IF NOT EXISTS Demo(
    s VARCHAR(5),
    x INTEGER,
    y INTEGER
)
"""
cursor.execute(table_creation)

inserted1 = """
INSERT INTO Demo (s, x, y)
VALUES ('g', 3, 9)
"""
inserted2 = """
INSERT INTO Demo (s, x, y)
VALUES ('v', 5, 7)
"""
inserted3 = """
INSERT INTO Demo (s, x, y)
VALUES ('f', 8, 7)
"""
#commented out to stop repeats
# cursor.execute(inserted1)
# cursor.execute(inserted2)
# cursor.execute(inserted3)
query1 = """
SELECT COUNT(x)
FROM Demo
"""
conn.commit()
result1 = cursor.execute(query1)
results1 = cursor.fetchall()
print(results1[0][0])

query2 = """
SELECT *
FROM Demo
WHERE x >= 5 AND y >= 5
"""

result2 = cursor.execute(query2)
results2 = cursor.fetchall()
print(results2)

query3 = """
SELECT COUNT(DISTINCT y)
FROM Demo
"""

result3 = cursor.execute(query3)
results3 = cursor.fetchall()
print(results3[0][0])