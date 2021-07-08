import sqlite3

# create and establish connection to database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# function to streamline query execution
def execute_query(query):
    curs.execute(query)

# query to create table
query = """CREATE TABLE IF NOT EXISTS demo (
    s charvar(1),
    x int,
    y int
)"""

execute_query(query)

# Insert rows into table
query = """INSERT INTO demo (s, x, y)
           VALUES ('g', 3, 9)"""
execute_query(query)

query = """INSERT INTO demo (s, x, y)
           VALUES ('v', 5, 7)"""
execute_query(query)

query = """INSERT INTO demo (s, x, y)
           VALUES ('f', 8, 7)"""
execute_query(query)

# Commit changes to finalize changes to database
conn.commit()

# Re-establish cursor
curs = conn.cursor()


# Function to execute exploratory query
def explore_query(query):
    result = curs.execute(query)
    result = result.fetchall()[0][0]
    return result

# Determine the number of rows in the table
query = """SELECT COUNT(*) FROM demo;"""
result = explore_query(query)

# Output: 'Query 1: The demo table has 3 rows'
print('Query 1: The demo table has ' + str(result) + ' rows')

# Determine how many rows have x and y values greater than 5
query = """SELECT COUNT(*)
           FROM demo
           WHERE x >= 5 AND y >= 5"""
result = explore_query(query)

# Output: 'Query 2: 2 rows have x and y values greater than or equal to 5'
print('Query 2: ' + str(result) + """ rows have x and y values greater than or
        equal to 5""")

# Determine how many unique values are in y
query = """SELECT COUNT(DISTINCT(y))
           FROM demo"""
result = explore_query(query)

# Output: 'Query 3: Column y has 2 unique values'
print('Query 3: Column y has ' + str(result) + ' unique values')

# Condensed Output
# Query 1: The demo table has 3 rows
# Query 2: 2 rows have x and y values greater than or
#         equal to 5
# Query 3: Column y has 2 unique values
