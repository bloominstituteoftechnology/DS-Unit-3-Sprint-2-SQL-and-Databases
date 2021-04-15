import os
import sys
import sqlite3
import pymongo

# ********************************************************************
# QUESTION: "How was working with MongoDB different from working with
#    PostgreSQL? What was easier, and what was harder?"
#
# Most of my database experience actually has been with MongoDB so I may not
# provide a fair or unbiased answer.  However from my general experience
# I like MongoDB and NoSQL database structures because they are very flexible to update.
# If you need a new field (column) or collection (table), your code can literally
# just add it on the fly and MongoDB will create it.  This is very helpful 
# when doing new or "greenfield" development while the database schema is being "discovered".
#
# A strength of RDBMS are foreign key references and the ability to normalize
# data and subsequently query data relationships via joins.  Because database schemas aren't set
# in NoSQL databases such as MongoDB, oftentimes data needs to be duplicated in multiple 
# places which can lead to higher storage requirements and the potential for stale or
# confusing states of data.
# 
# MongoDB has a javascript like shell in which ad hoc querying and other database interactions
# can be executed. However, the user needs to learn a new and unwieldy syntax.  I sometimes just
# miss the capability to whip out a handy "SELECT x FROM y WHERE z;" command!  If a user
# comes to NoSQL from the RDBMS world, they can't easily leverage their knowledge of standard SQL,
# well understood database concepts, and common tooling which have been in use for decades.
#
# As a weekend hacker and programming newbie, I didn't have to relearn SQL knowledge
# or ignore long held practices and conventions.  I was a good candidate for a NoSQL neophyte! :)
# ********************************************************************

# Connection details for the sqlite3 database
DB_FILEPATH = "./rpg_db.sqlite3"
DB_SLT_TABLES = [
    "charactercreator_character", 
    "charactercreator_character_inventory",
    "armory_item",
    "armory_weapon"]

# Connect to the sqlite3 database
print(f'\n**************\nINFO: Processing starting...')
conn_sl = sqlite3.connect(DB_FILEPATH)
conn_sl.row_factory = sqlite3.Row
cur_sl = conn_sl.cursor()

# Test that the script has connected to the sqlite3 database
print(f'INFO: Test the sqlite3 db connection...')
rslts_sl = conn_sl.execute("SELECT 1").fetchall()
# Test the sqlite connection
if rslts_sl[0][0] == 1:
    print(f'INFO: You have connected successfully to {DB_FILEPATH}')
else:
    print(f'ERROR: A connection error occurred. Exiting...')
    quit()

# Connection details for the MongoDB database
DB_MG_DMN = os.getenv("DB_MG_DMN", default="missing")
DB_MG_DB  = os.getenv("DB_MG_DB",  default="missing")
DB_MG_USR = os.getenv("DB_MG_USR", default="missing")
DB_MG_PWD = os.getenv("DB_MG_PWD", default="missing")
mg_conn_string = f'mongodb://{DB_MG_USR}:{DB_MG_USR}@{DB_MG_DMN}/{DB_MG_DB}?retryWrites=false'

# Connect to the MongoDB database
clnt_mg = pymongo.MongoClient(mg_conn_string)
db_mg   = clnt_mg[DB_MG_DB]

# Define a map of virtual "tables" and table row counts (stored in memory)
map_tables       = {}
map_tables_count = {}

# Iterate through the sqlite3 tables and import the table contents in to memory
for sqlt_tabl in DB_SLT_TABLES:
    # Define a temp array to house a sqlite db's rows
    arr_tmp = []

    # Query rows from the sqlite table being iterated upon
    query_sl = f'SELECT * FROM {sqlt_tabl}'
    rslts_sl = cur_sl.execute(query_sl).fetchall()

    # Iterate through each query (of table rows)
    for row in rslts_sl:
        # Append the table row to the temp array (as a dict)
        arr_tmp.append(dict(row))

    # Store the temp array in our "virtual" set of tables
    map_tables[sqlt_tabl] = arr_tmp

# Iterate through our set of virtual tables
print(f'INFO: Insert the sqlite table data into a collection of the same name')
for vtbl in map_tables.keys():
    # Set the current MongoDB collection
    col_mg = db_mg[vtbl]
    # Drop the collection if it exists
    col_mg.drop()

    # Insert the rows from the virtual table for the table being iterated upon
    col_mg.insert_many(map_tables[vtbl])

    # Save a count of the newly inserted documents
    map_tables_count[vtbl] = col_mg.count_documents({})

for coll in map_tables_count:
    print(f'INFO: Collection {coll} has {map_tables_count[coll]} documents')

# Close db connections
print(f'INFO: Close database connections')
cur_sl.close()
conn_sl.close()
clnt_mg.close()

print(f'INFO: Stop processing.\n**************')