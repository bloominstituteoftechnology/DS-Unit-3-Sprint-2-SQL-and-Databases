import sqlite3
import pandas as pd
import psycopg2

# convert csv file into a table and create a database for that table.

# #df = pd.read_csv('https://raw.githubusercontent.com/EvidenceN/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

# #sl_conn = sqlite3.connect('database name')

# add the data to the database. Once it is added, 
# the above connection is not needed and can be terminated

# #df.to_sql(name = 'titanic', con=sl_conn)

# function for running sql commands and connecting to database. 
def query(x, db="database name"):
    '''
    - This function connects to a database, 
    - establishes a cursor on top of the connection,
    - executes the SQL command = x
    - fetches the results from the SQL command and store it 
    in the variable ANSWER
    - Then commits and close the cursor and connection
    - then returns the result of the query.
    '''
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

def postgre(x):
    '''
    - Connects to elephant sql database
    - create a cursor on top of the connection
    - then commit the cursur to save it
    - then close the connection

    '''
    dbname = 'lqsujdux' 
    user = 'lqsujdux' 
    password =  'w7ih63BvRfpV_Mf9suEjW-6NmOGaTcP-'
    host =  'rajje.db.elephantsql.com'
    
    pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    pg_curs.execute(x)
    result = pg_curs.fetchall()
    pg_curs.close()
    pg_conn.commit()
    
    return result

if __name__ = "__main__":
    query()