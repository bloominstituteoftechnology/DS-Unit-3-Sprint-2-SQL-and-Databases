import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()

# connecting to the elephant sql titanic db
TITANIC_DB_NAME = os.getenv('TITANIC_DB_NAME', default='oops')
TITANIC_DB_USER = os.getenv('TITANIC_DB_USER', default='oops')
TITANIC_DB_PASSWORD = os.getenv('TITANIC_DB_PASSWORD', default='oops')
TITANIC_DB_HOST = os.getenv('TITANIC_DB_HOST', default='oops')
connection = psycopg2.connect(dbname=TITANIC_DB_NAME, host=TITANIC_DB_HOST, password=TITANIC_DB_PASSWORD, user=TITANIC_DB_USER)
cursor = connection.cursor()


# How many passengers survived, and how many died?
query = "SELECT survived, count(distinct id) from titanic GROUP BY survived"
cursor.execute(query)
result = cursor.fetchall()

for each in result:
  if each[0] == 1:
    print(f'{each[1]} passengers survived.')
  else:
    print(f'{each[1]} passengers died.')

# How many passengers were in each class?
query = "SELECT pclass, count(distinct id) from titanic GROUP BY pclass"
cursor.execute(query)
result = cursor.fetchall()

for each in result:
  if each[0] == 1:
    print(f'\n{each[1]} passengers were in first class.')
  elif each[0] == 2:
    print(f'{each[1]} passengers were in second class.')
  else:
    print(f'{each[1]} passengers were in third class.')

# How many passengers survived/died within each class?
query = "SELECT pclass, count(distinct id) from titanic WHERE survived = 1 GROUP BY pclass"
cursor.execute(query)
survived_result = cursor.fetchall()

query = "SELECT pclass, count(distinct id) from titanic WHERE survived = 0 GROUP BY pclass"
cursor.execute(query)
died_result = cursor.fetchall()

for each in died_result:
  if each[0] == 1:
    dead_first = each[1]
  elif each[0] == 2:
    dead_second = each[1]
  else:
    dead_third = each[1]

for each in survived_result:
  if each[0] == 1:
    print(f'\nIn first class {each[1]} passengers survived and {dead_first} died.')
  elif each[0] == 2:
    print(f'In second class {each[1]} passengers survived and {dead_second} died.')
  else:
    print(f'In third class {each[1]} passengers survived and {dead_third} died.')



# What was the average age of survivors vs nonsurvivors?

# What was the average age of each passenger class?

# What was the average fare by passenger class? By survival?

# How many siblings/spouses aboard on average, by passenger class? By survival?

# How many parents/children aboard on average, by passenger class? By survival?

  
# Do any passengers have the same name?

'''
(Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.
  '''



cursor.close()
connection.close()