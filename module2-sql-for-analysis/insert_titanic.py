import psycopg2
import pandas as pd

# Get credentials from ElephantSQL
dbname = 'TODO'
user = 'TODO'
password = 'TODO'
host = 'TODO'

# Connect to ElephantSQL
conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
                        
# Make cursor
curs = conn.cursor()

# Read titanic csv into pandas dataframe
titanic_url = 'https://raw.githubusercontent.com/tesseract314/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
df = pd.read_csv(titanic_url)

# Map strings for categorical values
df['Survived'] = df['Survived'].map({0:'False', 1:'True'})
df['Pclass'] = df['Pclass'].map({1:'First', 2:'Second', 3:'Third'})

# psycopb2 doesn't like apostrophes in the name columns for some reason
df['Name'] = df['Name'].str.replace("'", "")

# Create titanic schema/table
create_titanic = """
CREATE TYPE surv AS ENUM ('False', 'True');
CREATE TYPE pclass AS ENUM ('First', 'Second', 'Third');
CREATE TYPE sex_binary AS ENUM ('male', 'female');
CREATE TABLE Titanic2 (
  passenger_id SERIAL PRIMARY KEY,
  survived surv,
  class pclass,
  name VARCHAR(100),
  sex sex_binary,
  age smallint,
  sibling_spouse smallint,
  parent_child smallint,
  fare decimal
)
"""

# Execute schema
curs.execute(create_titanic)

# Loop through pandas dataframe to add each passenger to titanic table
for passenger in range(0, df.shape[0]):
  insert_passenger = """
  INSERT INTO Titanic2
  (survived, class, name, sex, age, sibling_spouse, parent_child, fare)
  VALUES """ + str(tuple(df.loc[passenger]))
  curs.execute(insert_passenger)
  
  # Commit/save to ElephantSQL
  conn.commit()
  
  # Remake cursor
  curs = conn.cursor()

