import psycopg2
import sqlite3
import pandas as pd

dbname = 'taymbqyq'
user = 'taymbqyq'
password = 'JOslYoz4AmPe2QkmWYVlOpHUWziadEzM'
host = 'rajje.db.elephantsql.com'


# csv to sqlite3 
names = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouse_Abroad', 'Parents_Children_Abroad', 'Fare']
df = pd.read_csv('titanic.csv', names=names).drop([0])
print(df.head())

sqlite_conn = sqlite3.connect('titanic.sqlite3')
sqlite_curs = sqlite_conn.cursor()
#df.to_sql('titanic', sqlite_conn) only once
data = sqlite_curs.execute('select * from titanic Limit 10;').fetchall()
print(data)


#sqlite3 to postgres
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
postgres_curs = postgres_conn.cursor()
postgres_curs.execute(create_postgres_table)       

show_table = """
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schemaname';
    """
postgres_curs.execute(show_table)
postgres_curs.fetchall()

for obs in data:
    insert_obs = """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouse_Abroad, Parents_Children_Abroad, Fare)
    VALUES {}; """.format(str(obs[1:]))
    postgres_curs.execute(insert_obs)
postgres_curs.execute('SELECT * FROM titanic LIMIT 10;')
pg_data = postgres_curs.fetchall()


#connfirming they are the same
for obs, pg_obs in zip(data, pg_data):
    assert obs == pg_obs


postgres_curs.close()
postgres_conn.commit()