
import psycopg2
from dotenv import load_dotenv
import os
import sqlite3
from my_second_assignment.app.helper import create_and_load_table

load_dotenv() # This is to make the .env file 
              # contents be put into the enviro
              # variables

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
        host=DB_HOST, password=DB_PASSWORD)
print("Connection:", connection)

p_cur = connection.cursor()
print("Cursor:", p_cur)



# Writing the path for the data from rpg_sqlite3 found in 
# This assignment
RPG_Path = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

sl_conn = sqlite3.connect(RPG_Path)
sl_cursor = sl_conn.cursor()

# doing a query to extract all the info from the charactercreator 
# table

quer_selectAll = """
        SELECT *

FROM charactercreator_character
"""

quer_create_charTable = """
                CREATE TABLE IF NOT EXISTS charactercreator_character (
                        character_id        SERIAL PRIMARY KEY,
                        name  VARCHAR(30) ,
                        level INT,
                        exp   INT,
                        hp    INT,
                        strength  INT, 
                        intelligence INT, 
                        dexterity INT,
                        wisdom INT
                
                );

                """

quer_insert = """
        INSERT INTO charactercreator_character 
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES 
        
        """

# This is the name of the table to be inserted
TABLE_NAME = "charactercreator_character"


# Doing the query
sl_cursor.execute(quer_selectAll)
# charTable is a list of tuples
charTable = sl_cursor.fetchall()

# Method found in the helper.py file that will load the chartable if needed
create_and_load_table(connection, charTable=charTable, create_query=quer_create_charTable,  
                        insert_query =quer_insert, tableName=TABLE_NAME, check_if_table_empty=True)



# Will now print the first row
p_cur.execute("Select *  FROM charactercreator_character  cc WHERE cc.character_id = 1")
result = p_cur.fetchall()
print("The first row:\n", result) 





