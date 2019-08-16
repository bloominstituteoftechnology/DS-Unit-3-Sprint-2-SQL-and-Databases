import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    'DS-Unit-3-Sprint-2-SQL-and-Databases-master/module2-sql-for-analysis/titanic.csv'
    )

# Apostrophes are problems, so they are removed
df['Name'] = df['Name'].str.replace("'", '')
# Make changes to column titles to meet convention and remove / and spaces
df.columns = df.columns.str.replace('/', '_').str.replace(' ', '_').str.lower()

dbname = 'ywzfehtm'
user = 'ywzfehtm'
password = 'BLANK'  # Don't commit this!
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute(create_passenger_table)

engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}/{dbname}'
    )

df.to_sql('titanic', engine, if_exists='replace')

pg_conn.commit()

pg_curs.execute('SELECT COUNT(*) FROM titanic;')
pg_curs.fetchall()
