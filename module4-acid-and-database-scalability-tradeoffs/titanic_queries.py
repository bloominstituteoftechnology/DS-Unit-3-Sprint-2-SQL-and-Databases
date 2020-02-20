import sqlite3
import pandas as pd

DB_FILEPATH = '/Users/josephbell/Desktop/sql-practice/titanic.csv'

df = pd.read_csv(DB_FILEPATH)
connection = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic', connection)
cursor = connection.cursor()
# How many passengers survived?
query = 'SELECT COUNT(Survived) FROM titanic WHERE survived = 1'
result = cursor.execute(query).fetchall()
print(result, 'passengers survived')
# How many passengers died?
query = 'SELECT COUNT(Survived) FROM titanic WHERE survived = 0'
result = cursor.execute(query).fetchall()
print(result, 'passengers died')
# How many passengers were in each class?
query = 'SELECT Pclass, COUNT(Pclass) FROM titanic GROUP BY Pclass'
result = cursor.execute(query).fetchall()
print('Number of passengers from each class:', result)
# How many passengers survived within each class?
query = 'SELECT Pclass, COUNT(Pclass) FROM titanic WHERE Survived = 1 GROUP BY Pclass'
result = cursor.execute(query).fetchall()
print('Number of passengers that survived within each class')
# How many passengers died within each class?
query = 'SELECT Pclass, COUNT(Pclass) FROM titanic WHERE Survived = 0 GROUP BY Pclass'
result = cursor.execute(query).fetchall()
print('Number of passengers that died within each class')
# Average age of survivors?
query = 'SELECT avg(Age) FROM titanic WHERE Survived = 1'
result = cursor.execute(query).fetchall()
print('Average age of survivors:', result)
# Average age of nonsurvivors?
query = 'SELECT avg(Age) FROM titanic WHERE Survived = 0'
result = cursor.execute(query).fetchall()
print('Average age of survivors:', result)
# Average age of each passenger class?
query = 'SELECT Pclass, avg(Age) FROM titanic GROUP BY Pclass'
result = cursor.execute(query).fetchall()
print('Average age by passenger class:', result)
# Average fare of each passenger class?
query = 'SELECT Pclass, avg(Fare) FROM titanic GROUP BY Pclass'
result = cursor.execute(query).fetchall()
print('Average fare by passenger class:', result)
# Average fare by survival?
query = 'SELECT Survived, avg(Fare) FROM titanic GROUP BY Survived'
result = cursor.execute(query).fetchall()
print('Average fare by survival:', result)
# Average siblings/spouses aboard?
query = """SELECT Pclass, avg("Siblings/Spouses Aboard") FROM titanic GROUP BY Pclass"""
result = cursor.execute(query).fetchall()
print('Average siblings/spouse aboard by passenger class:', result)
# Average siblings/spouses aboard by survival?
query = """SELECT Survived, avg("Siblings/Spouses Aboard") FROM titanic GROUP BY Survived"""
result = cursor.execute(query).fetchall()
print('Average siblings/spouse aboard by survival:', result)
# Average parents/children aboard by passenger class?
query = """SELECT Pclass, avg("Parents/Children Aboard") FROM titanic GROUP BY Pclass"""
result = cursor.execute(query).fetchall()
print('Average parents/children aboard by passenger class:', result)
# Average parents/children aboard by survival?
query = """SELECT Survived, avg("Parents/Children Aboard") FROM titanic GROUP BY Survived"""
result = cursor.execute(query).fetchall()
print('Average parents/children aboard by survival:', result)
