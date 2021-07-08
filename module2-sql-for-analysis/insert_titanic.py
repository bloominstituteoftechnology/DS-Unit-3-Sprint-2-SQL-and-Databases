import psycopg2
import pandas as pd

# Import titanic data into DataFrame
df = pd.read_csv('titanic.csv')

# Data cleaning
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
df = df.rename(columns={'siblings_spouses_aboard': 'siblings_spouses',
                        'parents_children_aboard': 'parents_children'})
df['name'] = df['name'].replace("'", '', regex=True)
df['name'] = df['name'].str.replace('\'', '')

# Convert DataFrame to list of lists
titanic = df.values.tolist()


# Postgresql login credentials
dbname = 'xgbbacwp'
user = 'xgbbacwp'
password = ''
host = 'raja.db.elephantsql.com'

# Create a connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

# Add Titanic table to postgresql database
create_titanic_table = """
CREATE TABLE Titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(6),
    age INT,
    siblings_spouses INT,
    parents_children INT,
    fare MONEY
)
"""
pg_curs.execute(create_titanic_table)


# Add passenger data to Titanic table
for passenger in titanic:
    insert = '''INSERT INTO Titanic(
        survived, pclass, name, sex, age, siblings_spouses, 
        parents_children, fare) VALUES''' + str(tuple(passenger))
    pg_curs.execute(insert)

# Commit changes
pg_conn.commit()

# Create new cursor and inspect data
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM Titanic;')
pg_passengers = pg_curs.fetchall()
len(pg_passengers)
