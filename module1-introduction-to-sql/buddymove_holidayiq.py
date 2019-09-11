import pandas as pd
import sqlite3
from pandas import DataFrame 

df = pd.read_csv('/Users/elliotgunn/Desktop/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.shape

conn = sqlite3.connect('buddymove_holidayiq.sqlite3.db')
c = conn.cursor()

df.to_sql('review', conn, if_exists='replace', index = False) # Insert the values from the csv file into the table 'X'

# look at table 
curs = conn.cursor()
query = 'SELECT * FROM review LIMIT 20'
pd.read_sql(query, conn)

# count rows: 249
curs.execute('''
SELECT count(*)
FROM review
''')
print(curs.fetchall())

# How many users who reviewed at least 100 Nature in the category 
# also reviewed at least 100 in the Shopping category?
# answer = 78

curs2 = conn.cursor()
query = '''
SELECT count(*)
FROM review 
WHERE Nature >= 100 AND Shopping >= 100'''
# pd.read_sql(query, conn)
print('Users who reviewed at least 100 in the Nature and 100 Shopping categories:', curs2.execute(query).fetchone()[0])

# Stretch: What are the average number of reviews for each category?
curs3 = conn.cursor()
query = '''
SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review
'''
print(curs3.execute(query).fetchall())
print('average sports reviews:', curs3.execute(query).fetchall()[0][0])
print('average religious reviews:', curs3.execute(query).fetchall()[0][1])
print('average nature reviews:', curs3.execute(query).fetchall()[0][2])
print('average theatre reviews:', curs3.execute(query).fetchall()[0][3])
print('average shopping reviews:', curs3.execute(query).fetchall()[0][4])
print('average picnic reviews:', curs3.execute(query).fetchall()[0][5])


