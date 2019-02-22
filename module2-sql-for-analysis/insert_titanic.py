import psycopg2 as pg
import pandas as pd
dbname = 'a'
user = 'a'
password = 'v'
host = 'b'
conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()
create_titanic_table = """CREATE TABLE passengers (
   Survived int,
   Pclass int,
   Name varchar(100),
   Sex text,
   Age int,
   Siblings_SpousesAboard int,
   Parents_ChildrenAboard int,
   Fare NUMERIC
)"""
cur.execute(create_titanic_table)
titanic = pd.read_csv('titanic.csv')
titanic.Name = titanic.Name.replace("'", '', regex=True)
titanic_list = titanic.values.tolist()
for item in titanic_list:
    insert_item = """INSERT INTO passengers (
    Survived, Pclass, Name, Sex, Age, Siblings_SpousesAboard,
    Parents_ChildrenAboard, Fare)
    VALUES""" + str(tuple(item))
    cur.execute(insert_item)
conn.commit()
