# Import sqlite3 for access to sql
# Import pandas for dataframe manipulation
# Import psycopg2 for access to postgreSQL

import sqlite3
import pandas as pd
import psycopg2


# Database name
dbname = 'eorspaxd'

# Username (e.g. Elephant SQL)
user = 'eorspaxd'

# Password
password = ''

# Server url (e.g. salt.db.elephantsql.com)
host = 'salt.db.elephantsql.com'

# wget https://raw.githubusercontent.com/justin-hsieh/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv


df = pd.read_csv('https://raw.githubusercontent.com/SarmenSinanian/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')


df['Name'] = df['Name'].str.replace("'", '', regex=True)
print(df.columns)
df.columns = df.columns.str.replace('/', "_")
df.columns = df.columns.str.replace(" ", '_')
print(df.columns)
print(df.shape)

# Establishing connection to sql table
conn = sqlite3.connect('titanic.sqlite3')
# Creating dataframe  to sql
df.to_sql('titanic', conn, index=False)
# Make cursor for sql
curs = conn.cursor()
# Save results from execution of sql command on sql table
titanic_data = curs.execute('SELECT * FROM titanic').fetchall()
print(titanic_data)

# Establish connection to postgreSQL
p_conn = psycopg2.connect(dbname = dbname, user=user, password=password, host=host)
# Make cursor for postgreSQL
p_curs = p_conn.cursor()
# Create table in postgreSQL
p_titanic_query = '''
    CREATE TABLE titanic(
        Survived INT,
        Pclass INT,
        Name VARCHAR(250),
        Sex VARCHAR(10),
        Age INT,
        Siblings_Spouses_Aboard INT,
        Parents_children_Aboard INT,
        Fare REAL
        )
    '''
# Execute query to create titanic table in postgreSQL WITH proper variables/columns
p_curs.execute(p_titanic_query)

# For loop which reuses the columns structure/schema and enters each row of the titanic_data as a string, then
# the cursor executes the "insert passenger" sql command on each loop
for passenger in titanic_data:
    insert_passenger = '''
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES
    ''' + str(passenger[:]) + ';'
    p_curs.execute(insert_passenger)

# Closing the cursor
p_curs.close()
# Committing the connection/changes
p_conn.commit()
# End of operation print statement
print('complete')