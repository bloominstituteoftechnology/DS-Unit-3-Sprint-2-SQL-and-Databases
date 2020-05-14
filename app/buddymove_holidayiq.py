# app/buddymove_holidayiq.py

import pandas as pd
import sqlite3
import os

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
df = pd.read_csv(CSV_FILEPATH)
#print(df.head())
df = df.rename(columns = {'User Id': 'User_id'})
#print(df.head())
print(df.shape)
print(df.isnull().values.any())
#print(df.dtypes)
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()
print ("Connection", connection)

df.to_sql('review', con = connection, if_exists='replace', index=False,
            dtype={
                "User_id": "TEXT",
                "Sports": "INTEGER",
                "Religious": "INTEGER",
                "Nature": "INTEGER",
                "Theatre": "INTEGER",
                "Shopping": "INTEGER",
                "Picnic": "INTEGER"
            })

query = """
SELECT COUNT(User_Id) as total_users
FROM review"""

result = cursor.execute(query).fetchall()
print(result)