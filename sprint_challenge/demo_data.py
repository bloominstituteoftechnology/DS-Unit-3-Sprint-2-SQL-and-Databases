
import sqlite3
import pandas as pd

# Here I define my data and the database name
database = "demo_data.sqlite3"
the_data = [('g', 3, 9),('v', 5, 7),('f', 8, 7)]

# This function makes the Database and creates the table. 
def make_db_w_table(db):
    print ("\nRunning Demo SQLite Operations...\n")
    create_table = """
        CREATE TABLE IF NOT EXISTS demo (
            s text NOT NULL,
            x integer,
            y integer 
        );"""
    
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(create_table)
    c.close
    conn.close
    print("Successfully created table\n")

# This function inserts my data into the table. 
def insert_into_database(data, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()    
    c.executemany("INSERT INTO demo VALUES (?,?,?)", data)
    conn.commit()
    c.close
    conn.close   
    print("Inserted values into table\n")


# These are my Queries for answering the questions
count_rows_query="""
      SELECT COUNT (s) AS Number_of_rows_in_database
        FROM demo 
    """

count_x_y_are_5 = """
    SELECT COUNT (s) AS Number_of_rows_where_X_and_Y_are_greaterthan_or_equal_to_5
      FROM demo
     WHERE x >= 5 AND y >= 5
"""

count_distinct_y ="""
    SELECT COUNT (DISTINCT y) as Count_of_Unique_Y_Values
      FROM demo
"""

# This function runs the queries and prints the results. 
def query_w_named_columns(query, db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    print("Query Result:\n", 
          pd.DataFrame(data, 
          columns=data[0].keys()).to_string(index=False))
    cur.close 
    conn.close

# This makes it all run automagically. 
if __name__ == '__main__':
    make_db_w_table(database)
    insert_into_database(the_data, database)
    print("Running Queries:")
    print("\nCount how many rows you have - it should be 3!")
    query_w_named_columns(count_rows_query, database)
    print("\nHow many rows are there where both `x` and `y` are at least 5?")
    query_w_named_columns(count_x_y_are_5, database)
    print("\nHow many unique values of `y` are there?")
    query_w_named_columns(count_distinct_y, database)