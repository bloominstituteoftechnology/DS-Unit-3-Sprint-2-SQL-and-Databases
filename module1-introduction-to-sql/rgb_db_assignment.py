# 
import sqlite3
from query import *
# connect the databse
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # connect to DB
    conn = connect_to_db()
    # Create Cursor
    curs = conn.cursor()
    # Execute query
    result1 = execute_query(curs, query.GET_CHARACTERS)
    print(result1[0])
    result2 = execute_query(curs, query.GET_CHARACTER_SUBCLASS)
    print(result2[0])
    result3 = execute_query(curs, query.GET_WEAPON_PER_CHARACTER)
    print(result3[0])