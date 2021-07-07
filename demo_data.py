import sqlite3


def make_database(db):
    '''Create table and insert data'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    make_table = '''
    CREATE TABLE demo (
    s text,
    x int,
    y int);
    '''

    insert_data = '''
    INSERT INTO demo
    VALUES
        ("g",3,9),
        ("v",5,7),
        ("f",8,7);
    '''

    cursor.execute(make_table)
    cursor.execute(insert_data)
    conn.commit()

def query_database(db):
    '''search database and print output'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    # Count how many rows you have - it should be 3!
    query = '''
    SELECT COUNT(*) from demo
    '''
    print('Total Rows: ',cursor.execute(query).fetchall()[0][0])

    # How many rows are there where both `x` and `y` are at least 5?
    query = '''
    SELECT COUNT(*) from demo
    WHERE x >=5 AND y>=5
    '''
    print('Rows where x, y >= 5: ',cursor.execute(query).fetchall()[0][0])

    # How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?
    query = '''
    SELECT COUNT(DISTINCT(y)) from demo
    '''
    print('Unique Values of y: ',cursor.execute(query).fetchall()[0][0])

db = 'demo_data.sqlite3'
make_database(db)
query_database(db)

# OUTPUT
################################ 
# Total Rows:  3
# Rows where x, y >= 5:  2
# Unique Values of y  2

