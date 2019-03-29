import sqlite3
import pandas
import psycopg2


'''converts titanic.csv to sqlite3 and then to psycopg2'''


'''formatting dataframe'''
df = pd.read_csv('titanic.csv')
df = df.rename(columns={"Siblings/Spouses Aboard":"Siblings_or_Spouse",
                        "Parents/Children Aboard":"Parents_or_Children"})


'''converting from csv to sqlite3'''
conn = sqlite3.connect('titanic.sqlite3')
cursor = conn.cursor()
df.to_sql('titanic', conn, index=True, if_exists='replace')
conn.commit()


'''permissions for psycopg2, connect'''
user = 'cfiwxdhp'
dbname = 'cfiwxdhp'
password = '9GYie0tbijLrBM_HgZJWPiz3KuMCZtzS'
host = 'isilo.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_cursor = pg_conn.cursor()


'''make Sex into an enumerated type'''
type_gender = """CREATE TYPE gender as ENUM ('female', 'male');"""
cursor.execute(type_gender)


'''define psycopg2 table properties'''
create_table = """CREATE TABLE titanic (index INT PRIMARY KEY,
                                        Survived INT,
                                        Pclass INT,
                                        Name VARCHAR(50),
                                        Sex gender,
                                        Age INT,
                                        Siblings_or_Spouse INT,
                                        Parents_or_Children INT,
                                        Fare REAL);"""
pg_cursor.execute(create_table)


'''loop that copies sqlite3 rows into pg table'''
passengers = cursor.execute('SELECT * FROM titanic;').fetchall()
for passenger in passengers:
    insert_passenger = """INSERT INTO titanic
                          (Survived,
                           Pclass,
                           Name,
                           Sex,
                           Age,
                           Siblings_or_Spouse,
                           Parents_or_Children,
                           Fare)
                           VALUES """
                           + str(passenger[1:])
    pg_cursor.execute(insert_passenger)
pg_conn.commit()


 '''confirmation a given row in sqlite3 and psycopg2 are equal'''
pg_cursor.execute('SELECT * FROM titanic;')
pg_passengers = pg_cursor.fetchall()
print(passengers[0])
print(pg_passengers[0])
