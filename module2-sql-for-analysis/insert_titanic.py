from psycopg_info import titanic_host, titanic_pass, titanic_user_db
import psycopg2
import pandas as pd

# Load Dataframe
df = pd.read_csv('titanic.csv')

# Open connection and create cursor
pg_conn = psycopg2.connect(dbname=titanic_user_db, user=titanic_user_db,
                           password=titanic_pass, host=titanic_host)
pg_curs = pg_conn.cursor()

# Clean items from Names that would cause problems
df['Name'] = df['Name'].str.replace('(', '_').str.replace(')', '_')
df['Name'] = df['Name'].str.replace("'", ' ')

# Create table format
create_titanic_table = '''
CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age FLOAT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare FLOAT
);
'''
# Create Table
pg_curs.execute(create_titanic_table)

# Create list to pull data from
titanic_list = []
for i in df.index:
    titanic_list.append(df.iloc[i, :].tolist())

# For loop to insert data (with yucky tricket replace to make it
# look like it should)
for i in titanic_list:
    insert_titanic_data = '''
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age,
    Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES''' + str(i).replace('[', '(').replace(']', ')') + ';'
    pg_curs.execute(insert_titanic_data)

pg_curs.close()
pg_conn.commit()
