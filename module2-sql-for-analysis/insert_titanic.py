import psycopg2
import sqlite3
import pandas as pd

dbname = 'fclyzfoe'
user = 'fclyzfoe'
password = 'YWxPKJ_aQaznjFA-6MJm2r1hsSugsIrX'
host = 'rajje.db.elephantsql.com'
sl_conn = sqlite3.connect('titanic_db')
sl_curs = sl_conn.cursor()
create_table = 'CREATE TABLE titanic_table (Survived, Pclass, Name, Sex, Age, Siblings_Spouses, Parents, Fare);'
sl_conn.commit()
titanic_df = pd.read_csv(
    'https://raw.githubusercontent.com/DavidVollendroff/'
    'DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
condition = titanic_df['Name'].str.contains("'")
titanic_df = titanic_df[~condition]
titanic_df.to_sql('titanic_table', sl_conn)
get_data = "SELECT * FROM titanic_table"
titanic_data = sl_curs.execute(get_data).fetchall()
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)
pg_curs = pg_conn.cursor()
pg_curs.execute(
    "CREATE TABLE titanic_table (Survived INT, Pclass INT, Name VARCHAR(100),"
    " Sex VARCHAR(100), Age DECIMAL, Siblings_Spouses INT, Parents INT, Fare DECIMAL);")
insert_row = """
    INSERT INTO titanic_table
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses, Parents, Fare)
    VALUES """ + str([row[1:] for row in titanic_data])[1:-1]

pg_curs.execute(insert_row)

pg_conn.commit()
