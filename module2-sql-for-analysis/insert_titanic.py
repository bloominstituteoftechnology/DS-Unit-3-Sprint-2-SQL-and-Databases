import psycopg2
import sqlite3
import pandas as pd


dbname = 'wpjclngs'
user = 'wpjclngs'
#pword = ''
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=pword, host=host)
pg_curs = pg_conn.cursor()

create_table_query = '''
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(100),
    age REAL,
    siblings_aboard INT,
    parents_aboard INT,
    fare REAL
   );
'''

pg_curs.execute(create_table_query)

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", '', regex=True)

dfRows = []
for i in range(len(df)):

    vals = f"""\
({df.iloc[i,0]},\
 {df.iloc[i,1]},\
 '{df.iloc[i,2]}',\
 '{df.iloc[i,3]}',\
 {df.iloc[i,4]},\
 {df.iloc[i,5]},\
 {df.iloc[i,6]},\
 {df.iloc[i,7]})"""

    dfRows.append(vals)

for i in dfRows:
    insert_person = """
INSERT INTO titanic \
(survived, pclass, name, sex, age, siblings_aboard, parents_aboard, fare) \
VALUES """ + str(i) + ";"
    pg_curs.execute(insert_person)

pg_curs.close()
pg_conn.commit()
