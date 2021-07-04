import sqlite3

'''
docsting for query results
Total number of rows : 3
Rows with x,y >=5: 2
Number of unique values in y: 2
'''


# Instaniate Connection to Database
conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()


# Variable to create a table schema
create_table = """
    CREATE TABLE demo (
        s TEXT,
        x INT,
        y INT
);
"""
curs.execute(create_table)


# List of data to be inserted
data = [("g", 3, 9), ("v", 5, 7), ("f", 8, 7)]


# Loop to execute data insertion
for datum in data:
    insert_data = (
        """
        INSERT INTO demo (s, x, y)
        VALUES """
        + str(datum[:])
        + ";"
    )
    curs.execute(insert_data)

conn.commit()


# Print query to find the number of rows in table
query = '''
    SELECT COUNT(s)
    FROM demo
'''
curs.execute(query)
print('Total number of rows:', curs.fetchall()[0][0])


# Print a conditional query from database
query = """
    SELECT COUNT(s) 
    FROM demo
    WHERE x >= 5 AND y >=5;
    """
curs.execute(query)
print("Rows with x,y >=5:", curs.fetchall()[0][0])


# Print a aggregate query from database
query = """
    SELECT COUNT(DISTINCT(y))
    FROM DEMO
    """
curs.execute(query)
print("Number of unique values in y:", curs.fetchall()[0][0])


# Commit actions and close cursor
curs.close()
conn.commit()
