import sqlite3
import os
import psycopg2
from dotenv import load_dotenv

# Postgresql credentials for database connection
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "OOPS")
DB_NAME = os.getenv("DB_NAME", "OOPS")
DB_USER = os.getenv("DB_USER", "OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", "OOPS")

#Sqlite database info to tranfer tables from
DB_FILE = os.path.join(os.path.dirname(__file__),
              "..", "module1-introduction-to-sql", "rpg_db.sqlite3")

def psyco_connection():
    """Function to create a connection to postgresql database"""
    p_conn = None

    try:
        p_conn= psycopg2.connect(   
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST
                )
    except psycopg2.OperationalError as e:
        print("Unable to connect!", e)
    
    return p_conn

def sqlite_connection(db_file):
    """Create a database connection to sqlite3 to pull rgb data from"""
    s_conn = None

    try:
        s_conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print("Unable to connect", e)

    return s_conn

def extract_table(table_name:str, conn:object )-> list:
    """Pulls all rows from a table in sqlite rgb database"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM """ + table_name
    )
    rows = cur.fetchall()
    
    cur.close()
    return rows

def create_character_table(conn):
    """Manually Create Charactor table to ensure data integretiy"""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE charactercreator_character(
            character_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            level INT,
            exp INT,
            hp INT,
            strength INT,
            intelligence INT,
            dexterity INT,
            wisdom INT
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

def load_character_table(data:list, conn:object):
    """Load all data from character table in sqlite rgb db into postgres using data from extract_table"""
    cur = conn.cursor()
    for row in data:
        cur.execute(
            """
            INSERT INTO charactercreator_character(
                name,
                level,
                exp,
                hp,
                strength,
                intelligence,
                dexterity,
                wisdom
            )
            VALUES"""
            + str(row[1:])
            +";"
        )
    conn.commit()
    cur.close()

def main():
    """Run all functions to transfer data from sqlite to postgres"""

    # Establish connections
    p_conn = psyco_connection()
    s_conn = sqlite_connection(DB_FILE)

    # Extract table
    table = 'charactercreator_character'
    characters = extract_table(table_name=table, conn=s_conn)

    # Create table in postgres db if it doesn't exist
    if not check_table_exist(table_name=table, conn= p_conn):
        create_character_table(p_conn)

    # Load data into newly created postgres table
    load_character_table(data=characters, conn=p_conn)

    # Close connections
    p_conn.close()
    s_conn.close()

if __name__  == "__main__":
    main()
