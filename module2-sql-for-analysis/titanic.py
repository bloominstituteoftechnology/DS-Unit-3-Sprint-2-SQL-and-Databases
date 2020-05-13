import os
import sqlite3
import json
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import numpy as np
from sqlalchemy import create_engine
load_dotenv()

engine = create_engine('postgres://kmrqsesi:SI812NtEmOK6uLeEMethleIXjorohwUB@rajje.db.elephantsql.com:5432/kmrqsesi', echo=False)
titanic = pd.read_csv('titanic.csv')
#commented out to stop my computer from giving me aids by taking an hour per query
#titanic.to_sql('titanic', con=engine, if_exists='replace', index=False)
# df = pd.read_csv(r'./titanic.csv')
# df['Fare'] = df['Fare'].astype(float)
# df['Survived'] = df['Survived'].astype(float)
# df['Age'] = df['Age'].astype(float)
# records = df.to_records(index=False)
# result = list(records)
# #print(result)

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_NAME=os.getenv("DB_NAME")
DB_PW= os.getenv("DB_PW")

pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                         password=DB_PW, host=DB_HOST)
pg_cur = pg_conn.cursor()

# create_table = """
#     CREATE TABLE IF NOT EXISTS titanic(
#         Survived INTEGER,
#         Pclass INTEGER,
#         Name VARCHAR(100),
#         Sex VARCHAR(10),
#         Age INTEGER,
#         Siblings_Spouses_Aboard INTEGER,
#         Parents_Children_Aboard INTEGER,
#         Fare INTEGER
#     )"""

# insertion_query = f"insert into titanic (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) VALUES %s"
# pg_cur.execute(create_table)
# execute_values(pg_cur, insertion_query, result)
# pg_conn.commit()
# pg_conn.close()

total_fare ="""
SELECT count('Sex') as gender
FROM titanic
GROUP BY "Sex"
"""

query = pg_cur.execute(total_fare)
query = pg_cur.fetchall()
print(query)