#!/usr/bin/env python
"""Inserting titanic data into postgres database"""

import psycopg2 as psg
import pandas as pd
from credentials import DBNAME, USER, PASSWORD, HOST

# Create table
create_titanic_table = """
CREATE TYPE sex AS ENUM ('male', 'female');

CREATE TABLE titanic (
    Survived int,
    Pclass int,
    Name varchar(255),
    Sex sex,
    Age real,
    Siblings_Spouses_Aboard int,
    Parents_Children_Aboard int,
    Fare real
);"""

conn = psg.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

cur.execute(create_titanic_table)

df = pd.read_csv('titanic.csv')
value_str = ""

for i in range(df.shape[0]):
    value_str = ""
    value = df.loc[i, :].values
    value[2] = value[2].replace("'", " ")
    value_str += str(tuple(value))
    insert_result = """INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, \
        Parents_Children_Aboard, Fare)
    VALUES""" + value_str

    cur.execute(insert_result)

conn.commit()
