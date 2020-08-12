# Reproduce (debugging as needed) the live lecture task of setting up and
# inserting the RPG data into a MongoDB instance, and add the code you write to do
# so here. Then answer the following question (can be a comment in the top of your
# code or in Markdown) - "How was working with MongoDB different from working with
# PostgreSQL? What was easier, and what was harder?"

# MongoDB was much easier to work with compared to PostgreSQL due to the ease of
# using less code to accomplish the same task. I have to consistently make sure
# I execute SQL commands, fetchall, and commit on my cursor and connection
# while simultaneously double checking the opening and closing of cursors and
# my connection. MongoDB has commands that greatly streamlined the import of the
# rpg tables into itself with relatively little code.

import pymongo
import sqlite3

if __name__ == "__main__":

    # Given code to connect to Mongo
    password = "EtZkty4uluNwiVyb"  # Don't commit/share this! Reset it if it leaks
    dbname = "rpg"
    client = pymongo.MongoClient(
        "mongodb+srv://xpandalord:"
        + password
        + "@cluster0.q6n34.mongodb.net/"
        + dbname
        + "?retryWrites=true&w=majority"
    )
    db = client.rpg

    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_character table
    get_characters = "SELECT * FROM charactercreator_character;"
    characters = sl_curs.execute(get_characters).fetchall()

    db.rpg.drop()

    for i in range(len(characters)):
        rpg_doc = {
            "doc_type": "characters",
            "character_id": characters[i][0],
            "name": characters[i][1],
            "level": characters[i][2],
            "exp": characters[i][3],
            "hp": characters[i][4],
            "strength": characters[i][5],
            "intelligence": characters[i][6],
            "dexterity": characters[i][7],
            "wisdom": characters[i][8],
        }
        db.rpg.insert_one(rpg_doc)

    print(list(db.rpg.find({"doc_type": "characters"})))
