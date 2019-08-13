import psycopg2
import sqlite3
import pandas as pd

# df = pd.read_csv('titanic.csv')
# df.to_sql('titanic', sqlite3.connect('titanic'))

dbname = 'phbjzmrx'
user = 'phbjzmrx'
password = ''
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()
 
sl_conn = sqlite3.connect('titanic')
sl_curs = sl_conn.cursor()

# Grab all of the passengers from the titanic data set with sqlite
sl_curs.execute('SELECT * FROM titanic;')
passengers = sl_curs.fetchall()

# Create a query for creating a table for the postgreSQL
create_table_pg = '''
    CREATE TABLE passengers (
        id INT PRIMARY KEY,
        survived INT,
        pclass INT,
        name VARCHAR(81),
        sex VARCHAR(6),
        age INT,
        siblings_spouses_aboard INT,
        parents_children_aboard INT,
        fare FLOAT
    );
'''

# Execute the query for postgreSQL
pg_curs.execute(create_table_pg)

# Use a for loop to insert all of the passengers into the postgreSQL table
passenger2 = ()
for passenger in passengers:
    for item in passenger:
        if type(item) == str and "'" in item:
            item2 = item.replace("'", " ")
            passenger2 += (item2,)
        else:
            passenger2 += (item,)
        
    pg_curs.execute(
        f"""
        INSERT INTO passengers (id, survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
        VALUES {passenger2};
        """
    )
    passenger2 = ()

# Print the fetchall to see if it worked
pg_curs.close()
pg_conn.commit()
