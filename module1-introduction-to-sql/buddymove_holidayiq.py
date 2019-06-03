'''
This module implements a solution to part 2 of the assignment.
'''

import pandas as pd
import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

buddy_df = pd.read_csv('buddymove_holidayiq.csv')
buddy_df.to_sql('review', conn, if_exists='replace', 
                index_label='id')
query = """SELECT * FROM review"""

conn.execute(query)
conn.commit()


# Count how many rows you have - it should be 249!
query = """SELECT COUNT(*) FROM review"""
results = conn.execute(query)
print("Rows: ", results.fetchall()[0][0])

# How many users who reviewed at least 100 Nature in the category also reviewed
# at least 100 in the Shopping category?
query = """SELECT COUNT(*)
FROM review
WHERE Nature >=100 AND Shopping >=100
"""
results = conn.execute(query)
print("More than 100 nature and shopping reviews: ", results.fetchall()[0][0])

# (Stretch) What are the average number of reviews for each category?
query_1 = """SELECT AVG("""
query_2 = """) FROM review;"""
for column in buddy_df.columns[1:]:
    query = query_1 + column + query_2
    print(query)
    results = conn.execute(query)
    print("Avg. for ", column, results.fetchall()[0][0])
