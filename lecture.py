"""practice queries on chinook database"""

import sqlite3 as sql

conn = sql.connect('chinook.db')
conn.row_factory = sql.Row
cur = conn.cursor()
# query = 'SELECT * FROM customers'
query = """
SELECT
    Country
    ,COUNT(DISTINCT CustomerId) as CustomerCount
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""
# result = cur.execute(query)
result = cur.execute(query).fetchall()

# print('Connection:', conn)
# print('Cursor:', cur)
# print('Query:', query)
# print('Result:', result)
# print('Result2:', result2)

print(result)
print(type(result))
print(len(result))

for row in result:
    print(row)
    print(type(row))
    print(row['Country'], row['CustomerCount'])
