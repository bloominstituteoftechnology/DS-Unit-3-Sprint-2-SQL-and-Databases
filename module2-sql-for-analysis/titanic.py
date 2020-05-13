# import appropriate modules
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# load contents of the .env file into the script's environment
load_dotenv()

# Read in the data from the local file path or website
df = pd.read_csv('C:/Users/kingf/Unit3/DS-Unit-3-Sprint-2-SQL-and-\
Databases/module2-sql-for-analysis/titanic.csv')
print(df.shape) # print the shape to ensure we have right rows and columns
print(df.head()) # print the head to ensure right format

print("----------")
# Open a connection to ElephantSQL postgreSQL database
DB_NAME = os.getenv('DB_NAME', default='OOPS')
DB_USER = os.getenv('DB_USER', default='OOPS')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='OOPS')
DB_HOST = os.getenv('DB_HOST', default='OOPS')

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST)
print("CONNECTION: ", connection)

# Create engine to use for df.to_sql
#engine = create_engine('postgres://suerwyip:mNWaqz...@drona.db.elephantsql.com\
#:5432/suerwyip')

# Use df.to_sql to insert the data into a new table 'titanic' in the PostgrSQL 
#. database
df.to_sql('titanic', engine)
conn = engine.raw_connection()

# How many passengers survived?
number_survived_query = '''
SELECT  count(survived) as count_survived
FROM    titanic
WHERE   survived = 1;
'''
total_survivors = cursor.execute(number_survived_query).fetchone()
print("----------")
print('Total # of Survivors:', total_survivors[0])

# How many passengers died?
number_died_query = '''
SELECT  count(survived) as count_died
FROM    titanic
WHERE   survived = 0;
'''
total_dead = cursor.execute(number_died_query).fetchone()
print("----------")
print('Total # of People who Died:', total_dead[0])


conn.commit()