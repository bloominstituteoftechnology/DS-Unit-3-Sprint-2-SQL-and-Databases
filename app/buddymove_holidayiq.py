import pandas
import sqlite3
import os


# construct a path to wherever your database exists
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "buddymove_holidayiq.csv")
data = pandas.read_csv(CSV_FILEPATH)

print(data.shape)

# create a connection to the 'buddymove_holidayiq.splite3' file path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", 'data', "buddymove_holidayiq.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

# read the pandas dataframe to the 'buddymove_holidayiq.sqlite3' database file
data.to_sql('buddymove_holidayiq', connection, if_exists='replace')


cursor = connection.cursor()


#query = "total number of characters;"
query = """
SELECT *
FROM buddymove_holidayiq
"""

result = cursor.execute(query).fetchall()
print(result)