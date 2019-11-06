import psycopg2, os, sqlite3
import pandas as pd
from settings import ELE_DBNAME, ELE_USER, ELE_PASS, ELE_HOST

DF_URL = "titanic.csv"
DB_URL = "titanic.sqlite3"

def pg_query(query, print_out=True):
    pg_curs.execute(query)
    res = pg_curs.fetchone()
    if print_out:
        print(res)
    return res

def make_insert_string(row):
    row = "(" + ", ".join([str(i) if not type(i) == str else "'" + i.replace("'", "") + "'" for i in row]) + ")"
    return """INSERT INTO titanic (index, Survived, Pclass, Name, Sex, Age, "Siblings/Spouses", "Parents/Children", Fare) VALUES {};""".format(row)
    

print(ELE_DBNAME)

pg_conn = psycopg2.connect(dbname=ELE_DBNAME,
                           user=ELE_USER,
                           password=ELE_PASS,
                           host=ELE_HOST)
print(pg_conn)
pg_curs = pg_conn.cursor()


df = pd.read_csv(DF_URL) # Load dataframe
if os.path.exists(DB_URL): # Delete DB if exists
    os.remove(DB_URL)
sl_conn = sqlite3.connect(DB_URL) # Create database and convert dataframe
df.to_sql("review", con=sl_conn)
sl_curs = sl_conn.cursor()
sl_conn.commit()


db_exists = pg_query("SELECT * FROM information_schema.tables WHERE table_name ='titanic';", print_out=False)

if not db_exists:
    qry_creator = """CREATE TABLE titanic (index SERIAL PRIMARY KEY,
                                       Survived INT,
                                       Pclass INT,
                                       Name TEXT,
                                       Sex TEXT,
                                       Age REAL,
                                       "Siblings/Spouses" INT,
                                       "Parents/Children" INT,
                                       Fare REAL);"""
    pg_query(qry_creator, print_out=False)


try:
    assert(pg_query("SELECT COUNT(*) FROM titanic;", print_out=False)[0] == 887)
    print("DB already exists!")
except Exception as e:
    print("Loading DB from CSV...")
    rows = sl_curs.execute(dthnbt+'SELECT * from review;').fetchall()
    for row in rows:
        pg_query(make_insert_string(row), print_out=False)
    pg_conn.commit()
    pass


pg_query("SELECT AVG(Age) FROM titanic;")
pg_query("SELECT AVG(Survived) FROM titanic WHERE Sex='female';")

pg_curs.close()
sl_curs.close()
pg_conn.close()
pg_conn.close()
