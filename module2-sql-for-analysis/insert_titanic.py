import pandas as pd
import psycopg2
import sqlite3
from csv import DictReader
import csv

"""
# DictReader : 
# Looks similar to sqlite3, but needs auth/host info to connect
# Note - this is sensitive info (particularly password)
"""
"""change csv to sqlite"""
df = pd.read_csv("titanic.csv")
df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
              'Parents/Children Aboard', 'Fare']
"""
insert data into new table
"""
connection = sqlite3.connect('titanics.sqlite3')
df.to_sql('review', connection, index=False)
# DB_FILEPATH = "titanic.sqlite3"
# sl_conn = sqlite3.connect(DB_FILEPATH)
# sl_curs = sl_conn.cursor()
"""
Connect to the elphant database
"""
dbname = 'vbmmjeoc'
user = 'vbmmjeoc'  # ElephantSQL happens to use same name for db and user
password = 'qiPPfJeCLmtX5-yUZcV27SmlTz75PQka'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
"""
cursor - check rows
"""
cursor = connection.cursor()
cursor.execute('SELECT * FROM review').fetchall()
print(df.shape)
print(df.head)
cursor.execute('PRAGMA table_info(review);')
cursor.fetchall()
# Defining a function to refresh connection and cursor
"""def refresh_conn_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs
pg_conn, pg_curs = refresh_conn_and_cursor(pg_conn, pg_curs)"""
# A bunch of integers, and a varchar
# We need to make a create statement for PostgreSQL that captures this
create_titanic_table = """
CREATE TABLE titanic (
  Survived INTEGER,
  Pclass INTEGER,
  Name VARCHAR(30),
  Sex TEXT,
  Age REAL,
  Siblings_Spouses_Aboard INTEGER,
  Parent_Childeren_Aboard INTEGER,
  Fare REAL
);
"""
for row in df:
    cursor.execute(
        """
                    INSERT INTO 
                        passengers (
                            survived, 
                            name, 
                            pclass, 
                            sex, 
                            age, 
                            siblings_spouse_count, 
                            parents_children_count, 
                            fare
                        ) 
                    VALUES 
                        (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s   
                        );
                """,
        (
            row['Survived'],
            row['Name'],
            row['Pclass'],
            row['Sex'],
            row['Age'],
            row['Siblings/Spouses Aboard'],
            row['Parents/Children Aboard'],
            row['Fare']
        )
    )
    print(df)
# Execute the create table
pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()
# pandas to records
pg_curs.execute("""
CREATE TYPE SEX_SEX AS ENUM ('male', 'female');
CREATE TABLE abc (
  id SERIAL PRIMARY KEY,
  survived BOOLEAN NOT NULL, 
  pclass INTEGER NOT NULL,
  name varchar(255) NOT NULL,
  sex SEX_SEX NOT NULL,
  age DECIMAL NOT NULL, 
  siblings_spouse_count INTEGER NOT NULL,
  parents_children_count INTEGER NOT NULL,
  fare DECIMAL NOT NULL
);
""")
# NOTE - these types are PostgreSQL specific. This won't work in SQLite!
# iterate over each line as a ordered dictionary and print only few column by column name
# https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/ (Documentation)
# with open('titanic.csv', 'r') as read_obj:
#     csv_dict_reader = DictReader(read_obj)
#     for row in csv_dict_reader:
#         pg_curs.execute(
with open('titanic.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pg_curs.execute(
            """
                INSERT INTO 
                    abc (
                        survived, 
                        name, 
                        pclass, 
                        sex, 
                        age, 
                        siblings_spouse_count, 
                        parents_children_count, 
                        fare
                    ) 
                VALUES 
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s   
                    );
            """,
            (
                row['Survived'],
                row['Name'],
                row['Pclass'],
                row['Sex'],
                row['Age'],
                row['Siblings/Spouses Aboard'],
                row['Parents/Children Aboard'],
                row['Fare']
            )
        )
pg_conn.commit()  # "Save" by committing
pg_curs.close()
pg_conn.close()  # If we were really done
