'''
Sprint Challenge Unit 3 Sprint 2

'''


from query_func import run_query
# Part 1 - Making and populating a Database

# Create new db by connecting to it, and open a cursor
db = 'demo_data.sqlite3'
conn = sqlite3.connect(db)
curs = conn.cursor()
if curs:
    print('yay')

# Drop table to start so the file can be rerun no issues
run_query(db, 'DROP TABLE demo;')
# Create the table with its schema
query = '''CREATE TABLE IF NOT EXISTS demo(
              s TEXT,
              x INT,
              y INT
            );'''
run_query(db, query, commit=True)
# Confirm that table created correctly by grabbing its' schema
print(run_query(db, 'PRAGMA table_info(demo);'))

# Insert data into table
query = """INSERT INTO demo
        (s, x, y)
        VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);"""
run_query(db, query, commit=True)
# Confirm data is inserted
print(run_query(db, 'SELECT * FROM demo;'))

# Test queries to confirm table is correct
# How many lines in file?
print(run_query(db, 'SELECT COUNT(*) FROM demo;', commit=True))

# How many rows where both x and y >= 5
query = """SELECT COUNT(*)
           FROM demo
           WHERE x >=5 AND y >=5;"""
print(run_query(db, query, commit=True))

# How many unique y values?
query = """SELECT COUNT(DISTINCT y)
           FROM demo;"""
print(run_query(db, query, commit=True))
