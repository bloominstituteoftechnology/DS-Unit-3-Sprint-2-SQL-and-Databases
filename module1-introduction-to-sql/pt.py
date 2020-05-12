import pandas as pd
import sqlite3
import os
# construct my data dir path
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", '')
DB_FILENAME = DATA_PATH + "buddymove_holidayiq.sqlite3"
# load a df with the dat that is going to be in the sql table
df = pd.read_csv(DATA_PATH + "buddymove_holidayiq.csv")

conn = sqlite3.connect(DB_FILENAME)
curs = conn.cursor()
df.to_sql(index=False, name="review", con=conn, if_exists="replace")
# getting the number of rows in the database
# should be 249
query = """
SELECT
	count("User id") AS counts
FROM review
"""
result = curs.execute(query).fetchall()
print(f"The number of rows in the db are:{result[0][0]}")

# print the number of filtered users in Nature and Shopping
query = """
SELECT count(Nature) AS "count" FROM review
WHERE (Nature >= 100) AND (Shopping >=100)
"""
result = curs.execute(query).fetchall()
print(f"{result[0][0]} user's recived 100 Nature and Shopping")