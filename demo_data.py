import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS demo ( \
s TEXT NOT NULL, \
x INT NOT NULL, \
y INT NOT NULL \
)')
cur.execute("INSERT INTO demo(s,x,y) \
VALUES \
('g', 3, 9), \
('v', 5, 7), \
('f', 8, 7)")
test = cur.execute('SELECT * FROM demo').fetchall()
print(test)
# [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
conn.commit()
rows = cur.execute("SELECT COUNT(*) FROM demo").fetchall()
print(rows[0][0])
# 3
five_up = cur.execute("SELECT COUNT(*) FROM demo WHERE x > 4 AND y > 4").fetchall()
print(five_up[0][0])
# 2
unique = cur.execute("SELECT COUNT(DISTINCT y) FROM demo").fetchall()
print(unique[0][0])
# 2
conn.close()
