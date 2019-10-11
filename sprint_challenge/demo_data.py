import sqlite3

# Establishing connection and cursor. The connection has to be done in text
conn = sqlite3.connect('demo_data.sqlite3')
r = conn.cursor()

# creating multi-line SQL query to execute in the cursor
create_demo_table = """
CREATE TABLE IF NOT EXISTS demo(
s varchar(1),
X INT,
Y INT)
"""
# Execute create demo_table function in the cursor
r.execute(create_demo_table)

# insert values into tables
insert_data = """
INSERT INTO demo(s,x,y)
VALUES ('g',3,9),('v',5,7),('f',8,7)
"""
# executing insert_data with cursor
r.execute(insert_data)

# Executing these queries can be done either this way
q1 = ("""SELECT COUNT(*) FROM demo""")
q1a = r.execute(q1)
print(q1a.fetchall())

# or can be don this way. They have to be text though
print(r.execute("SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5").fetchall())

print(r.execute("SELECT COUNT(DISTINCT y) FROM demo").fetchall())



conn.commit()
conn.close
