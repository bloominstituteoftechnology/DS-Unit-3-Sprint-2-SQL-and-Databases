import os
import sqlite3
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# load in environmnet variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

lite_conn = sqlite3.connect(DB_FILEPATH)
#print("CONNECTION:", connection)

lite_curs = lite_conn.cursor()

get_first_table = '''
select *
from armory_item
'''

q1 = lite_curs.execute(get_first_table).fetchall()
print(q1[0])

armory_items = pd.read_sql(sql=get_first_table, con=lite_conn)
print(armory_items)

gres_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)

gres_curs = gres_conn.cursor()

create_table = '''
create table if not exists armory_items(
    item_id INTEGER NOT NULL PRIMARY KEY,
    name    varchar(200),
    value   INTEGER,
    weight  INTEGER
)
'''
# actually create the table
gres_curs.execute(create_table)
# commit the created table
gres_conn.commit()
# insertion query string
insertion_query = f"INSERT INTO armory_items (item_id, name, value, weight) VALUES %s"
# use insertion query above and q1 (first query), to insert table into postgresql
execute_values(gres_curs, insertion_query, q1)
gres_conn.commit()
gres_curs.close()
gres_conn.close()

