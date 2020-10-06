import psycopg2
import sqlite3
import pandas as pd

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

curs.execute('CREATE TABLE titanic (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)')
conn.commit()

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].apply(lambda x: x.replace("'", "''"))

df.to_sql('titanic', conn, if_exists ='replace', index= False)