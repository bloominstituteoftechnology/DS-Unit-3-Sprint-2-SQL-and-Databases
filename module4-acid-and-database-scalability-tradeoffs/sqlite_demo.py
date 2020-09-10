"""
Creating and inserting data with SQlite.
"""
import sqlite3


def create_table(conn):
    curs = conn.cursor()
    create_statement = """
      CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(20),
        favorite_number INTEGER,
        least_favorite_number INTEGER
      );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()


def insert_data(conn):
    my_data = [
        ('Malven', 7, 12),
        ('Dondre', -5, 101),
        ('Peggy', 14, 74)
    ]
    curs = conn.cursor()
    for row in my_data:
        insert_statement = curs.execute("""INSERT INTO students VALUE (?,?,?), my_data""")
        # Exercise - write an insert statement!
    curs.close()
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('example_db.sqlite3')
    create_table(conn)
    insert_data(conn)

"""
Our first business query!
"""
"""
Let's figure out what the duplicate character names are
SELECT - how we choose which columns to get
WHERE - how we set conditions on the rows to be returned
LIMIT - when we only want a certain number of rows
ORDER - when we want to sort the output
JOIN - when we need data from multiple tables combined
"""
