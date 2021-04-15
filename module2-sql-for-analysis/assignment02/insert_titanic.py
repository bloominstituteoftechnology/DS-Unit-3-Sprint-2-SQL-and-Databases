import os
import pandas as pd 
import psycopg2
from psycopg2.extras import execute_values

# Connection details for the Postgres database
DB_PG_HOST = os.getenv("DB_PG_HOST", default="missing")
DB_PG_DBNAME = os.getenv("DB_PG_DBNAME", default="missing")
DB_PG_USER = os.getenv("DB_PG_USER", default="missing")
DB_PG_PASSWORD = os.getenv("DB_PG_PASSWORD", default="missing")

# Define a dataframe data transformation function
def trans_num_bool(val):
    if val == 1:
        return "True"
    
    return "False"
    
def trans_pclass(val):
    map = {
        1: "First",
        2: "Second",
        3: "Third"
    }

    return map.get(val, "MISSING")

def trans_sex(val):
    if val == "male":
        return val 
    if val == "female":
        return val
    return "MISSING"

def transform_df(df_in):
    df_out = df_in.copy()

    df_out["Survived"] = df_out["Survived"].apply(trans_num_bool)
    df_out["Pclass"] = df_out["Pclass"].apply(trans_pclass)
    df_out["Sex"] = df_out["Sex"].apply(trans_sex)
    df_out["Siblings/Spouses Aboard"] = df_out["Siblings/Spouses Aboard"].apply(trans_num_bool)
    df_out["Parents/Children Aboard"] = df_out["Parents/Children Aboard"].apply(trans_num_bool)

    return df_out

# Read in the titanic csv dataset
print(f'\n**************\nINFO: Starting processing...')
print(f'INFO: Importing data from "titanic.csv"')
df_csv = pd.read_csv("../titanic.csv")

# Transform the dataframe
df_trn = transform_df(df_csv)

# Connect to the Postgres database
print(f'INFO: Connecting to the Postgres database...')
conn_pg = psycopg2.connect(
    dbname=DB_PG_DBNAME, 
    user=DB_PG_USER, 
    password=DB_PG_PASSWORD, 
    host=DB_PG_HOST)

# Test that have connected to the database
query_pg = f'SELECT 1'
csr_pg = conn_pg.cursor()
csr_pg.execute(query_pg)
rslts_pg = csr_pg.fetchall()

# Test the Postgres connection
if rslts_pg[0][0] == 1:
    print(f'INFO: You have connected successfully to server: {DB_PG_HOST} database: {DB_PG_DBNAME}')
else:
    print(f'ERROR: A connection error occurred\nExiting...')
    quit()

# SQL used to create a titanic table in Postgres
PG_CREATE_TABLE = """
CREATE TABLE titanic_data (
	titanic_id serial NOT NULL,
	survived bool NOT NULL,
	passenger_class text NOT NULL,
	"name" text NOT NULL,
	sex varchar(10) NOT NULL,
	age smallint, 
	siblings_spouse_aboard bool NOT NULL,
	parents_children_aboard bool NOT NULL,
	fare money,
	PRIMARY KEY (titanic_id)
);
"""

# Drop the intended table if it exists
print(f'INFO: Drop and create a new Postgres db table...')
csr_pg.execute("DROP TABLE IF EXISTS titanic_data")
conn_pg.commit()      # commit the create transaction

# Create the new Postgres table
csr_pg.execute(PG_CREATE_TABLE)
conn_pg.commit()      # commit the create transaction

# execute_values insert statement
PG_INSERT = """
INSERT INTO titanic_data 
  (survived, passenger_class, name, sex, age, siblings_spouse_aboard, parents_children_aboard, fare) 
  VALUES %s;
"""

# Convert the dataframe to a list of tuples
records = df_trn.to_records(index=False)
rows = list(records)

# Insert the rows exported from the sqlite database into the Postgres database table 
print(f'INFO: Insert the transformed titanic.csv data into the Postgres db...')
execute_values(
    csr_pg, 
    PG_INSERT, 
    rows)
conn_pg.commit() 

# Count the number of rows in the the newly imported table
csr_pg.execute("SELECT count(*) FROM titanic_data")
rslts_pg = csr_pg.fetchone()
print(f'INFO: The number of rows imported into Postgres (expecting: {len(df_trn.index)}) is: {rslts_pg[0]}')
print(f'INFO: Processing complete\n**************\n')