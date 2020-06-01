import os
import sqlite3 as sq

# Defining file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILEPATH = os.path.join(BASE_DIR, 'rpg_db.sqlite3')

connection = sq.connect(DB_FILEPATH)
print("CONNECTION : ", connection)

cursor = connection.cursor()
print("CURSOR : ", cursor)

