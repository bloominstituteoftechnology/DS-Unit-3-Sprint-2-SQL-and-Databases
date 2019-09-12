import psycopg2
import sqlite3
import pandas as pd

dbname = 'wpjclngs'
user = 'wpjclngs'
# pword = ''
host = 'salt.db.elephantsql.com'

con = psycopg2.connect(dbname=dbname, user=user, password=pword, host=host)
curs = con.cursor()

curs.execute('SELECT * FROM titanic WHERE survived = 1')

survived = len(curs.fetchall())

curs.execute('SELECT * FROM titanic WHERE survived = 0')

died = len(curs.fetchall())

curs.execute('SELECT AVG(age) FROM titanic WHERE survived = 1')

avgAgeLive = curs.fetchall()[0][0]

curs.execute('SELECT AVG(age) FROM titanic WHERE survived = 0')

avgAgeDie = curs.fetchall()[0][0]

curs.execute('SELECT AVG(age) FROM titanic WHERE pclass = 1')

avgAgeClass1 = curs.fetchall()[0][0]

curs.execute('SELECT AVG(age) FROM titanic WHERE pclass = 2')

avgAgeClass2 = curs.fetchall()[0][0]

curs.execute('SELECT AVG(age) FROM titanic WHERE pclass = 3')

avgAgeClass3 = curs.fetchall()[0][0]

curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass = 1')

avgFareClass1 = curs.fetchall()[0][0]

curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass = 2')

avgFareClass2 = curs.fetchall()[0][0]

curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass = 3')

avgFareClass3 = curs.fetchall()[0][0]
