
import sqlite3

db_name = 'demo_data.sqlite3'
conn = sqlite3.connect(db_name)
curs = conn.cursor()

# create table and insert values
sqls = [''] * 5
sqls[0] = """
CREATE TABLE IF NOT EXISTS demo
("s" varchar(30) NOT NULL,
 "x" integer NOT NULL,
 "y" integer NOT NULL,
 PRIMARY KEY("s")
);"""
sqls[1] = "INSERT INTO demo VALUES ('g', 3, 9);"
sqls[2] = "INSERT INTO demo VALUES ('v', 5, 7);"
sqls[3] = "INSERT INTO demo VALUES ('f', 8, 7);"
sqls[4] = "COMMIT;"
for sql in sqls:
    curs.execute(sql)

sql = "SELECT COUNT(*) FROM demo"
curs.execute(sql)
print(curs.fetchall()[0][0])

sql = """
SELECT COUNT(*) FROM demo
 WHERE x >= 5 
   AND y >= 5
"""
curs.execute(sql)
print(curs.fetchall()[0][0])

sql = """
SELECT COUNT(DISTINCT(y)) FROM demo
"""
curs.execute(sql)
print(curs.fetchall()[0][0])

curs.close()
conn.close()