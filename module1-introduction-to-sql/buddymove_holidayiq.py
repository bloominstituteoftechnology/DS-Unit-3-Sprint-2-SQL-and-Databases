import sqlite3 
import pandas as pd 

df = pd.read_csv('buddymove_holidayiq.csv', index_col=None)
# print('df shape', df.shape, df.info())

bh_conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = bh_conn.cursor()

query = 'DROP TABLE IF EXISTS review'
curs.execute(query)

df.to_sql('review', con=bh_conn)

query = """
        SELECT COUNT(*)
        FROM review;
        """
result = curs.execute(query)
print('Number of rows',result.fetchall())

query = """
        SELECT Nature, Shopping
        FROM review
        WHERE Nature >= 100
        AND Shopping >= 100
        """
result = curs.execute(query)
print(result.fetchall())