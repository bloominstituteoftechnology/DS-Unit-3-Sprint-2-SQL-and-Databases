import json
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import psycopg2
from psycopg2.extras import execute_values
import requests

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "data", "rpg_db.sqlite3")


class StorageService():
    def __init__(self):
        self.sqlite_connection = sqlite3.connect(DB_FILEPATH)
        self.sqlite_cursor = self.sqlite_connection.cursor()
        self.pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        self.pg_cursor = self.pg_connection.cursor()

    def get_characters(self):
        return self.sqlite_connection.execute("SELECT * FROM charactercreator_character;").fetchall()

    def create_characters_table(self):
        create_query = """
        DROP TABLE IF EXISTS characters; -- allows this to be run idempotently, avoids psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "characters_pkey" DETAIL:  Key (character_id)=(1) already exists.
        CREATE TABLE IF NOT EXISTS characters (
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
        print(create_query)
        self.pg_cursor.execute(create_query)
        self.pg_connection.commit()

    def insert_characters(self, characters):
        insertion_query = "INSERT INTO characters (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s"
        list_of_tuples = characters
        execute_values(self.pg_cursor, insertion_query, list_of_tuples)
        self.pg_connection.commit()

if __name__ == "__main__":

    service = StorageService()

    #
    # EXTRACT AND TRANSFORM
    #

    characters = service.get_characters()
    print(type(characters), len(characters))
    print(characters[0])

    #
    # LOAD
    #

    service.create_characters_table()

    service.insert_characters(characters)