!pip install psycopg2-binary

import sqlite3
import pandas as pd
import psycopg2

conn = sqlite3.connect('titanic.sqlite3')
cur = conn.cursor()

# Loading in data and cleaning it for good SQL schema
df = pd.read_csv('https://raw.githubusercontent.com/lechemrc/DS-Unit-3-Sprint\
-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

columns_dict = {'Survived':'survived', 'Pclass':'passenger_class',
                'Name':'name', 'Sex':'sex', 'Age':'age',
                'Siblings/Spouses Aboard':'siblings_spouses',
                'Parents/Children Aboard':'parents_children', 'Fare':'fare'}
df = df.rename(columns=columns_dict)
df.head()

df.to_sql('titanic', con=conn)

cur.execute('''
    PRAGMA table_info(titanic)
''')
cur.fetchall()

cur.execute("SELECT * FROM titanic")
titanic = cur.fetchall()
titanic

len(titanic)

host = 'salt.db.elephantsql.com'
user = 'itczlnew'
database = 'itczlnew'
password = '0OMYQYy2K1WZvM1TYfcMiKh1tW1hnkgP'

pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)

pg_cur = pg_conn.cursor()

create_titanic_table = """
CREATE TABLE titanic(
    index serial PRIMARY KEY,
    survived INT,
    passenger_class INT,
    name VARCHAR (100) NOT NULL,
    sex VARCHAR (100) NOT NULL,
    age INT,
    siblings_spouses INT,
    parents_children INT,
    fare INT
);
"""

query = "INSERT INTO titanic VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
pg_cur.executemany(query, titanic)