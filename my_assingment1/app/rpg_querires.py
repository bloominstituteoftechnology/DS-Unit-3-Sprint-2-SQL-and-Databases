import sqlite3
import os

DB_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")



conn = sqlite3.connect(DB_filepath)


curs1 = conn.cursor()

# query for finding out the total number of characters in the 
# game
totalChars_query = """
                    SELECT 
	count(distinct(character_id))
FROM charactercreator_character_inventory;
"""
