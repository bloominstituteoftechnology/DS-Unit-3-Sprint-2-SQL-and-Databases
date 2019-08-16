import sqlite3

# Instaniate Connection to Database
conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()


# Variable to create a table schema
create_table = """
    #CREATE TABLE demo (
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


# Print a conditional query from database
query = """
    SELECT s 
    FROM demo
    WHERE x >= 5 AND y >=5;
    """
curs.execute(query)
print("Rows with x,y >=5:", curs.fetchall())


# Print a aggregate query from database
query = """
    SELECT COUNT(DISTINCT(y))
    FROM DEMO
    """
curs.execute(query)
print("Number of unique values in y:", curs.fetchall())


# Commit actions and close cursor
curs.close()
conn.commit()
