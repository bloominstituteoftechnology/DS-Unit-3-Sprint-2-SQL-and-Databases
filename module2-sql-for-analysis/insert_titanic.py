import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')



print(df.head(1).T)

df.Name = df.Name.str.replace("'","''")

print(df.Name)

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
  Name varchar(100),
  Sex varchar (6),
  Age INT,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare float 
)
"""

#pg_curs.execute(create_titantic_table)

#df.to_sql('titantic',pg_conn)

def insert_sql(record):

    insert_titantic_record = """
        INSERT INTO titantic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES""" + str(tuple(record)).replace('"',"\'")
    return insert_titantic_record

for index, row in df.iterrows():
    pg_curs.execute(insert_sql(row))




pg_conn.commit()