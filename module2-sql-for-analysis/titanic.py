'''
This module implements a solution to part 2 of the assignment.
'''

import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import psycopg2
import sqlite3
import pandas as pd
import numpy as np

titanic_url = """https://raw.githubusercontent.com/will-cotton4/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv"""

titanic = pd.read_csv(titanic_url)
titanic = titanic.rename(columns={'Sex': 'is_female'})
titanic = titanic.replace({'male': 0, 'female': 1})
titanic['Name'] = titanic['Name'].str.replace(r"[\"\',]", '')
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

titanic.to_sql('titanic', conn, if_exists='replace',
               index_label='id')
query = """SELECT * FROM titanic"""

conn.execute(query)
conn.commit()

dbname = 'gosxmeyr'
user = 'gosxmeyr'
password = 'bwJU_pVJYZwLh82_fcAue5wQlzIrvHPq'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute("DROP TABLE IF EXISTS titanic")

create_titanic_table = """
CREATE TABLE titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(200),
    is_female INT,
    age INT,
    siblings_spouses INT,
    parents_children INT,
    fare REAL
)
"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()

titanic_listed = titanic.values.tolist()
i = 0
for passenger in titanic_listed:
    passenger_copy = passenger
    passenger_copy.insert(0, i)
    passenger_copy = tuple(passenger_copy)
    insert_pass = """
    INSERT INTO titanic
    VALUES """ + str(passenger_copy)
    i += 1
    pg_curs.execute(insert_pass)
pg_conn.commit()
