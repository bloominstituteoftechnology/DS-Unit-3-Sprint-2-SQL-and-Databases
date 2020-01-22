import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.replace(' ', '_')
df.Name = df.Name.str.replace("'", '')

dbname = 'tjqpupzb'
user = 'tjqpupzb'
password = 'ExCV1Zaq1teecCPRXMCo9lA-wetfjcCO' #Don't commit or share for security purposes
host = 'rajje.db.elephantsql.com' #Port should be included or default

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

create_enum = "CREATE TYPE sex AS ENUM ('male', 'female');"
curs.execute(create_enum)
conn.commit()

create_table = '''
    CREATE TABLE titanic(
        survived int,
        pclass int,
        name text,
        sex sex,
        age int,
        siblings_or_spouses_aboard int,
        parents_or_children_aboard int,
        fare float
    );
'''
curs.execute(create_table)
conn.commit()

for index, r in df.iterrows():
    insert_item = f'''INSERT INTO titanic VALUES {
        r.Survived, r.Pclass, r.Name, r.Sex,
        r.Age, r.Siblings_Spouses_Aboard,
        r.Parents_Children_Aboard, r.Fare};'''
    curs.execute(insert_item) 
conn.commit()