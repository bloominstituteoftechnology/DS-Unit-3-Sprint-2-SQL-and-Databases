import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')



print(df.head(1).T)

dbname = 'xzxvsmya'
user = 'xzxvsmya'
password = ''  # Don't commit!
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

create_titantic_table = """
CREATE TABLE titantic (
  id SERIAL PRIMARY KEY,
  Survived INT ,
  Pclass INT,
  Name varchar(50),
  Sex varchar (5),
  Age INT,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare float 
)
"""

pg_curs.execute(create_titantic_table)

#df.to_sql('titantic',pg_conn)
record = tuple(df.loc[0])
print(record)

insert_titantic_record = """
  INSERT INTO titantic
  (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
  VALUES""" + str(record)

pg_curs.execute(insert_titantic_record)
pg_conn.commit()