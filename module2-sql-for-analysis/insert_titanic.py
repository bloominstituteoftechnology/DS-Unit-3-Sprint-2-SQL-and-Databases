import psycopg2
import pandas as pd

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host)

df = pd.read_csv('titanic.csv')
df['Survived'] = df['Survived'].map({0:False, 1:True})


create_titanic_table = """
    CREATE TABLE titanic (
        survived BOOLEAN,
        pclass smallint,
        name varchar,
        sex varchar,
        age smallint,
        siblings_spouses smallint,
        parents_children smallint,
        fare float
    );
"""

# Create table
pg_curs = pg_conn.cursor()
try:
    pg_curs.execute(create_titanic_table)
    print('created table')
except:
    print('failed to create table')
finally:
    pg_curs.close()
    pg_conn.commit()

# Insert Passengers
pg_curs = pg_conn.cursor()
try:
    for index,value in df.iterrows():
        if("'" in value[2]):
            value[2] = value[2].replace("'", "\"")

        insert_passenger = """
            INSERT INTO titanic
            (survived, pclass, name, sex , age, siblings_spouses, parents_children, fare)
            VALUES {};""".format(tuple(value))
        pg_curs.execute(insert_passenger)
    print('Inserted all passengers')
except:
    print('failed to insert passengers')
finally:
    pg_curs.close()
    pg_conn.commit()
