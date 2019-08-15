import pymongo
import sqlite3

"""
How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
I think it was easier to create a database and insert the RGB data into MongoDB from SQLite. On the other hand,
it was harder to query the database to get useful information such as descriptive statistics.

"""

client = pymongo.MongoClient("mongodb+srv://admin:SmSYv1x9fglCx9hk@cluster0-a9ve9.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()


#Insert RGB data into MongoDB by converting list of tuples into list of dictionaries

def get_list_of_dict(keys, list_of_tuples):
     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
     return list_of_dict

keys = ('character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom')
dictionary = get_list_of_dict(keys, characters)
db.test.insert_many(dictionary)

#Test updating values

db.test.update_many({'name': 'Debit'},
                   {'$set': {'name': 'Trial'}})

print(list(db.test.find({'name': 'Trial'})))