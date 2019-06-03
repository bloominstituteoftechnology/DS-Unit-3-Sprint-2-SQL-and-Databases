import pandas as pd
import sqlite3
import pymongo
import urllib

# verify at https://cloud.mongodb.com/
# uid = admin, password = at die cedar Addlerz

conn = sqlite3.connect('data/rpg_db.sqlite3')
df_chars = pd.read_sql('SELECT * FROM charactercreator_character', conn, coerce_float=False)
print(df_chars.dtypes)

password = input("Enter MongoDB password: ")
conn_str = "mongodb+srv://admin:" +\
            urllib.parse.quote(password) + \
           "@cluster0-d1iho.mongodb.net/test?retryWrites=true"

client = pymongo.MongoClient(conn_str)

db = client.characters

# from https://stackoverflow.com/questions/20167194/insert-a-pandas-dataframe-into-mongodb-using-pymongo
db.characters.insert_many(df_chars.to_dict('records'))

for item in list(db.characters.find()):
    print(item)
