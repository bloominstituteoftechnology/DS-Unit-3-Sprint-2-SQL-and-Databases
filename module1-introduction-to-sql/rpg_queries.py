import sqlite3


class Querier():
    def __init__(self):
        self.conn = sqlite3.connect('rpg_db.sqlite3')

    def query(self, query):
        c0 = self.conn.cursor()
        r1 = c0.execute(query).fetchall()
        c0.close()
        return r1