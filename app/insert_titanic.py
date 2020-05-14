# app/insert_titanic.py

# connect to the db
# make a table
# read the csv file, transform the data
#insert data into the table

import os
import json
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
load_dotenv()
import pandas as pd
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

#1 connect to the db
#Postgre connection

RPGE_NAME = os.getenv("RPGE_NAME")
RPGE_USER = os.getenv("RPGE_USER")
RPGE_PASSWORD = os.getenv("RPGE_PASSWORD")
RPGE_HOST = os.getenv("RPGE_HOST")

pg_connection = psycopg2.connect(dbname=RPGE_NAME, user=RPGE_USER, password=RPGE_PASSWORD, host=RPGE_HOST)
#print("CONNECTION:", pg_connection)

pg_cursor = pg_connection.cursor()
#print("CURSOR:", pg_cursor)

# titanic csv filepath

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")

#2 make a table

# creating a new table

create_table = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers(
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR NOT NULL,
    gender VARCHAR NOT NULL,
    age FLOAT,
    sib_spouse_count INT,
    parent_child_count INT,
    fare FLOAT
);
"""

pg_cursor.execute(create_table)


# read the csv file, transform the data

df = pd.read_csv(CSV_FILEPATH)
#print(df.head())

#insert data into the table


insert = """
INSERT INTO passengers
(survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare)
VALUES %s
"""
rows_to_insert =  df.to_records(index=False)

execute_values(pg_cursor, insert, rows_to_insert)
pg_connection.commit()


query_1_1 = """
SELECT COUNT (survived)
FROM passengers
WHERE survived = 1
"""

pg_cursor.execute(query_1_1)
number_1_1= pg_cursor.fetchall()
print("survived:", number_1_1)

query_1_2 = """
SELECT COUNT (survived)
FROM passengers
WHERE survived = 0
"""

pg_cursor.execute(query_1_2)
number_1_2 = pg_cursor.fetchall()
print("Didn't survive:", number_1_2)
# queries to insert

"""
--How many passengers survived, and how many died?
--survived - 342
SELECT COUNT (survived)
FROM passengers
WHERE survived = 1

-- didn't survive - 545

SELECT COUNT (survived)
FROM passengers
WHERE survived = 0

--How many passengers were in each class?
--class = 3 - 487
SELECT COUNT ("name")
FROM passengers
WHERE pclass = 3

--class = 2 - 184
SELECT COUNT ("name")
FROM passengers
WHERE pclass = 2

--class = 1 - 216

SELECT COUNT ("name")
FROM passengers
WHERE pclass = 1


--What was the average age of survivors vs nonsurvivors?
--avg age of survivors - 28.4083918128655

SELECT AVG(age) as average_age_survived
FROM passengers
WHERE survived = 1

--avg age of non survivors - 30.1385321100917

SELECT AVG(age) as avg_age_non_survived
from passengers
WHERE survived = 0

--What was the average age of each passenger class?

--average age of class 1 - 38.7889814814815

SELECT AVG (age) as p1_class_average_age
FROM passengers
WHERE pclass = 1

--average age of class 2 - 29.8686413043478

SELECT AVG(age) as p2_class_average_age
FROM passengers
WHERE pclass = 2

--average age of class 3 - 25.1887474332649

SELECT AVG(age) as p3_class_average_age
FROM passengers
WHERE pclass = 3

--What was the average fare by passenger class? By survival?

--avg fare of p1 class - 84.1546874999999

SELECT AVG(fare) as avg_fare_p1_class
FROM passengers
WHERE pclass = 1

--avg fare of p2 class - 20.6621831521739

SELECT AVG(fare) as avg_fare_p2_class
FROM passengers
WHERE pclass = 2

--avg fare of p3 class - 13.7077073921971

SELECT AVG(fare) as avg_fare_p3_class
FROM passengers
WHERE pclass = 3

--avg fare of survivors - 48.3954076023392

SELECT AVG(fare) as avg_fare_survivors
FROM passengers
WHERE survived = 1

--avg fare of non survivors - 22.2085840366972

SELECT AVG(fare) as avg_fare_non_survivors
FROM passengers
WHERE survived = 0


--How many siblings/spouses aboard on average, by passenger class? By survival?

--average sibilings/spouces aboard p1 class - 0.41666666666666666667

SELECT AVG(sib_spouse_count) as avg_s_s_p1
FROM passengers
WHERE pclass = 1


--averare sibilings/spouces aboard p2 class - 0.40217391304347826087

SELECT AVG(sib_spouse_count) as avg_s_s_p2
FROM passengers
WHERE pclass = 2


--averare sibilings/spouces aboard p2 class - 0.62012320328542094456

SELECT AVG(sib_spouse_count) as avg_s_s_p3
FROM passengers
WHERE pclass = 3

--averare sibilings/spouces aboard survived - 0.47368421052631578947

SELECT AVG(sib_spouse_count) as avg_s_s_s
FROM passengers
WHERE survived = 1

--average sibilings/spouces aboard didn't survive - 0.55779816513761467890

SELECT AVG(sib_spouse_count) as avg_s_s_n_s
FROM passengers
WHERE survived = 0

--How many parents/children aboard on average, by passenger class? By survival?

--average parent/children aboard p1 class - 0.35648148148148148148

SELECT AVG(parent_child_count) as avg_p_c_p1
FROM passengers
WHERE pclass = 1


--average parent/children aboard p2 class - 0.38043478260869565217

SELECT AVG(parent_child_count) as avg_p_c_p2
FROM passengers
WHERE pclass = 2



--average parent/child aboard p3 class - 0.39630390143737166324

SELECT AVG(parent_child_count) as avg_p_c_p3
FROM passengers
WHERE pclass = 3

--averagearent/child aboard survived - 0.46491228070175438596

SELECT AVG(parent_child_count) as avg_p_c_s
FROM passengers
WHERE survived = 1

--average parent/child aboard didn't survive - 0.33211009174311926606

SELECT AVG(parent_child_count) as avg_p_c_s
FROM passengers
WHERE survived = 0


--Do any passengers have the same name? - No
SELECT "name",
COUNT(DISTINCT id)  AS num_of_occurance
FROM passengers
GROUP BY "name"
ORDER BY num_of_occurance DESC
LIMIT 5
"""