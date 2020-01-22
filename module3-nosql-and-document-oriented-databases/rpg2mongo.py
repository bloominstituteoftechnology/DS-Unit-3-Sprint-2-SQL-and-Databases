#!/usr/bin/env python3

import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb+srv://Okocha:qoH3DyAYDe8KREAC@cluster0-5sv8d.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(get_characters).fetchall()

curs.close()

for character in characters:
    insert_character = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    }
    db.charactercreator_character.insert_one(insert_character)

print(db.charactercreator_character.find_one())