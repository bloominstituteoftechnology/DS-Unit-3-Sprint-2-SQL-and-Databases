import urllib.parse as up
import psycopg2
import pandas as pd

'''
Reproduce (debugging as needed) the live lecture task of setting up and inserting the RPG data into a PostgreSQL database, 
and add the code you write to do so. Then, set up a new table for the Titanic data (titanic.csv) - spend some time thinking about the 
schema to make sure it is appropriate for the columns. Enumerated types may be useful. Once it is set up, 
write a insert_titanic.py script that uses psycopg2 to connect to and upload the data from the csv, and add the file to your repo. 
Then start writing PostgreSQL queries to explore the data!
'''

def open_connection():
    up.uses_netloc.append("postgres")
    url = up.urlparse('postgres://auujdjzp:ix5sMoaR8u0KSTM0cFREq_4G5Srgtxad@raja.db.elephantsql.com:5432/auujdjzp')
    conn = psycopg2.connect(database=url.path[1:],
                        user=url.username,
                        password=url.password,
                        host=url.hostname,
                        port=url.port)
    
    return conn

def close_connection(conn):

    conn.close()
    return print('Closed connection to DB')


def create_table(conn):
    cur = conn.cursor()
    query = '''
        CREATE TABLE titanic (
        survived INT,
        class INT,
        name varchar(255),
        sex varchar(255),
        age INT,
        siblings_spouses INT,
        parents_children INT,
        fare float);'''

    cur.execute(query)
    conn.commit()
    cur.close()
    return print('Successfully created titanic table')


def insert_data(conn):
    df = pd.read_csv('titanic.csv')
    cur = conn.cursor()
    tup = [tuple(x) for x in df.values]
    cur.executemany('''INSERT INTO titanic VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''', tup) 
    conn.commit()   
    return


if __name__ == '__main__':

    connection = open_connection()
    create_table(connection)
    insert_data(connection)
    close_connection(connection)