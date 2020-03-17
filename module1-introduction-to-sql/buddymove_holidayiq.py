import pandas as pd
import sqlite3

url = 'https://raw.githubusercontent.com/jacobpad/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
con = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = con.cursor()

df = pd.read_csv(url)
df.to_sql('review', con=con)

#-- Count how many rows you have - it should be 249!
query1 = '''
SELECT COUNT(*) FROM review;
'''
result1 = curs.execute(query1).fetchone()[0]
print('\n****RESULT1:****\n-- Count how many rows you have - it should be 249!\n', result1, '\n')

#-- How many users who reviewed at least 100 Nature in 
# the category also reviewed at least 100 in the Shopping category?
query2 = '''
SELECT count('User id') 
FROM review
WHERE Nature >= 100 AND Shopping >= 100;
'''
result2 = curs.execute(query2).fetchone()[0]
print('\n****RESULT2:****\n-- How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category\n', result2, '\n')



