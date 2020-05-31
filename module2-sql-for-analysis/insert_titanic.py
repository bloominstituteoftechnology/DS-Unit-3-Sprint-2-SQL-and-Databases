import os
import pandas as pd
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
import numpy as np
load_dotenv()
print(__file__)
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# load csv to dataframe
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(CSV_FILE_PATH)
# print(df.head())
# print(df.columns)
# print(df.values)
print('df.dtypes\n', df.dtypes)
# Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("dbname"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host")
)
# A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

# Drop the table if exist
cur.execute('DROP TABLE IF EXISTS Titanic;')

# CREATE TABLE query
query_create = """CREATE TABLE Titanic (
    Survived            INT,
    Pclass              INT,
    Name                varchar(120),
    Sex                 varchar(10),
    Age                 INT,
    SiblingsSpouses     INT,
    ParentsChildren     INT,
    Fare                INT);
"""
cur.execute(query_create)

# test

# query = 'INSERT INTO Titanic VALUES (0, 3, \'Mr. Owen\', \'male\', 22.0, 1, 0, 7.25);'
# cur.execute(query)
# cur.execute('SELECT * FROM Titanic')
# print('first fetch', cur.fetchall())

# this is a solution from Mike
list_of_tuples = list(df.to_records(index=False))
ins_query = 'INSERT INTO Titanic (Survived, Pclass, Name, Sex, Age, SiblingsSpouses, ParentsChildren, Fare) VALUES %s;'
extras.execute_values(cur, ins_query, list_of_tuples)

# this was my initial code but not working
# for row in df.values:
#     print('######')
#     print(type(row))
#     print(row)
#     cur.execute("INSERT INTO Titanic (Survived, Pclass, Name, Sex, Age, SiblingsSpouses, ParentsChildren, Fare) VALUES %s;", tuple(row))

conn.commit()

cur.execute('SELECT * FROM Titanic')
print('second fetch', cur.fetchall())
