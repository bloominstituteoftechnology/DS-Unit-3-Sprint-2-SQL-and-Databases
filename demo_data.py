import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

curs.execute("""
    CREATE TABLE demo(
    s varhar(2),
    x smallint,
    y smallint)
""")
conn.commit()

curs.execute("""
    INSERT INTO demo
        (s, x, y)
    VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
""")
conn.commit()

# Number of rows
print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())

# Number of rows where both x and y are at least 5
print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 and y >= 5;').fetchall())

# Unique values of y
print(curs.execute('SELECT COUNT(DISTINCT y) from demo').fetchall())
