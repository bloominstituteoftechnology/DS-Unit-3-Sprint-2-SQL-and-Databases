import pandas
import sqlite3
import os


# construct a path to wherever your database exists
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "buddymove_holidayiq.csv")
data = pandas.read_csv(CSV_FILEPATH)

print(data.shape, data.isnull().sum())

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", 'data', "buddymove_holidayiq.sqlite3")
