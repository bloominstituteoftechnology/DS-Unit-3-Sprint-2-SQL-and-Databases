import sqlite3

conn = sqlite3.connect('p1.db')

curs= conn.cursor()

print(curs.execute("""SELECT COUNT(*) FROM sxy""").fetchall())
conn.commit()

print(curs.execute("""SELECT COUNT(*) FROM sxy WHERE x>=5 AND y >= 5""").fetchall())
conn.commit()

print(curs.execute("""SELECT COUNT(DISTINCT y) from sxy""").fetchall())
conn.commit()


