import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
print(curs)

"""
Create table mytable
"""
command = "CREATE TABLE IF NOT EXISTS mytable (" \
        "s text PRIMARY KEY NOT NULL, x INTEGER NOT NULL, y INTEGER NOT NULL);"
result = curs.execute(command)

"""
Populate table mytable
"""
command2 = "INSERT INTO mytable (s, x, y)" \
          "VALUES ('g', 3, 9)," \
          "('v', 5, 7)," \
          "('f', 8, 7);"
result2 = curs.execute(command2)
conn.commit()


def select_all_tasks(conn):

    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM mytable")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    command = cur.execute("SELECT COUNT(*) FROM mytable")
    print(command.fetchall())
    command = cur.execute("SELECT COUNT(DISTINCT y) FROM mytable")
    print(command.fetchall())

select_all_tasks(conn)
