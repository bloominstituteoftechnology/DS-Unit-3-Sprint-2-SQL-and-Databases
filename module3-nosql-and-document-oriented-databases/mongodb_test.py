"""
Help documentation for mongodb_test:

    This module is designed to upload data from a JSON format
    to the mongodb hosted shard. 
"""

import pymongo as pm
import sqlite3 as sql


if __name__ == '__main__':

    # Connect to mongoDB

    client = pm.MongoClient("mongodb+srv://asherg1:<password>@cluster0-yre6g.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test

    # Get Data from sqlite3 database

    sl_conn = sql.connect('rpg.sqlite3')
    sl_curs = sl_conn.cursor()
    character_data = sl_curs.execute(
        """
        SELECT * FROM charactercreator_character;
        """
    ).fetchall()

    # Set up list of dictionaries
    docs = []
    for character in character_data:
        doc = {'table' : 'charactercreator_character'}
        doc['id'] = character[0]
        doc['name'] = character[1]
        doc['level'] = character[2]
        doc['exp'] = character[3]
        doc['hp'] = character[4]
        doc['strength'] = character[5]
        doc['intelligence'] = character[6]
        doc['dexterity'] = character[7]
        doc['wisdom'] = character[8]
        docs.append(doc)
    
    # Put data into mongoDB
    db.test.insert_many(docs)

    print('Success! Finished script.')