import psycopg2
import sqlite3
import csv

dbname = 'ejnhvpax'
user = 'ejnhvpax'
password = 'BLANK'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

""" How many passengers survived, and how many died?"""

query1 = '''SELECT Survived, COUNT(*) 
            FROM titanic 
            GROUP BY Survived
            ORDER BY Survived DESC;'''

""" How many passengers were in each class?"""

query2 = '''SELECT Pclass, COUNT(*) 
            FROM titanic 
            GROUP BY Pclass
            ORDER BY Pclass ASC;'''

""" How many passengers survived/died within each class?"""

query3 = '''SELECT Pclass, Survived, COUNT(*) 
            FROM titanic 
            GROUP BY Pclass, Survived
            ORDER BY Survived DESC, Pclass ASC;'''

""" What was the average age of survivors vs nonsurvivors?"""

query4 = '''SELECT AVG(Age), Survived
            FROM titanic 
            GROUP BY Survived
            ORDER BY Survived DESC;'''

""" What was the average age of each passenger class?"""

query5 = '''SELECT AVG(Age), Pclass
            FROM titanic 
            GROUP BY Pclass
            ORDER BY Pclass ASC;'''

""" What was the average fare by passenger class? By survival?"""

query6 = '''SELECT AVG(Fare), Pclass
            FROM titanic 
            GROUP BY Pclass
            ORDER BY Pclass ASC;'''

query7 = '''SELECT AVG(Fare), Survived
            FROM titanic 
            GROUP BY Survived
            ORDER BY Survived ASC;'''

""" How many siblings/spouses aboard on average, by passenger class? By survival?"""

query8 = '''SELECT AVG(siblings_spouses_aboard), Pclass
            FROM titanic 
            GROUP BY Pclass
            ORDER BY Pclass ASC'''


query9 = '''SELECT AVG(siblings_spouses_aboard), Survived
            FROM titanic 
            GROUP BY Survived
            ORDER BY Survived ASC'''

""" How many parents/children aboard on average, by passenger class? By survival?"""


query10 = '''SELECT AVG(parents_children_aboard), Pclass
            FROM titanic 
            GROUP BY Pclass
            ORDER BY Pclass ASC'''

query11 = '''SELECT AVG(parents_children_aboard), Survived
            FROM titanic 
            GROUP BY Survived
            ORDER BY Survived ASC'''

""" Do any passengers have the same name?"""

query12 = '''SELECT SUM(total.ct) FROM
            (SELECT a.first_name, COUNT(*) AS ct
            FROM 
            (SELECT split_part(name, ' ', 2) AS first_name
            FROM titanic) as a
            GROUP BY a.first_name
            HAVING COUNT(*) > 1) as total'''


def postgre_fetch(pg_conn):
    pg_curs2 = pg_conn.cursor()

    #Question 1
    pg_curs2.execute(query1)
    rows1 = pg_curs2.fetchall()
    rows_result1 = [x[1] for x in rows1]
    labels1 = ['survived','died']
    for label, row in zip(labels1, rows_result1):
        print(f'Total number of passengers who {label}: {row}')

    #Question 2
    
    pg_curs2.execute(query2)
    rows2 = pg_curs2.fetchall()
    rows_result2 = [x[1] for x in rows2]
    labels2 = ['class 1','class 2', 'class 3']
    for label, row in zip(labels2, rows_result2):
        print(f'Total number of passengers who are in {label}: {row}')

    #Question 3

    pg_curs2.execute(query3)
    rows3 = pg_curs2.fetchall()
    rows_result3 = [x[2] for x in rows3]
    labels3 = ['in class 1 who survived','in class 2 who survived', 'in class 3 who survived', 'in class 1 who died', 'in class 2 who died', 'in class 3 who died']
    for label, row in zip(labels3, rows_result3):
        print(f'Total number of passengers who are {label}: {row}')

    #Question 4

    pg_curs2.execute(query4)
    rows4 = pg_curs2.fetchall()
    rows_result4 = [x[0] for x in rows4]
    labels4 = ['survived', 'died']
    for label, row in zip(labels4, rows_result4):
        print(f'Average age of those who {label}: {row:.2f}')


    #Question 5

    pg_curs2.execute(query5)
    rows5 = pg_curs2.fetchall()
    rows_result5 = [x[0] for x in rows5]
    labels5 = ['class 1', 'class 2', 'class 3']
    for label, row in zip(labels5, rows_result5):
        print(f'Average age of those who were in {label}: {row:.2f}')


    #Question 6
    
    pg_curs2.execute(query6)
    rows6 = pg_curs2.fetchall()
    rows_result6 = [x[0] for x in rows6]
    labels6 = ['class 1', 'class 2', 'class 3']
    for label, row in zip(labels6, rows_result6):
        print(f'Average fare of those who were in {label}: {row:.2f}')

    pg_curs2.execute(query7)
    rows7 = pg_curs2.fetchall()
    rows_result7 = [x[0] for x in rows7]
    labels7 = ['died', 'survived']
    for label, row in zip(labels7, rows_result7):
        print(f'Average fare of those who {label}: {row:.2f}')


    #Question 7

    pg_curs2.execute(query8)
    rows8 = pg_curs2.fetchall()
    rows_result8 = [x[0] for x in rows8]
    labels8 = ['class 1', 'class 2', 'class 3']
    for label, row in zip(labels8, rows_result8):
        print(f'Average no. of siblings, spouses of those who were in {label}: {row:.2f}')


    pg_curs2.execute(query9)
    rows9 = pg_curs2.fetchall()
    rows_result9 = [x[0] for x in rows9]
    labels9 = ['died', 'survived']
    for label, row in zip(labels9, rows_result9):
        print(f'Average no. of siblings, spouses of those who {label}: {row:.2f}')

    #Question 8

    pg_curs2.execute(query10)
    rows10 = pg_curs2.fetchall()
    rows_result10 = [x[0] for x in rows10]
    labels10 = ['Class 1', 'Class 2', 'Class 3']
    for label, row in zip(labels10, rows_result10):
        print(f'Average no. of parents, children aboard of those who were in {label}: {row:.2f}')

    pg_curs2.execute(query11)
    rows11 = pg_curs2.fetchall()
    rows_result11 = [x[0] for x in rows11]
    labels11 = ['died', 'survived']
    for label, row in zip(labels11, rows_result11):
        print(f'Average no. of parents, children aboard of those who {label}: {row:.2f}')

    
    #Question 9

    pg_curs2.execute(query12)
    rows12 = pg_curs2.fetchall()
    for row in rows12:
        print(f'Total number of people with the same name: {row[0]}')


    pg_curs2.close()
    pg_conn.commit()

postgre_fetch(pg_conn)