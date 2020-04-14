

import psycopg2

DB_NAME = 'idxmbhro'
DB_PW = 'DQIxtzVagU-jSEK44j7YJjPimqsEyOOV'
DB_HOST = 'drona.db.elephantsql.com'
DB_USER = 'idxmbhro'

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)


### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
result1 = cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result2 = cur.fetchone()

print(result1)
print(result2)

