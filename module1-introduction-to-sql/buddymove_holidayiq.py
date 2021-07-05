import pandas as pd
import sqlite3

connection = sqlite3.connect('buddymove_holidayiq.sqlite3')

buddy_df = pd.read_csv('https://raw.githubusercontent.com/tbradshaw91/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

buddy_df.to_sql(name='review',con=connection, if_exists="append", index=False)

connection.execute("SELECT * FROM review").fetchall()

query_1 = 'SELECT count() FROM review;'
print ('Rows:',connection.cursor().execute(query_1).fetchone()[0], '\n')

df = pd.read_sql("SELECT * FROM review", connection)

df.loc[(df['Nature'] >= 100) & (df['Shopping'] >= 100)]



