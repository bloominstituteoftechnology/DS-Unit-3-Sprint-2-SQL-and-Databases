#!/usr/bin/env python
""" 
Function copy and load Pandas dataframe as 
SQL table into PostgreSQL
Here using 'titanic.csv'
"""
import pandas as pd
import psycopg2 as pg
pg.connect

# Posgresql database parameters
dbname ='hartabvb'
user = 'hartabvb'
password = '9jk1ptYGv0qclPjUQybvhF8bnmAXPmNv'
host = 'stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)

def copy_table(table_name, csv_file):
    import pandas as pd

    df = pd.read_csv(csv_file)
    #df.Name = df.Name.str.replace('[^\w\s]','')
    df.Name = df.Name.str.replace("'",'')
    # Cursor
    pg_curs = pg_conn.cursor()
    
    # dataframe of columns and types
    convert_types ={'int64':'int', 'object': 'text', 'float64': 'real'}
    
    col_types = pd.DataFrame(df.dtypes, columns=['types'])
    col_types = col_types.replace(convert_types)
    
    # Creating string of column names and type for creating SQL table
    col_n_type = []
    for i, j in zip(col_types.index, col_types.types.values):
        result = i + ' ' + j
        col_n_type.append(result)
    
    # Converting into one string
    col_n_type = ','.join(col_n_type).replace('/', '_').replace(' Aboard', '_Aboard')
    
    # Creating SQL table
    create = f"CREATE TABLE {table_name}({col_n_type});"
    pg_curs.execute(create)

    # Now we insert the data in the empty table created
    col_names = ','.join(df.columns).replace('/', '_').replace(' Aboard', '_Aboard')
    rows = df.values
    
    for row in [tuple(i) for i in rows]:
        insert_result = f"INSERT INTO {table_name} ({col_names}) VALUES" + str(row)
        pg_curs.execute(insert_result)


    pg_conn.commit()