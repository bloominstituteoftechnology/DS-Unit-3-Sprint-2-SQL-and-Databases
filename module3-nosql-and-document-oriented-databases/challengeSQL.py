import sqlite3
import pandas
connect = sqlite3.connect()
cursor = connect.cursor()

query = '''
SELECT *
FROM SELECT(
    index
    value
    LAG(value) OVER (ORDER BY index) as lagindex,
    LEAD(value) OVER (ORDER BY index) as leadindex
    FROM consecutives
)
WHERE value = lagindex AND value = leadindex;
'''
cursor.execute(query).fetchall()
print('xyz')