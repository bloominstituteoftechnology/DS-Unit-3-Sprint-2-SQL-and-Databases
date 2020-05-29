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
query = "SELECT * from titanic"
cursor.execute(query)
print(cursor.fetchall())


# How many passengers were in each class?

# How many passengers survived/died within each class?

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