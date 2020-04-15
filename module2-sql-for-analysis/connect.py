# still needs work

import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os 

load_dotenv() # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_PORT =  os.getenv("DB_PORT", default="OOPS") 

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print(type(conn))
        # create a cursor
        curs = conn.cursor()
        print(type(curs))
	# execute a statement
        print('PostgreSQL database version:')
        curs.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = curs.fetchone()
        print("version", db_version)
       
	    # close the communication with the PostgreSQL
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()