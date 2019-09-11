import sqlite3
import pymongo


'''
MongoDB was much easier to work with than PostgreSQL.
I found it excessive that we had to create a table and then populate it,
and that we had to add each row line by line (with a for loop).
I still had to use a for loop here with mongo but it was much easier to add
since I did not need to create a table for items and charecters first.
I could just create the tables at the same time as I inserted the information.
So Mongo seems to be much more flexable than postgreSQL but I think it would
get difficult to navagate and find what you are looking for unless you know
how all of the ids were set up originaly.
'''

path = '../module1-introduction-to-sql/rpg_db.sqlite3'
sl_con = sqlite3.connect(path)

sl_cur1 = sl_con.cursor()
sl_cur1.execute('Select * FROM charactercreator_character')
chars = sl_cur1.fetchall()

sl_cur2 = sl_con.cursor()
sl_cur2.execute('Select * FROM armory_item')
items = sl_cur2.fetchall()


# client = pymongo.MongoClient('') removed to hide password
db = client.RPG

for i in range(len(chars)):
    db.characters.insert_one({
        'sql_id': chars[i][0],
        'name': chars[i][1],
        'level': chars[i][2],
        'exp': chars[i][3],
        'hp': chars[i][4],
        'str': chars[i][5],
        'int': chars[i][6],
        'dex': chars[i][7],
        'wis': chars[i][8],
    })

for i in range(len(items)):
    db.items.insert_one({
        'sql_id': chars[i][0],
        'name': chars[i][1],
        'cost': chars[i][2],
        'weight': chars[i][3],
    })
