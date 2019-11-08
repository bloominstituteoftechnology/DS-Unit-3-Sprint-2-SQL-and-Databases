import sqlite3
import psycopg2

dbname = 'yjdfdntkp' 
user = 'yjbsdfsdfsdp'
password = 'euAfsdfsdfsdf7Wa6Fb_K9FVhQaU1Y3uLPgj9B'
host = 'ssdfsdfsd.elephantsql.com'

# PostgresQL setup
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Sqlite setup
s3_conn = sqlite3.connect('new_titanic2.sqlite3')
s3_curs = s3_conn.cursor()

table = """
    CREATE TABLE iceberg (
    id SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    sibling_spouse_aboard INTEGER,
    parents_children_aboard INTEGER,
    Fare REAL
    );
"""
pg_curs.execute(table)

# Set query
ppls = s3_curs.execute('SELECT * FROM new_titanic2;').fetchall()

# Insert data from sqlite into postgres 
for ppl in ppls:
    insert_ppl = """
        INSERT INTO iceberg
        (Survived, Pclass, Name, Sex, Age, sibling_spouse_aboard, parents_children_aboard, Fare)
        VALUES
        """ + str(ppl[1:]) + ';'
    pg_curs.execute(insert_ppl)


# Save
pg_curs.close()
pg_conn.commit()
