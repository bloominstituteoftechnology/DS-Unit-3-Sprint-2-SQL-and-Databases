import sqlite3

DB_FILE = 'demo_data.sqlite3' # database to connect to

def create_connection(db_file):
    """Create a database connection to SQLite specified by db_file"""
    conn = None

    try: 
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
            print ("Error in connection", e)
    
    return conn

def create_table(conn):
    """Add a table to database using a connection"""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS demo(
            s varchar(30),
            x int,
            y int
        )
        """
    )
    conn.commit()
    cur.close()

def load_data(conn):
    """Load required data into db using connection"""
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO demo(
            s,x,y
        )
        VALUES(
            "g",3,9
        );
        """
    )
    cur.execute(
        """
        INSERT INTO demo(
            s,x,y
        )
        VALUES(
            "v",5,7
        );
        """
    )
    cur.execute(
        """
         INSERT INTO demo(
            s,x,y
        )
        VALUES(
            "f",8,7
        );
        """
    )
    conn.commit()
    cur.close()

def queries(conn):
    """make queried to verify data loaded correctly"""
    cur = conn.cursor()

    # Get row count
    cur.execute(
        """
        SELECT *
        FROM demo
        """
    )
    row_count = cur.fetchall()
    print(f' There are {len(row_count)} rows in the database')

    # Get count of rows where x and y >5
    cur.execute(
        """
        SELECT *
        FROM demo
        WHERE x > 4
        AND y > 4
        """
    )
    xy_count = cur.fetchall()
    print(f' There are {len(xy_count)} rows in the database where x and y > 5')

    # count unique values of y
    cur.execute(
        """
        SELECT COUNT(DISTINCT y)
        FROM demo
        """
    )
    y_unique = cur.fetchall()
    print(f' There are {y_unique} unique values of "y" in the database')

    cur.close()

def main():
    """Run all functions to create and load db, then verfiy values"""
    
    # create connection
    conn = create_connection(DB_FILE)

    # create table if it doesnt exist
    create_table(conn)

    # load data
    load_data(conn)

    # print values loaded
    queries(conn)

    # close connection
    conn.close()

if __name__ == "__main__":
    main()

    """OUTPUT"""

    """
    There are 3 rows in the database
    There are 2 rows in the database where x and y > 5
    There are [(2,)] unique values of "y" in the database
    """