import sqlite3

#create connection
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

create_demo_table = """
CREATE TABLE demo(
   s serial PRIMARY KEY,
   x INTEGER NOT NULL,
   y INTEGER NOT NULL
);
"""

cur.execute(create_demo_table)
conn.commit()

demo_data = [('g',3,9),('v',5,7),('f',8,7)]

for row in demo_data:
	query = f"INSERT INTO demo VALUES {str(row)}"
	cur.execute(query)

conn.commit()

query_rows = """
	SELECT COUNT(s)
	FROM demo
	"""
cur.execute(query_rows)
total_rows = cur.fetchall()

print(f'There are {total_rows[0][0]} total rows')

query_atleast_five = """
	SELECT COUNT(*)
	FROM demo
	WHERE x >=5 AND y >= 5
	"""
cur.execute(query_atleast_five)
total_atleast_five = cur.fetchall()

print(f'There are {total_atleast_five[0][0]} rows where x and y are at least 5')

query_distinct_y = """
	SELECT COUNT(DISTINCT y)
	FROM demo
	"""
cur.execute(query_distinct_y)
total_distinct_y = cur.fetchall()

print(f'There are {total_distinct_y[0][0]} distinct y-values')