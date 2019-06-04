'''assingment 2'''

import pandas as pd
import sqlite3 

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')
df = df.rename(columns={'User Id':'User_Id'})
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('table2', con=conn, if_exists='replace')
curs= conn.cursor()
query = 'select count(*) from table2'
result = curs.execute(query)
print(result.fetchall())
query = 'select count(User_Id) from table2 where Nature>100 and Shopping'
result = curs.execute(query)
print(result.fetchall())
query = 'select avg(Sports) as sports,avg(Religious) as religious,avg(Nature) as nature,avg(Theatre) as theatre,avg(Shopping) as shopping,avg(Picnic) as picnic from table2'
result = curs.execute(query)
print(result.fetchall())