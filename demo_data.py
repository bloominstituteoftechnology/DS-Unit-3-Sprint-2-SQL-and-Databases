import sqlite3 as sql

db = sql.connect("demo_data.sqlite3")


cursor = db.cursor()


db.execute("DROP TABLE demo")


t = db.execute(
    """
    CREATE TABLE demo(
      s TEXT,
      x INTEGER,
      y INTEGER
    )
    """
)


cursor.executemany(
    """
    INSERT INTO demo (s,x,y) VALUES(?,?,?)
    """,
    [
        ('s', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)
    ]
)


print(f'rows: {db.execute("SELECT COUNT(*) FROM demo").fetchone()[0]}')
# rows: 3

c = db.execute(
    "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5").fetchone()[0]
print(f'number of x,y >= 5: {c}')
# number of x,y >= 5: 2


c = db.execute("SELECT COUNT(DISTINCT y) FROM demo").fetchone()[0]
print(f"How many unique values of `y` are there: {c}")
# How many unique values of `y` are there: 2