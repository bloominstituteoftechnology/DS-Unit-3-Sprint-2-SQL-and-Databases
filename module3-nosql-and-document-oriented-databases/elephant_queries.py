
import psycopg2

DB_NAME = 'DS 23.DB'
DB_USER = 'tlrztomk'
DB_PASSWORD = 'bc7MwOEWu6dNtmiBc8Cn8vbXCMOttZst'
DB_HOST = 'ziggy.db.elephantsql.com'
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
print("CONNECTION", connection)

cursor.execute('SELECT * from test_table;')
print("CURSOR", cursor)

result = cursor.fetchall()
print(result)
