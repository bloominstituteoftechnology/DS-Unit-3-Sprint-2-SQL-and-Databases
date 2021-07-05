import sqlite3

# Create connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create demo table
create_demo_table = """
CREATE TABLE demo_data (
  s VARCHAR(10),
  x INT,
  y INT
)
"""

curs.execute(create_demo_table)

insert_1 = """
  INSERT INTO demo_data
  VALUES""" + '("g", 3, 9)'
curs.execute(insert_1)

insert_2 = """
  INSERT INTO demo_data
  VALUES""" + '("v", 5, 7)'
curs.execute(insert_2)

insert_3 = """
  INSERT INTO demo_data
  VALUES""" + '("f", 8, 7)'
curs.execute(insert_3)

curs.execute('SELECT * FROM demo_data')
pg_data = curs.fetchall()
print(pg_data)

# Question 1
q1 = curs.execute('SELECT COUNT(*) FROM demo_data').fetchall()[0][0]
print("There are ", q1, "rows in the database")

# Question 2
q2 = curs.execute("""
SELECT COUNT(*) FROM demo_data
WHERE x >= 5
AND y >= 5;
""").fetchall()[0][0]
print("There are ", q2, "rows where both x and y are at least 5")


# Question 3
q3 = curs.execute("""
SELECT COUNT(DISTINCT y) FROM demo_data
""").fetchall()
print("There are ", q3, "unique values in y")
