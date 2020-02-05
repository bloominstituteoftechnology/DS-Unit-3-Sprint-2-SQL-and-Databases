import psycopg2
import json
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3
from psycopg2.extras import execute_values

df = pd.read_csv('titanic.csv')
conn = sqlite3.connect("titanic.sqlite3")
df.to_sql('titanic', conn, if_exists='replace')
curs = conn.cursor()

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

DB_FILEPATH = "titanic.sqlite3"


class StorageService():
    def __init__(self):
        self.sqlite_connection = sqlite3.connect(DB_FILEPATH)
        self.sqlite_cursor = self.sqlite_connection.cursor()
        self.pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        self.pg_cursor = self.pg_connection.cursor()

    def get_passengers(self):
        return self.sqlite_connection.execute("SELECT * FROM titanic;").fetchall()

    def create_passengers_table(self):
        create_query = """
        DROP TABLE IF EXISTS titanic;
        CREATE TABLE IF NOT EXISTS titanic (
            index SERIAL PRIMARY KEY,
            Survived INT, -- wanted as BOOL but couldn't get to convert in script, used PostgreSQL browser window instead
            Pclass INT,
            Name VARCHAR(255),
            Sex VARCHAR(6),
            Age INT,
            SiblingsSpousesAboard INT,
            ParentsChildrenAboard INT,
            Fare MONEY
        );
        """
        self.sqlite_cursor.execute(create_query)
        self.pg_cursor.execute(create_query)
        self.pg_connection.commit()

    def insert_passengers(self, passengers):
        insertion_query = "INSERT INTO titanic (index, Survived, Pclass, Name, " \
                          "Sex, Age, SiblingsSpousesAboard, ParentsChildrenAboard, Fare) VALUES %s"
        list_of_tuples = passengers
        execute_values(self.pg_cursor, insertion_query, list_of_tuples)
        execute_values(self.sqlite_cursor, insertion_query, list_of_tuples)
        self.pg_connection.commit()


if __name__ == "__main__":
    service = StorageService()


    passengers = service.get_passengers()

    # LOAD

    service.create_passengers_table()

    service.insert_passengers(passengers)