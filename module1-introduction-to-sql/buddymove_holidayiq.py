import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

print(df.head())

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('Review',con=conn)
curs = conn.cursor()