import pandas as pd
import psycopg2 as pg
from setup import dbname,user, host, password,url

dbname = dbname
user = user
host = host
password = password
url = url

def elephant_query(dbname,user,host,password,query):
    pg_conn = pg.connect(dbname=dbname,user=user,host= host,password = password)
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    result = pg_curs.fetchall()
    pg_conn.commit()
    pg_curs.close()
    pg_conn.close()
    print(result)


one = """
SELECT survived, COUNT(survived)
FROM titanic
GROUP BY survived
"""

two = """
SELECT "Pclass", COUNT("Pclass")
FROM titanic
GROUP BY "Pclass"
"""
three = """
SELECT "Pclass", COUNT("Pclass")
FROM titanic
GROUP BY "Pclass"
"""

four = """
SELECT "Pclass", COUNT("Pclass")
FROM titanic
GROUP BY "Pclass"
"""
five = """
SELECT "Pclass", AVG(age)
FROM titanic
GROUP BY "Pclass"
"""

six = """
SELECT "Pclass", AVG(fare)
FROM titanic
GROUP BY "Pclass"
"""

seven = """
SELECT survived, AVG(fare)
FROM titanic
GROUP BY survived
"""
eight = """
SELECT "Pclass", AVG(siblings_spouses_aboard)
FROM titanic
GROUP BY "Pclass"
"""
nine = """
SELECT survived, AVG(siblings_spouses_aboard)
FROM titanic
GROUP BY survived
"""
ten = """
SELECT survived, AVG(parents_children_aboard)
FROM titanic
GROUP BY survived
"""
eleven = """
SELECT survived, AVG(parents_children_aboard)
FROM titanic
GROUP BY survived
"""
twelve = """
SELECT name, COUNT(name)
FROM titanic
GROUP BY name
HAVING COUNT(name) >1
"""

thirteen = """
SELECT name, siblings_spouses_aboard, age
FROM titanic
"""


