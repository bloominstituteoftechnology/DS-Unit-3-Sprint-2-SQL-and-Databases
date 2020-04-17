import psycopg2
import os
import json
"""
from dotenv import load_dotenv

load_dotenv()

DBNAME = os.getenv("DB_NAME")
DBUSER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
"""

# for reference, here's the elephant link https://api.elephantsql.com/console/bb02e75f-0739-4555-9ae3-cf022a9af2a8/details?

DBNAME = 'rsswtvhb'
DBUSER = "rsswtvhb"
DB_PASS = "qImj0x6_ofnmgQYeEY9VD2q-93dNW1pt"
DB_HOST = 'drona.db.elephantsql.com'

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DBNAME, user=DBUSER,
                        password=DB_PASS, 
                        host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()


table_name = "test_table"

my_dict = {"a":1, "b":['dog', 'cat', 42], "c":True}

# create format for our query
insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
"""
# use format to insert a row
cur.execute(insertion_query, ("a row", 'null'))

# use format to insert another row
cur.execute(insertion_query, ("another row", json.dumps(my_dict) ) )
"""



# let's try to do the 2 insertions from above using a loop
"""
row_list = [("a row", 'null') , ("another row", json.dumps(my_dict) ) ]

for row in row_list:
    cur.execute(insertion_query, query)
"""

# let's try to do the 2 insertions in a single command
from psycopg2.extras import execute_values

# to use this function, we need to remove one of the placeholders
new_insertion_query = f"INSERT INTO {table_name} (name, data) VALUES %s"

row_list = [("a row", 'null') , ("another row", json.dumps(my_dict) ) ]

execute_values(cur, new_insertion_query, row_list)


cur.execute('SELECT * from test_table;')

results = cur.fetchall()

for line in results:
    print(line)

conn.commit()

