import sqlite3 as sl

conn = sl.connect('demo_data.sqlite3')

c = conn.cursor()

try:
    c.execute("DROP TABLE demo")
except BaseException:
    c.execute("CREATE TABLE demo (s VARCHAR[1], x INT, y INT);")
else:
    c.execute("CREATE TABLE demo (s VARCHAR[1], x INT, y INT);")
finally:
    try:
        c.execute("INSERT INTO demo VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);")
    except Exception as e:
        print(e)
        print("insertion failed")
    else:
        print("insertion succeeded")
    finally:
        print("all done")

conn.commit()

c.execute("SELECT COUNT(*) FROM demo")
N = c.fetchall()[0][0]

c.execute("SELECT COUNT(*) FROM demo WHERE x>4 AND y>4")
J = c.fetchall()[0][0]

c.execute("SELECT COUNT(DISTINCT y) FROM demo")
L = c.fetchall()[0][0]

conn.close()

report = f"""\n\tThe number of rows is {N}.
        The number of rows in which both x and y are >=5 is {J}.
        The number of distinct values in y is {L}.
    may your journeys bring you blessings. """

print(report)
