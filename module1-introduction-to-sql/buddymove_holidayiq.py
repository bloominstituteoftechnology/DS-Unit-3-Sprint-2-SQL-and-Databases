import pandas as pd
import sqlite3

df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql(name='df', con=conn)

query = 'SELECT COUNT(*) FROM df'
results = conn.execute(query)
print(results.fetchall())
