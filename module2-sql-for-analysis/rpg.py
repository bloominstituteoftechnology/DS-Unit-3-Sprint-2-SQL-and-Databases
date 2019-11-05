import sqlite3
import psycopg2

from db import DBNAME, USER, PASSWORD, HOST

# connect to sqlite3 database
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# connect to ElephantSQL database
pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER,
                           password=PASSWORD,
                           host=HOST)
pg_curs = pg_conn.cursor()

# grabbing items instead of characters to avoid redundancy
items = sl_curs.execute('SELECT * FROM armory_item;').fetchall()

create_item_table = """
    CREATE TABLE armory_item (
        item_id SERIAL PRIMARY KEY,
        name varchar(30),
        value INT,
        weight INT
    );
"""

pg_curs.execute(create_item_table)

# iteratively add every item from the local database to the elephant
for item in items:
    current = str(item[1:])
    insert_item = f"""
        INSERT INTO armory_item (name, value, weight)
        VALUES {current};
    """
    pg_curs.execute(insert_item)


pg_curs.close()
pg_conn.commit()
