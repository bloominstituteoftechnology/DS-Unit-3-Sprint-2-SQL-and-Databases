#!/usr/bin/env python
"""Inserting titanic data into postgres database"""

import psycopg2 as psg
import pandas as pd
from credentials import DBNAME, USER, PASSWORD, HOST
from collections import defaultdict

conn = psg.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

"""
Survived int,
Pclass int,
Name varchar(255),
Sex sex,
Age real,
Siblings_Spouses_Aboard int,
Parents_Children_Aboard int,
Fare real
"""
print('How many passengers survived, and how many died?')
command = """
    SELECT COUNT(*)
    FROM titanic
    WHERE Survived = 1;
    """
cur.execute(command)
print(f'Passengers survived {cur.fetchall()[0][0]}')

command = """
    SELECT COUNT(*)
    FROM titanic
    WHERE Survived = 0;
    """
cur.execute(command)
print(f'Passengers died {cur.fetchall()[0][0]}')

print('\nHow many passengers were in each class?')
command = """
    SELECT Pclass, COUNT(Pclass)
    FROM titanic
    GROUP BY Pclass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has passenger count {int(value[1])}')

print('\nHow many passengers survived/died within each class?')
command = """
    SELECT Pclass, COUNT(Pclass)
    FROM titanic
    WHERE Survived = 1
    GROUP BY Pclass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has survival count {int(value[1])}')

command = """
    SELECT Pclass, COUNT(Pclass)
    FROM titanic
    WHERE Survived = 0
    GROUP BY Pclass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has died count {int(value[1])}')

print('\nWhat was the average age of survivors vs nonsurvivors?')
command = """
    SELECT AVG(Age)
    FROM titanic
    WHERE Survived = 1;
    """
cur.execute(command)
print(f'Passengers survived avg age {int(cur.fetchall()[0][0])}')

command = """
    SELECT AVG(Age)
    FROM titanic
    WHERE Survived = 0;
    """
cur.execute(command)
print(f'Passengers died avg age {int(cur.fetchall()[0][0])}')

print('\nWhat was the average age of each passenger class?')
command = """
    SELECT PClass, AVG(Age)
    FROM titanic
    GROUP BY Pclass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has avg age {int(value[1])}')

print('\nWhat was the average fare by passenger class? By survival?')
command = """
    SELECT Pclass, AVG(Fare)
    FROM titanic
    GROUP BY Pclass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has avg fare {round(value[1], 2)}')

command = """
    SELECT Survived, AVG(Fare)
    FROM titanic
    GROUP BY Survived;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Survived {value[0]} has avg fare {round(value[1], 2)}')

print('\nHow many siblings/spouses aboard on average, by passenger class? '
      'By survival?')
command = """
    SELECT Pclass, AVG(Siblings_Spouses_Aboard)
    FROM titanic
    GROUP BY PClass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has avg siblings/spouses aboard \
{round(value[1], 2)}')

command = """
    SELECT Survived, AVG(Siblings_Spouses_Aboard)
    FROM titanic
    GROUP BY Survived;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Survived {value[0]} has avg siblings/spouses aboard \
{round(value[1], 2)}')

print('\nHow many parents/children aboard on average, by passenger class? '
      'By survival?')
command = """
    SELECT Pclass, AVG(Parents_Children_Aboard)
    FROM titanic
    GROUP BY PClass;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Class {value[0]} has avg parents/children aboard \
{round(value[1], 2)}')

command = """
    SELECT Survived, AVG(Parents_Children_Aboard)
    FROM titanic
    GROUP BY Survived;
    """
cur.execute(command)
for value in cur.fetchall():
    print(f'Survived {value[0]} has avg parents/children aboard \
{round(value[1], 2)}')

print('\nDo any passengers have the same name?')
command = """
    SELECT A.Name, B.Name
    FROM titanic as A, titanic as B
    WHERE (A.Name = B.Name
           AND NOT (A.Survived = B.Survived
                    AND A.Pclass = A.Pclass
                    AND A.Sex = B.Sex
                    AND A.Age = B.Age
                    AND A.Siblings_Spouses_Aboard = B.Siblings_Spouses_Aboard
                    AND A.Parents_Children_Aboard = B.Parents_Children_Aboard
                    AND A.Fare = B.Fare)
          )
    """

command = """
    SELECT Name
    FROM titanic
    WHERE Name IN (SELECT Name
                   FROM titanic
                   GROUP BY Name HAVING COUNT(*) > 1);
    """
command = """
    SELECT Name
    FROM titanic
    GROUP BY Name HAVING COUNT(*) > 1;
    """
cur.execute(command)
for value in cur.fetchall():
    print(value)

print('\nHow many married couples were aboard the Titanic?')
command = """
    SELECT Name
    FROM titanic
    WHERE Siblings_Spouses_Aboard > 0
    AND NAME LIKE 'Mr%';
    """
cur.execute(command)

last_name_dict = defaultdict(list)
for full_name in cur.fetchall():
    last_name = full_name[0].split(' ')[-1]
    last_name_dict[last_name].append(full_name)

for last_name, full_names in last_name_dict.items():
    if len(full_names) == 2:
        print(full_names)
    elif len(full_names) > 2:
        print('\nNeeds additional processing')
        print(full_names)
        print('Needs additional processing end\n')

