import sqlite3
connection = sqlite3.connect('demo_data.sqlite3')
c = connection.cursor()
c.execute("CREATE TABLE demo(S TEXT PRIMARY KEY, X INTEGER, Y INTEGER)")
c.execute("INSERT INTO demo VALUES('g', 3, 9)")
c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
c.execute("INSERT INTO demo VALUES ('f', 8 , 7)")
connection.commit()
c.execute("SELECT COUNT(*) FROM demo")
c.fetchone()
### (3,)
c.execute("SELECT COUNT(*) FROM demo WHERE X >= 5 AND Y >= 5")
c.fetchone()
### (2,)
c.execute("SELECT COUNT(Y) DISTINCT FROM demo")
c.fetchone()
### (2,)