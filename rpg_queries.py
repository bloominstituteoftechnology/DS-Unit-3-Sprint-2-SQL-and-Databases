import sqlite3

conn = sqlite3.connect('\module1-introduction-to-sql\rpg_db.sqlite3')

c = conn.cursor()

c.execute("SELECT * FROM charactercreator_character")