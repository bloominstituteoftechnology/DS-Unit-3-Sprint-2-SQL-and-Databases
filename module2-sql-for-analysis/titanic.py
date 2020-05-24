import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

load_dotenv() 

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

#CSV_FILEPATH = "titanic.csv"
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection)) 

cursor = connection.cursor()
print(type(cursor)) 

sql = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived boolean,
    pclass int4,
    full_name text,
    gender text,
    age int4,
    sib_spouse_count int4,
    parent_child_count int4,
    fare float8
);
"""
cursor.execute(sql)

df = pandas.read_csv(CSV_FILEPATH)
print(df.columns.tolist())

df["Survived"] = df["Survived"].values.astype(bool) 
df = df.astype("object") 

list_of_tuples = list(df.to_records(index=False))

insertion_query = f"INSERT INTO passengers (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) 

connection.commit() 

cursor.close()
connection.close()