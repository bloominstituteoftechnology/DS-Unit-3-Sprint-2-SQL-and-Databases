import sqlite3

# Making a new database (connection, new cursor)
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

# Make a table
table_schema = """CREATE TABLE "demo" (
    "s" TEXT,
    "x" INT,
    "y" INT
);"""
cur.execute(table_schema)

# Insert data to 'demo'
insert_data = """
INSERT INTO "demo"
VALUES ('g',3,9),
       ('v',5,7),
       ('f',8,7);
"""
cur.execute(insert_data)

# Check database contents
cur.execute("""
SELECT COUNT(*)
FROM demo
""")
print()
print(f'All rows: {cur.fetchall()[0][0]}')

cur.execute("""
SELECT COUNT(*)
FROM demo
WHERE
    x >= 5
AND y >= 5
""")
print()
print(f'Rows where x and y >= 5: {cur.fetchall()[0][0]}')

cur.execute("""
SELECT COUNT(DISTINCT y)
FROM demo
""")
print()
print(f'Unique values of y: {cur.fetchall()[0][0]}')

# Putting it all together
conn.commit()
cur.close()
conn.close()


# The print statements will output the appropriately formatted responses
