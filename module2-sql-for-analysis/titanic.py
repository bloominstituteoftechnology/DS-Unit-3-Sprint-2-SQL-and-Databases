import psycopg2

dbname = 'zaddfkaj'
user = 'zaddfkaj'
password = 'PvcjNh59KEhsprLQnRCfJ0uAn2La90R9'
host = 'rajje.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

q = '''
  CREATE TABLE peeps (
    survived INTEGER,
    pclass INTEGER,
    name TEXT,
    sex TEXT,
    age INTEGER,
    sibspouse INTEGER,
    parchil INTEGER,
    fare REAL
  )
'''
curs.execute(q)

import pandas as pd
df = pd.read_csv('titanic.csv')

for k, row in df.iterrows():
  vals = f"{row['Survived']}, {row['Pclass']}, %s, '{row['Sex']}', {row['Age']}, {row['Siblings/Spouses Aboard']}, {row['Parents/Children Aboard']}, {row['Fare']}"
  q = f"INSERT INTO peeps (survived, pclass, name, sex, age, sibspouse, parchil, fare) VALUES ({vals});"
  curs.execute(q, (row['Name'],))

curs.close()
conn.commit()