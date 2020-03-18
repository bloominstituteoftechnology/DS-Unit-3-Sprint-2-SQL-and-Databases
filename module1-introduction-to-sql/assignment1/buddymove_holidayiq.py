# Uncomment LINE 19 df.to_sql if table doesn't exist yet.
# Comment it to run the rest of the code
# Uncomment Lines 15, 17 to test connection in terminal

import pandas as pd
import os
import sqlite3

file_path = '../buddymove_holidayiq.csv'

df = pd.read_csv(file_path)

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
#print('CONNECTION: ', connection)
cursor = connection.cursor()
#print('CURSOR: ', cursor)

df.to_sql('review', connection)

#print(df.head())
#print(df.shape)

# number of rows
query = """SELECT count('index')
FROM review;"""

result2 = cursor.execute(query).fetchall()
print('Number of rows ', result2)

# How many users who reviewed at least 100 Nature in the category 
# also reviewed at least 100 in the Shopping category
query = """SELECT count('index') FROM review
WHERE Nature >= 100 and Shopping >= 100;"""

result2 = cursor.execute(query).fetchall()
print('Number who reviews Nature and Shopping >= 100: ', result2)

# Stretch example: average review for a category. Could repeat 5x for others

query = """SELECT AVG(Sports) FROM review;"""

result2 = cursor.execute(query).fetchall()
print('Average sports review: ', result2)