import sqlite3

# cursor and connection
conn = sqlite3.connect('\demo_data.sqlite3')
curs = conn.cursor()
curs2 = conn.cursor()
curs3 = conn.cursor()
curs4 = conn.cursor()
curs5 = conn.cursor()
curs6 = conn.cursor()

# create table statement
create_demo = """CREATE TABLE demo(
        S varchar(1)
        x int
        y int
);"""

# INSERT statements
column_1 = """INSERT INTO demo (s)
VALUES
 ("g"),
 ("v"),
 ("f");"""
column_2 = """INSERT INTO demo (x)
VALUES
 (3),
 (5),
 (8);"""
 column_3 = """INSERT INTO demo (y)
VALUES
 (9),
 (7),
 (7);"""
curs.execute(column_1)
curs2.execute(column_2)
curs3.execute(column_3)

# Saved Queries
Q_1 = """SELECT COUNT(s) FROM demo;"""
Q_2 = """SELECT COUNT(s) FROM demo WHERE x > 5 AND y > 5;"""
Q_3 = """SELECT COUNT(DISTINCT y) FROM demo;"""
curs4.execute(Q_1)
curs5.execute(Q_2)
curs6.execute(Q_3)

# checkpoint reached!
conn.commit()
