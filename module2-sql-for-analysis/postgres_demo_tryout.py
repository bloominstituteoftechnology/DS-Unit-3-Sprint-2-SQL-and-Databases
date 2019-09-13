
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("ELEPHANT_PW")

dbname = 'htcgadjc'
user = 'htcgadjc'
host = ('salt.db.elephantsql.com')

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute("SELECT * FROM staff;")
all_staff = pg_curs.fetchall()

for staff in all_staff:
    print(staff)

print('*********************')

pg_curs.execute("SELECT * FROM charactercreator_character LIMIT 10;")
characters = pg_curs.fetchall()

for character in characters:
    print(character)
