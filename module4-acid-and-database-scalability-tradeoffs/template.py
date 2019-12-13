"""Describe file"""

import sqlite3

conn = sqlite3.connect('NAME_OF_DATABASE')

#put your variables, etc.

def make_db():
    """Describe this function here!!"""
    curs = conn.cursor()
    #execute your queries related to creating database and inserting stuff
    curs.close()
    conn.commit()

def run_queries():
    """Describe this function here!!"""
    curs = conn.cursor()
    print(curs.execute('SELECT * from table;').fetchall())

if __name__ == "__main__":
    make_db()
    run_queries()
