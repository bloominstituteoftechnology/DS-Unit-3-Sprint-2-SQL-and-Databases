import pandas as pd
import sqlite3
from sqlalchemy import create_engine
df = pd.read_csv('https://raw.githubusercontent.com/cmgospod/\
DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/\
buddymove_holidayiq.csv')
engine = create_engine('sqlite://', echo=False)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', conn)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM review")
rows = cur.fetchall()
print(f'Total rows: {rows[0][0]}')
cur2 = conn.cursor()
cur2.execute("SELECT COUNT(*) FROM review \
WHERE Nature > 99 AND Shopping > 99")
reviewers = cur2.fetchall()
print(f'{reviewers[0][0]} people reviewed 100 or more \
in both Nature and Shopping')
