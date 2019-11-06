"""
Connects the Titanic dataset to psycopg2 and uploads it.
"""

import psycopg2
import pandas as pd

dbname = 'fill'
user = 'fill'
password = 'fill'
host = 'fill'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()
curs.execute("CREATE TYPE gender AS ENUM ('male', 'female', 'other');")

create_table = """CREATE TABLE titanic (
                    id SERIAL PRIMARY KEY,
                    Survived BOOL,
                    Pclass INT,
                    Name VARCHAR(100),
                    Sex gender,
                    Age FLOAT,
                    Siblings_Spouses_Aboard INT,
                    Parents_Children_Aboard INT,
                    Fare FLOAT);
               """


curs.execute(create_table)

df = pd.read_csv('titanic.csv')
df['Survived'] = df['Survived'].astype(bool)

df2 = df.replace("'", '"', regex=True)

for i in range(len(df2)):
    row = df2.loc[i]
    insert_row = """
        INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES """ + str(tuple(row)) + ';'
    curs.execute(insert_row)

curs.close()
conn.commit()

curs = conn.cursor()
curs.execute('SELECT * FROM titanic ORDER BY id;')
rows = curs.fetchall()

df3 = df2.copy()
df3 = df3.reset_index()
df3 = df3.rename(columns={'index': 'id'})
df3['id'] = df3['id'] + 1

survived = df3['Survived'].tolist()
survived_bool = [bool(number) for number in survived]
df3['Survived'] = survived_bool

df3_rows = []
for i in range(len(df3)):
    row = df3.loc[i]
    df3_rows.append(tuple(row))

for row, df3_row in zip(rows, df3_rows):
    assert row == df3_row

curs.close()
conn.commit()