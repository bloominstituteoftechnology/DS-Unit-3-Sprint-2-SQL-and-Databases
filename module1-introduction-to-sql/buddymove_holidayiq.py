import sqlite3
import pandas as pd

raw_csv_url = 'https://raw.githubusercontent.com/DavidVollendroff/DS-Unit-3-Sprint-2-' \
              'SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
df = pd.read_csv(raw_csv_url)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymove_holidayiq', conn)
curs = conn.cursor()
query = "SELECT * FROM buddymove_holidayiq"
result = curs.execute(query).fetchall()
print(len(result), 'rows present')
query = "SELECT * FROM buddymove_holidayiq WHERE Nature > 100 and Shopping > 100;"
result = curs.execute(query).fetchall()
print(len(result), 'users have reviewed both 100 Nature and 100 shopping.')