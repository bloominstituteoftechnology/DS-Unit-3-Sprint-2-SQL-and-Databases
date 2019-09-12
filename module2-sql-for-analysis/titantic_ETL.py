import pandas as pd
import psycopg2
import sqlite3

# don't commit this 
dbname = ''
user = ''
password = '' 
host = ''

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

# connection object and cursor
pg_conn
pg_curs = pg_conn.cursor()

# extract: csv file
titanic_csv = 'titanic.csv'
df = pd.read_csv(titanic_csv)

df['Name'] = df['Name'].str.replace("'", "")

# create connection to blank sql 'titanic.sqlite3'
conn = sqlite3.connect('titanic.sqlite3')

# thus extract data from df to sql file
df.to_sql('titanic', conn, index=False, if_exists='replace') # Insert the values from the csv file into the table 'X'

# look at table 
curs = conn.cursor()
query = 'SELECT * FROM titanic LIMIT 20'
pd.read_sql(query, conn)


t_curs = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'

t_curs.execute(query).fetchall()


# our goal - an ETL/data pipeline from SQLite to Python
titanic = t_curs.execute('SELECT * FROM titanic;').fetchall()


# validate what we got
titanic[0]


# look at data types
t_curs.execute('PRAGMA table_info(titanic);').fetchall()



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


# create pg table
pg_curs.execute(create_titanic_table)


str(titanic[0])


# transform (making the target ready to get data) done

# now we need to insert actual characters
# example first

example_insert = """
INSERT INTO titanic
(Survived, PClass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
VALUES """ + str(titanic[0])

print(example_insert)


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


# we can see it from this cursor but not elephantsql.com
# we must commit

pg_curs.close()
pg_conn.commit()

