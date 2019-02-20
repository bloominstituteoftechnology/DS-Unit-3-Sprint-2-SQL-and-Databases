import psycopg2
import pandas as pd

psycopg2.connect

dbname = ''
user = ''
password = ''
host = ''

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
postgres_cursor = conn.cursor()
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

postgres_cursor.execute(create_titanic_table)
conn.commit()

for item in titanic_list:
    insert_item = """INSERT INTO titanic (
    survived, pclass, name, sex, age, siblings_spouses_aboard,
    parents_children_aboard, fare)
    VALUES""" + str(tuple(item))
    postgres_cursor.execute(insert_item)

conn.commit()