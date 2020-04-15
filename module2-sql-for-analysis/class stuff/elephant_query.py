import psycopg2

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DBNAME, user='rsswtvhb',
                        password=DB_PASS, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cur.fetchall()

for line in results:
    print(line)