import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

# Postgresql credentials for database connection
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "OOPS")
DB_NAME = os.getenv("DB_NAME", "OOPS")
DB_USER = os.getenv("DB_USER", "OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", "OOPS")

#Get titanic csv data to load into db
TITANIC = 'titanic.csv'

def psyco_connection():
    """Function to create a connection to postgresql database"""
    conn = None

    try:
        conn= psycopg2.connect(   
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST
                )
    except psycopg2.OperationalError as e:
        print("Unable to connect!", e)
    
    return conn

def create_titanic_table(conn):
    """Schema for titanic dataset"""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE titanic(
            survived int,
            pclass int,
            name text,
            sex varchar(30),
            age float,
            siblings_or_spouse int,
            parents_or_children int,
            fare float
        );
        """
    )
    conn.commit()
    cur.close()

def check_table_exist(table_name:str, conn:object) -> bool:
    """Used as conditional to avoid error being thrown for duplicate tables"""
    cur = conn.cursor()
    exist = False

    try:
        cur.execute(
            """
            SELECT EXISTS(
                SELECT *
                FROM information_schema.tables
                WHERE table_name = %s
            )""", (table_name,)
        )
        exist = cur.fetchone()[0]
    except psycopg2.Error as e:
        print("Error in checking table exist", e)
    
    cur.close()
    return exist

def load_table(data, table_name:str, conn:object):
    """Load data into postgres db table using file"""
    cur = conn.cursor()

    with open(data, 'r') as f:
        next(f) # skip header
        cur.copy_from(f, table_name, sep=',')

    conn.commit()
    cur.close()

def main():
    """Establish connection, create table, and load data"""

    # Establish connection
    conn = psyco_connection()

    # check for table and create
    table = 'titanic'
    if not check_table_exist(table, conn):
        create_titanic_table(conn)
    
    # load titanic data 
    load_table(data=TITANIC, table_name=table, conn=conn)

    # close connection to db
    conn.close()

if __name__ == "__main__":
    main()
    print("Data successfully loaded!")

