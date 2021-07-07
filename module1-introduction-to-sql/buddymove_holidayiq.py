import pandas as pd
import sqlite3
import os
import sys


URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv"
df = pd.read_csv(URL)

BLANK_DATABASE = "buddymove_holidayiq.sqlite3"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 
                           BLANK_DATABASE)

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

df.to_sql("review", 
          connection, 
          if_exists="replace")

connection.close()

######################################
######################################

DB_FILEPATH = os.path.join(os.path.dirname(__file__), 
                           BLANK_DATABASE)

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# Count how many rows you have - it should be 249!
question_row_count = "Count how many rows you have - it should be 249!"

query_row_count = """
SELECT COUNT(*)
FROM review;
"""

# How many users who reviewed at least 100 `Nature` in the category also reviewed at least 100 in the `Shopping` category?
question_dedicated_reviewers = """
How many users who reviewed at least 100 `Nature` in the category also reviewed at least 100 in the `Shopping` category?
"""

query_dedicated_reviewers = """
SELECT COUNT(*)
FROM review
WHERE (Nature >= 100 AND Shopping >= 100)
"""

questions = [question_row_count,
             question_dedicated_reviewers]

queries = [query_row_count,
           query_dedicated_reviewers]

for question, query in zip(questions, queries):
    print("\n", question, "\n", query, "\n", cursor.execute(query).fetchall(), "\n\n-------------")

#What are the average number of reviews for each category?
question_avg_reviews_per_category = "What are the average number of reviews for each category?"

CATEGORIES = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

print(question_avg_reviews_per_category)

for CATEGORY in CATEGORIES:
    mean = cursor.execute('SELECT AVG('+CATEGORY+') FROM review').fetchall()[0][0]
    print( CATEGORY , '\n' , mean, '\n', '-----------')

cursor.close()
