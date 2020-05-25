import os
import sqlite3
import pandas as pd 

FILEPATH = os.path.join(os.path.dirname(__file__), 'buddymove_holidayiq.csv')
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'buddymove_holidayiq.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# creat dataframe
df = pd.read_csv(FILEPATH)

df.to_sql('review', connection, if_exists='replace')

query = "SELECT COUNT('index') FROM review"
result = cursor.execute(query).fetchall()
print(f'Total number of rows is {result[0][0]}')

query = "SELECT COUNT('index') FROM review WHERE Nature>=100 and Shopping>=100"
result = cursor.execute(query).fetchall()
print(f'Number of people who reveiwed more that 100 Shopping and Nature: {result[0][0]}')
