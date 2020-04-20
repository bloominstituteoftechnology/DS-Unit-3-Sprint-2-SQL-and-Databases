import pandas as pd 
import sqlite3 
from sqlalchemy import create_engine

buddy_df = pd.read_csv('buddymove_holidayiq.csv')

DB_FILEPATH = 'buddymove_holidayiq.sqlite3'

connection = sqlite3.connect(DB_FILEPATH)
print('Connection:', connection)

cursor = connection.cursor()
print("Cursor", cursor)

engine = create_engine('sqlite://', echo=False)

buddy_df.to_sql('user', con=engine)
result = engine.execute('SELECT * FROM user').fetchall()

print(
    "Id", result[0][0],
    "User", result[0][1],
    "Sports", result[0][2],
    "Religion", result[0][3],
    "Nature", result[0][4],
    "Theatre", result[0][5],
    "Shopping", result[0][6],
    "Picnic", result[0][7]
)


# print('Results:' result)
# #> a list of tuples 
