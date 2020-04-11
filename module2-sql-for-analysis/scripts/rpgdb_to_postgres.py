import os
import sqlite3
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

#connect to postgres db
load_dotenv()

HOST = os.getenv('RPG_HOST')
NAME = os.getenv('RPG_NAME')
USER = os.getenv('RPG_USER')
PASSWORD = os.getenv('RPG_PASSWORD')

post_con = psycopg2.connect(dbname = NAME, 
                        user = USER, 
                        password = PASSWORD, 
                        host = HOST)

post_cur = post_con.cursor()

#connect to the sqlite db
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'data', 
                            'rpg_db.sqlite3')

lite_con = sqlite3.connect(DB_FILEPATH)

lite_cur = lite_con.cursor()

#get a list of table names
query = '''
SELECT name 
FROM sqlite_master
WHERE type='table'
ORDER BY name;
'''

res = lite_cur.execute(query).fetchall()

#this gives me a list of tuples containing strings. I really
#just want a list of strings so lets get that
tables = []

for i in range(len(res)):

    #I only want RPG tables
    if 'auth' in res[i][0]:
        continue
    elif 'django' in res[i][0]:
        continue
    elif 'sqlite' in res[i][0]:
        continue
    else:
        tables.append(res[i][0])

#i want to extract the column names from the table
#I'm doing it this way because sqlite doesn't use schema
#that I can query, like other sql implementations do
# def get_cols(name):

#     query = 'PRAGMA table_info(' + name + ');'

#     res = lite_cur.execute(query).fetchall()

#     columns = []

#     for i in range(len(res)):
#         columns.append((res[i][1], res[i][0])
    
#     return columns

# print(get_cols(tables[0]))

#okay I have a list of tables, and a way to get column names
#so I need to:

#make create table and insert queries
def make_queries(name):
    q1 = 'PRAGMA table_info(' + name + ');'

    info = lite_cur.execute(q1).fetchall()

    tableq = 'CREATE TABLE ' + name + ' ('

    insertq = 'INSERT INTO ' + name + ' ('

    bool_pos = False

    for i in range(len(info)):

        tableq += info[i][1] + '  ' + info[i][2]

        insertq += info[i][1]

        # Check if primary key
        if info[i][5]:
            tableq += ' PRIMARY KEY'

        #check if column is not nul    
        elif info[i][3]:
            tableq += ' NOT NULL'

        #ugh booleans are messing me up this is a little hacky but I can't
        #think around it right now
        if info[i][2] == 'bool':
            bool_pos = i

        #check if last entry info
        if i == (len(info) - 1):
            continue
        else:
            tableq += ', '
            insertq += ', '

    tableq += ');'
    insertq += ') VALUES %s'

    return tableq, insertq, bool_pos

def table_copier(name):

    create_table, insertion_query, bool_pos = make_queries(name)

    #create a new table in postgres database
    post_cur.execute(create_table)

    # query and get the whole table in sqlite
    lite_data = lite_cur.execute('SELECT * FROM ' + name + ';').fetchall()

    #this is a hack to deal with booleans giving me hell. Not ideal, but
    #honestly using execute_values is a nightmare of an interpreter
    if not (bool_pos == False):
        for i in range(len(lite_data)):
            temp = list(lite_data[i])
            temp[bool_pos] = temp[bool_pos] is 1

            lite_data[i] = tuple(temp)

    # use execute values to to insert the whole lite table into postres
    execute_values(post_cur, insertion_query, lite_data)

    # sanity checks table length, and first 5 values
    print('Sanity check for ' + name + ' table')
    print('------------------------------------------------------------------')

    lite_data = lite_cur.execute('SELECT * FROM ' + name + ';').fetchall()

    post_cur.execute('SELECT * FROM ' + name + ';')
    
    post_data = post_cur.fetchall()

    print('SQLite table length: ', len(lite_data))
    print('Postgres table length: ', len(post_data))
    print('------------------------------------------------------------------')
    print('SQLite table width: ', len(lite_data[0]))
    print('Postgres table length: ', len(post_data[0]))
    print('------------------------------------------------------------------')
    print('First 5 of SQLite table')
    print('------------------------------------------------------------------')
    for i in range(5):
        print(lite_data[i])
    print('------------------------------------------------------------------')
    print('First 5 of Postgres table')
    print('------------------------------------------------------------------')
    for i in range(5):
        print(post_data[i])
    print('------------------------------------------------------------------')
    print()

for tab in tables:
    table_copier(tab)

#commented out for testing
#con.commit()
post_cur.close()
post_con.close()
lite_cur.close()
lite_con.close()