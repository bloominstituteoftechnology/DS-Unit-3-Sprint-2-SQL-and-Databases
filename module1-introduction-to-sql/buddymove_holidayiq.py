import sqlite3
import pandas as pd
"""
Load the data (use `pandas`) from the provided file `buddymove_holidayiq.csv`
"""
df = pd.read_csv('buddymove_holidayiq.csv')

"""
- Open a connection to a new (blank) database file `buddymove_holidayiq.sqlite3`
"""
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
c = conn.cursor()

"""
- Use `df.to_sql`
Load the data (use `pandas`) from the provided file `buddymove_holidayiq.csv`
  ([documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html))
  to insert the data into a new table `review` in the SQLite3 database
"""
try:
    df.to_sql('review', conn)
except ValueError:
    print('table already exists')

"""
Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category?
- 
"""
querylist = {}    # queries

querylist['COUNT_ROWS'] =('SELECT COUNT(*) FROM review')
querylist['DISTINCT_USERS'] =  f"SELECT COUNT(DISTINCT(\"User Id\")) FROM review"
cond2 = f"('Nature' >= 100) AND ('Shopping' >= 100)"
querylist['>=100 nature and shopping'] = f"SELECT COUNT('User Id') FROM review WHERE {cond2}"  

"""(*Stretch*) What are the average number of reviews for each category?
"""

for q in querylist.items():
    name = q[0]   #query name
    result = c.execute(q[1]).fetchall()[0][0]  # query result
    print(name,result)

categorys = df.columns.drop(['User Id']).to_list()

for cl in categorys:
    result = c.execute(f"SELECT AVG({cl}) FROM review").fetchall()[0][0]  # query result
    print(cl,result)
"""
Your code (to reproduce all above steps) should be saved in
`buddymove_holidayiq.py`, and added to the repository along with 

the generated
SQLite database.

## Resources and Stretch Goals

For a more complicated example SQLite database with a number of tables to play
with, check out this [SQLite Sample
Database](https://www.sqlitetutorial.net/sqlite-sample-database/).

The RPG data also exists in a [JSON
file](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json) -
try loading it with the standard [json
module](https://docs.python.org/3.5/library/json.html), and reproducing the
above queries with direct manipulation of the Python dictionaries. Also, try to
load it into a `pandas` dataframe and reproduce the above queries with
appropriate dataframe function calls.
"""