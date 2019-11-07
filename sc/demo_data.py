import pandas as pd
import sqlite3
from pandas import DataFrame 

### Part 1 - Making and populating a Database

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = """
    CREATE TABLE demo (
        s VARCHAR(10)
        x INT,
        y INT
);
"""

data = [['g', 3, 9],['v', 5, 7],['f', 8, 7]]
df = pd.DataFrame(data,columns=['s', 'x', 'y'],dtype=int)
print(df)

df.to_sql('demo', conn, index=False, if_exists='replace') # Insert the values from the df into the table 'X'

curs = conn.cursor()
query = 'SELECT * FROM demo LIMIT 20'
pd.read_sql(query, conn)

# how many rows
query = """
SELECT COUNT(*)
FROM demo
"""
curs.execute(query)
print(curs.fetchall())

# How many rows are there where both `x` and `y` are at least 5?
query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5
AND y >=5
"""
curs.execute(query)
print(curs.fetchall())

# How many unique values of `y` are there 
# (hint - `COUNT()` can accept a keyword `DISTINCT`)?

query = """
SELECT COUNT(DISTINCT(y))
FROM demo
"""
curs.execute(query)
print(curs.fetchall())

curs.close()
