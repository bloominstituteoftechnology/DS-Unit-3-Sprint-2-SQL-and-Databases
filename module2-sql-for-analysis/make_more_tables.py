#!/usr/bin/env python3

import psycopg2
import sqlite3


# Open postgres connection
dbname = 'nsvybuvb'
user = 'nsvybuvb' # same as dbname
password= 'ZSQQPpNjrb78uZJLGrGliTLdiTaWCAK5' # not my real password
password = 'MFDDCcAweo78hMWYTeTyvGYqvGnJPNX5'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host)
pg_curs = pg_conn.cursor()


# Open mysqlite local database
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

table_list = ['armory_item','armory_weapon', 'charactercreator_character_inventory',
        'charactercreator_cleric','charactercreator_fighter','charactercreator_mage', 
        'charactercreator_necromancer','charactercreator_thief']
## NOTE: 'charactercreator_character' not present because this was done in class and already exists in the online postgress



# Create and insert values into each table (above) form the database

def create_table(table):
    translate_dtype = {'integer':'int','bool':'boolean','varchar(30)':'varchar(30)'}
    print(f"\n\ncreating table {table}:\n")
    info = sl_curs.execute(f'PRAGMA table_info({table});').fetchall()
    query = f"""create table {table} ("""
    id_string = f"\n{info[0][1]} serial primary key,"
    query += id_string
    query_list = []
    for item in info[1:]:
        item = item[1:3]
        query_list.append(f"\n{item[0]} {translate_dtype[item[1]]}")
    query += ','.join(query_list)
    query += ");"
    return query

print("CREATING TABLES:\n")
for table in table_list:
    create_table_query = create_table(table)
    print(create_table_query)
    pg_curs.execute(create_table_query)



def add_table_values(table):
    info = sl_curs.execute(f'PRAGMA table_info({table});').fetchall()
    dtypes = [item[2] for item in info]
    #print(dtypes)
    info = [item[1] for item in info]
    insert_start = f"""
insert into {table}
({','.join(info)})
values """
    rows = sl_curs.execute(f'select * from {table};').fetchall()
    for row in rows:
        if "bool" in dtypes: #booleans must be strings not integers
            ind = dtypes.index('bool')
            row = list(row) # tuples are immutable, must convert to list
            row[ind] = str(row[ind])
            row = tuple(row)
            #print(row)
        insert_row = insert_start + str(row)
        #print(insert_row)
        pg_curs.execute(insert_row)

for table in table_list:
    print(f"\nInserting values into {table}")
    add_table_values(table)

# Finalize changes
pg_curs.close()
pg_conn.commit()
