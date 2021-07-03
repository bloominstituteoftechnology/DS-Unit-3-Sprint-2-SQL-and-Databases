#!/usr/bin/env python3

import psycopg2

dbname = 'nhworfxj'
user = 'nhworfxj'
password = 'kP5yE4IqyZ80aWYuhHUkPzrTCrvetxgP'
host = 'balarama.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)
curs = conn.cursor()

print('Question 1: How many passengers survived, and how many died?')
query = """ 
SELECT Survived, COUNT(*)
FROM titanic
GROUP BY Survived;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 2: How many passengers were in each class?')
query = """ 
SELECT Pclass, COUNT(*)
FROM titanic
GROUP BY Pclass;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 3: How many passengers survived/died within each class?')
query = """ 
SELECT Survived, Pclass, COUNT(*)
FROM titanic
GROUP BY Survived, Pclass;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 4: What was the average age of survivors vs nonsurvivors?')
query = """ 
SELECT Survived, ROUND(AVG(Age),2)
FROM titanic
GROUP BY Survived;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 5: What was the average age of each passenger class?')
query = """ 
SELECT Pclass, ROUND(AVG(Age),2)
FROM titanic
GROUP BY Pclass;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 6: What was the average fare by passenger class? By survival?')
query = """ 
SELECT Pclass, AVG(Fare)
FROM titanic
GROUP BY Pclass;
"""
curs.execute(query)
print(curs.fetchall())

query = """ 
SELECT Survived, AVG(Fare)
FROM titanic
GROUP BY Survived;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 7: How many siblings/spouses aboard on average, by passenger class? By survival?')
query = """ 
SELECT Pclass, AVG(siblings_or_spouses_aboard)
FROM titanic
GROUP BY Pclass;
"""
curs.execute(query)
print(curs.fetchall())

query = """ 
SELECT Survived, AVG(siblings_or_spouses_aboard)
FROM titanic
GROUP BY Survived;
"""
curs.execute(query)
print(curs.fetchall())

print('Question 8: How many parents/children aboard on average, by passenger class? By survival?')
query = """ 
SELECT Pclass, AVG(parents_or_children_aboard)
FROM titanic
GROUP BY Pclass;
"""
curs.execute(query)
print(curs.fetchall())

query = """ 
SELECT Survived, AVG(parents_or_children_aboard)
FROM titanic
GROUP BY Survived;

"""
curs.execute(query)
print(curs.fetchall())

print('Question 9: How many passengers have the same name?')
query = """ 
SELECT COUNT(Name) - COUNT (DISTINCT Name)
FROM titanic;
"""
curs.execute(query)
print(curs.fetchall())

curs.close()
conn.commit()
