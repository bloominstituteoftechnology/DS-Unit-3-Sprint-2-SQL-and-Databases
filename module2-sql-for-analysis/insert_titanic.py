import psycopg2
import sqlite3
import pandas as pd
from postgres_info import dbname, user, password, host

# One way
# csv -> sqlite3 -> postgres

# QUESTION: df.to_sql (pd to sqlite) converts types automatically, is this reliable? Or is
# it better to obtain the types first and then create the types manually
# like how we did in lecture when creating the table:

names = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouse_Abroad', 'Parents_Children_Abroad', 'Fare']
df = pd.read_csv('titanic.csv', names=names).drop([0])
# print(df.head())
sqlite_con = sqlite3.connect('titanic.db') # | titanic.sqlite3 if it was a database
df.to_sql('titanic', sqlite_con)
# sqlite_cursor.execute('DELETE FROM titanic WHERE index = 0;').fetchall()
# (select * from titanic;) to verify in DB browser

sqlite_cursor = sqlite_con.cursor()
data = sqlite_cursor.execute('select * from titanic limit 10;').fetchall()
print(data)
# sqlite_con = sqlite3.connect('titanic.db')
# >>> data = sqlite_con.cursor().execute('select * from titanic;').fetchall()
# >>> columns_and_types = [col[1:3] for col in sqlite_cursor.execute('PRAGMA table_info(titanic);').fetchall() if col[1] not in ['index']]

# ------
# to get the dtypes we'll need for the new postgres table, first get the dtypes from sqlite3
# sqlite_cursor.execute('PRAGMA table_info(titanic);').fetchall()
# get_col_info = """
#     SELECT * FROM PRAGMA_TABLE_INFO('titanic');
#     """
# how can we generalize this more? x instead of titanic

# PRAGMA table_info(titanic);
# and
# SELECT * FROM PRAGMA_TABLE_INFO('titanic');
# are equivalent

# columns_and_types = [col[1:3] for col in sqlite_cursor.execute('PRAGMA table_info(titanic);').fetchall() if col[1] not in ['index']]

# move from sqlite3 to postgres, very complicated to get output
# from columns_and_types directly to new, created table so we'll do it manually

# process would be something like this: but..
# for col, dtype in columns_and_types:
    # create_table = """
    # CREATE TABLE titanic (
    #     ) """

# transforming schema
create_postgres_table = """
    CREATE TABLE titanic (
        Survived INTEGER,
        Pclass INTEGER,
        Name TEXT,
        Sex TEXT,
        Age FLOAT,
        Siblings_Spouse_Abroad INTEGER,
        Parents_Children_Abroad INTEGER,
        Fare FLOAT );
        """

postgres_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
postgres_cursor = postgres_conn.cursor()
postgres_cursor.execute(create_postgres_table)

show_table = """
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schemaname';
    """

postgres_cursor.execute(show_table)
postgres_cursor.fetchall()

for obs in data:
    insert_obs = """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouse_Abroad, Parents_Children_Abroad, Fare)
    VALUES {}; """.format(str(obs[1:]))
    postgres_cursor.execute(insert_obs)

postgres_cursor.execute('SELECT * FROM titanic LIMIT 5;')
postgres_cursor.fetchall()

postgres_cursor.close()
postgres_conn.commit()
