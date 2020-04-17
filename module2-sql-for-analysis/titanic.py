import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
from sqlalchemy import create_engine
import sqlite3


# construct a path to wherever your database exists
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
data = pandas.read_csv(CSV_FILEPATH)
data = data.rename(columns={'User Id': 'user_id'})

# create a connection to the 'buddymove_holidayiq.splite3' file path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", 'data', "titanic.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


# read the pandas dataframe to the 'titanic.sqlite3' database file
data.to_sql('titanic_table', connection, if_exists='replace')


average_fare_class_survived = """
SELECT
	CASE
	WHEN survived = 1 THEN 'survived'
	WHEN survived = 0 THEN 'Perished'
	ELSE 'unknown'
	END AS survived_or_perished
	,CASE
	WHEN pclass = 1 THEN 'first_class'
	WHEN pclass = 2 THEN 'second_class'
	WHEN pclass = 3 THEN 'third_class'
	ELSE 'unknown'
	END AS passenger_class
	, AVG(fare)
FROM titanic_table
GROUP BY survived_or_perished, passenger_class
"""

result = cursor.execute(average_fare_class_survived).fetchall()
for row in result:
    print(row['survived_or_perished'])
    print(row['passenger_class'])
    print(row['AVG(fare)'])
    print("_________")
    print("\n")
