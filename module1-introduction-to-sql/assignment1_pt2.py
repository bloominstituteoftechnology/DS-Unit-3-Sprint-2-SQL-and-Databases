import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cur = conn.cursor()

df = pd.read_csv('https://raw.githubusercontent.com/lechemrc/DS-Unit-3-Sprint-2\
-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
df = df.rename(columns={'User Id':'User_id'})
df.head()

# df.to_sql('buddymove_holidayiq', con=conn)

cur.execute('''
    SELECT * FROM buddymove_holidayiq
''')
result = cur.fetchall()
print(result)

# Selecting all values with > 100 for Nature and Shopping
cur.execute('''
    SELECT COUNT(*)
    FROM buddymove_holidayiq
    WHERE Nature >= 100
    AND Shopping >= 100
''')
result = cur.fetchall()
print(result)

# Creating iterable list
avg_list = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

# Iterating through each category to find the average
for item in avg_list:
    cur.execute(f"""
        SELECT AVG({item})
        FROM buddymove_holidayiq
    """)
    result = cur.fetchall()
    print(f'The average of {item} is {result}')