import pandas as pd
import sqlite3

conn = sqlite3.connect('module1-introduction-to-sql/buddymove_holidayiq.sqlite3')
df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')

df.to_sql('users', conn)

cur = conn.cursor()

query1 = """
SELECT COUNT(*)
FROM users
"""

cur.execute(query1)
print(cur.fetchall())

query2 = """
SELECT COUNT(*)
FROM users u
WHERE u.Nature >= 100 AND u.Shopping >= 100
"""

cur.execute(query2)
print(cur.fetchall())
