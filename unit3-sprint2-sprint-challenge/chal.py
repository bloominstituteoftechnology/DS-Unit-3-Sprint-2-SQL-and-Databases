import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

create_table = """
    CREATE TABLE demo
    s VARCHAR(1),
    x INT,
    y INT
    """

curs0 = conn.cursor()

try:
    curs0.execute(create_table)
    print('Created Table demo')
except Exception as e:
    print(e)
finally:
    curs0.close()
    conn.commit()

insert_data = """
    INSERT INTO demo
    VALUES
        ('g',3,9),
        ('v',5,7),
        ('f',8,7)
    """