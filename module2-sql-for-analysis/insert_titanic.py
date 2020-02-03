import psycopg2
import os
from dotenv import load_dotenv
import sqlite3
import csv

load_dotenv()

DB_HOST = os.getenv("DB_HOST_TITANIC", default="OOPS")
DB_NAME = os.getenv("DB_NAME_TITANIC", default="OOPS")
DB_USER = os.getenv("DB_USER_TITANIC", default="OOPS")
DB_PASS = os.getenv("DB_PASS_TITANIC", default="OOPS")

# If this code appears complicated, it's because there are artifacts of two different attempts at problem solving this one. I tried both the psycopg2 built-in copy_from() method and inserting the csv into a sqlite3 database in python to more closely fit the in-class example. The psycopg2 copy_from() method ended up being the way to go for me, though I wasn't able to get a primary key to work.

# Connect to databases
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)
pg_curs = pg_conn.cursor()
# sl_conn = sqlite3.connect('titanic.sqlite3')
# sl_curs = sl_conn.cursor()

# Define columns and types
create_titanic_table = """
CREATE TABLE titanic (
    survived INT,
    pclass INT,
    name TEXT,
    sex TEXT,
    age DECIMAL,
    siblings_spouses INT,
    parents_children INT,
    fare DECIMAL
);
"""
# Create SQLite3 titanic table
# sl_curs.execute(create_titanic_table)

# Create PostgreSQL titanic table
pg_curs.execute(create_titanic_table)
pg_conn.commit()

with open('titanic_insert.csv') as f:
    pg_curs.copy_from(f, 'titanic', sep=',')

pg_conn.commit()

# Fill SQLite3 titanic table with data
# with open('titanic.csv') as fin:
#     dr = csv.DictReader(fin)
#     to_db = [(i['Survived'], 
#             i['Pclass'], 
#             i['Name'], 
#             i['Sex'], 
#             i['Age'], 
#             i['Siblings/Spouses Aboard'], 
#             i['Parents/Children Aboard'],
#             i['Fare']) for i in dr]

# insert_titanic = """
# INSERT INTO titanic (survived, pclass, name, sex, age, siblings_spouses, parents_children, fare) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
# """

# sl_curs.executemany(insert_titanic, to_db)
# sl_conn.commit()

# get_passengers = 'SELECT * FROM titanic'
# passengers = sl_curs.execute(get_passengers).fetchall()

# for passenger in passengers:
#     insert_passenger = """
#         INSERT INTO titanic
#         (survived, pclass, name, sex, age, siblings_spouses, parents_children, fare)
#         VALUES """ + str(passenger[1:]) + ";"
#     pg_curs.execute(insert_passenger)
# pg_conn.commit()