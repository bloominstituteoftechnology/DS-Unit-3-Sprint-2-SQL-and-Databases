import sqlite3


def create_db():
    global cursor, conn
    conn = sqlite3.connect('demo_data.sqlite3')
    cursor = conn.cursor()
    print("Opened database successfully")


def create_table():
    cursor.execute("DROP TABLE IF EXISTS demo")
    cursor.execute("CREATE TABLE demo\
                 (ID INT PRIMARY KEY NOT NULL,\
                 s CHAR(1) NOT NULL,\
                 x INT NOT NULL,\
                 y INT NOT NULL);")
    print("Table `demo` created successfully")


def populate_table():
    cursor.execute("INSERT INTO demo (ID, s, x, y) VALUES (1, 'g', 3, 9);")
    cursor.execute("INSERT INTO demo (ID, s, x, y) VALUES (2, 'v', 5, 7);")
    cursor.execute("INSERT INTO demo (ID, s, x, y) VALUES (3, 'f', 8, 7);")
    print("Table `demo` populated with data successfully")

    conn.commit()


def queries():
    print("How many rows `demo` table have?")
    print(cursor.execute("SELECT count(*) FROM demo;").fetchall(), '\n')

    print("How many rows any rows are there where both `x` and `y` are at least 5?")
    print(cursor.execute("SELECT count(*) FROM demo WHERE x >= 5 AND y >= 5;").fetchall(), '\n')

    print('How many unique values of `y` are there?')
    print(cursor.execute("SELECT COUNT(DISTINCT y) FROM demo;").fetchall())


def main():
    create_db()
    create_table()
    populate_table()
    queries()
    conn.close()


if __name__ == "__main__":
    main()