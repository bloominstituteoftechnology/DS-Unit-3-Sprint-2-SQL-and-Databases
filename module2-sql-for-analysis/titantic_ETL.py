#!/usr/bin/env python
# coding: utf-8

# ## Live Lecture Task
# 
# Yesterday we used a simple local workflow with SQLite - today, we'll work on
# inserting the same RPG data into a more production-style PostgreSQL database
# running on a server. We will use [psycopg](http://initd.org/psycopg/), a Python
# library for connecting to PostgreSQL, and specifically we will install
# [psycopg2-binary](https://pypi.org/project/psycopg2-binary/).
# 
# Once we get the data inserted, we will continue exploring querying as yesterday,
# first answering the same questions and then going deeper. We'll also explore
# some of the specific functions that are different in PostgreSQL than SQLite.
# 
# ## Assignment
# 
# Reproduce (debugging as needed) the live lecture task of setting up and
# inserting the RPG data into a PostgreSQL database, and add the code you write to
# do so.
# 
# Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
# thinking about the schema to make sure it is appropriate for the columns.
# [Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
# be useful. Once it is set up, write a `insert_titanic.py` script that uses
# `psycopg2` to connect to and upload the data from the csv, and add the file to
# your repo. Then start writing PostgreSQL queries to explore the data!

# In[230]:


import pandas as pd
import psycopg2
import sqlite3


# In[231]:


# don't commit this 
dbname = 'stppkqaz'
user = 'stppkqaz'
password = '8SmasUR6fET2bcgKxng7y7Xre5d6fIwp' 
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

# connection object and cursor
pg_conn
pg_curs = pg_conn.cursor()


# In[232]:


# extract: csv file
titanic_csv = 'titanic.csv'
df = pd.read_csv(titanic_csv)

df['Name'] = df['Name'].str.replace("'", "")

# create connection to blank sql 'titanic.sqlite3'
conn = sqlite3.connect('titanic.sqlite3')

# thus extract data from df to sql file
df.to_sql('titanic', conn, index=False, if_exists='replace') # Insert the values from the csv file into the table 'X'


# In[233]:


# look at table 
curs = conn.cursor()
query = 'SELECT * FROM titanic LIMIT 20'
pd.read_sql(query, conn)


# In[234]:


t_curs = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'

t_curs.execute(query).fetchall()


# In[235]:


# our goal - an ETL/data pipeline from SQLite to Python
titanic = t_curs.execute('SELECT * FROM titanic;').fetchall()


# In[236]:


# validate what we got
titanic[0]


# In[237]:


# look at data types
t_curs.execute('PRAGMA table_info(titanic);').fetchall()


# In[238]:


# extract done! next step, transform:
# we need the postgresql db to have a table
# with an appropriate schema

# we need a serial primary key as it's what links
# all the tables together
create_titanic_table = """
    CREATE TABLE titanic (
        id SERIAL PRIMARY KEY, 
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex VARCHAR(10),
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare REAL
);

"""


# In[239]:


# create pg table
pg_curs.execute(create_titanic_table)


# In[240]:


str(titanic[0])


# In[241]:


# transform (making the target ready to get data) done

# now we need to insert actual characters
# example first

example_insert = """
INSERT INTO titanic
(Survived, PClass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
VALUES """ + str(titanic[0])

print(example_insert)


# In[242]:


# now do this for all characters

for row in titanic: # this refers to titanic in row 25
    
    insert_titanic = """
        INSERT INTO titanic
        (Survived, PClass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES """ + str(titanic[0]) + ';'
    
    pg_curs.execute(insert_titanic)
    


# In[243]:


pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()


# In[245]:


# we can see it from this cursor but not elephantsql.com
# we must commit

pg_curs.close()
pg_conn.commit()

