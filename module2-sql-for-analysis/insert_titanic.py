import psycopg2
import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv

connect = sqlite3.connect('insert_titanic.sqlite3')
cursor = connect.cursor()

df = pd.read_csv('titanic.csv')

df.to_sql('titanic', connect)

cursor.execute('SELECT COUNT(*) FROM titanic')
print('1. ', cursor.fetchall())

cursor.execute('SELECT COUNT(*)')
print('2. ', cursor.fetchall())

load_dotenv()

DB_NAME = os.getenv("DB_NAME2")
DB_USER = os.getenv("DB_USER2")
DB_PASS = os.getenv("DB_PASS2")
DB_HOST = os.getenv("DB_HOST2")

conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)

cursor2 = conn.cursor()

sl_conn = sqlite3.connect("titanic.csv")
sl_cursor = sl_conn.cursor()
titanic = sl_cursor.execute('SELECT * FROM titanic.csv LIMIT 10').fetchall()
print(titanic)

titanic_query = '''
CREATE TABLE IF NOT EXISTS titanic (
    Name,
	Survived,
	Pclass,
	Sex,
	Age,
	Siblings/Spouses Aboard, 
	Parents/Children Aboard,
	Fare
)
'''

cursor.execute(titanic_query)
conn.commit()

for character in titanic:

    insert_query = f''' INSERT INTO titanic 
        (Name, Survived, Pclass, Sex, Age, Siblings/Spouses Aboard, Parents/Children Aboard, Fare) VALUES
        {character}
    '''
    cursor2.execute(insert_query)

conn.commit()
