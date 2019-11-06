import sqlite3
import psycopg2

dbname = 
user = 
password = 
host = 

# PostgresQL setup
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Sqlite setup
s3_conn = sqlite3.connect('Titanic.sqlite3')
s3_curs = s3_conn.cursor()

table = """
    CREATE TABLE titanic (
    "index" SERIAL PRIMARY KEY,
    "Survived" INT,
    "Pclass" INT,
    "Name" TEXT,
    "Sex" TEXT,
    "Age" REAL,
    "Siblings/Spouses Aboard" INTEGER,
    "Parents/Children Aboard" INTEGER,
    "Fare" REAL
    );
"""
pg_curs.execute(table)

# Set query
ppls = s3_curs.execute('SELECT * FROM Titanic;').fetchall()

# Insert data from sqlite into postgres 
for ppl in ppls:
    insert_ppl = """
        INSERT INTO titanic
        ("Survived", "Pclass", "Name", "Sex", "Age", "Siblings/Spouses Aboard", "Parents/Children Aboard", "Fare")
        VALUES
        """ + str(ppl[1:]) + ';'
    pg_curs.execute(insert_ppl)


# Save
pg_curs.close()
pg_conn.commit()
