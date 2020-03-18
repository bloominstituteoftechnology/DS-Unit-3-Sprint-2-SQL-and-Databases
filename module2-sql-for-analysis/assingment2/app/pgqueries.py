import psycopg2

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname='TODO', user='TODO',
                        password='TODO', host='baasu.db.elephantsql.com')
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
cur.fetchone()