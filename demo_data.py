import sqlite3

# Connect to empty sqlite3 file
conn = sqlite3.connect('demo_data.sqlite3')

# Create cursor
curs = conn.cursor()

#Create table
create_demo_table = """
CREATE TABLE demo (
  s VARCHAR(1),
  x INT,
  y INT
)
"""
# Execute create_demo_table
curs.execute(create_demo_table)

# Create data
data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

# Insert data into table
for n in range(0, len(data)):
  insert_data = """
  INSERT INTO demo
  (s, x, y)
  VALUES """ + str(data[n])
  curs.execute(insert_data)

# Commit changes to file
conn.commit()

# Queries
num_of_rows = """
SELECT COUNT(*) FROM demo;
"""

xy_at_least_5 = """
SELECT COUNT(*) FROM demo
WHERE x >= 5
AND y >=5;
"""

unique_y_rows = """
SELECT COUNT(DISTINCT y) FROM demo
"""

# Print results of queries
print('Total rows in demo:', curs.execute(num_of_rows).fetchall()[0][0])
print('Rows where both x and y are at least 5:', curs.execute(xy_at_least_5).fetchall()[0][0])
print('Number of unique y values:', curs.execute(unique_y_rows).fetchall()[0][0])

# Outputs
# Total rows in demo: 3
# Rows where both x and y are at least 5: 2
# Number of unique y values: 2

