import sqlite3
import os

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?

query1 = '''
SELECT COUNT (character_id) FROM
charactercreator_character;
'''

answer_1 = curs.execute(query1)
answer_1 = curs.fetchall()[0][0]
