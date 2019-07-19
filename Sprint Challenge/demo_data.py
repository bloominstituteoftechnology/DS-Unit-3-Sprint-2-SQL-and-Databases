import sqlite3

#Task One, create connection
conn = sqlite3.connect('demo_data.sqlite3')
print("Task one, connection created successfully")

#Task Two, create cursor
cur = conn.cursor()
print("Task two, cursor created successfully")

def createTable():
    """Task two: create table"""
    cur.execute('''
        CREATE TABLE demo (
            s TEXT NOT NULL,
            x INTEGER NOT NULL,
            y INTEGER NOT NULL
        )
    ''')
    conn.commit()
    print("Task two, tabled created successfully")

def insertData():
    """Task three: insert data through separate statements"""
    cur.execute("""
        INSERT INTO demo (s, x, y)
        VALUES ('g', 3, 9)
    """)
    conn.commit()

    cur.execute("""
        INSERT INTO demo (s, x, y)
        VALUES('v', 5, 7)
    """)
    conn.commit()

    cur.execute("""
        INSERT INTO demo (s, x, y)
        VALUES('f', 8, 7)
    """)
    conn.commit()
    print("Task three: data inserted successfully")


def questionOne():
    """Part One, Question One: 3"""
    cur.execute("""
        SELECT COUNT(*)
        FROM demo;
    """)
    conn.commit()
    print("Part One, Question One: 3")
    print(cur.fetchone(), "\n")

def questionTwo():
    """Part One, Question Two: 2"""
    cur.execute("""
        SELECT COUNT(*) 
        FROM demo
        WHERE x >= 5 and y >= 5;
    """)
    conn.commit()
    print("Part One, Question Two: 2")
    print(cur.fetchone(), "\n")

def questionThree():
    """Part One, Question Three: 2"""
    cur.execute("""
        SELECT COUNT(DISTINCT y)
        from demo;
    """)
    conn.commit()
    print("Part One, Question Three: 2")
    print(cur.fetchall(), "\n")


print("Task Two, create table")
createTable()

print("Task Three, insert data")
insertData()

print("Question One")
questionOne()

print("Question Two")
questionTwo()

print("Question Three")
questionThree()