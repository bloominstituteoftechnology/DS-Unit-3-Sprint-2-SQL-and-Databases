import pandas as pd
import sqlite3

df = pd.read_csv("data/buddymove_holidayiq.csv")
#print(df.head())
db_table = 'buddymove_holidayiq'
conn = sqlite3.connect('data/' + db_table + '.sqlite3')
df.to_sql(db_table, conn, if_exists='replace')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM buddymove_holidayiq;'
curs.execute(query)
print("There are", curs.execute(query).fetchall()[0][0], "rows in the buddymove_holidayiq table")
query = 'SELECT COUNT(*) FROM buddymove_holidayiq WHERE (Nature > 100 and  Shopping > 100)';
curs.execute(query)
print(curs.execute(query).fetchall()[0][0], "rows have both Nature and Shopping attributes > 100")
