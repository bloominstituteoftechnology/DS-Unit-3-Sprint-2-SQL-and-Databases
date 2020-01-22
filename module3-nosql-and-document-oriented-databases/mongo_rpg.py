import pymongo
import sqlite3
import pandas as pd

rpg_db = 'C:/Users/David/Downloads/rpg_db.sqlite3'  # This obviously won't work if not run locally

sl_conn = sqlite3.connect(rpg_db)
sl_curs = sl_conn.cursor()
client = pymongo.MongoClient('mongodb://davidvollendroff:Fuckhackers^^^666'
                             '@cluster0-shard-00-00-or4st.mongodb.net:27017,'
                             'cluster0-shard-00-01-or4st.mongodb.net:27017,'
                             'cluster0-shard-00-02-or4st.mongodb.net:27017/'
                             'test?ssl=true&replicaSet=Cluster0-shard-0&aut'
                             'hSource=admin&retryWrites=true&w=majority')

db = client.test
table_names_query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
unformatted_table_names = sl_curs.execute(table_names_query).fetchall()
table_names = [item[0] for item in unformatted_table_names]

for table in table_names:
    column_names_query = f'pragma table_info({table});'
    unformatted_column_names = sl_curs.execute(column_names_query).fetchall()
    column_names = [item[1] for item in unformatted_column_names]
    rows = sl_curs.execute(f"SELECT * FROM {table}").fetchall()
    for row in rows:
        db.test.insert_one(dict(zip(column_names, row)))

# How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
'''
Mongo has a somewhat simpler method for adding data, considering that there are no table to concern youself with.
Not needing to determine schema meant you could just dump data in through the lid at the top of the container.
I would say that querying is more difficult in some ways using Mongo, but insertion was much easier than PostgreSQL.
'''