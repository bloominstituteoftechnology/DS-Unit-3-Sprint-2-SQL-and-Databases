import psycopg2
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
import datetime
from psycopg2.extras import execute_values


load_dotenv()

# connecting to our elephant sql rpg database
RPG_DB_NAME = os.getenv('RPG_DB_NAME', default='oops')
RPG_DB_USER = os.getenv('RPG_DB_USER', default='oops')
RPG_DB_PASSWORD = os.getenv('RPG_DB_PASSWORD', default='oops')
RPG_DB_HOST = os.getenv('RPG_DB_HOST', default='oops')
postgresql_connection = psycopg2.connect(dbname=RPG_DB_NAME, user=RPG_DB_USER, password=RPG_DB_PASSWORD, host=RPG_DB_HOST)



# connecting to local rpg database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', '..', 'module1-introduction-to-sql', 'rpg_db.sqlite3')
sqlite_connection = sqlite3.connect(DB_FILEPATH)

# creating cursors for both of the databases
sqlite_cursor = sqlite_connection.cursor()
postgresql_cursor = postgresql_connection.cursor()

# getting all of the tables names from the local rpg database
query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
table_names = sqlite_cursor.execute(query).fetchall()

query = 'SELECT * FROM armory_item'
result = sqlite_cursor.execute(query).fetchall()

total_query = ''
for table in table_names:
    # getting all of the schema for the tables from the local db
    query = f"SELECT sql from sqlite_master WHERE name = \'{table[0]}\'"
    result = sqlite_cursor.execute(query).fetchall()
    '''
    was going to implement this using python code but had to hard code it in using sql queries in tables plus due to differences between sqlite and postgres
    # creating the tables in the elephant db
    query = result[0][0].replace('integer NOT NULL PRIMARY KEY AUTOINCREMENT', 'SERIAL PRIMARY KEY')
    query = query.replace('CREATE TABLE ', 'CREATE TABLE IF NOT EXISTS ')
    query = query.replace('datetime', 'date')
    total_query += query + ';'
    #print(total_query)
    postgresql_cursor.execute(total_query)
    '''
    # getting data to insert into table from local db
    query = f'SELECT * from {table[0]}'
    result = sqlite_cursor.execute(query).fetchall()
    print(f'\n{table[0]}')

    insertion_query = f'INSERT INTO {table[0]} VALUES %s'
    if table[0] in ['charactercreator_cleric', 'charactercreator_fighter', 'charactercreator_mage',
        'charactercreator_necromancer', 'charactercreator_thief']:
        new_result = []
        for each in result:
            each = list(each)
            each[1] = bool(each[1])
            new_result.append(each)
        execute_values(postgresql_cursor, insertion_query, new_result)
    elif table[0] != 'sqlite_sequence':
        execute_values(postgresql_cursor, insertion_query, result)
    
        
    # inserting the data into the elephant db
    
    

postgresql_connection.commit()

postgresql_cursor.close()
postgresql_connection.close()
