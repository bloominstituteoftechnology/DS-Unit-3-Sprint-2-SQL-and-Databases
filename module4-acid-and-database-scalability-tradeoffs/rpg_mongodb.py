#!/usr/bin/env python3

import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://Okocha:qoH3DyAYDe8KREAC@cluster0-5sv8d.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg

print('Question: How many total Characters are there?')
num_chars = db.charactercreator_character.count_documents({})
print(f'Answer: There are {num_chars} Characters in total.')

# I did not add other RPG tables into MongoDB, so unfortunately, no more queries.

