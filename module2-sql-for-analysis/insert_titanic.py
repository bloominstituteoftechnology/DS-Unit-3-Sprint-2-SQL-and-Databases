import pandas as pd
import psycopg2
import sqlite3

"""change csv to sqlite"""
df = pd.read_csv("titanic.csv")
df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
              'Parents/Children Aboard', 'Fare']
"""
connecting to the database
"""
"""
insert data into new table
"""
df.to_sql('review', connection, index=False)
"""
cursor
"""
connection = sqlite3.connect('titanic.sqlite3')
cursor = connection.cursor()
cursor.execute('SELECT * FROM review').fetchall()
print(df.shape)
print(df.head)
"""
Count how many rows you have
"""
query = "SELECT COUNT(*) FROM review"
print(cursor.execute(query).fetchall()[0][0])
"""
Connect to the elphant database
"""
dbname = 'vbmmjeoc'
user = 'vbmmjeoc'  # ElephantSQL happens to use same name for db and user
password = 'qiPPfJeCLmtX5-yUZcV27SmlTz75PQka'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
DB_FILEPATH = "titanic.sqlite3"
sl_conn = sqlite3.connect(DB_FILEPATH)
sl_curs = sl_conn.cursor()
"""
Query
"""
sl_curs.execute('PRAGMA table_info(review);')
sl_curs.fetchall()


# Defining a function to refresh connection and cursor
def refresh_conn_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


pg_conn, pg_curs = refresh_conn_and_cursor(pg_conn, pg_curs)
# A bunch of integers, and a varchar
# We need to make a create statement for PostgreSQL that captures this
create_titanic_table = """
CREATE TABLE titanic (
  Survived INTEGER,
  Pclass INTEGER,
  Name VARCHAR(30),
  Sex TEXT,
  Age REAL,
  Siblings_Spouses_Aboard INTEGER,
  Parent_Childeren_Aboard INTEGER,
  Fare REAL
);
"""
# Execute the create table
pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()
#pandas - to_records