import os
import sqlite3

# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")


SELECT
	count(character_id)
FROM charactercreator_character