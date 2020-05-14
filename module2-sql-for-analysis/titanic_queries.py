# titanic_queries.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
import sqlite3

load_dotenv()

# Set path to titanic data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')


DB_HOST = os.getenv("DB_HOST2", default="You Don't Belong Here")
DB_NAME = os.getenv("DB_NAME2", default="You Don't Belong Here")
DB_USER = os.getenv("DB_USER2", default="You Don't Belong Here")
DB_PASSWORD = os.getenv("DB_PW2", default="You Don't Belong Here")

# Check that .env file is working correctly
# print(DB_HOST)
# print(DB_NAME)
# print(DB_USER)
# print(DB_PASSWORD)

# Create connection to database
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
                              password=DB_PASSWORD, host=DB_HOST)
print(f"CONNECTION: {type(connection)}")

# Create cursor
cursor = connection.cursor()
print(f"CURSOR {type(cursor)}")

# Create New Table using titanic data
# 1. Read in csv file
# 2. Convert csv file to sql
# 3. Add new table to sql connection
# 4. Add data to titanic table
# 5. Explore titanic data using sql commands

# Read in titanic dataset
titanic_df = pd.read_csv(DATA_PATH)
print(titanic_df.head(1))
print(titanic_df.columns)
# Index(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']

# Rename some of the columns for easy acces later
titanic_df.rename(columns={'Siblings/Spouses Aboard' : 'sibspouse', 'Parents/Children Aboard' : 'parentchild'}, inplace=True)

# Check that rename worked
print(titanic_df.columns)

# Change datatypes to avoid insertion errors
titanic_df['Survived'] = titanic_df['Survived'].values.astype(bool)
titanic_df = titanic_df.astype("object")

# Create New Table using SQL commands
create_titanic_table = """
                DROP TABLE IF EXISTS 
                    titanic_data;
                CREATE TABLE IF NOT EXISTS
                    titanic_data (
                    id SERIAL PRIMARY KEY,
                    survived BOOL, 
                    pclass INT, 
                    name VARCHAR(100), 
                    sex VARCHAR(30), 
                    age FLOAT, 
                    sibspouse INT, 
                    parentchild INT, 
                    fare FLOAT
                    );
                """
# Execute create table commands
cursor.execute(create_titanic_table)

#
# Now to insert the data!
#

# Create insertion query plugging in column names in order wanted
insertion_query = f"INSERT INTO titanic_data (survived, pclass, name, sex, age, sibspouse, parentchild, fare) VALUES %s"

# Convert titanic dataframe to list of tuples 
list_of_tuples = list(titanic_df.to_records(index=False))

# Run execute values for easy conversion to SQL data insertion commands
execute_values(cursor, insertion_query, list_of_tuples)

#
# Save the Changes
#
connection.commit()

# titanic_queries.py

#Imports
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
import sqlite3

load_dotenv()

# Set path to titanic data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')


DB_HOST = os.getenv("DB_HOST2", default="You Don't Belong Here")
DB_NAME = os.getenv("DB_NAME2", default="You Don't Belong Here")
DB_USER = os.getenv("DB_USER2", default="You Don't Belong Here")
DB_PASSWORD = os.getenv("DB_PW2", default="You Don't Belong Here")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
                              password=DB_PASSWORD, host=DB_HOST)
print(f"CONNECTION: {type(connection)}")

# Create cursor
cursor = connection.cursor()
print(f"CURSOR {type(cursor)}")

#
# Perform some data exploration
#


get_survived = """
                     SELECT
                        survived
                     FROM 
                        titanic_data
                     """

get_dead_count = """
                 SELECT 
                    count(survived) as death_count
                 FROM 
                    titanic_data
                 WHERE 
                    survived = False;
                 """

get_1st_class_count = """
                      SELECT 
                          count(pclass) as first_class
                      FROM
                          titanic_data
                      WHERE
                          pclass = 1
                      """

get_2nd_class_count = """
                      SELECT 
                          count(pclass) as second_class
                      FROM
                          titanic_data
                      WHERE
                          pclass = 2
                      """

get_3rd_class_count = """
                      SELECT 
                          count(pclass) as third_class
                      FROM
                          titanic_data
                      WHERE
                          pclass = 3
                      """

get_male_count = """
                 SELECT
                     count(sex) as male_count
                 FROM
                     titanic_data
                 WHERE
                     sex = 'male'
                 """

get_female_count = """
                   SELECT
                     count(sex) as female_count
                   FROM
                     titanic_data
                   WHERE
                     sex = 'female'
                   """

survived = cursor.execute(get_survived).fetchall()
dead_count = cursor.execute(get_dead_count).fetchall()
first_class_count = cursor.execute(get_1st_class_count).fetchall()
second_class_count = cursor.execute(get_2nd_class_count).fetchall()
third_class_count = cursor.execute(get_3rd_class_count).fetchall()
male_counts = cursor.execute(get_male_count).fetchall()
female_counts = cursor.execute(get_female_count).fetchall()

for row in survived:
    print(f"Number of survivors: {row['survived']}")
for row in dead_count:
    print(f"Number of non-survivors: {row['death_count']}")
for row in first_class_count:
    print(f"Number of 1st class passengers: {row['first_class']}")
for row in second_class_count:
    print(f"Number of 2nd class passengers: {row['second_class']}")
for row in third_class_count:
    print(f"Number of 3rd class passengers: {row['third_class']}")
for row in male_counts:
    print(f"Number of male passengers: {row['male_count']}")
for row in female_counts:
    print(f"Number of female passengers: {row['female_count']}")
    
cursor.close()
connection.close()
