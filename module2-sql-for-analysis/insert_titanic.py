import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME2")
DB_USER = os.getenv("DB_USER2")
DB_PASS = os.getenv("DB_PASS2")
DB_HOST = os.getenv("DB_HOST2")

CSV_FILEPATH = "titanic.csv"

# CONNECT TO THE PG DATABASE

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = connection.cursor()


# CREATE A TABLE TO STORE THE PASSENGERS
#
# ... optionally renaming some of the columns, adding a primary key, and changing survived to a bool

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

#
# READ PASSENGER DATA FROM THE CSV FILE
#

df = pandas.read_csv(CSV_FILEPATH)
print(df.columns.tolist())

# to avoid PG insertion errors related to datatype mismatches (psycopg2.ProgrammingError: can't adapt type 'numpy.int64'),
# ... we need to convert np.int64 columns to normal integers
# ... https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html
# ... https://stackoverflow.com/questions/34838378/dataframe-values-tolist-datatype
# ... https://stackoverflow.com/questions/47423930/how-to-convert-pandas-dataframe-columns-to-native-python-data-types

df["Survived"] = df["Survived"].values.astype(bool) # do this before converting to native types, because this actually converts to np.bool
df = df.astype("object") # converts numpy dtypes to native python dtypes (avoids psycopg2.ProgrammingError: can't adapt type 'numpy.int64')

#
# INSERT DATA INTO THE PASSENGERS TABLE
#

# how to convert dataframe to a list of tuples
list_of_tuples = list(df.to_records(index=False))

insertion_query = f"INSERT INTO passengers (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!

# CLEAN UP
connection.commit() # actually save the records / run the transaction to insert rows
print('Titanic Data successfully saved to Postgres!')

cursor.close()
connection.close()
