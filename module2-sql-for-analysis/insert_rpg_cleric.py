import os
from dotenv import load_dotenv
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

# what is the filepath to connect to our sqlite database?
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg_db.sqlite3")
class SqliteService_cleric():
    def __init__(self, db_filepath=DB_FILEPATH):
        self.connection = sqlite3.connect(db_filepath)
        self.cursor = self.connection.cursor()
    def fetch_characters_cleric(self):
        return self.cursor.execute("SELECT * FROM charactercreator_cleric;").fetchall()
class ElephantSQLService_cleric():
    def __init__(self):
        self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        self.cursor = self.connection.cursor()
    def create_characters_cleric_table(self):
        create_query = """
        DROP TABLE IF EXISTS characters_cleric; -- allows this to be run idempotently, avoids psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "characters_cleric_pkey" DETAIL:  Key (character_id)=(1) already exists.
        CREATE TABLE IF NOT EXISTS characters_cleric (
            character_ptr_id INT,
            using_shield INT,
            mana INT
        );
        """
        print(create_query)
        self.cursor.execute(create_query)
        self.connection.commit()
    def insert_characters_cleric(self, characters_cleric):
        """
        Param characters_cleric needs to be a list of tuples, each representing a row to insert (each should have each column)
        """
        insertion_query = """
            INSERT INTO characters_cleric (character_ptr_id, using_shield, mana)
            VALUES %s
        """
        execute_values(self.cursor, insertion_query, characters_cleric)
        self.connection.commit()
if __name__ == "__main__":
    #
    # EXTRACT (AND MAYBE TRANSFORM IF NECESSARY)
    #
    sqlite_service = SqliteService_cleric()
    characters_cleric = sqlite_service.fetch_characters_cleric()
    print(type(characters_cleric), len(characters_cleric))
    print(type(characters_cleric[0]), characters_cleric[0])
    #
    # LOAD
    #
    pg_service = ElephantSQLService_cleric()
    pg_service.create_characters_cleric_table()
    pg_service.insert_characters_cleric(characters_cleric)