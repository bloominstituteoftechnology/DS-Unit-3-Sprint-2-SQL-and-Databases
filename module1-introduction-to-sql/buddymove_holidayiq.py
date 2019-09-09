import pandas as pd
import sqlite3
from pandas import DataFrame 

df = pd.read_csv('/Users/elliotgunn/Desktop/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.shape

conn = sqlite3.connect('buddymove_holidayiq.sqlite3.db')
c = conn.cursor()

df.to_sql('review', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'X'
