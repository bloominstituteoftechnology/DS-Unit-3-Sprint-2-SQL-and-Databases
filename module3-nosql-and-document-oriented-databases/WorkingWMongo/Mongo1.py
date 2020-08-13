import pymongo
import sqlite3

password = 'suh264tUm'
dbname = 'character_data_base'
connection = ('mongodb+srv://jonatan5696:' + password +
              '@cluster0.jalzo.gcp.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient(connection)
db = client.character_data

# Step 1 - Extract, getting data out of SQlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# goal is to copy the charactercreator_character table
get_characters = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(get_characters).fetchall()
print(characters)
character_observations = []
for char in characters:
    get_rpg_characters = {'Character_id':char[0],
                         'name':char[1],
                          'level':char[2],
                          'exp':char[3],
                          'hp': char[4],
                          'strength': char[5],
                          'intelligence': char[6],
                          'dexterity': char[7],
                          'wisdom': char[8]}
    character_observations.append(get_rpg_characters)
    db.character_data.insert_one
    db.character_data.insert
