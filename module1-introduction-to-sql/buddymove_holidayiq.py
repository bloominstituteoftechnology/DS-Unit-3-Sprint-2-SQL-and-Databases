import pandas as pd
import sqlite3
df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review',con=conn,if_exists='replace')
curs = conn.cursor()
print('Number of rows')
print(curs.execute("SELECT COUNT(*) FROM review").fetchall())
print('Users who reviewed at least 100 Nature who also reviewed at least 100 in Shopping')
print(curs.execute("SELECT COUNT(CASE WHEN Shopping >= 100 then 1 else null end) FROM review WHERE Nature>=100").fetchall())
curs.close()
conn.commit()