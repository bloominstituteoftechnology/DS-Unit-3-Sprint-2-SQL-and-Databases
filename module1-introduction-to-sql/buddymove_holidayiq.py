import pandas as pd
import sqlite3


conn = sqlite3.connect('TestDB1.db')
c = conn.cursor()

data = 'buddymove_holidayiq.csv'
df = pd.read_csv(data)

print(df.shape)

df.to_sql('buddymove_holidayiq', con=conn)

# How many rows
# 249
query = 'SELECT COUNT(*) FROM buddymove_holidayiq'
c.execute(query)
results = c.fetchall()
print(results)

# Nature > 100 And Shopping > 100
# 78
query2 = 'SELECT COUNT(*) FROM buddy.move_holidayiq WHERE Nature > 100 AND Shopping > 100'
c.execute(query2)
results2 = c.fetchall()
print(results2)