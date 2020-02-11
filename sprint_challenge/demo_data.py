import sqlite3

DB_FILEPATH = ("demo_data.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

create_table = """
    CREATE TABLE IF NOT EXISTS demo (
        s TEXT,
        x INT,
        y INT);
"""

curs.execute(create_table)
conn.commit()

insert_data = """
    INSERT INTO demo (s, x, y)
    VALUES ("g", 3, 9),
     ("v", 5, 7),
     ("f", 8, 7);
"""

curs.execute(insert_data)
conn.commit()
conn.close()
