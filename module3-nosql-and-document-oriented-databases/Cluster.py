# If colab not locally Find out the IP address of this Colab Instance
# !curl ipecho.net/plain
"""
"How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?":
-MongoDB and PostgrSQL biggest difference is hpw the data/information is stored.
-In PostgreSQL there are schemas that are used to connect to individual data tables. MongoDB formats and stores the
all the data formated in documents.  The two have unique differences and but in my opinon MongoDB seems simpler/easier
way to store data and PostgreSQL has in my opinion extra steps so its harder.
"""
"""first make shell and install pymongo and dnspython"""
import pymongo

password = 'Aa02155120'  # Don't commit/share this! Reset it if it leak
User = 'John-Thomas'
dbname = 'test'
connection = (
        "mongodb+srv://John-Thomas:" + password + "@cluster.y2ftp.mongodb.net/" + dbname + "?retryWrites=true&w"
                                                                                           "=majority")
client = pymongo.MongoClient(connection)
db = client.test
dir(db.test)
# Let's figure out inserting some data
db.test.count_documents({'x': 1})
# 0
db.test.insert_one({'x': 1})
# <pymongo.results.InsertOneResult at 0x7f52ad9fd208>
db.test.count_documents({'x': 1})
# 1
# Let's start the afternoon project
rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)
# We need key-value pairs, i.e. a dictionary!
# Lazy way (probably not ideal)
db.test.insert_one({'rpg_character': rpg_character})
db.test.find_one({'rpg_character': rpg_character})
# We can do better
# Mongo doesn't force us to have a schema, but
# we *should* try to choose useful/informative key names
rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}
db.test.insert_one(rpg_doc)
list(db.test.find({'level': 3}))
# Make our doc better - annotate type so we can query on it
rpg_doc = {
    'doc_type': 'rpg_character',
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}
db.test.insert_one(rpg_doc)
list(db.test.find({'doc_type': 'rpg_character'}))
# Our goal - copy the charactercreator_character table
get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()
characters[:10]
# worked on first two assignents to review and stufy guide
