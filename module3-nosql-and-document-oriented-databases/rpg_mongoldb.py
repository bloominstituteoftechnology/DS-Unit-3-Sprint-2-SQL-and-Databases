"""
Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a MongoDB instance, and add the code you write to do
so here. Then answer the following question (can be a comment in the top of your
code or in Markdown) - 
"How was working with MongoDB different from working with
PostgreSQL? 
It had syntax that seemed more flexible, but I still need to look
more into query to see how I can JOIN and do other useful things
I know I can do in SQL. But overall a good experience because it did
not feel as tedious.
What was easier, and what was harder?"
It was definately easier to put data into the server. The server log
in was quicker if you knew what you are doing. And the security with 
IP is good. I do believe that it would be harder to manipulate the data
to JOIN and updating is also easy to mess up.
"""

import pymongo
import sqlite3


client = pymongo.MongoClient("mongodb+srv://admin:{secret}@rpg-5e7if.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

conn = sqlite3.connect('module1-introduction-to-sql\\rpg_db.sqlite3') 
curs = conn.cursor()

query = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(query).fetchall()

# I use this as reference to create my for loop
# str(characters[0])[1:-1]
# characters[0][0]

for character in characters:
    db.test.insert_one({
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    })