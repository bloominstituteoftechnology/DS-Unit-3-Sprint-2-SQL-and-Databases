import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import numpy as np

#connect to titanic db
load_dotenv()

HOST = os.getenv('TITANIC_HOST')
NAME = os.getenv('TITANIC_NAME')
USER = os.getenv('TITANIC_USER')
PASSWORD = os.getenv('TITANIC_PASSWORD')

con = psycopg2.connect(dbname = NAME, 
                        user = USER, 
                        password = PASSWORD, 
                        host = HOST)

cur = con.cursor()

# sanity checks comment out later
print('Sanity Checks')
print('--------------------------------------------')
print('Con:', con)
print('Cur:', cur)

# set up the os agnostic path
TITANIC_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 
                            'titanic.csv')

# Load into pandas
df = pd.read_csv(TITANIC_PATH)

# for MVP, just dump all the titanic CSV into your postgres db
# create a titanic table.
# not sure how to do this programmatically, so I'm just going to hard
# code it.  Less than ideal.
create_table = '''
CREATE TABLE passengers (
    survived INTEGER
    ,pclass INTEGER
    ,name VARCHAR(100)
    ,sex VARCHAR(10)
    ,age INTEGER
    ,siblings_spouse INTEGER
    ,parents_children INTEGER
    ,fare MONEY
);
'''

cur.execute(create_table)

# Insert dataframe into titanic table, use execute_values to avoid
# running a query for each line
insertion_query = '''
INSERT INTO passengers (
    survived
    ,pclass
    ,name
    ,sex
    ,age
    ,siblings_spouse
    ,parents_children
    ,fare
) VALUES %s
'''

# this sucks and I don't like it.  But psycopg does not recognize numpy
# data types, so I have to register the np.int64 data type so it knows how to
# handle it. For my future self, just run a bunch of insertion queries, or just
# append the database using .to_sql() from the data frame.
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# prep dataframe for execute_values.  Should be a list of tuples
prepped = list(df.to_records(index = False))

execute_values(cur, insertion_query, prepped)

# Exploratory queries/sanity checks
print('--------------------------------------------')

q1 = '''
SELECT count(name) as length
FROM passengers
'''

cur.execute(q1)
res = cur.fetchone()

print('Dataframe length', df.shape[0])
print('Database length', res[0])

q2 = '''
SELECT
    name
    ,sex
    ,age
    ,fare
FROM passengers
LIMIT 5
'''

cur.execute(q2)
res2 = cur.fetchall()


print('--------------------------------------------')
for i in range(len(res2)):
    print(res2[i])

columns = ['Name', 'Sex', 'Age', 'Fare']
print(df[columns][:5])

# Stretch actually split this up into appropriate tables
# like a passenger table, survivors table, class tables, etc
# TODO 

#commented out for testing
#con.commit()
cur.close()
con.close()