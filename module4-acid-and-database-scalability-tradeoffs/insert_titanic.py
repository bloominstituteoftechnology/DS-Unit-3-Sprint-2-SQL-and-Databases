import psycopg2, os, sqlite3
import pandas as pd
from settings import ELE_DBNAME, ELE_USER, ELE_PASS, ELE_HOST

DF_URL = "titanic.csv"
DB_URL = "titanic.sqlite3"

def pg_query(query, print_out=True):
    pg_curs.execute(query)
    res = pg_curs.fetchall()
    if print_out:
        print(res)
    return res

def make_insert_string(row):
    row = "(" + ", ".join([str(i) if not type(i) == str else "'" + i.replace("'", "") + "'" for i in row]) + ")"
    return """INSERT INTO titanic (index, Survived, Pclass, Name, Sex, Age, "Siblings/Spouses", "Parents/Children", Fare) VALUES {};""".format(row)


pg_conn = psycopg2.connect(dbname=ELE_DBNAME, user=ELE_USER, password=ELE_PASS, host=ELE_HOST)
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
    qry_creator = """CREATE TABLE titanic (index SERIAL PRIMARY KEY, Survived INT, Pclass INT, Name TEXT,
                                           Sex TEXT, Age REAL, "Siblings/Spouses" INT, "Parents/Children" INT, Fare REAL);"""
    pg_query(qry_creator, print_out=False)


try:
    assert(pg_query("SELECT COUNT(*) FROM titanic;", print_out=False)[0][0] == 887)
    print("DB already exists!")
except Exception as e:
    print("Loading DB from CSV...")
    rows = sl_curs.execute(dthnbt+'SELECT * from review;').fetchall()
    for row in rows:
        pg_query(make_insert_string(row), print_out=False)
    pg_conn.commit()
    pass


print("Survived, Count")
pg_query("SELECT Survived, COUNT(*) FROM titanic GROUP BY Survived;")
print()

print("Class, Count")
pg_query("SELECT Pclass, COUNT(*) FROM titanic GROUP BY Pclass ORDER BY Pclass;")
print()

print("Class, Survived, Count")
pg_query("SELECT Pclass, Survived, COUNT(*) FROM titanic GROUP BY Pclass, Survived ORDER BY Pclass, Survived;")
print()

print("Survived, Average Age")
pg_query("SELECT Survived, AVG(Age) FROM titanic GROUP BY Survived;")
print()

print("Class, Average Age")
pg_query("SELECT Pclass, AVG(Age) FROM titanic GROUP BY Pclass ORDER BY Pclass;")
print()

print("Survived, Average Fare")
pg_query("SELECT Survived, AVG(Fare) FROM titanic GROUP BY Survived;")
print()

print("Class, Average Fare")
pg_query("SELECT Pclass, AVG(Fare) FROM titanic GROUP BY Pclass ORDER BY Pclass;")
print()

print("Survived, Average Siblings/Spouses")
pg_query('SELECT Survived, AVG("Siblings/Spouses") FROM titanic GROUP BY Survived;')
print()

print("Class, Average Siblings/Spouses")
pg_query('SELECT Pclass, AVG("Siblings/Spouses") FROM titanic GROUP BY Pclass ORDER BY Pclass;')
print()

print("Survived, Average Parents/Children")
pg_query('SELECT Survived, AVG("Parents/Children") FROM titanic GROUP BY Survived;')
print()

print("Class, Average Parents/Children")
pg_query('SELECT Pclass, AVG("Parents/Children") FROM titanic GROUP BY Pclass ORDER BY Pclass;')
print()

names = [i[0].split(" ")[-1] for i in pg_query("SELECT Name from titanic;", print_out=False)]
names = set([i for i in names if names.count(i) > 1])
print("Names with more than one occurrence:")
for name in names:
    print(name)

pg_curs.close()
sl_curs.close()
pg_conn.close()
sl_conn.close()
