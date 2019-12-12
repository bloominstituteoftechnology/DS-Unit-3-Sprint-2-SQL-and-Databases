import sqlite3

def query(x, db):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.commit()
    conn.close()
    return answer
    