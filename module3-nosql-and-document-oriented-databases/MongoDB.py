"""
Connecting to Mongo DB in order to upload RPG sqlite DB
"""

# imports for today
from pymongo import MongoClient
import sqlite3 as sql
import ssl


sl_conn = sql.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute("SELECT * FROM charactercreator_character").fetchall()

keys = (
    'character_id',
    'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom'
)

password = 'XXX'
dbname = 'test'

db = MongoClient(f"mongodb+srv://twjames:{password}@cluster0.aplgy.gcp.mongodb."
                 f"net/{dbname}?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE).rpg_db.characters

# db.insert_many(
#     {k: v for k, v in zip(keys, char)} for char in characters
# )

print(*db.find(), sep='\n')
