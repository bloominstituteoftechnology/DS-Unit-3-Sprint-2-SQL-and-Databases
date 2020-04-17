import os
from sqlalchemy import create_engine
import sqlite3
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


# Set up .env variables to connect to postgres later
envpath = os.path.join(os.path.dirname(__file__),'..', '.env')
print(envpath)
load_dotenv(envpath)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

# set up the connection to postgres
sql_url = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
engine = create_engine(sql_url)
print('ENGINE:', engine)

print('1. How many passengers survived, and how many died?')

query = '''
SELECT
survived as Survived
,count(survived) as SurvivedCount
FROM titanic_data
GROUP BY survived
'''
print(pd.read_sql(query, engine), '\n')

# ----------------------------------------
print('2. How many passengers were in each class?')

query = '''
SELECT
pclass as Class
,count(pclass) as ClassCount
FROM titanic_data
GROUP BY pclass
'''

print(pd.read_sql(query, engine),'\n')

# ----------------------------------------
print('3. How many passengers survived in each class?')

query = '''
SELECT
pclass as Class
,survived as Survived
,count(survived) as SurvivedCount
FROM titanic_data
GROUP BY pclass, survived
ORDER BY Class, Survived
'''

print(pd.read_sql(query, engine), '\n')

# ----------------------------------------
print('4. What was the average age of survivors vs nonsurvivors')

query = '''
SELECT
survived as Survived
,avg(age) as AverageAge
FROM titanic_data
GROUP BY Survived
'''

print(pd.read_sql(query, engine), '\n')


# ----------------------------------------
print('5. What was the average age of each passenger class')

query = '''
SELECT
pclass as Class
,avg(age) as AverageAge
FROM titanic_data
GROUP BY Class
'''

print(pd.read_sql(query, engine), '\n')

# ------------------------------------------
print('6. What was the average fare by passenger class and by survival')

query = '''
SELECT
pclass as Class
,survived as Survived
,avg(fare) as AverageFare
FROM titanic_data
GROUP BY Class, Survived
ORDER BY Class, Survived
'''

print(pd.read_sql(query, engine), '\n')

# ------------------------------------------
print('7. How many siblings/spouses by passenger class and by survival')

query = '''
SELECT
sibling_spouse_aboard as SibSpouseAboard
,survived as Survived
,avg(fare) as AverageFare
FROM titanic_data
GROUP BY SibSpouseAboard, Survived
ORDER BY SibSpouseAboard, Survived
'''

print(pd.read_sql(query, engine), '\n')

# ------------------------------------------
print('7. How many parents/children by passenger class and by survival')

query = '''
SELECT
parent_children_aboard as ParentChildAboard
,survived as Survived
,avg(fare) as AverageFare
FROM titanic_data
GROUP BY ParentChildAboard, Survived
ORDER BY ParentChildAboard, Survived
'''

print(pd.read_sql(query, engine), '\n')

# ---------------------------------------------
print('8. Do any passengers have the same name?')

query = '''
SELECT
*
FROM (
    SELECT
    name as PassengerName
    ,count(name) as NameCount
    FROM titanic_data
    GROUP BY PassengerName
) as sub_table
WHERE NameCount>1
'''

print(pd.read_sql(query, engine), '\n')

# ---------------------------------------------
