# !pip install psycopg2-binary
import sqlite3
import pandas as pd
import os
import psycopg2


dbname = 'lhpxbhtd'
user = 'lhpxbhtd'
password = 'QQ4rSEm-icpuN1nuRS-HWJCicEMyXWT2'
host = 'salt.db.elephantsql.com'

pgconn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pgconn

pgcursor = pgconn.cursor()
pgcursor

df = pd.read_csv('titanic.csv')
assert df.shape == (887, 8)

pgcursor.execute('''
    CREATE TABLE titanic(
    survived BOOLEAN,
    pclass INT,
    name VARCHAR(85),
    sex VARCHAR(10),
    age NUMERIC (4, 2),
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare NUMERIC (7,4) );''')

# pgcursor.execute('ROLLBACK')

with open('titanic.csv', 'r') as f:
    next(f)
    pgcursor.copy_from(f, 'titanic', sep=',')
    pgconn.commit()

query1 = '''SELECT COUNT(*) FROM titanic
            WHERE survived = 'true';'''
q1 = pgcursor.execute(query1)
p1 = pgcursor.fetchall()
print('No. of Survivors:', p1)

query2 = '''SELECT name FROM titanic
            WHERE siblings_spouses_aboard = 0 AND parents_children_aboard = 0;'''
q2 = pgcursor.execute(query2)
p2 = pgcursor.fetchall()
print('Alone Passengers:', p2)