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
class SqliteService_mage():
    def __init__(self, db_filepath=DB_FILEPATH):
        self.connection = sqlite3.connect(db_filepath)
        self.cursor = self.connection.cursor()
    def fetch_characters_mage(self):
        return self.cursor.execute("SELECT * FROM charactercreator_mage;").fetchall()
class ElephantSQLService_mage():
    def __init__(self):
        self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        self.cursor = self.connection.cursor()
    def create_characters_mage_table(self):
        create_query = """
        DROP TABLE IF EXISTS characters_mage; -- allows this to be run idempotently, avoids psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "characters_mage_pkey" DETAIL:  Key (character_id)=(1) already exists.
        CREATE TABLE IF NOT EXISTS characters_mage (
            character_ptr_id INT,
            has_pet INT,
            mana INT
        );
        """
        print(create_query)
        self.cursor.execute(create_query)
        self.connection.commit()
    def insert_characters_mage(self, characters_mage):
        """
        Param characters_mage needs to be a list of tuples, each representing a row to insert (each should have each column)
        """
        insertion_query = """
            INSERT INTO characters_mage (character_ptr_id, has_pet, mana)
            VALUES %s
        """
        execute_values(self.cursor, insertion_query, characters_mage)
        self.connection.commit()
if __name__ == "__main__":
    #
    # EXTRACT (AND MAYBE TRANSFORM IF NECESSARY)
    #
    sqlite_service = SqliteService_mage()
    characters_mage = sqlite_service.fetch_characters_mage()
    print(type(characters_mage), len(characters_mage))
    print(type(characters_mage[0]), characters_mage[0])
    #
    # LOAD
    #
    pg_service = ElephantSQLService_mage()
    pg_service.create_characters_mage_table()
    pg_service.insert_characters_mage(characters_mage)