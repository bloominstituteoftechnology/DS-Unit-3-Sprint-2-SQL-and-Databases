import sqlite3

# initialize connection
sql3_conn = sqlite3.connect('demo_data.sqlite3')
sql3_curs = sql3_conn.cursor()

# drop demo table if nec
sql3_stmt = """DROP TABLE
    IF EXISTS demo;
    """
sql3_curs.execute(sql3_stmt)
sql3_conn.commit()

# create table
sql3_stmt = """CREATE TABLE demo (
    s string,
    x int,
    y int
    );
    """
sql3_curs.execute(sql3_stmt)
sql3_conn.commit()

# insert data
sql3_stmt = """INSERT INTO demo
    VALUES
   ('g', 3, 9),
   ('v', 5, 7),
   ('f', 8, 7);
   """
sql3_curs.execute(sql3_stmt)
sql3_conn.commit()

# get number of rows in table
sql3_stmt = """SELECT COUNT(*)
    FROM demo;
    """
print("There are", sql3_curs.execute(sql3_stmt).fetchone()[0], "rows in the demo table\n")

# get number of rows in table where both x and y are at least 5
sql3_stmt = """SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5;
    """
print("There are", sql3_curs.execute(sql3_stmt).fetchone()[0], "instances in the demo table where both x and y are at least 5\n")

# get number of unique values of y in table
sql3_stmt = """SELECT COUNT (DISTINCT y)
    FROM demo;
    """
print("There are", sql3_curs.execute(sql3_stmt).fetchone()[0], "unique values of y in the demo table")
