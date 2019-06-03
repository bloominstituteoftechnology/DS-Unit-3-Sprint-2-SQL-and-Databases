import pandas as pd
import sqlite3
import pymongo
import urllib

# verify at https://cloud.mongodb.com/
# uid = admin, password = at die cedar Addlerz

db_table = 'titanic'
sql3_conn = sqlite3.connect('data/' + db_table + '.sqlite3')
df_titanic = pd.read_sql('SELECT * FROM titanic', sql3_conn, coerce_float=False)

password = input("Enter MongoDB password: ")
conn_str = "mongodb+srv://admin:" +\
            urllib.parse.quote(password) + \
           "@cluster0-d1iho.mongodb.net/test?retryWrites=true"

client = pymongo.MongoClient(conn_str)

db = client.titanic

dict_titanic_list = df_titanic.to_dict('records') # actually gives a list
# first get rid of index
list_titanic = []
for dict_item in dict_titanic_list:
    dict_item = {k:v for k,v in dict_item.items() if k != 'index'}
    list_titanic.append(dict_item)
# from https://stackoverflow.com/questions/20167194/insert-a-pandas-dataframe-into-mongodb-using-pymongo
db.titanic.insert_many(list_titanic)

for item in list(db.titanic.find()):
    print(item)
