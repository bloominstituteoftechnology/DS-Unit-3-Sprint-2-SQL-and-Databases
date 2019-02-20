import psycopg2 as pg
import pandas as pd

pg.connect

dbname = 
user = 
password = 
host = 

conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
pg_cur = conn.cursor()
titanic = pd.read_csv('titanic.csv')
titanic.Name = titanic.Name.replace("'", '', regex=True)
titanic_list = titanic.values.tolist()

create_titanic_table = """
CREATE TABLE titanic (
    person_id SERIAL PRIMARY KEY,
    survived int,
    pclass int,
    name varchar(100),
    sex varchar(6),
    age int,
    siblings_spouses_aboard int,
    parents_children_aboard int,
    fare float
 );"""

pg_cur.execute(create_titanic_table)
conn.commit()

for item in titanic_list:
    insert_item = """INSERT INTO titanic (
    survived, pclass, name, sex, age, siblings_spouses_aboard,
    parents_children_aboard, fare)
    VALUES""" + str(tuple(item))
    pg_cur.execute(insert_item)

conn.commit()
