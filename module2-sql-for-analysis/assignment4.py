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


DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_NAME=os.getenv("DB_NAME")
DB_PW= os.getenv("DB_PW")

pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                         password=DB_PW, host=DB_HOST)
pg_cur = pg_conn.cursor()

query1 = """
SELECT count('Survived')
FROM titanic
GROUP BY "Survived" 
"""

result1 = pg_cur.execute(query1)
results1 = pg_cur.fetchall()

print(results1)


query2 = """
SELECT count('Pclass')
FROM titanic
GROUP BY "Pclass"
"""
result2 = pg_cur.execute(query2)
results2 = pg_cur.fetchall()

print(results2)

#how many passengers survived/died within each class?

query3 = """
SELECT count("Pclass"),
       count("Survived")
FROM titanic
GROUP BY "Survived", "Pclass"
"""

result3 = pg_cur.execute(query3)
results3 = pg_cur.fetchall()
print(results3)

#What was the average age of survivors vs nonsurvivors
query4 = """
SELECT AVG("Age")
FROM titanic
GROUP BY "Survived"
"""
result4 = pg_cur.execute(query4)
results4 = pg_cur.fetchall()
print(results4)

#What is the averate age of each passenger class
query5 = """
SELECT AVG("Age")
FROM titanic
GROUP BY ("Pclass")
"""

result5 = pg_cur.execute(query5)
results5 = pg_cur.fetchall()
print(results5)


#What was the average fare by passenger class?
query6 ="""
SELECT AVG("Fare")
FROM titanic
GROUP BY "Pclass"
"""

result6 = pg_cur.execute(query6)
results6 = pg_cur.fetchall()
print(results6)


#What was the average fare by Survival?

query7 = """
SELECT AVG("Fare")
FROM titanic
GROUP BY ("Survived")
"""

result7 = pg_cur.execute(query7)
results7 = pg_cur.fetchall()
print(results7)

#How many siblings/spouses aboard on average by passenger class?

query8 = """
SELECT AVG("Siblings_Spouses_Aboard"),
       COUNT("Pclass")
FROM titanic
GROUP BY ("Pclass")
ORDER BY ("Pclass")
"""

result8 = pg_cur.execute(query8)
results8 = pg_cur.fetchall()
print(results8)


#How many parents/children aboard on average by passenger class?
query9 = """
SELECT AVG("Parents_Children_Aboard")
FROM titanic
GROUP BY ("Pclass")
"""

result9 = pg_cur.execute(query9)
results9 = pg_cur.fetchall()
print(results9)


#Do any passengers have the same name?
query10 = """
SELECT COUNT(DISTINCT "Name"),
       COUNT("Name")
FROM titanic
"""

result10 = pg_cur.execute(query10)
results10 = pg_cur.fetchall()
print(results10)
#how many married couples where aboard the titanic