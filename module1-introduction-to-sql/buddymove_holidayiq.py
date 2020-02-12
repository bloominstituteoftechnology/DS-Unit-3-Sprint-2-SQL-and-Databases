import sqlite3
import os
import pandas as pd

# get file name and create a database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_csv_file = os.path.join(BASE_DIR, 'buddymove_holidayiq.csv')
db_file = os.path.join(BASE_DIR, 'buddymove_holidayiq.sqlite3') #new db

def create_connection(db_file):
    """Create a database connection to SQLite specified by db_file"""
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print("Error in connection", e)

    return conn

def load_data(CONN):
    """use pandas to read and check csv and load into database"""
    df = pd.read_csv(db_csv_file)

    # Check dataframe values and nulls
    assert df.shape == (249,7)
    assert all(df.notna())

    # load data into db and create a table
    df.to_sql(name='review', con=CONN, if_exists='replace')
    
def get_row_count(conn):
    """Fetch number of rows from created database"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM review
        """
    )
    
    return len(cur.fetchall())
def get_nature_shopper_count(conn):
    """
    count users who reviewed at least 100 Nature in the category
    and also reviewed at least 100 in the Shopping category
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT COUNT(Shopping)
        FROM review
        WHERE Nature >= 100
        """
    )
    return cur.fetchall()[0][0]

def main():
    """Print results from queries"""
    CONN = create_connection(db_file)

    # use connection to load data
    load_data(CONN)

    # Confirm rows in database equate to rows in dataframe
    row_counts = get_row_count(CONN)
    print(f"There are {row_counts} rows in the data base")

    # Print Nature & Shopper Relationship
    ns_count = get_nature_shopper_count(CONN)
    print(f"Total users who reviewed 100 Nature and Shopper locations: {ns_count}")

    # close connection to db
    CONN.close()

if __name__ == "__main__":
    main()