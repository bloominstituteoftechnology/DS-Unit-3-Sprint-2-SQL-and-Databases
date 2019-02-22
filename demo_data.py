import sqlite3


def create_demo_data():
    connection = sqlite3.connect('demo_data.sqlite3')
    cursor = connection.cursor()

    create_demo_data = """
    CREATE TABLE demo (
        s CHAR PRIMARY KEY,
        x INT, 
        y INT 
    )
    """

    insert_demo_data = """
    INSERT INTO demo(s, x, y)
    VALUES ('g', 3, 5),
           ('v', 5, 7), 
           ('f', 8, 7)
    """

    cursor.execute(create_demo_data)
    cursor.execute(insert_demo_data)
    connection.commit()


def db_queries():
    connection = sqlite3.connect('demo_data.sqlite3')
    cursor = connection.cursor()
    count_rows = cursor.execute('SELECT COUNT(*) FROM demo')

    print('Number of rows in demo table: ', count_rows.fetchall()[0][0])

    count_rows_when_five_or_more = cursor.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5')
    # strangely, x AND y in parentheses returns 0, seems the you have to perform the operation on each variable?

    print("Number of rows when >= 5: ", count_rows_when_five_or_more.fetchall()[0][0])

    unique_y = cursor.execute('SELECT COUNT (DISTINCT y) FROM demo')

    print("Number of unique y values: ", cursor.fetchall()[0][0])

# uncomment below if you need fresh db
# create_demo_data()


db_queries()
