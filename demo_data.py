import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()

curs.execute("""
CREATE TABLE demo (
  s VARCHAR(10),
  x INT,
  y INT
);
""")

demo_insert = """
  INSERT INTO demo (s, x, y)
  VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""

curs.execute(demo_insert)
conn.commit()

conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()

q_1 = 'SELECT COUNT(*) FROM demo;'
results_1 = curs.execute(q_1)
print("How many rows are there?:", results_1.fetchall())

q_2 = 'SELECT COUNT(*) FROM demo WHERE x>=5 AND y>=5;'
results_2 = curs.execute(q_2)
print("How many rows are there where both x and y are at least 5?:", results_2.fetchall())

q_3 = 'SELECT COUNT (DISTINCT y) FROM demo;'
results_3 = curs.execute(q_3)
print("How many unique values of y are there?:", results_3.fetchall())
