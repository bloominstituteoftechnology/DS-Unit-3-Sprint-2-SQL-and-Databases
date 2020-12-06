import os
import json
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

# Load contents of the .env file into the script's environment
load_dotenv() 

# Add credentials for accessing the elephant 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# Load the dataframe with pandas
df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

# Create the psychopg2 connection and cursor objections to access the elephant 
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

# Create the titanic table
create_query = "CREATE TABLE titanic (Survived INT, Class INT, Name VARCHAR(255), Sex CHAR(10), Age FLOAT, Sibling_Spouse INT, Parent_Child INT, Fare FLOAT);"

# Create placeholder insertion query for the titanic table
# insertion_query = "INSERT INTO titanic2 (Survived, Class, Name, Sex, Age, Sibling_Spouse, Parent_Child, Fare) VALUES %s"
insertion_query = f"INSERT INTO titanic (Survived, Class, Name, Sex, Age, Sibling_Spouse, Parent_Child, Fare)" \
                    "VALUES ({Survivor},{Class},{Name},{Sex},{Age},{Sibing_Spouse},{Parent_Child},{Fare})"


# Change the format of database into a list of tuples
list_of_tuples = []
for row in df.iterrows():
    list_of_tuples.append(row)
print(list_of_tuples)

lines = []
for i in range(0,len(df)):
    result = []
    for j in range(0,8):
        result.append(list_of_tuples[i][1][j])
    lines.append(tuple(result))
print(lines)

# Use execute_values to insert the list of tuples into the titanic table as rows

execute_values(cursor, insertion_query, lines)

# Save the transactions
connection.commit()
cursor.close()
connection.close()
