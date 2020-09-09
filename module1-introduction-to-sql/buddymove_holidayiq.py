import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.py')
curs = conn.cursor()
df = pd.read_csv('buddymove_holidayiq.csv')
review = df.to_sql(df, con=sqlite3)



def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


COUNT = SELECT * FROM buddymove_holidayiq


execute_query(curs, COUNT)