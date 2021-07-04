import sqlite3
import pandas as pd 

"""
IF the database didn't already exist

path = 'C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv'

df = pd.read_csv(path)

conn = sqlite3.connect('buddymove_holiday.sqlite3')

df.to_sql('review', con=conn)

"""

path = 'C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases/buddymove_holidayiq.sqlite3'
conn = sqlite3.connect(path)
curs = conn.cursor()

query = 'SELECT COUNT(Sports) FROM review'
curs.execute(query)
print('Total rows:', curs.fetchall()[0][0])

query = '''SELECT User_id FROM review WHERE Nature >= 100
 AND Shopping >=100'''
curs.execute(query)
print('Ten Users with >=100 in Nature & Shopping:', curs.fetchmany(10))

query = 'SELECT AVG(Sports) FROM review'
curs.execute(query)
print('Average Sports Rating:', curs.fetchall()[0][0])

query = 'SELECT AVG(Religious) FROM review'
curs.execute(query)
print('Average Religious Rating:', curs.fetchall()[0][0])

query = 'SELECT AVG(Nature) FROM review'
curs.execute(query)
print('Average Nature Rating:', curs.fetchall()[0][0])

query = 'SELECT AVG(Theatre) FROM review'
curs.execute(query)
print('Average Theatre Rating:', curs.fetchall()[0][0])

query = 'SELECT AVG(Shopping) FROM review'
curs.execute(query)
print('Average Shopping Rating:', curs.fetchall()[0][0])

query = 'SELECT AVG(Picnic) FROM review'
curs.execute(query)
print('Average Picnic Rating:', curs.fetchall()[0][0])

curs.close()