"""
transfering titanic dataset into elephantsql
"""

import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

df = pd.read_csv('titanic.csv')

df['Siblings/Spouses Aboard'].rename('siblingsspouse', axis=1)
df['Parents/Children Aboard'].rename('parentschildren', axis=1)

df['Name'] = df['Name'].str.replace("'", "")

dbname = 'zgexitff'
user = 'zgexitff'
password = 'XXX'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()


create_titanic_table = """
DROP TABLE IF EXISTS Titanic;
CREATE TABLE Titanic (
    index INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    siblingsspouse INT,
    parentschildren INT,
    Fare REAL
);
"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()

# get_titanic = "SELECT * FROM titanic;"
# st_curs.execute(get_titanic)
# titanic_data = st_curs.fetchall()
#
# for titanic in titanic_data:
#     insert_data = """
#         INSERT INTO titanic8
#         (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
#         VALUES """ + str(titanic[1:]) + ";"
#     pg_curs.execute(insert_data)

execute_values(pg_curs, """
INSERT INTO Titanic
(Survived, Pclass, Name, Sex, Age, siblingsspouse, parentschildren, Fare)
VALUES %s;
""", [tuple(row) for row in df.values])


pg_conn.commit()

# pg_curs.execute('SELECT * FROM titanic7 LIMIT 5;')
# titanic_pg = pg_curs.fetchall()

# show_table = """
# SELECT *
# FROM pg_catalog.pg_tables
# """
#
# pg_curs.execute(show_table)

pg_curs.execute("""
SELECT *
FROM Titanic
LIMIT 1;
""")

print(pg_curs.fetchall())

