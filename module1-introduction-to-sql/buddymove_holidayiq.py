''' Making and populating a Database'''
import sqlite3
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape)

#Creating connection to a new database file
conn = sqlite3.connect("boddymove_holidayiq.sqlite3")


# Insert data into new table review in sqlite3 database
#df.to_sql(name= 'review', con=conn)

curs = conn.cursor()
#Count how many rows 
query1 = "SELECT count(*) FROM review;"
results = curs.execute(query1).fetchall()
print(results)  

 #How many users who reviewed at least 100 Nature in the category
 #  also reviewed at least 100 in the Shopping category?   

query2 ='''SELECT count(*) 
          FROM review 
          WHERE Nature > 100 AND Shopping > 100;'''

results2 = curs.execute(query2).fetchall()
print(results2)

#What are the average number of reviews for each category?
query3 = '''
          SELECT avg(Sports), avg(Religious), avg(Nature),
          avg(Theatre),avg(Shopping)
          FROM review;
          '''
results3 = curs.execute(query3).fetchall()
print(results3)
