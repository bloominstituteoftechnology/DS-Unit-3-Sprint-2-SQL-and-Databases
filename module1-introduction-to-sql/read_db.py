import sqlite3


class Read_DB():

    def __init__(self, db_file):
        self.db_file = db_file

    def read_db(self, columns, table):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('SELECT {} FROM {}'.format(columns, table))
        for row in c.fetchall():
            print(row)
