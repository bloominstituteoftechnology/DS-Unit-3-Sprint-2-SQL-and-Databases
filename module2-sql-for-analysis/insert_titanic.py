import psycopg2
import pandas as pd 

"""
This script will take a local csv and insert the data into
a postgreSQL table
"""

# Database info
dbname = 'jehgnrff'
user = 'jehgnrff'
password = '21Al2FjnMu8SMSi6q505r4qfFZ7JLGTO'
host = 'otto.db.elephantsql.com'

# Initialzie connection and cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

# Retrieve data
PATH = 'C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv'

df = pd.read_csv(PATH)

# Add index column SQL congruancy and rename
df = df.reset_index()
df = df.rename(columns={'index':'person_id'})

# Replace apostrophe's in 'Name' to prevent SQL new column
df['Name'] = df['Name'].map(lambda x: x.replace("'", ''))

# Construct list of all the rows for later insertion
people = []
for i in range(len(df)):
    people.append(tuple(df.loc[i]))

# Store table creation string as variable
create_table = '''
    CREATE TABLE titanic (
        person_id SERIAL PRIMARY KEY,
        survived INT,
        pclass INT,
        name TEXT,
        sex CHAR(7),
        age FLOAT(2),
        siblings_spouses_aboard INT,
        parents_children_aboard INT,
        fare NUMERIC(8,5)
    );
'''

# Send instructions to create table
pg_curs.execute(create_table)

# Send looped INSERT intructions to table
for person in people:
    insert_data = '''
        INSERT INTO titanic
        (survived, pclass, name, sex, age, siblings_spouses_aboard,
         parents_children_aboard, fare)
         VALUES ''' + str(person[1:]) + ';'
    pg_curs.execute(insert_data)

# Close cursor and commit to database
pg_curs.close()
pg_conn.commit()
