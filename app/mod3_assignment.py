# importing needed libraries to transfer the rpg_data to mongoDB
import pymongo
import psycopg2
import sqlite3
import dns
import os
from dotenv import load_dotenv
import pandas as pd

# construct my data dir path
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", '')
# pint to my .sqlite file with the full data set
DB_FILENAME = "rpg_db.sqlite3"


def _mongo_connect() -> pymongo.mongo_client.MongoClient:
    """summary:
    ------------------------------------
    takes nothing and connects to a Mongo server

    defined by enviroment variables that are loaded via dotenv package
    requirements:
    ------------------------------------
    SYSTEM VARIABLES DEFINED AS FOLLOWING:

    MONGO_USER {str} : username for the database

    MONGO_PASSWORD {str} : password for the database

    MONGO_HOST {str} : refers to the cluster name and host of the mongo instance

    MONGO_TABLE {str} : defualt table for the database

    returns:
    ------------------------------------
    returns a pymongo.mongo_client.MongoClient object
    """
    # load inviroment variables from <project root>/.env
    # for security it might be a good ide to use an ssl cert here @TODO
    if os.getenv("CREDS_LOADED", default="FALSE") == "FALSE":
        load_dotenv()

    DB_USER = os.getenv("MONGO_USER")
    DB_PASSWORD = os.getenv("MONGO_PASSWORD")
    CLUSTER_NAME = os.getenv("MONGO_HOST")
    DB_TABLE = os.getenv("MONGO_TABLE")

    #establish a connecting using the loades credientals from the enviroment
    connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}/{DB_TABLE}?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_uri)
    return client


def _postgre_connect() -> psycopg2._psycopg.connection:
    """summary:
    ------------------------------------
    takes nothing and connects to a PostgreSQL server

    defined by enviroment variables that are loaded via dotenv package
    requirements:
    ------------------------------------
    SYSTEM VARIABLES DEFINED AS FOLLOWING:

    PG_USER {str} : username for the database

    PG_PASSWORD {str} : password for the database

    PG_HOST {str} : host name of the database

    PG_TABLE {str} : defualt table for the database

    PG_PORT {int} : port to connect to the database

    returns:
    ------------------------------------
    returns a psycopg2._psycopg.connection object
    """
    # check if we need to load enviroment variables if not the assign values
    # for addes security i can look into configuring ssl tunnel to connect @TODO
    if os.getenv("CREDS_LOADED", default="FALSE") == "FALSE":
        load_dotenv()

    DB_USER = os.getenv("PG_USER")
    DB_PASSWORD = os.getenv("PG_PASSWORD")
    DB_HOST = os.getenv("PG_HOST")
    DB_TABLE = os.getenv("PG_TABLE")
    DB_PORT = os.getenv("PG_PORT")

    # esablish a connection to my postgreSQL table on elephant
    conn = psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            dbname=DB_TABLE,
                            user=DB_USER,
                            password=DB_PASSWORD)
    return conn


# SQLITE FUNCTIONS


def _sqlite_connect() -> sqlite3.Connection:
    """summary:
    ------------------------------------
    takes nothing and connects to a db file locally
    defined by "DATA_PATH + DB_FILENAME"
    requirements:
    ------------------------------------
    DATA_PATH {str} : a string that points to the parent folder of the db

    DB_FILENAME {str} : the file name for the db,sqlite3 file
    returns:
    ------------------------------------
    returns a sqlite3.Connection object
    """
    # i dont need any creds or anything so im going to just return a conn obj
    return sqlite3.connect(DATA_PATH + DB_FILENAME)


def encSQLtoDict(curs: sqlite3.Cursor, table_name: str) -> dict:
    """
    takes a cursor object and a table name and returns all of the column headers
    from the table
    """
    # tranforing a SELECT * FROM table query to a dictionary
    responses = curs.execute(f"""
            SELECT * FROM {table_name};
        """).fetchall()

    # get my key names from the PRAGMA builtin function in an sqlite db
    columns = curs.execute(f"PRAGMA table_info({table_name});").fetchall()
    columns = [columns[x][1] for x in range(len(columns))]

    # actually assign keys to values and loop through the rows that we get from the query
    list_out = []
    for response in responses:
        out = {}
        for k, v in zip(columns, response):
            out[k] = v
        list_out.append(out)
    # return all of the encoded responses from the db
    return list_out


def getLiteTableNames(curs: sqlite3.Cursor, db_name: str):
    """takes a cursor object and a database name and returns a list of tables
    that are contained in that database in the form of a python list
    """
    o = curs.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    return [
        o[x][0] for x in range(len(o)) if o[x][0] not in ['sqlite_sequence']
    ]
