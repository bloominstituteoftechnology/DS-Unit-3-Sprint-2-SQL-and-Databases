import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

# Convert to SQLite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql(name='review', con=conn, if_exists='replace')
curs = conn.cursor()

# Query Function
def query(query):
    result = curs.execute(query)
    return result.fetchall()

count_rows = 'SELECT COUNT(*) FROM review;'
count_rows = query(count_rows)[0][0]
print('This dataset contains', count_rows, 'rows')

reviewed = """
SELECT r.Nature, r.Shopping
FROM review as r
WHERE r.Nature >= 100
AND r.Shopping >= 100;
"""
reviewed = query(reviewed)[0][0]
print("This dataset contains", reviewed, "instances where both Nature and Shopping categories received as score above 100")