import pandas as pd
import os.path
import sqlite3

file_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv'
df = pd.read_csv(file_path)
print(f'DATA FRAME SHAPE : {df.shape}')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILEPATH = os.path.join(BASE_DIR, 'buddymove_holidayiq.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

df.to_sql(name='review', con=connection)

no_rows = 'SELECT COUNT(*) FROM review'
result_rows = cursor.execute(no_rows).fetchall()
print('No. of Rows :', result_rows)

reviews = 'SELECT COUNT(Nature), COUNT(Shopping) FROM review WHERE Nature >= 100 AND Shopping >= 100'
result_reviews = cursor.execute(reviews).fetchall()
print('No. of Users Reviewing Nature & Shopping at >= 100 :', result_reviews)